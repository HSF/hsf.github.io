# Inference Optimization pipeline

KubeFlow was the platform of choice for making a reproducible and scalable machine learning inference pipeline for the `g4fastsim` inference project. CERN IT Department has built [ml.cern.ch](https://ml.cern.ch) which is KubeFlow service accessible to all CERN members and was used for building the pipeline.

`g4fastsim` is broken into 2 parts - `Training` and `Inference`. Inference Pipeline is aimed at reducing memory footprint of the ML model from performing various 

The Inference pipeline is broken down into 3 main components:
* Inference
* Benchmark
* Optimization

Below given image gives an overview of how the pipeline is being built:

![InfOptim-Workflow](https://user-images.githubusercontent.com/47216475/181177926-1230f534-7eb8-4e01-a4ea-ecbff078e8c8.jpg)

## MacroHandler

`par04` or Inference component takes in input as a Macro file. This macro file contains the command in the exact order they are supposed to be run. Normally, if we want to change a macro file we will have to change the `.mac` file, upload it to gitlab, EOS or someplace from where it will be downloaded and pass the URL in KubeFlow Run UI Dashboard. This will become a tedious process.

MacroHandler component solves this issue by generating a `.mac` file based on the inputs from the KubeFlow Run UI.

The input to this component will be a `.jsonl` file containing `jsonlines`, where each `jsonline` contain 2 keys - `command` and `value`. An example of `.jsonl` macro file can be seen [here](https://gitlab.cern.ch/prmehta/geant4_par04/-/blob/master/pipelines/model-optimization/macros/examplePar04_onnx.jsonl).

`.jsonl` file will be converted to `.mac` file after value modifications and passed to the respective `par04` or inference component.

> ***This component is specifically designed for KubeFlow usage***

## Inference

Inference Component is a C++ program which takes in an ONNX model as an input, performs inference using it and outputs a `.root` file containing the simulated physics quantities which can be used downstream for analysis of particle showers. 

Inference component currently supports 2 libraries - `ONNXRuntime` and `LWTNN`. Support for `PyTorch` is on the way. The inference optimization pipeline currently being built is geared towards using `ONNXRuntime`. The ONNX model will optimized using different execution providers with GPU based being a priority - 
* ***Nvidia TensorRT*** - GPU
* ***Nvidia CUDA*** - GPU
* ***Intel oneDNN*** - CPU

> *Support for **Intel OpenVINO** is currently on halt due to compatibility issues.*

### Macro file

The inference takes a macro file as an input. This macrofile contains Geant4 as well as custom commands for manipulating the simulation process.
An example of the macrofile has been shared below. It uses `CUDA` backend for performing inference in `ONNXRuntime`.
```bash
#  examplePar04_onnx.mac
#
# Detector Construction 
/Par04/detector/setDetectorInnerRadius 80 cm
/Par04/detector/setDetectorLength 2 m
/Par04/detector/setNbOfLayers 90
/Par04/detector/setAbsorber 0 G4_W 1.4 mm true
/Par04/detector/setAbsorber 1 G4_Si 0.3 mm true
## 2.325 mm of tungsten =~ 0.25 * 9.327 mm = 0.25 * R_Moliere
/Par04/mesh/setSizeOfRhoCells 2.325 mm
## 2 * 1.4 mm of tungsten =~ 0.65 X_0
/Par04/mesh/setSizeOfZCells 3.4 mm
/Par04/mesh/setNbOfRhoCells 18
/Par04/mesh/setNbOfPhiCells 50
/Par04/mesh/setNbOfZCells 45

# Initialize
/run/numberOfThreads 1
/run/initialize

/gun/energy 10 GeV
/gun/position 0 0 0
/gun/direction 0 1 0

# Inference Setup
## dimension of the latent vector (encoded vector in a Variational Autoencoder model)
/Par04/inference/setSizeLatentVector 10
## size of the condition vector (energy, angle and geometry)  
/Par04/inference/setSizeConditionVector 4
## path to the model which is set to download by cmake
/Par04/inference/setModelPathName ./MLModels/Generator.onnx
/Par04/inference/setProfileFlag 1
/Par04/inference/setOptimizationFlag 0
/Par04/inference/setCudaFlag 1

# cuda options
/Par04/inference/cuda/setDeviceId 0
/Par04/inference/cuda/setGpuMemLimit 2147483648
/Par04/inference/cuda/setArenaExtendedStrategy kSameAsRequested
/Par04/inference/cuda/setCudnnConvAlgoSearch DEFAULT
/Par04/inference/cuda/setDoCopyInDefaultStream 1
/Par04/inference/cuda/setCudnnConvUseMaxWorkspace 1

/Par04/inference/setInferenceLibrary ONNX

## set mesh size for inference == mesh size of a full sim that
## was used for training; it coincides with readout mesh size
/Par04/inference/setSizeOfRhoCells 2.325 mm
/Par04/inference/setSizeOfZCells 3.4 mm
/Par04/inference/setNbOfRhoCells 18
/Par04/inference/setNbOfPhiCells 50
/Par04/inference/setNbOfZCells 45

# Fast Simulation
/analysis/setFileName 10GeV_100events_fastsim_onnx.root
## dynamically set readout mesh from particle direction
## needs to be the first fast sim model!
/param/ActivateModel defineMesh
## ML fast sim, configured with the inference setup /Par04/inference
/param/ActivateModel inferenceModel
/run/beamOn 100
```

There are lots of additional commands which can be used for further manipulation. A detailed example of macrofile for `ONNXRuntime` can be viewed [here](https://gitlab.cern.ch/prmehta/geant4_par04/-/blob/master/examplePar04_onnx.mac).

### Output .root file

The output of the inference component will be a `.root` file which can be opened using `TSystem` (C++) and `uproot` (python). The `.root` file contains the following data:

```text
output_file.root
├── energyDeposited;1
├── energyParticle;1
├── energyRatio;1
├── events;1
│   ├── CPUResMem
│   ├── CPUVirMem
│   ├── EnergyCell
│   ├── EnergyMC
│   ├── GPUMem
│   ├── phiCell
│   ├── rhoCell
│   ├── SimTime
│   └── zCell
├── hitType:1
├── longFirstMoment;1
├── longProfile;1
├── longSecondMoment;1
├── time;1
├── transFirstMoment;1
├── transProfile;1
└── transSecondMoment;1
```

For better understanding of physics quantity refer [this](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Examples/extended/Par04.html#output-data).

`CPUResMem`, `CPUVirMem`, `GPUMem` were added in this update and will be visible in the `geant4` docs after a couple of updates.

### Dependencies

`par04` has a number of optional dependencies which can be added to customise it for different host hardware and usecase.

#### Mandatory
- `Geant4` - A platform for simulation of the passage of particles through matter.
---
#### Optional
- `ONNXRuntime` - Machine learning platform developed by microsoft which is acting as the backend for using different hardware specific execution providers.

- `CUDA` - Parallel computing interface for Nvidia GPUs developed by Nvidia.

- `TensorRT` - Machine learning framework developed by Nvidia for optimizing ML model deployment on Nvidia GPUs. It is built on top of CUDA.

- `oneDNN` - Machine learning library which optimized model deployment on Intel hardware. It is part of oneAPI - a cross platform performance library for deep learning applications.

- `OpenVINO` - Machine Learning toolkit facilitating optimization of deep learning models from a framework and deployment on Intel Hardware.
  - Currently, `OpenVINO`'s integration is on halt due to compatibility issues.

- `ROOT` - An object oriented library developed by CERN for for particle physics data analysis. It is also used for Astronomy and data mining.
  - In `par04`, `ROOT` is used to get host memory usage.

- `Valgrind` - Valgrind is a programming tool for memory debugging, memory leak detection, and profiling.
  - In `par04`, `Valgrind` is used for function call profiling of inference block.

### Run Inference

To run `par04` simulation program, follow the below given steps:

1. Clone the git repo
```bash
git clone --recursive https://gitlab.cern.ch/prmehta/geant4_par04.git
```
2. Build the program
```bash
cmake -DCMAKE_BUILD_TYPE="Debug" -DCMAKE_CXX_FLAGS_DEBUG="-ggdb3" <source folder>
```

If you want build `par04` using dependencies, then use the `DCMAKE_PREFIX_PATH` flag.
```bash
cmake -DCMAKE_BUILD_TYPE="Debug" \
    -DCMAKE_PREFIX_PATH="/opt/valgrind/install;/opt/root/src/root;/opt/geant4/install;/opt/onnxruntime/install;/opt/onnxruntime/data;/usr/local/cuda;" \
    -DCMAKE_CXX_FLAGS_DEBUG="-ggdb3" \
    <source folder>
```

3. Install the program - go into the directory where program was build and run
```bash
make -j`nproc`
make install
```

4. Go to the install directory and run:
```bash
./examplePar04 -m <macro file> -k -g True -o <output filename> -do <output directory>
```

> :warning: Make sure to add path to dependencies in `PATH` and `LD_LIBRARY_PATH` respectively

Checkout [dependencies section](#dependencies) for more info on customising `par04` for your purpose.

#### Flags
- `-m` - Macrofile path
- `-k` - Whether it is kubeflow deployment or not. Adding `-k` will indicate `True`.
- `-g` - Whether to enable GPU memory usage collection or not.
- `-o` - Name of the output file. Make sure it ends with `.root`.
- `-do` - Path of the directory where output file will be saved.

> :warning: `-o` and `-do` will only be used when `-k` is set as these 2 flags are KubeFlow deployment specifc. They are added to make the Inference component compatible with KubeFlow's data passing mechanism. Inorder to make KubeFlow component's reusable, KubeFlow recommends allowing the KubeFlow sdk to generate paths at compile time.
> 
> The paths generated can or cannot be present in the docker container, so, we need to handle both the cases and when path is not present, then our code should auto generate the directories as the per the path.
> 
> If you are using `par04` as a standalone program, you can also use `/analysis/setFileName` in Macrofile to set the filename.

## Benchmark

The benchmark component is built for comparing the output of different `par04` runs. Currently, it supports `2` output files and the plan to support 3 files is in roadmap. The current benchmark component is tailored a lot towards using in a pipeline rather than a standalone program.

The output of benchmark component will be plots, lots of plots, which will help with comparison as well as a `.json` file which will contain Jensen Shannon Divergence values for different physics quantity histograms.

It is a full python component and requires the following dependencies:
-   `scipy`
-   `uproot`
-   `numpy`
-   `matplotlib`
-   `json`

### Run Benchmark

1.  To run `Benchmark`, clone the `par04` repository
```bash
git clone --recursive https://gitlab.cern.ch/prmehta/geant4_par04.git
```
2.  Go into the `Benchmark` component directory
```bash
cd <source directory>/pipelines/model-optimization/benchmark
```
3.  Run `benchmark.py`
```bash
python3 benchmark.py \
    --input_path_A <Path of first input directory> \
    --input_path_B <Path of second input directory> \
    --rootFilename <Filename of the output root file> \
    --truthE <Energy of the particles> \
    --truthAngle <Angle of the particles> \
    --yLogScale <Whether to scale the y-axis using log> \
    --saveFig <Whether to save the plots> \
    --eosDirectory <EOS directory path where you want to save the files> \
    --eosSaveFolderPath <EOS folder inside the EOS directory where you want to save the output> \
    --saveRootDir <Directory path inside docker container where you want the data to be saved for further passing>
```
> :warning: If you are running `benchmark.py` as a standalone program, make sure the output filename of both the runs is same and both are in different folders. There values will be passed to `input_path_A`, `input_path_B` and `rootFilename`.

> :warning: If you are running `Benchmark` as a kubeflow component, use `runBenchmark.sh`. It performs Kerberos authentication for EOS access and then runs `benchmark.py`. Everytime a Kubeflow component is created it needs to authenticate itself for EOS access, it is not feasible to do it manually and `runBenchmark.sh` takes care of that.
> 
> Before running a pipeline which requires EOS access, make sure your `krb-secret` is up-to-date and also run `kinit CERN_ID`. If you want to renew your `krb-secret` perform the steps mentioned [here](https://gitlab.cern.ch/ai-ml/examples/-/tree/master/pipelines/argo-workflows/access_eos).

An example plot is given below:

![transProfile_1_E_10_GeV_A_90](https://user-images.githubusercontent.com/47216475/181178000-328c5f36-9e71-475e-965f-80b94eb652d1.jpg)

## InputChecker

KubeFlow passes all the parameters as string from its run UI. In order to debug type issues a small input checker component is build which will output the value of every parameter and the values type.
This is not a crucial component and can be eliminated altogether.

> ***This component is specifically designed for KubeFlow usage***

## Pipeline:

The pipeline can be found on [ml.cern.ch](https://ml.cern.ch) under the name of `Geant4-Model-Optimization-Pipeline`. 
![Kubeflow_inference_optimization_pipeline](https://user-images.githubusercontent.com/47216475/181178052-004f7dfa-7d1b-4f31-afaa-7361e89d0d51.jpg)


-   `FullSimMacroHandler`, `OnnxFastSimNoEPMacroHandler` - Macro Handler components which output a macro file that gets passed to the respective Inference components.
-   `FullSim`, `OnnxFastSimNoEP` - Inference components which use Full Simulation and `ONNXRuntime` without any execution providers respectively.
-   `FullSimV/SOnnxFastSimNoEP` - Benchmark component that takes in inputs from `FullSim` and `OnnxFastSimNoEP` and compares them for similarity check.

> :green_book: To understand `arena` in relation to memory, check out this [stack overflow post](https://stackoverflow.com/questions/12825148/what-is-the-meaning-of-the-term-arena-in-relation-to-memory)

### Parameters:
* `fullSimJsonlUrl` - Url of FullSim Jsonl file which generates macrofile for full sim inference
* `fastSimJsonlUrl` - Url of FastSim Jsonl file which generates macrofile for fast sim inference
* `jsonlSavePath` - Path where JSONL file will be saved after downloading, inside the docker container
* `particleEnergy` - Energy of the particle
* `particleAngle` - Angle of the particle.
* `setSizeLatentVector` - Dimension of the latent vector (encoded vector in a Variational Autoencoder model)
* `setSizeConditionVector` - Size of the condition vector (energy, angle and geometry)
* `setModelPathName` - Path of the `ONNX` model to be used for Fast Sim
* `setProfileFlag` - Whether to perform profiling during inference using `ONNXRuntime`.
* `setOptimizationFlag` - Whether to perform graph optimization on the model when using `ONNXRuntime`.
* `setDnnlFlag` - Whether to use `oneDNN` Execution Provider as compute backend when using `ONNXRuntime`.
* `setOpenVINOFlag` - Whether to use `OpenVINO` Execution Provider as compute backend when using `ONNXRuntime`.
* `setCudaFlag` - Whether to use `CUDA` Execution Provider as compute backend when using `ONNXRuntime`.
* `setTensorrtFlag` - Whether to use `TensorRT` Execution Provider as compute backend when using `ONNXRuntime`.
* `setInferenceLibrary` - Whether to use `ONNXRuntime` or `LWTNN` for inference in FastSim
* `setFileName` - Name of the the output `.root` file.
* `beamOn` - No.of Events to run
* `yLogScale` - Whether to set y scale of plot to `log`.
* `saveFig` - Whether to save plots in `Benchmark` component
* `eosDirectory` - Path of the EOS directory where output plots will be saved.

#### oneDNN
* `setDnnlEnableCpuMemArena` - Whether to enable memory arena when using `oneDNN` Execution Provider.

#### CUDA
* `setCudaDeviceId` - ID of the device on which to run `CUDA` Execution Provider.
* `setCudaGpuMemLimit` - GPU Memory Limit when using `CUDA` Execution Provider.
* `setCudaArenaExtendedStrategy` - Strategy to use for extending memory arena. For more details, go [here](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#arena_extend_strategy)
* `setCudaCudnnConvAlgoSearch` - Type of search done for finding which `cuDNN` convolution algorithm to use. For more details, go [here](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#cudnn_conv_algo_search)
* `setCudaDoCopyInDefaultStream` - Whether to perform data copying operation from host to device and viceversa in default stream or separate streams. For more details, check [here](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#do_copy_in_default_stream)
* `setCudaCudnnConvUseMaxWorkspace` - Amount of memory to use when querying `cuDNN` to find the most optimal convolution algorithm. Lower value will result in sub-optimal querying and higher value will lead to higher peak memory usage. For more details, chech [here](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#cudnn_conv_use_max_workspace).

#### TensorRT
* `setTrtDeviceId` - ID of device on which to run `TensorRT` Execution Provider
* `setTrtMaxWorksapceSize` - Maximum memory usage of TensorRT Engine.
* `setTrtMaxPartitionIterations` - Maximum no.of iterations allowed while partitioning the model for TensorRT
* `setTrtMinSubgraphSize` - Minimum node size in a subgraph after partitioning.
* `setTrtFp16Enable` - Whether to enable FP16 computation in TensorRT
* `setTrtInt8Enable` - Whether to enable INT8 computation in TensorRT
* `setTrtInt8UseNativeCalibrationTable` - Select what calibration table is used for non-QDQ (Quantize- DeQuantize) models in INT8 mode. If 1, native TensorRT generated calibration table is used; if 0, ONNXRUNTIME tool generated calibration table is used.
* `setTrtEngineCacheEnable` - Enable TensorRT engine caching. The purpose of using engine caching is to save engine build time in the case that TensorRT may take long time to optimize and build engine.
> :warning: Each engine is created for specific settings such as model path/name, precision (FP32/FP16/INT8 etc), workspace, profiles etc, and specific GPUs and it’s not portable, so it’s essential to make sure those settings are not changing, otherwise the engine needs to be rebuilt and cached again.
> 
> :warning: Please clean up any old engine and profile cache files (.engine and .profile) if any of the following changes:
> * Model changes (if there are any changes to the model topology, opset version, operators etc.)
> * ORT version changes (i.e. moving from ORT version 1.8 to 1.9)
> * TensorRT version changes (i.e. moving from TensorRT 7.0 to 8.0)
> * Hardware changes. (Engine and profile files are not portable and optimized for specific Nvidia hardware)
* `setTrtEngineCachePath` -  Specify path for TensorRT engine and profile files if `setTrtEngineCacheEnable` is True, or path for INT8 calibration table file if `setTrtInt8Enable` is True.
* `setTrtDumpSubgraphs` - Dumps the subgraphs that are transformed into TRT engines in onnx format to the filesystem. This can help debugging subgraphs.

#### OpenVINO
* `setOVDeviceType` - Type of device to run `OpenVINO` Execution Provider on
* `setOVDeviceId` - ID of the device to run `OpenVINO` Execution Provider on
* `setOVEnableVpuFastCompile` -  During initialization of the VPU device with compiled model, Fast-compile may be optionally enabled to speeds up the model’s compilation to VPU device specific format.
* `setOVNumOfThreads` - No.of threads to use while performing computation using `OpenVINO` Execution Provider
* `setOVUseCompiledNetwork` - It can be used to directly import pre-compiled blobs if exists or dump a pre-compiled blob at the executable path. 
* `setOVEnableOpenCLThrottling` - This option enables OpenCL queue throttling for GPU devices (reduces CPU utilization when using GPU).


## Optimizations

#### To be build
