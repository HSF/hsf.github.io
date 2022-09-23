---
project: Geant4
title: Geant4-FastSim - Geant4-FastSim - Building an ML pipeline for fast shower simulation
author: Guneet Singh Kohli
date: 29.07.2022
year: 2022
layout: blog_post
logo: Geant4-logo.png
intro: |
  A KubeFlow pipeline for training ML Fast Simulation in Geant4.
---

# Problem Statement:

In Large Hadron Collider (LHC) experiments at CERN in Geneva, the calorimeter is a crucial detector technology to measure the energy of particles. These particles interact electromagnetically and/or hadronically with the material of the calorimeter, creating cascades of secondary particles or showers. Describing the showering process relies on simulation methods describing all particle interactions with matter. A detailed and accurate simulation is based on the Geant4 toolkit. Constrained by the need for precision, the simulation is inherently slow and constitutes a bottleneck for physics analysis. Furthermore, with the upcoming high luminosity upgrade of the LHC with more complex events and a much-increased trigger rate, the amount of required simulated events will increase. Machine Learning (ML) techniques such as generative modeling are used as fast simulation alternatives to learn to generate showers in a calorimeter, i.e., simulating the calorimeter response to certain particles. The pipeline of a fast simulation solution can be categorized into five components: data preprocessing, ML model design, validation, inference, and optimization. The preprocessing module allows us to derive a suitable representation of showers and to perform data cleaning, scaling, and encoding. The preprocessed data is then used by the generative model for training. To search for the best set of hyperparameters of the model, techniques such as Automatic Machine Learning (AutoML) are used. The validation component is based on comparing different ML metrics and physics quantities between the input and generated data. The aim of this project is to optimize the ML pipeline of the fast simulation approach using the open-source platform Kubeflow. Furthermore, a byproduct of this project is that the student will gain expertise in cutting-edge ML techniques and learn to use them in the context of high granularity image generation and fast simulation. Moreover, this project can serve as a baseline for future ML pipelines for all experiments at CERN.You can check furthe details [**here**](https://g4fastsim.web.cern.ch/).
# ML FastSim in Geant4 Training Pipeline
***
The project's objective is to use Kubeflow to handle the development of a scalable ML Pipeline for the ML FastSimulation in Geant4. The Training would be used to generate an optimised tuned generative model which will later be connected with Inference. Motivation behind using Kubeflow ML pipelines is as follows:
- Utilise power of Kubernetes to run ML jobs
- Support for the entire lifecycle of ML applications
- Training, inference, deployment
- Katib powered hyperparameter tuning 
- Open source, wide community support

## The ML FastSim in Geant4  components
- **Training** 
- **Inference**

>Training a  pipeline involves preparing an ML workflow that can be broken down into individual functionalities through which respective Pipeline components can be derived and made into a separate entity. Some basic functionalities are Input Parameters, Preprocessing, Exploratory Data Analysis, Model Hyperparameters, Model architecture definition, Model Instantiation and training, Model Validation, Tuning and many more based on the type of projects we are dealing with.

## The ML FastSimulation (Training) in Geant4 can be broken down into the following functional components
- **Input Parameters**
- **Preprocessing of Data**
- **Model Parameters**
- **Model architecture and Training** 
- **Hyperparameter Tuning through Katib**
- **Generation of Showers (Generative Modelling)**
- **Validations of Results through Visualisations**


## Par04 Project Structure

Before beginning the discussion about the Kubeflow Component Creation, it is important to look at the python code base which will later be reformatted according to kubeflow pipeline generation requirements
```
|---convert.py
|---generate.py
|---README.md
|---requirements.txt
|---setup.py
|---train.py
|---validate.py
|   
+---core
|-------constants.py
|-------model.py
|       
+---utils
|-------observables.py
|-------preprocess.py
```
>The Full codebase can be found [here.](https://github.com/DalilaSalamani/MLFastSim)

## Refactored Par04 Project into Kubeflow Pipeline
```
|---main.py
|---configuration.py
|---README.md
|---generate_yaml.py
|---Katib_yaml
|   
+---pipeline_components
|-------generate.py
|-------input_parameters.py
|-------preprocess.py
|-------validate.py
|-------model_parameters.py
|-------Katib_setup.py
|       
+---training_docker
|-------Dockerfile
|-------krb5.conf
|-------main.py
```
- Pipeline Components: Directory containing original python components refactored in Kubeflow functions 
- Training Docker: Directory containing the model training script with docker setup for its integration into the pipeline
- Configuration File: Defines and initialised the constant variables to be used in the pipeline. All the components digest the variables through this configuration file
- Katib YAML Template: Pipeline Components: Directory containing original python components refactored in Kubeflow functions 
Training Docker: Directory containing the model training script with docker setup for its integration into the pipeline
Configuration File: Defines and initialised the constant variables to be used in the pipeline. All the components digest the variables through this configuration file
Katib YAML Template: A yaml template has been prepared which is edited at runtime by the code. This makes Katib integration smooth and automated.
Generate YAML file : A file to process the refactored kubeflow python scripts into kubeflow components yaml
Main file to encapsulate the logic and generate results.
Curating the components YAML together into a Pipeline and submitting it automatically to the Kubeflow Dashboard
Configure the EOS memory with the components
Configure the resource allocation of all the components
A yaml template has been prepared which is edited at runtime by the code. This makes Katib integration smooth and automated.
- Generate YAML file : A file to process the refactored kubeflow python scripts into kubeflow components yaml
- Main file to encapsulate the logic and generate results.
  - Curating the components YAML together into a Pipeline and submitting it automatically to the Kubeflow Dashboard
  - Configure the EOS memory with the components
  - Configure the resource allocation of all the components

# Kubeflow
***

## What is Kubeflow?
>Kubeflow is a free, open-source machine learning platform that makes it possible for machine learning pipelines to orchestrate complicated workflows running on Kubernetes. Kubeflow was first released in 2017, built by developers from Google, Cisco, IBM, Red Hat, and more.The “Kube” in Kubeflow comes from the server orchestration tool Kubernetes. Kubeflow runs on Kubernetes clusters either locally or in the cloud, easily enabling the power of training machine learning models on multiple computers, accelerating the time to train a model. “Flow” was given to signal that Kubeflow sits among other workflow schedulers like ML Flow, FBLearner Flow, and Airflow.
## Why Kubeflow ?
- Have separate environments and resources configured for each component in the pipeline
- Leverage the power of Katib for smooth hyperparameter tuning. Use algorithms like NAS, grid search etc.
- Run multiple pipelines together without affecting each other resource requirements
- Allows to use dedicated (GPU) resources at **CERN** **_(ml.cern.ch)_**
- Has a DSL (Domain Specific Language) compiler that transforms pipeline’s python code into a static configuration (YAML) 

## Kubeflow Pipeline
Kubeflow Pipelines is the Kubeflow extension that provides the tools to create machine learning workflows. Basically these workflows are chains of tasks designed in the form of graphs and that are represented as Directed Acyclic Graphs (DAGs). Each node of the graph is called a component, where that component represents a self-contained task which lives inside a docker container

## Kubeflow Elements
The following section mentions about some of the common Kubeflow SDK functions and packages that are constantly used while creating a Kubeflow Pipeline. These elements are native to Kubeflow and help in building the pipeline with ease.

### Kubeflow Packages
- [`kfp.Client`](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/#:~:text=the%20boolean%20expression.-,kfp.Client,-contains%20the%20Python) contains the Python client libraries for the Kubeflow Pipelines API.
- [`kfp.dsl`](https://kubeflow-pipelines.readthedocs.io/en/stable/source/kfp.dsl.html) contains the domain-specific language (DSL) that you can use to define and interact with pipelines and components. 
- [`kfp.components`](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/#:~:text=resources%20for%20execution.-,kfp.components,-includes%20classes%20and) includes classes and methods for interacting with pipeline components.
- [`kfp.compiler`](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/#:~:text=the%20following%20packages%3A-,kfp.compiler,-includes%20classes%20and) includes classes and methods for compiling pipeline Python DSL into a workflow yaml spec.

### Kubeflow functions
>Note : The Kubeflow Pipeline SDK currently have two versions: v1 and v2. The current pipeline developed in the project was done using v1 but for future reference it is important to consider the migration to stable v2 version as well.
- `kfp.components.create_component_from_func` Converts a user defined Python function to a Kubeflow component. The following [example](https://kubeflow-pipelines.readthedocs.io/en/1.8.13/source/kfp.components.html#:~:text=in%20a%20container.-,Examples,-The%20function%20name) explains about the given function in details. 
- `kfp.components.create_component_from_func_v2` Converts a Python function to a component for the v2 version of kubeflow SDK.
- `kfp.compiler.Compiler.compile` Compiles your Python DSL code into a single static configuration (in YAML format) that the Kubeflow Pipelines service can process.
- `kfp.dsl.component` It is a decorator for DSL functions that returns a pipeline component.
- `kfp.dsl.VolumeOp` Represents a pipeline task (op) which creates a new PersistentVolumeClaim (PVC). It aims to make the common case of creating a PersistentVolumeClaim fast.
- `kfp.Client.create_experiment` Creates a pipeline experiment and returns an experiment object.
- `kfp.Client.run_pipeline` It runs a pipeline and returns a run object.
- `kfp.Client.create_run_from_pipeline_func` Compiles a pipeline function and submits it for execution on Kubeflow Pipelines.
- `kfp.Client.create_run_from_pipeline_package` Runs a local pipeline package on Kubeflow Pipelines.
- `kfp.Client.upload_pipeline` Uploads a local file to create a new pipeline in Kubeflow Pipelines.
- `kfp.Client.upload_pipeline_version` It uploads a local file to create a pipeline version

### Kubeflow Pipelines CLI Interactions
- [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) Kubernetes provides a command line tool for communicating with a Kubernetes cluster's control plane, using the Kubernetes API.
  -  `kubectl get pods` Returns the list of the pods living inside your namespace
  - `kubectl describe pod <pod_name>` Describes the pod specifications and configurations
  - `kubectl get pod POD_NAME -oyaml` To get the pod YAML
  - `kubectl logs <Katib Job Pod Name> -c training-container` Describes the details about the Katib experiment running
  - `kubectl delete pod <pod_name>` Delete a Pod in your namespace
  - `kubectl top pod` Display Resource usage
>Note: For more kubectl commands visit this amazing [cheatsheet](https://www.bluematador.com/learn/kubectl-cheatsheet) by **BlueMatador**
- [`kfp diagnose_me`](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/#:~:text=kfp%20diagnose_me%20runs%20environment%20diagnostic) Runs environment diagnostic
- `kfp pipeline <COMMAND>` provides the following commands to help you manage pipelines
  - `get`  Gets detailed information about a Kubeflow pipeline from your Kubeflow Pipelines cluster
  - `list`  Lists the pipelines that have been uploaded to your Kubeflow Pipelines cluster.
  - `upload`  Uploads a pipeline to your Kubeflow Pipelines cluster.
- `kfp run <COMMAND>` provides the following commands to help you manage pipeline runs:
  - `get` - Displays the details of a pipeline run.
  - `list` - Lists recent pipeline runs.
  - `submit` - Submits a pipeline run.

# Kubeflow Pipeline Preparation
***

To design any pipeline, the following steps are essential:

* Identify individual functionalities present in existing workflow which will be refactored into Kubeflow Components
* The early identification of the components eases the process of organising your software design and intercommunication between the Components
* Identify inputs and outputs of all your python files and functions
* Define and instantiate the model architecture in the single component if the pickle doesn't allow saving the model template because of Nested Class Structure
* The Trained model can be saved into the persistent memory and be later called upon in some other component for the downstream tasks.
* The primitive variables: Boolean, Integer, String, and Float can be passed from one component to another without explicitly storing them in the memory. 
* To handle large files or complex data structures like lists, arrays, dictionaries, etc., it is important that the component saves these in the persistent memory or EOS.
* The Files can later be accessed in other components via the file path provided
* CERN provides some [standard docker images](https://gitlab.cern.ch/ai-ml/kubeflow_images) on which we can run our individual kubeflow components. 
* Custom Docker Images can be created if the standard images doesn't fulfill the requirement
* Creation of Docker Images and custom environments for the components have discussed in later sections
* CERN employs the use of EOS for its memory management. EOS will be used as persistent memory for our kubeflow pipelines
* The setup of EOS in the Kubeflow has been discussed in `Memory Management Section`.
* Kubeflow Visualisations Tool is great for visualising classification models and basic regression metrics.
* Create an HTML page or a Markdown File to showcase your visualizations through Kubeflow because the UI is still incapable of handling the complex visualizations implicitly.
* Kubeflow also provides a powerful tool called Kale which can convert any standard jupyter notebook into a kubeflow pipeline without writing a single line of code. 
>Kale is sometimes not preferred since it doesn't offer great control over the workflow and eventually would not help in moving ahead with complex code bases 
>
> However if the code logic is simple Kale can act as a quick problem solver by creating a End to End Pipeline through Kubeflow UI.
* Your component’s goal may be to create a dataset in an external service, such as a BigQuery table. In this case, it may make sense for the component to output an identifier for the produced data, such as a table name, instead of the data itself.
* Since input and output paths are passed in as command-line arguments, your component’s code must be able to read inputs from the command line. If your component is built with Python, libraries such as argparse and absl.flags make it easier to read your component’s inputs.
* Your component’s code can be implemented in any language, so long as it can run in a container image.

# Pipeline Components of ML FastSim in Geant4 Training 
![full_pipeline](https://user-images.githubusercontent.com/43180442/191947451-0f3ade57-4ece-4754-8a87-83623e84e008.png)
***
## Input Parameters
- The `/pipeline_components/input_parameters` defines the variables that are going to be used throughout the pipeline.
- The parameters inside the `input_parameters` component are initialised using a `configuration.py` file which you can edit to control your workflow

##  Preprocessing of Data
- Before refactoring preprocess.py had the following functions `preprocess` ,` get_condition_arrays ` and `load_showers` 
- After refactoring into Kubeflow Format the `get_condition_arrays` was added into generate component, `preprocess` function became the `/pipeline_components/preprocess` and the `load_showers` was added to validate component.
- The preprocess functions returns the training data. The data is saved into the EOS memory and the file location of the training data is passed onto next components.
- The other component can then use this file location to access the data from EOS memory and use it inside the component container
- The connection between `input_parameters` and `preprocess` components can be well understood in the `Demonstration section`.


## Model Parameters
- This component defined and initialised the model training parameters and configurations

## Katib Setup
- The `Katib_setup` aims to focus on the integration of Katib hyperparameter tuning into our pipeline.
- This component submits the Katib Yaml automatically and communicates with a dockerized model training setup.
- It saves the weights of the best model trained.
- A UI dashboard summarises all experiments that Katib ran
- A detailed discussion about the Katib Setup and its component construction can be found [here](https://g4fastsim.web.cern.ch/docs/ML_Deployment_Kubeflow/)


## Generate Component
- The generate.py aimed to generate showers for the FastSim. 
- The generate functionality depends on `get_condition_array` from the preprocess.py, instantiated model for using the decoder for generation and the function's own existing code.
- This component helps in understanding the way how Models trained in one component can be used to perform actions in another.
- Here `generate` was configured to load the Saved Model from `EOS` and produce the shower generation for number of events specified by the user.
- The output of this component is the location of saved shower generation which is passed onto the validate component to visualise the results.

## Validate Component
- The component aims at generating plots to analyse the results generated by the model
- It loads the predictions made by the generate component.
- The results produced are stored in the EOS memory
- If required the plots can visualise by creating markdown page and hosting it on Kubeflow

# Demonstration of Pipeline building steps:
***
> This sections aims to showcase how Kubeflow Pipeline is created by refactoring the simple python code into Kubeflow component format .
> All the examples demonstrates different use cases which are intensively required in any ML workflow. 
> In reference to the discussion in `Kubeflow Pipeline Preparation` the upcoming points would help in grasping those suggestions and understand the blockers usually faced and how to solve them.

## Setting up a configuration file for initialising all the global variables that would be used throughout the project

```
nCells_z = 45
nCells_r =  18
nCells_phi = 50
min_energy = 1
max_energy = 1
min_angle = 50
max_angle = 50
init_dir = '/eos/user/g/gkohli/'
checkpoint_dir = '/eos/user/g/gkohli/checkpoint/'
conv_dir = '/eos/user/g/gkohli/conversion/'
valid_dir = '/eos/user/g/gkohli/validation/'
gen_dir = '/eos/user/g/gkohli/generation/'
save_dir = '/eos/user/g/gkohli/visualisations/'
Katib_files = '/eos/user/g/gkohli/Katib_test/'
batch_size = 100
intermediate_dim1 = 100
intermediate_dim2 = 50
intermediate_dim3 = 20
intermediate_dim4 = 14
latent_dim = 10
epsilon_std = 1
mu = 0
epochs = 100
lr = 0.001
outActiv = 'sigmoid'
validation_split = 0.05
wkl = 0.5
ki = 'RandomNormal'
bi = 'Zeros'
earlyStop = True
name_experiment = 'demo-test1'

```
 ## Identifying the First Component of the Pipeline
- The first section of any Pipeline would aim to initialise the variables that will be required throughout the pipeline
- In our case the first component was `Input Parameters` 
- This component digest all the parameters from the configuration.py file

```
def input_parameters(nCells_z: int, nCells_r: int, nCells_phi: int, min_energy: int, max_energy: int, min_angle: int,
                     max_angle: int, init_dir: str, checkpoint_dir: str, valid_dir: str, gen_dir: str, save_dir: str,
                     Katib_files: str) \
        -> NamedTuple('Variable_Details',
                      [('nCells_z', int), ('nCells_r', int), ('nCells_phi', int), ('original_dim', int),
                       ('min_energy', int), ('max_energy', int), ('min_angle', int), ('max_angle', int),
                       ('init_dir', str), ('checkpoint_dir', str), ('conv_dir', str), ('valid_dir', str),
                       ('gen_dir', str), ('save_dir', str), ('Katib_files', str)]):
    """
    Handling Input Parameters of the project
    :return: The global input variables
    """
    nCells_z, nCells_r = nCells_z, nCells_r
    nCells_phi = nCells_phi
    min_energy = min_energy
    max_energy = max_energy
    min_angle = min_angle
    max_angle = max_angle
    init_dir = init_dir
    checkpoint_dir = checkpoint_dir
    conv_dir = '<USE IF REQUIRED>'
    valid_dir = valid_dir
    gen_dir = gen_dir
    save_dir = save_dir
    Katib_files = Katib_files

    return (nCells_z, nCells_r, nCells_phi, nCells_z * nCells_r * nCells_phi, min_energy, max_energy,
            min_angle, max_angle, init_dir, checkpoint_dir, conv_dir, valid_dir, gen_dir, save_dir, Katib_files)
```


## Transferring variables which are not string, integer, boolean or float

### Preprocess Python function
```
def preprocess():
    energies_train = []
    cond_e_train = []
    cond_angle_train = []
    cond_geo_train = []
    # This example is trained using 2 detector geometries
    for geo in ["SiW", "SciPb"]:
        dir_geo = INIT_DIR + geo + "/"
        # loop over the angles in a step of 10
        for angle_particle in range(MIN_ANGLE, MAX_ANGLE + 10, 10):
            f_name = f"{geo}_angle_{angle_particle}.h5"
            f_name = dir_geo + f_name
            # read the HDF5 file
            h5 = h5py.File(f_name, "r")
            # loop over energies from min_energy to max_energy
            energy_particle = MIN_ENERGY
            while energy_particle <= MAX_ENERGY:
                # scale the energy of each cell to the energy of the primary particle (in MeV units)
                events = np.array(h5[f"{energy_particle}"]) / (energy_particle * 1000)
                energies_train.append(events.reshape(len(events), ORIGINAL_DIM))
                # build the energy and angle condition vectors
                cond_e_train.append([energy_particle / MAX_ENERGY] * len(events))
                cond_angle_train.append([angle_particle / MAX_ANGLE] * len(events))
                # build the geometry condition vector (1 hot encoding vector)
                if geo == "SiW":
                    cond_geo_train.append([[0, 1]] * len(events))
                if geo == "SciPb":
                    cond_geo_train.append([[1, 0]] * len(events))
                energy_particle *= 2
    # return numpy arrays
    energies_train = np.concatenate(energies_train)
    cond_e_train = np.concatenate(cond_e_train)
    cond_angle_train = np.concatenate(cond_angle_train)
    cond_geo_train = np.concatenate(cond_geo_train)
    return energies_train, cond_e_train, cond_angle_train, cond_geo_train
```
### Preprocess Kubeflow Function
```
def preprocess_new(nCells_z: int, nCells_r: int, nCells_phi: int, original_dim: int, min_energy: int, max_energy: int,
                   min_angle: int, max_angle: int, init_dir: str, checkpoint_dir: str, conv_dir: str, valid_dir: str,
                   gen_dir: str) -> NamedTuple('Variable_Details',
                                               [('energies_train_location', str), ('condE_train_location', str),
                                                ('condAngle_train_location', str), ('condGeo_train_location', str)]):
    """
    Helps in preprocessing the input data for the VAE
    :param nCells_z:
    :param nCells_r:
    :param nCells_phi:
    :param original_dim:
    :param min_energy: Min energy in the training data
    :param max_energy: Max energy in the training data
    :param min_angle: Min angle in the training data
    :param max_angle: Max angle in the training data
    :param init_dir: Directory where all your corresponding results will be saved
    :param checkpoint_dir: Saving the training checkpoints
    :param conv_dir: Directory to save the converted model
    :param valid_dir: Saving the validation results
    :param gen_dir: Saving to generate model
    :return: Returns the path of the training files locations
    """
    import h5py
    import numpy as np
    import os
    import shutil
    energies_Train = []
    condE_Train = []
    condAngle_Train = []
    condGeo_Train = []
    training_data_inputs = init_dir + 'Intermediate_Train'
    shutil.rmtree(training_data_inputs)
    os.mkdir(training_data_inputs)
    # This example is trained using 2 detector geometries
    for geo in ['SciPb']:
        dirGeo = init_dir + geo + '/'
        # loop over the angles in a step of 10
        for angleParticle in range(min_angle, max_angle + 10, 10):
            fName = '%s_angle_%s.h5' % (geo, angleParticle)
            fName = dirGeo + fName
            h5 = h5py.File(fName)
            energyParticle = min_energy
            while energyParticle <= max_energy:
                # scale the energy of each cell to the energy of the primary particle (in MeV units) 
                events = np.array(h5['%s' % energyParticle]) / (energyParticle * 1000)
                energies_Train.append(events.reshape(len(events), original_dim))
                # build the energy and angle condition vectors
                condE_Train.append([energyParticle / max_energy] * len(events))
                condAngle_Train.append([angleParticle / max_angle] * len(events))
                # build the geometry condition vector (1 hot encoding vector)
                if geo == 'SiW':
                    condGeo_Train.append([[0, 1]] * len(events))
                if geo == 'SciPb':
                    condGeo_Train.append([[1, 0]] * len(events))
                energyParticle *= 2
    # return numpy arrays 
    energies_Train = np.concatenate(energies_Train)
    condE_Train = np.concatenate(condE_Train)
    condAngle_Train = np.concatenate(condAngle_Train)
    condGeo_Train = np.concatenate(condGeo_Train)
    energies_train_location = training_data_inputs + '/energies_train.npy'
    np.save(energies_train_location, energies_Train)
    condE_train_location = training_data_inputs + '/condE_train.npy'
    np.save(condE_train_location, condE_Train)
    condAngle_train_location = training_data_inputs + '/condAngle_train.npy'
    np.save(condAngle_train_location, condAngle_Train)
    condGeo_train_location = training_data_inputs + '/condGeo_train.npy'
    np.save(condGeo_train_location, condGeo_Train)
    return energies_train_location, condE_train_location, condAngle_train_location, condGeo_train_location

```
> - In Python files the variables are accessible to different files in same repo. 
> 
> - In Kubeflow we can not transfer arrays, list ,dictionaries, dataframes, etc. like we pass str,int,bool or float. 
> 
> - Each Kubeflow component lives and executes in different containers.
>
> - To establish the connection between these components we use persistent memory (EOS) to store large data structures or data
> and pass the location path of these from component to another which can be observed in the last part of code snippet above
> 
## Interacting with Class definitions and instantiations in Kubeflow
- The model.py file, as seen [here](https://github.com/DalilaSalamani/MLFastSim/blob/main/core/model.py) shows the definition of a Model Class and its functions. 
- The Model Architecture Class can be handled by first defining model class ,followed by instantiating, training and saving in one single component.
- Another way of handling class is saving the class definition in the memory as pickle or a dill object in one component and loading this saved object in other component to instantiate it and use its functions
- The problem in the latter case, is that pickle fails to handle nested class structure.Thus it's better to define , instantiate, train and save the model in a single component to avoid complexities.
- You can click [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/model_setup.py) to see the Kubeflow implementation of Model setup.

## Loading saved Model in other component.
- The Model trained by the `Model_Setup` component has to be loaded in the `Generate Component`
- To generate showers after the model training a sampling from the distribution of the latent space is performed for which we require the decoder from the trained model
- To load the weights from the memory, an object of the Model class will be required
- To create the object, the model class needs to be defined and instantiated again in the calling component 
- Once object is created successfully, it is capable to load the saved weights from the `EOS`
- To understand the execution of such case, check my repo [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/generate.py).

## Conversion of 'Kubeflow Python Functions' to 'Kubeflow Components'
The python function formatted according to Kubeflow requirements become **components** by using the `kfp.components` package which contains inbuilt function to convert python functions to components and store them in YAML format.
To generate YAML files of all the components check my repo [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/generate_yaml.py )

## Connecting the Components using DSL package
The snippet below shows how the kubeflow components are brought together and connected into a single pipeline. The `components.dsl` package provides functions for components connections and pipeline formulation.
```
@dsl.pipeline(
    name='ML first',
    description='ML first).'
)
def ml_pipeline_first(nCells_z=configuration.nCells_z, nCells_r=configuration.nCells_r,
                      nCells_phi=configuration.nCells_phi, min_energy=configuration.min_energy,
                      max_energy=configuration.max_energy, min_angle=configuration.min_angle,
                      max_angle=configuration.max_angle, init_dir=configuration.init_dir,
                      checkpoint_dir=configuration.checkpoint_dir, valid_dir=configuration.valid_dir,
                      gen_dir=configuration.gen_dir, save_dir=configuration.save_dir,
                      Katib_files=configuration.Katib_files, batch_size=configuration.batch_size,
                      intermediate_dim1=configuration.intermediate_dim1,
                      intermediate_dim2=configuration.intermediate_dim2,
                      intermediate_dim3=configuration.intermediate_dim3,
                      intermediate_dim4=configuration.intermediate_dim4,
                      latent_dim=configuration.latent_dim, epsilon_std=configuration.epsilon_std, mu=configuration.mu,
                      epochs=configuration.epochs, lr=configuration.lr, outActiv=configuration.outActiv,
                      validation_split=configuration.validation_split, wkl=configuration.wkl, ki=configuration.ki,
                      bi=configuration.bi, earlyStop=configuration.earlyStop,
                      name_experiment=configuration.name_experiment):
    """
    Function to curate the Kubeflow component by connecting through the data flow between each other
    """
    data_dir = input_parameters_comp(nCells_z, nCells_r, nCells_phi, min_energy, max_energy, min_angle, max_angle,
                                     init_dir, checkpoint_dir, valid_dir, gen_dir, save_dir, Katib_files) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)

    model_instantations = model_input_parameters_comp(data_dir.outputs['original_dim'],
                                                      data_dir.outputs['checkpoint_dir'],
                                                      batch_size, intermediate_dim1, intermediate_dim2,
                                                      intermediate_dim3, intermediate_dim4, latent_dim, epsilon_std, mu,
                                                      epochs, lr, outActiv, validation_split,
                                                      wkl, ki, bi, earlyStop) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)
    preprocessed_input = preprocess_comp(data_dir.outputs['nCells_z'], data_dir.outputs['nCells_r'],
                                         data_dir.outputs['nCells_phi'], data_dir.outputs['original_dim'],
                                         data_dir.outputs['min_energy'], data_dir.outputs['max_energy'],
                                         data_dir.outputs['min_angle'], data_dir.outputs['max_angle'],
                                         data_dir.outputs['init_dir'], data_dir.outputs['checkpoint_dir'],
                                         data_dir.outputs['conv_dir'], data_dir.outputs['valid_dir'],
                                         data_dir.outputs['gen_dir']) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)

    model_setup = model_setup_comp(model_instantations.outputs['batch_size'],
                                   model_instantations.outputs['original_dim'],
                                   model_instantations.outputs['intermediate_dim1'],
                                   model_instantations.outputs['intermediate_dim2'],
                                   model_instantations.outputs['intermediate_dim3'],
                                   model_instantations.outputs['intermediate_dim4'],
                                   model_instantations.outputs['latent_dim'],
                                   model_instantations.outputs['epsilon_std'],
                                   model_instantations.outputs['mu'], model_instantations.outputs['epochs'],
                                   model_instantations.outputs['lr'], model_instantations.outputs['outActiv'],
                                   model_instantations.outputs['validation_split'],
                                   model_instantations.outputs['wReco'],
                                   model_instantations.outputs['wkl'], model_instantations.outputs['ki'],
                                   model_instantations.outputs['bi'], model_instantations.outputs['earlyStop'],
                                   model_instantations.outputs['checkpoint_dir'],
                                   preprocessed_input.outputs['energies_train_location'],
                                   preprocessed_input.outputs['condE_train_location'],
                                   preprocessed_input.outputs['condAngle_train_location'],
                                   preprocessed_input.outputs['condGeo_train_location'],
                                   data_dir.outputs['Katib_files'], name_experiment) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)

    generate = generate_comp(model_setup.outputs['best_model'], data_dir.outputs['max_energy'],
                             model_instantations.outputs['checkpoint_dir'],
                             data_dir.outputs['gen_dir'],
                             model_instantations.outputs['batch_size'], model_instantations.outputs['original_dim'],
                             model_instantations.outputs['latent_dim'], model_instantations.outputs['epsilon_std'],
                             model_instantations.outputs['mu'], model_instantations.outputs['epochs'],
                             model_instantations.outputs['lr'], model_instantations.outputs['outActiv'],
                             model_instantations.outputs['validation_split'], model_instantations.outputs['wReco'],
                             model_instantations.outputs['wkl'], model_instantations.outputs['ki'],
                             model_instantations.outputs['bi'], model_instantations.outputs['earlyStop']) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)

    validate = validate_comp(generate.outputs['generate_data'], data_dir.outputs['nCells_z'],
                             data_dir.outputs['nCells_r'], data_dir.outputs['nCells_phi'],
                             data_dir.outputs['save_dir'], data_dir.outputs['max_energy'],
                             model_instantations.outputs['checkpoint_dir'], data_dir.outputs['init_dir'],
                             data_dir.outputs['gen_dir'], data_dir.outputs['save_dir'],
                             model_instantations.outputs['original_dim'], data_dir.outputs['valid_dir']) \
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)

```

> Observe the passing of arguments from one component to another, which establishes the link among the components, and defines the workflow.

# Containerizing your components
***

A specific methodology needs to be followed while creating your docker image. The following steps discuss its creation:

`Step1`:  ```$ docker login gitlab-registry.cern.ch```

`Step2`: Goto this [link](https://gitlab.cern.ch/ai-ml/kubeflow_images/-/tree/cern_14/base) and download the folder. The Dockerfile and requirements.txt found here are the base images over which we will be adding our own additional requirements.

`Step3`: **If unable to login in step 1, try this first and then again put in login credentials**

```$ sudo chmod 666 /var/run/docker.sock```

`Step4`: Update the requirements.txt file according to the needs of the projects and mention the libraries to be installed using pip.

`Step5`: Custom DockerFile content:
```
# Select a base image from which to extend
FROM <SPECIFY YOUR BASE IMAGE>
# or: FROM custom_public_registry/username/image

USER root

# Install required packages
COPY custom_requirements.txt /requirements.txt
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FEEA9169307EA071 8B57C5C2836F4BEB && apt-get -qq update && pip3 install -r /requirements.txt

USER jovyan

# The following line is mandatory:
CMD ["sh", "-c", \
     "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser \
      --allow-root --port=8888 --LabApp.token='' --LabApp.password='' \
      --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]
```

`Step6`: ```$ docker build. -f <Base_Dockerfile_Name>  -t <your_alias>```

`Step7`: ```$ docker build . -f <Custom_Dockerfile_name> -t gitlab-registry.cern.ch/<repo_name>/<container_name>:<tag_name>```

`Step8`:``` $ docker push gitlab-registry.cern.ch/<repo_name>/<container_name>:<tag_name>```

`Step9`: Once you have pushed the image to the GitLab registry, it is now easily accessible for the containers. My images can be found [here.](https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/container_registry)

# Memory Management using EOS
***

`Step1`:  ```$ git clone https://gitlab.cern.ch/ai-ml/examples.git```

`Step2`: Navigate to examples/pipelines/argo-workflows/access\_eos and login to Kerberos with kinit by typing:
`$ kinit <CERN-USER-ID>`

`Step3`: Delete existing Kerberos Secret:
`kubectl delete secret krb-secret`

`Step4`: Create a new general Kerberos Secret:

```kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000```

`Step5`: Configure EOS in the Pipeline Code. Mounting Kerberos and EOS to the kubeflow environment
```
eos_host_path = k8s_client.V1HostPathVolumeSource(path='/var/eos')
eos_volume = k8s_client.V1Volume(name='eos', host_path=eos_host_path)
eos_volume_mount = k8s_client.V1VolumeMount(name=eos_volume.name, mount_path='/eos')

krb_secret = k8s_client.V1SecretVolumeSource(secret_name='krb-secret')
krb_secret_volume = k8s_client.V1Volume(name='krb-secret-vol', secret=krb_secret)
krb_secret_volume_mount = k8s_client.V1VolumeMount(name=krb_secret_volume.name, mount_path='/secret/krb-secret-vol')
```

`Step 6`: To add the volumes so that EOS is accessible through each component, we add the following to each of the function components created using the kfp sdk:

```
        .add_volume(krb_secret_volume) \
        .add_volume_mount(krb_secret_volume_mount) \
        .add_volume(eos_volume) \
        .add_volume_mount(eos_volume_mount)
```
`Step7`: Once the above setup completes, we can access publicly visible files from the EOS.

# Large Data Handling
***
![data_loading drawio](https://user-images.githubusercontent.com/43180442/191947915-b36ef6b9-2253-402f-8f73-97e3e73c8348.png)


- The training data used in the model training was approximately 40 GB stored in `h5` format
- The preprocessing component loaded the h5 files and saved individual arrays of 3.2 GB each
- A single large array corresponded to a Single Energy at Single Angle for a particular geometry
- The energies ranged from 1 to 1024 MeV and angle ranged from 50 to 90 for 2 different geometries `SciPb` and `SiW`
- This lead to generate 11 numpy arrays for 10000 events each for a single angle
- Thus total 55 numpy arrays _(each array was 3.2 GB)_ of 10000 events each were present for a single geometry
- To handle such a massive data in a 8GB RAM, the data was loaded batch wise
- Each numpy array was loaded into the memory and was fed into training with batch size of 50
- Once training completed the next numpy array was loaded and the sequence followed
- After loading the numpy array and training the model over it, the array was set to none and deleted so that the CPU memory was completely free to handle the next batch 
- Once all batches were trained the model was saved and stored in the memory

# Running our Kubeflow Pipeline
***
>The following steps would provide you a guided workflow through which you can import this project
> onto your Kubeflow Namespace and run the experiments.

`STEP1`: Go to ml.cern.ch and login into the Kubeflow Dashboard

`STEP2`: Go to Notebook tab on the side panel and create a working space

`STEP3`: Confirm the allocated resources and create the workspace with kf-14-tensorflow-jupyter:v1

`STEP4`: Create a folder from the sidebars

`STEP5`: Once inside the folder open a Terminal and <notebook.ipynb> 

> Before Step 6 Create your kerberos secret to access the EOS memory space from inside the Pipeline
> 
> The commands are to be entered in the Terminal as follows:
> 1) `kinit <your namespace>`
> 2) `kubectl delete secret krb-secret`
> 3) `kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000`
> 
`STEP6`: Run`!git clone <repo name>` in the notebook cell

`STEP7`: Change the parameter values in the `configuration.py` so to adjust according to your experiment setup

`STEP8`: Run `!python3 generate_yaml.py` in the next notebook cell
> The above step would create
YAML files for each python component which will be a part of the Kubeflow Pipeline

`STEP9`: Run `!python3 main.py --namespace <Specify your namespace name> --pipeline_name <Specify your pipeline name>` in the notebook cell

`STEP10`: To check the results open the `runs` tab to see final pipeline graphs and `AutoML` tab to access the Katib Hyper Parameter Tuning 

# Outcomes from GSOC 2022
1. Persistent Memory setup and configuration with EOS in Kubeflow Pipeline
2. Reformatted the python code into Kubflow function format
3. One click pipeline implementation with all the Kubeflow workflow abstracted
4. Refactoring the training loop to handle large amount of data
5. Experimented with different float precisions, number of events, max/ min angle and energy to determine the maximum data handling capabilities of the pipeline with 8GB CPU
6. Katib Hyperparameter tuning integration into Pipeline
7. Submitting and configuring the Pipeline setup and Katib YAML automatically into Kubeflow Dashboard without user involvement
8. Well Designed Documented Code written to help users implement Kubeflow methodology for different workflows.
9. In detail documentation to understand and adopt Kubeflow Workflow


















