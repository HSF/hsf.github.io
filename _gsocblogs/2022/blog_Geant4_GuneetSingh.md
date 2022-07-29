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
The project's objective is to use Kubeflow, whose instance is hosted at [ml.cern.ch](https://ml.cern.ch/) to handle the development of a scalable ML Pipeline for the ML FastSimulation in Geant4. The Training would be used to generate an optimised tuned generative model which will later be connected with Inference. Motivation behind using Kubeflow ML pipelines is as follows:
- Utilise power of Kubernetes to run ML jobs
- Web UI to interact with components and features
- Support for the entire lifecycle of ML applications
- Training, inference, deployment
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
- **Generation of Showers (Generative Modelling)**
- **Validations of Results through Visualisations**


## Current ML Code Base

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

# Kubeflow
***

## What is Kubeflow?
>Kubeflow is a free, open-source machine learning platform that makes it possible for machine learning pipelines to orchestrate complicated workflows running on Kubernetes. Kubeflow was first released in 2017, built by developers from Google, Cisco, IBM, Red Hat, and more.The “Kube” in Kubeflow comes from the server orchestration tool Kubernetes. Kubeflow runs on Kubernetes clusters either locally or in the cloud, easily enabling the power of training machine learning models on multiple computers, accelerating the time to train a model. “Flow” was given to signal that Kubeflow sits among other workflow schedulers like ML Flow, FBLearner Flow, and Airflow.

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

