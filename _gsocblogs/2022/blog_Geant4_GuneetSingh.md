---
project: Geant4
title: Geant4-FastSim - Building an ML pipeline for fast shower simulation
author: Guneet Singh Kohli
photo: blog_authors/GuneetSingh.jpg
date: 29.07.2022
year: 2022
layout: blog_post
logo: Geant4-logo.png
intro: |
  A KubeFlow pipeline for training ML Fast Simulation in Geant4.
---
# Introduction:
Hi, I am Guneet Singh a recent Computer Science graduate who participated in GSoC 2022 and was a part of Geant4 fast simulation group to build an end to end Kubeflow Pipeline for training machine learning based model for fast shower simulation. The project was completed over the summer and the outcomes of the project have been highlighted in the next section.

The project's objective is to use Kubeflow to handle the development of a scalable ML Pipeline for the ML FastSimulation in Geant4. The Training would be used to generate an optimised tuned generative  model which will later be used to perform Inference in Geant4. Motivation behind using Kubeflow ML pipelines is as follows:
- Utilise power of Kubernetes to run ML jobs
- Support for the entire lifecycle of ML applications
- Training, inference, deployment
- Katib powered hyperparameter tuning 
- Open source, wide community support
> Kubeflow is a free, open-source machine learning platform that makes it possible for machine learning pipelines to orchestrate complicated workflows running on Kubernetes.
# Outcomes from GSOC 2022
1. Experimented with different float precisions, number of events, max/ min angle and energy to determine the maximum data handling capabilities of the pipeline with 8GB CPU
2. Reformatted the python code into Kubeflow function format
3. One click pipeline implementation with all the Kubeflow workflow abstracted
4. Persistent Memory setup and configuration with EOS in Kubeflow Pipeline
5. Refactoring the training loop to handle large amount of data
6. Katib Hyperparameter tuning integration into Pipeline
7. Submitting and configuring the Pipeline setup and Katib YAML automatically into Kubeflow Dashboard without user involvement
8. Well Designed Documented Code written to help users implement Kubeflow methodology for different workflows.
9. In detail documentation to understand and adopt Kubeflow Workflow
# Problem Statement:

In Large Hadron Collider (LHC) experiments at CERN in Geneva, the calorimeter is a crucial detector technology to measure the energy of particles. These particles interact electromagnetically and/or hadronically with the material of the calorimeter, creating cascades of secondary particles or showers. Describing the showering process relies on simulation methods describing all particle interactions with matter. A detailed and accurate simulation is based on the Geant4 toolkit. Constrained by the need for precision, the simulation is inherently slow and constitutes a bottleneck for physics analysis. Furthermore, with the upcoming high luminosity upgrade of the LHC with more complex events and a much-increased trigger rate, the amount of required simulated events will increase. Machine Learning (ML) techniques such as generative modeling are used as fast simulation alternatives to learn to generate showers in a calorimeter, i.e., simulating the calorimeter response to certain particles. The pipeline of a fast simulation solution can be categorized into five components: data preprocessing, ML model design, validation, inference, and optimization. The preprocessing module allows us to derive a suitable representation of showers and to perform data cleaning, scaling, and encoding. The preprocessed data is then used by the generative model for training. To search for the best set of hyperparameters of the model, techniques such as Automatic Machine Learning (AutoML) are used. The validation component is based on comparing different ML metrics and physics quantities between the input and generated data. The aim of this project is to optimize the ML pipeline of the fast simulation approach using the open-source platform Kubeflow. You can check further details [**here**](https://g4fastsim.web.cern.ch/).
# ML FastSim Training Pipeline
***

The ML FastSim in Geant4  components
- **Training** 
- **Inference**

The ML FastSimulation (Training) in Geant4 can be broken down into the following functional components:
- **Input Parameters**
- **Preprocessing of Data**
- **Model Parameters**
- **Model architecture and Training** 
- **Hyperparameter Tuning through Katib**
- **Generation of Showers (Generative Modelling)**
- **Validations of Results through Visualisations**


**ML FastSim project**

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

**Refactored ML FastSim project into Kubeflow Pipeline**
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
- Training Docker: Directory containing the model training script with docker setup for its integration into the pipeline
- Configuration File: Defines and initialised the constant variables to be used in the pipeline. All the components digest the variables through this configuration file
- Katib YAML Template: A yaml template has been prepared which is edited at runtime by the code. This makes Katib integration smooth and automated.
- Generate YAML file : A file to process the refactored kubeflow python scripts into kubeflow components yaml
- Main file to encapsulate the logic and generate results.
  - Curating the components YAML together into a Pipeline and submitting it automatically to the Kubeflow Dashboard
  - Configure the EOS memory with the components
  - Configure the resource allocation of all the components

    
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
* Kubeflow also provides a powerful tool called Kale which can convert any standard jupyter notebook into a kubeflow pipeline without writing a single line of code.
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
- A detailed discussion about the Katib Setup and its component construction can be found in Katib section.


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

- Setting up a configuration file for initialising all the global variables that would be used throughout the project
- Configuration file can be found [here](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/configuration.py)

 ### Identifying the First Component of the Pipeline
- The first section of any Pipeline would aim to initialise the variables that will be required throughout the pipeline
- In our case the first component was `Input Parameters` about which had discussed in previous section.
- This component digest all the parameters from the configuration.py file


### Transferring variables which are not string, integer, boolean or float
- Original `Preprocess Python Function` has been implemented [here](https://github.com/DalilaSalamani/MLFastSim/blob/f8ecea36d2f7bd55cd406c452bdb5248088d058d/preprocess.py)
- Refactored `Preprocess Kubeflow Function` focuses on how transferring of variables between components take place. [Check here](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/preprocess.py)

> - In Python files the variables are accessible to different files in same repo. 
> 
> - In Kubeflow we can not transfer arrays, list ,dictionaries, dataframes, etc. like we pass str,int,bool or float. 
> 
> - Each Kubeflow component lives and executes in different containers.
>
> - To establish the connection between these components we use persistent memory (EOS) to store large data structures or data
> and pass the location path of these from component to another which can be observed in the last part of code snippet above
> 

### Interacting with Class definitions and instantiations in Kubeflow
- The model.py file, as seen [here](https://github.com/DalilaSalamani/MLFastSim/blob/main/core/model.py) shows the definition of a Model Class and its functions. 
- The Model Architecture Class can be handled by first defining model class ,followed by instantiating, training and saving in one single component.
- Another way of handling class is saving the class definition in the memory as pickle or a dill object in one component and loading this saved object in other component to instantiate it and use its functions
- The problem in the latter case, is that pickle fails to handle nested class structure.Thus it's better to define , instantiate, train and save the model in a single component to avoid complexities.
- You can click [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/model_setup.py) to see the Kubeflow implementation of Model setup.

### Loading saved Model in other component.
- The Model trained by the `Model_Setup` component has to be loaded in the `Generate Component`
- To generate showers after the model training a sampling from the distribution of the latent space is performed for which we require the decoder from the trained model
- To load the weights from the memory, an object of the Model class will be required
- To create the object, the model class needs to be defined and instantiated again in the calling component 
- Once object is created successfully, it is capable to load the saved weights from the `EOS`
- To understand the execution of such case, check my repo [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/generate.py).

### Conversion of 'Kubeflow Python Functions' to 'Kubeflow Components'
The python function formatted according to Kubeflow requirements become **components** by using the `kfp.components` package which contains inbuilt function to convert python functions to components and store them in YAML format.
To generate YAML files of all the components check my repo [**here**](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/generate_yaml.py )

### Connecting the Components using DSL package
The [following file](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/main.py#:~:text=def%20ml_pipeline_first) below shows how the kubeflow components are brought together and connected into a single pipeline. The `components.dsl` package provides functions for components connections and pipeline formulation.
In the `ml_pipeline_first` function the components are stitched together logically.
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
> The Original Data was trained on a 240 GB RAM. Thus, it was important to refactor the code to handle ~175 GB worth of data in 8 GB RAM
> through batch loading, progressive training and appropriate cache management. Detailed Discussion is available [here](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/tree/large_data_handle)

## Katib 
>Katib is a hyperparameter tuning framework that comes with Kubeflow. It provides scalability through k8s environment as it 
> can run multiple trials in parallel. Katib is a host of various powerful algorithms that can be added in our workflow 
> such as **NAS**, **Bayesian Optimisation**,**Grid Search**,etc. The Katib experiments are parallelly run on GPUs
> and would strongly depend on the resource allocated to your namespace
>

### How to run Katib experiments from Kubeflow Dashboards
- Open the Kubeflow Dashboard at ml.cern.ch
- Go the **AutoML Experiments** tab on the left hand of the screen
- Click on `+ New Experiment`
- Go to the lower part of the screen and click on `Edit and submit YAML`
- Paste your YAML and submit it
- The Katib Experiments will soon be visible on the AutoML Experiments

### Understanding Katib YAML
> For indepth understanding of Katib YAML visit the [official documentation](https://www.kubeflow.org/docs/components/katib/trial-template/)

### Creating Docker Images of Model Training
Dockerizing the components is an essential step in Kubeflow Pipeline construction 
This helps in setting up different environments and resources for each component of a pipeline
It is also necessary if we want KATIB to attach with our model training setup since KATIB runs this image multiple times in parallel
Following steps would help in creating a custom image for a component
>Note:Use of VS Code for Docker Related Workflow is suggested

`STEP1`: Open VS Code and add your training script

`STEP2`: Get the `krb5.conf` file from the [repo](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/training_docker/krb5.conf)

`STEP3`: Refactor the training script to accept arguments through args parser

> For reference our Dockerized Model Setup and Training can be found [here](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/tree/master/training_docker)

`STEP4`: Create a Dockerfile

`STEP5`: In the Dockerfile define the Base Image, set up the krb configuration for EOS access, add the command to run the training script and pip install the requirements 

> Note: krb configuration inside Dockerfile looks as follows:
> ```commandline
> ENV DEBIAN_FRONTEND=noninteractive
> RUN apt-get -qq update && \
>    apt-get -yqq install libpam-krb5 krb5-user && \
>    apt-get -yqq clean && \
>    apt-get install -y --no-install-recommends \
>        ca-certificates bash-completion tar less \
>        python3-pip python-setuptools build-essential python-dev \
>        python3-wheel && \
>    rm -rf /var/lib/apt/lists/*
> COPY krb5.conf /etc/krb5.conf

`STEP6`: Once the files are in place open Terminal

`STEP7`: Run `sudo chmod 666 /var/run/docker.sock`

`STEP8`: Run `docker login gitlab-registry.cern.ch` and enter your credentials

`STEP9`: Run `docker build . -f Dockerfile -t <your_repo_name>:<image_tag>`

`STEP10`: Run `docker push <your_repo_name>:<image_tag>`

`STEP11`: Your script is now Dockerized and can be found in the gitlab registry under your repo

### Refactoring training script for Katib 
- To understand the training module refactored into docker image for katib, observe the [model_setup](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/training_docker/main.py) function.
- The function is a standalone module which is communicated via args parser through main()
- The Katib YAML digests the image of this script and attaches to the parameters via the args parser
- This can be observed in the [Katib YAML template](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/katib.yaml) from the repo. Here the `--lr` and `--batch_size` are being tuned through Katib

### Integrating Katib into Kubeflow Pipeline

![Docker_Setup](https://user-images.githubusercontent.com/43180442/191949913-6f2e8ba4-53b0-40a0-bc9b-fdd78a3a6a5d.png)


- The Image above explains the Setup of Katib when we want to execute it from inside our Kubeflow Pipeline.
- Katib and the pipeline we run on different pods. To establish a communication the KATIB Pod is initiated from inside the 
- Kubeflow Pipeline. The Component waits for Katib to complete its execution and yield the best model.
- The Best model is then extracted and passed onto the further components of the pipeline.
- To understand the execution please check out the preparation of a KATIB Component from inside a Kubeflow Pipeline [here](https://gitlab.cern.ch/fastsim/kubeflow/geant4-kubeflow-pipeline/-/blob/master/pipeline_components/katib_setup.py).

#### Features of the created Katib Setup
- Automatically submits the YAML file to the Kubeflow Dashboard and create the KATIB Pods without user interference
- The code refactors the KATIB Template created during runtime and thus provides smoother execution of the pipeline
- Selects the Best model from all the experiments and delete the remaining model checkpoints

_The Katib Results looks as follows:_

![katib_trial_visual](https://user-images.githubusercontent.com/43180442/191950013-bf7cd048-5fc5-4e27-946b-631764cf75b9.png)


_The Kubeflow Dashboard also provides a Tabular presentation of experiment details:_

![trials_tabular_katib](https://user-images.githubusercontent.com/43180442/191950051-5409641f-8b01-42b5-a06d-f2dc5dfdd5ec.png)


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




