### Kubeflow Pipelines CLI tool 
- [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) Kubernetes provides a command line tool for communicating with a Kubernetes cluster's control plane, using the Kubernetes API.
- [`kfp diagnose_me`](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/#:~:text=kfp%20diagnose_me%20runs%20environment%20diagnostic) Runs environment diagnostic
- `kfp pipeline <COMMAND>` provides the following commands to help you manage pipelines:
-- `get`  Gets detailed information about a Kubeflow pipeline from your Kubeflow Pipelines cluster.
-- `list`  Lists the pipelines that have been uploaded to your Kubeflow Pipelines cluster.
-- `upload`  Uploads a pipeline to your Kubeflow Pipelines cluster.
- `kfp run <COMMAND>` provides the following commands to help you manage pipeline runs:
-- `get` - Displays the details of a pipeline run.
-- `list` - Lists recent pipeline runs.
-- `submit` - Submits a pipeline run.

# Kubeflow Pipeline Preparation
***

To design any pipeline, the following steps are essential:

* Identify individual functionalities present in the Workflow as they can be considered as the Kubeflow component.This early identification can help in envisioning the pipeline structure easily.
* For each python file or function that we have, understand and confirm what are the inputs and the outputs of that particular module
* Kubeflow cannot convert a class or a nested class structure to a pipeline component. Therefore, the definition of  model architectures or custom layers must remain intact and be part of a single Kubeflow component where it will later be instantiated. 
* The Trained model can be saved into the persistent memory and be later called upon in some other component for the downstream tasks.
* The primitive variables: Boolean, Integer, String, and Float can be passed from one component to another without explicitly storing them in the memory. 
* To handle large files or complex data structures like lists, arrays, dictionaries, etc., it is important that the component saves these in the memory,so that later they are accessible for other components.
* CERN provides some [standard docker images](https://gitlab.cern.ch/ai-ml/kubeflow_images) on which we can run our individual kubeflow components. 
* Usually, the basic docker images are not enough to fulfill the project's requirements, and in those cases, it is better to create your own custom docker images. The steps of creating a custom docker image will be discussed in upcoming sections.
* CERN employs the use of EOS for its memory management. This would be everyone’s go-to place for saving and accessing files for experimentation. The setup of EOS will be discussed `Memory Management Section`.
* Kubeflow Visualisations components suits the purpose of mostly classification models and basic regression metrics. However most of the time we deal with many custom metrics and their corresponding visualisations like graphs, plots, and images which should be saved in the directory.
* Create an HTML page or a Markdown File to showcase your visualizations through Kubeflow because the UI is still incapable of handling the complex visualizations implicitly.
* Kubeflow also provides a powerful tool called Kale which can convert any standard jupyter notebook into a kubeflow pipeline without writing a single line of code. 
>Kale is sometimes not preferred since it doesn't offer control over the workflow and eventually would not help in moving ahead with complex code bases however if the code is simple Kale can act as a quick problem solver as it can convert your jupyter notebook into a Kubeflow pipeline through Kubeflow provided UI.
* Your component’s goal may be to create a dataset in an external service, such as a BigQuery table. In this case, it may make sense for the component to output an identifier for the produced data, such as a table name, instead of the data itself. We recommend limiting this pattern to cases where the data must be put into an external system instead of keeping it inside the Kubeflow Pipelines system.
* Since input and output paths are passed in as command-line arguments, your component’s code must be able to read inputs from the command line. If your component is built with Python, libraries such as argparse and absl.flags make it easier to read your component’s inputs.
* Your component’s code can be implemented in any language, so long as it can run in a container image.

# Pipeline Components of ML FastSim in Geant4 Training 
***
## Input Parameters
The following component initialises the variables that will be common to all the components throughout. They can be treated as a set of global variables whose access would be required numerously by other functions. To construct this component it is important to note that it will act as the first pipeline component and thus would not include any input in the function definition. The function aims to returns all the parameters which can be seen in the `Demonstration` Section.
>**Component creation of this function**:
input_parameters_comp = create_component_from_func(
    func=input_parameters,
    base_image='python:3.7')

##  Preprocessing of Data
In the original code base the preprocess.py consisted of the following functions `preprocess` ,` get_condition_arrays ` and `load_showers` However when structuring the preprocess component only the   `preprocess` was kept a part of the component as it served the purpose of generating `energies_train, cond_e_train, cond_angle_train, cond_geo_train.`. In kubeflow these variables can not be directly passed into the downstream components therefore it was important to first save them in `EOS` and return their paths as outputs from this components. Also the preprocess uses the global variables from the input parameters above which leads to our first basic Kubeflow Connection between two components. The following discussion can be well understood in the `Demonstration section`.
>**Component creation of this function**:
preprocess_comp = create_component_from_func(
func=preprocess,
base_image='gitlab-registry.cern.ch/ai-ml/kubeflow_images/tensorflow-notebook-gpu-2.1.0:v0.6.1-33')

## Model Parameters
The Parameters involving models had to be kept as a separate Kubeflow component because this component would later be attached with`Katib` in the next phase which would help in managing the Hyperparameter Tuning of our model. 
>**Component creation of this function**:
input_parameters_comp = create_component_from_func(
    func=input_parameters,
    base_image='python:3.7')

## Model Setup
The core component of any ML workflow is the model architecture definition and training. At first the aim was to pickle the Model definition and reload it into a training component and carry on the other implementations from that point however it was not possible because python pickle module faces lots of errors while pickling nested class structure and objects because of which it was not able to pickle the Model definition which consisted of `VAE, VAEHandler, Sampling Layer and Reparameterizr layer`. Due to this it became difficult to construct a modular pipeline and the component was restructured in a way that the Class definition, Instantiation as well as training was combined and the Model was saved in the EOS at specified location. This component was connected with all the previously discussed components since it required the outputs from all the above corresponding components. CERN Base image tends to use `TF2.1` which was different from the development environment of the FastSim project hence it was important to create our custom image and push it to the registry so that it could be accessed inside the pod assigned to us for the development.The detailed steps have been discussed in the `Containerizing your components`. The below code snippet shows a custom image that was created by me which include `TF2.8`
>**Component creation of this function**:
input_parameters_comp = create_component_from_func(
func=input_parameters,
base_image='gitlab-registry.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/kube_gkohli:cern_pipelinev2')

## Generate Component
The generate.py aimed to produce the generate showers for the FastSim. The generate functionality depends on `get_condition_array` from the preprocess.py, instantiated model for using the decoder for generation and the function's own existing code. This component also helps in understanding the way how Models trained in one component can be used to perform actions in another. Here the generate was configured to load the Saved Model from `EOS` and the produce the shower generation for 100 events. The output of this component is the location of saved shower generation so that it can be passed onto the validation layer to visualise the results. The custom base image was selected since the model was trained and created with environment of `TF2.8` which had to remain consistent throughout
>**Component creation of this function**:
input_parameters_comp = create_component_from_func(
func=input_parameters,
base_image='gitlab-registry.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/kube_gkohli:cern_pipelinev2')

# Demonstration of Pipeline building steps:
***
This sections aims to showcase how kubeflow pipeline is created and different python elements are formulated into becoming the part of pipeline. All the examples considered here demonstrates different use cases which are intensively required in any ML workflow. In reference to the discussion in `Kubeflow Pipeline Preparation` the upcoming points would help in grasping those suggestions and understand the blockers usually faced and how to solve them.

 ## Identifying the First Component of the Pipeline
- Mostly the first section of any Pipeline would aim to initialise the variables that will be required throughout the pipeline
- In our case the first component would be the `Input Parameters` which is looks as follows

```
def input_parameters() -> NamedTuple('Variable_Details',
        [('nCells_z',int), ('nCells_r',int),('nCells_phi',int), ('original_dim',int),
         ('min_energy',int), ('max_energy',int),('min_angle',int), ('max_angle', int),
         ('init_dir', str), ('checkpoint_dir', str), ('conv_dir', str), ('valid_dir', str),
         ('gen_dir', str),('save_dir', str)]):
    nCells_z =45
    nCells_r = 18
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
    return (nCells_z,nCells_r,nCells_phi,nCells_z*nCells_r*nCells_phi,min_energy,max_energy,min_angle,max_angle,init_dir,checkpoint_dir,conv_dir,valid_dir,gen_dir,save_dir)
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
def preprocess_new(nCells_z:int,nCells_r:int,nCells_phi:int,original_dim:int,min_energy: int,max_energy: int,min_angle :int,max_angle :int,init_dir :str,checkpoint_dir :str,conv_dir :str,valid_dir :str,gen_dir :str)-> NamedTuple('Variable_Details',[('energies_train_location', str), ('condE_train_location', str), ('condAngle_train_location', str), ('condGeo_train_location', str)]):
    import h5py
    import numpy as np
    energies_Train = []
    condE_Train = []
    condAngle_Train = []
    condGeo_Train = []
    for geo in [ 'SciPb'  ]: 
        dirGeo = init_dir + geo + '/'
        # loop over the angles in a step of 10
        for angleParticle in range(min_angle,max_angle+10,10): 
            fName = '%s_angle_%s.h5' %(geo,angleParticle)
            fName = dirGeo + fName
            h5 = h5py.File(fName,'r')
            # loop over energies from min_energy to max_energy
            energyParticle = min_energy
            while(energyParticle<=max_energy):
                # scale the energy of each cell to the energy of the primary particle (in MeV units) 
                events = np.array(h5['%s'%energyParticle])/(energyParticle*1000)
                energies_Train.append(events.reshape(len(events),original_dim))
                # build the energy and angle condition vectors
                condE_Train.append( [energyParticle/max_energy]*len(events) )
                condAngle_Train.append( [angleParticle/max_angle]*len(events) )
                # build the geometry condition vector (1 hot encoding vector)
                if( geo == 'SiW' ):
                    condGeo_Train.append( [[0,1]]*len(events) )
                if( geo == 'SciPb' ):
                    condGeo_Train.append( [[1,0]]*len(events) )
                energyParticle *=2
    energies_Train = np.concatenate(energies_Train)
    condE_Train = np.concatenate(condE_Train)
    condAngle_Train = np.concatenate(condAngle_Train)
    condGeo_Train = np.concatenate(condGeo_Train)
    energies_train_location='/eos/user/g/gkohli/input_save/energies_train4.npy'
    np.save(energies_train_location,energies_Train)
    condE_train_location='/eos/user/g/gkohli/input_save/condE_train.npy'
    np.save(condE_train_location,condE_Train)
    condAngle_train_location='/eos/user/g/gkohli/input_save/condAngle_train.npy'
    np.save(condAngle_train_location,condAngle_Train)
    condGeo_train_location='/eos/user/g/gkohli/input_save/condGeo_train.npy'
    np.save(condGeo_train_location,condGeo_Train)
    return energies_train_location,condE_train_location,condAngle_train_location,condGeo_train_location
```
>In the case of python files the variables will be easily accessible in a different file in same repo. However when we talk about Kubeflow Components, these dont have shared memories and are individual Entities. Also in Kubeflow we can not transfer arrays, list ,dictionaries, dataframes, etc like we pass str,int,bool or float. Therefore the best way is to save the variable data at a location which in our case is `EOS` and access it in another component by loading it from the memory.
## Interacting with Class definitions and instantiations in Kubeflow
- The model.py file, as seen [here](https://github.com/DalilaSalamani/MLFastSim/blob/main/core/model.py) shows the definition of a Model Class and its functions. 
- The Model Architecture Class can be handled by first defining model class ,followed by instantiating, training and saving in one single component.
- Another way of handling class is saving the class definition in the memory as pickle or a dill object in one component and loading this saved object in other component to instantiate it and use its functions
- The problem in the latter case, is that pickle fails to handle nested class structure which will generally be encountered in actual scenarios thus, it's better to former technique were from definition to training and saving is happening in a single component.
- You can click [**here**](https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/-/blob/master/Pipeline_Components/Model_Setup/model.py) to see the Kubeflow implementation of Model setup.

## Loading saved Model in other component.
- The Model trained by the `Model_Setup` component has to be loaded in the `Generate Component`
- To generate showers after the model training a sampling from the distribution of the latent space is performed for which we require the decoder from the trained model
- To load the weights from the memory, an object of the Model class will be required
- To create the object, the model class needs to be defined and instantiated again in the calling component 
- Once object is created successfully, it is capable to load the saved weights from the `EOS`
- To understand the execution of such case, check my repo [**here**](https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/-/blob/master/Pipeline_Components/Generate/generate.py).

## Conversion of 'Kubeflow Python Functions' to 'Kubeflow Components'
The python function formatted according to Kubeflow requirements become **components** by using the `kfp.components` package which contains inbuilt function to convert python functions to components and store them in YAML format.The component creation has been discussed at the end of every section in `Pipeline Components of ML FastSim in Geant4 Training`. To generate YAML files of the components, check my repo [**here**](https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/-/blob/master/yaml_generation_from_python.py)

## Connecting the Components using DSL package
The snippet below shows how the kubeflow components are brought together and connected into a single pipeline. The `components.dsl` package provides functions for components connections and pipeline formulation.
```
@dsl.pipeline(
    name='ML first',
    description='ML first).'
)
def ml_pipeline_first():
    data_dir = input_parameters_comp() \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)

    preprocessed_input = preprocess_comp1(data_dir.outputs['nCells_z'],data_dir.outputs['nCells_r'],data_dir.outputs['nCells_phi'],data_dir.outputs['original_dim'],data_dir.outputs['min_energy'],data_dir.outputs['max_energy'],data_dir.outputs['min_angle'],data_dir.outputs['max_angle'],data_dir.outputs['init_dir'],data_dir.outputs['checkpoint_dir'],data_dir.outputs['conv_dir'],data_dir.outputs['valid_dir'],data_dir.outputs['gen_dir']) \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)
    model_instantations= model_input_parameters_comp(data_dir.outputs['original_dim'],data_dir.outputs['checkpoint_dir']) \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)
    generate = generate_comp(data_dir.outputs['max_energy'],model_instantations.outputs['checkpoint_dir'],data_dir.outputs['gen_dir'],model_instantations.outputs['batch_size'],model_instantations.outputs['original_dim'],model_instantations.outputs['latent_dim'],model_instantations.outputs['epsilon_std'],model_instantations.outputs['mu'],model_instantations.outputs['epochs'],model_instantations.outputs['lr'],model_instantations.outputs['outActiv'],model_instantations.outputs['validation_split'],model_instantations.outputs['wReco'],model_instantations.outputs['wkl'],model_instantations.outputs['ki'],model_instantations.outputs['bi'],model_instantations.outputs['earlyStop']) \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)
    model_setup = model_setup_comp(model_instantations.outputs['batch_size'],model_instantations.outputs['original_dim'],model_instantations.outputs['intermediate_dim1'],model_instantations.outputs['intermediate_dim2'],model_instantations.outputs['intermediate_dim3'],model_instantations.outputs['intermediate_dim4'],model_instantations.outputs['latent_dim'],model_instantations.outputs['epsilon_std'],model_instantations.outputs['mu'],model_instantations.outputs['epochs'],model_instantations.outputs['lr'],model_instantations.outputs['outActiv'],model_instantations.outputs['validation_split'],model_instantations.outputs['wReco'],model_instantations.outputs['wkl'],model_instantations.outputs['ki'],model_instantations.outputs['bi'],model_instantations.outputs['earlyStop'],model_instantations.outputs['checkpoint_dir'],preprocessed_input.outputs['energies_train_location'],preprocessed_input.outputs['condE_train_location'],preprocessed_input.outputs['condAngle_train_location'],preprocessed_input.outputs['condGeo_train_location']) \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)
    validate = validate_comp(generate.outputs['generate_data'],data_dir.outputs['nCells_z'],data_dir.outputs['nCells_r'],data_dir.outputs['nCells_phi'],data_dir.outputs['save_dir'],data_dir.outputs['max_energy'],model_instantations.outputs['checkpoint_dir'],data_dir.outputs['init_dir'],data_dir.outputs['gen_dir'],data_dir.outputs['save_dir'],model_instantations.outputs['original_dim'],data_dir.outputs['valid_dir']) \
                .add_volume(krb_secret_volume) \
                .add_volume_mount(krb_secret_volume_mount) \
                .add_volume(eos_volume) \
                .add_volume_mount(eos_volume_mount)
```

>The important factor to observe here is the passing of arguments from one component to another, establishing the link among the components, and defining the workflow.

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
FROM testrun1:latest
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

`Step6`: ```$ docker build. -f <Base\_Dockerfile\_Name>  -t <your\_alias>```

`Step7`: ```$ docker build . -f <Custom\_Dockerfile\_name> -t gitlab-registry.cern.ch/<repo\_name>/<container\_name>:<tag\_name>```

`Step8`:``` $ docker push gitlab-registry.cern.ch/<repo\_name>/<container\_name>:<tag\_name>```

`Step9`: Once you have pushed the image to the GitLab registry, it is now easily accessible for the containers. My images can be found [here.](https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline/container_registry)

# Memory Management using EOS
***

`Step1`:  ```$ git clone https://gitlab.cern.ch/ai-ml/examples.git```

`Step2`: Navigate to examples/pipelines/argo-workflows/access\_eos and login to Kerberos with kinit by typing:
`$ kinit <CERN-USER-ID>`

`Step3`: Delete existing Kerberos Secret:
`kubectl delete secret krb-secret`

`Step4`: Create a new general Kerberos Secret:

```kubectl create secret generic krb-secret --from-file=/tmp/krb5cc\_1000```

`Step5`: Configure EOS in the Pipeline Code. Mounting Kerberos and EOS to the kubeflow environment
```
eos\_host\_path = k8s\_client.V1HostPathVolumeSource(path='/var/eos')
eos\_volume = k8s\_client.V1Volume(name='eos', host\_path=eos\_host\_path)
eos\_volume\_mount = k8s\_client.V1VolumeMount(name=eos\_volume.name, mount\_path='/eos')

krb\_secret = k8s\_client.V1SecretVolumeSource(secret\_name='krb-secret')
krb\_secret\_volume = k8s\_client.V1Volume(name='krb-secret-vol', secret=krb\_secret)
krb\_secret\_volume\_mount = k8s\_client.V1VolumeMount(name=krb\_secret\_volume.name, mount\_path='/secret/krb-secret-vol')
```

`Step 6`: To add the volumes so that EOS is accessible through each component, we add the following to each of the function components created using the kfp sdk:

```
.add\_volume(krb\_secret\_volume) \
`                `.add\_volume\_mount(krb\_secret\_volume\_mount) \
`                `.add\_volume(eos\_volume) \
`                `.add\_volume\_mount(eos\_volume\_mount)
```
`Step7`: Once the above setup completes, we can access publicly visible files from the EOS.

# Running our Kubeflow Pipeline
***
## Through Notebook Format
`Step1` Access ml.cern.ch

`Step2` Open the Kubeflow Dashboard > Go to Notebooks > Create an instance > Open the jupyter 

`Step3` `!git clone https://gitlab.cern.ch/gkohli/mlfastsim-kubeflow-pipeline.git`

`Step4`  Open Base_Pipeline_Geant4FastSim.ipynb 

`Step5` Goto `Terminal` and follow `Step2 to Step4` discussed in `Memory Management using EOS` Section

`Step6` Try `cd /eos/users/`, if working your instance can access `EOS` and now you are good to go 

`Step7` In the Notebook change the directory path in the Input_Component and run  all the cells

`Step8` The notebook would automatically run the pipeline in the backend.

`Step9` In the last cell click on `Experiment Details` to see the Pipeline in action 

`Step10` All the outputs will get saved in your specified memory location

## Through Python Command Line

_**Currently work in progress fixing some minor bugs**_

















