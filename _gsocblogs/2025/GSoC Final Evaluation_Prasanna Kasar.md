---
project: ML4EP - TMVA SOFIE
title: Enhancing Keras Parser and JAX/FLAX Integration
author: Prasanna Kasar
photo: blog_authors/PrasannaKasar.jpeg
date: 07.09.2025
year: 2025
layout: blog_post
logo: "[TMVA - SOFIE](https://www.google.com/imgres?q=root%20tmva%20sofie%20logo&imgurl=x-raw-image%3A%2F%2F%2F476d34aa4cdf4014ea93a65d187760a7576a158f8785051edf10d5e4c7968fa6&imgrefurl=https%3A%2F%2Findico.jlab.org%2Fevent%2F459%2Fcontributions%2F11746%2Fattachments%2F9716%2F14215%2FTMVA_SOFIE_%2520CHEP23.pdf&docid=ERFh1aCeXyKOeM&tbnid=FEDfTKo0bUcNfM&vet=12ahUKEwjI0dGK1MaPAxUYzjgGHfFeGxsQM3oECBYQAA..i&w=1282&h=364&hcb=2&ved=2ahUKEwjI0dGK1MaPAxUYzjgGHfFeGxsQM3oECBYQAA)"
intro: |
    Developed parser within SOFIE to parse Machine Learning models trained with Keras. Rewrote the existing parser, which was written C++, in Python. Added support for parsing missing layers such as Pooling and LayerNormalization and wrote unit tests for the parser. 
---

# Final Evaluation Report for GSoC 2025
<img width="1434" height="413" alt="image" src="https://gist.github.com/user-attachments/assets/6b8528de-aeb7-465b-9720-0b8d9d94d9a4" />

## Details

|  |  |
| --- | --- |
| Name | [Prasanna Kasar](https://github.com/prasannakasar) |
| Organisation | [CERN HSF (Root Project)](https://github.com/root-project/root) |
| Mentor | [Sanjiban Sengupta](https://github.com/sanjibansg), [Dr. Lorenzo Moneta](https://github.com/lmoneta)|
| Project | [TMVA SOFIE - Enhancing Keras Parser and JAX/FLAX Integration](https://summerofcode.withgoogle.com/programs/2025/projects/uAjGYhgX) |


## Project Description

The SOFIE (System for Optimized Fast Inference Code Emit) project is an initiative within the TMVA (Toolkit for Multivariate Data Analysis) framework in ROOT, which aims to enhance the efficiency and speed of inference for machine learning models. SOFIE converts ML models trained in different frameworks such as ONNX, PyTorch, and TensorFlow into an Intermediate Representation (IR). This IR allows SOFIE to generate optimized C++ functions for fast and effective inference of neural networks and subsequently convert them into C++ header files, which can be used in plug-and-go style for inference.

## SOFIE's workflow

To reduce the overhead of using multiple frameworks for inference, SOFIE generates unified inference code for models trained with different frameworks.

<img width="512" height="235" alt="image" src="https://gist.github.com/user-attachments/assets/bf1f9c4d-28e4-46c0-bdff-ab5653960512" />

SOFIE has mainly 2 components: Parser and inference code generator.

<img width="867" height="274" alt="image" src="https://gist.github.com/user-attachments/assets/096f2af8-72d4-4551-8fd5-4208f3ed1894" />

SOFIE currently supports parsing mechanisms for ML models built with frameworks such as ONNX, PyTorch, and TensorFlow.

## About SOFIE's Keras Parser

Currently, SOFIE's existing Keras parser is written in C++ and is quite old. Although it's written in C++, the actual parsing logic is implemented in Python. Additionally, it lacks support for parsing layers such as Pooling and LayerNormalization.

## Project Objectives

- Rewrite the Keras model parser in Python, replacing earlier C++ logic to improve modular design and flexibility,
and simplify future extensions
- Extend parser functionality to support Pooling and LayerNormalization layers
- Enable support for Keras 3, while preserving support for Keras 2.x models, ensuring full backward compatibility
- Add support for both types of models i.e. models built using Keras' Functional as well as Sequential API.
- Design comprehensive unit tests for the parser to guarantee robustness and correctness

## Work Accomplished

Since SOFIE's operators are written entirely in C++, we had to leverage ROOT's `Pythonization` functionality, which essentially lets us use SOFIE's C++ object in Pythonic interface.
The overall structure of the parser is very similar to the previous one. The sequence of operations is as follows:
### 1. Load the Keras model

### 2. Instantiate the `RModel` class

### 3. Iterate over the individual layers and extract required information
To create the RModel object, we had to extract layer-specific information such as Layer name, its type (Dense, Convolution, etc.) and its input and output layer name. 
In case of Keras 2.x and models built using Functional API, the output name of the current layer is same as input name for the next layer. But in the case of Keras 3, particularly with models built using Sequential API, this changes, and the input and output names are no more consistent. (This is better explained in here [issue link](https://github.com/keras-team/keras/issues/21599)). So, we used a custom iterator which would iterate over each of the layers and replace the suffix of the input and output name to be perfectly consistent.

Then we had to extract weight's name and some more operator specific information such as in case of Convolutional and Pooling layers, ONNX only supports `channels_first` data format. Whereas Keras supports both i.e. `channels_first` and `channels_last`.
After extracting the layer information for a particular layer we add it to the `rmodel` object.

### 4. Adding layer to `rmodel` object
For all the other operators, the process of adding layer operators to the `rmodel` object is quite easy. But for Convolutional and Pooling layers, its a bit different. For these layers, if the data format is `channels_last`, we have to perform a transpose before and after adding the layer to the `rmodel` object.

### 5. Operator specific functions
To add the layer operators, we create the layer operator in layer specific functions and return it. For this, we make use of the extracted layer information from step [3](#3-iterate-over-the-individual-layers-and-extract-required-information).

### 5. Extract model's weights

### 6. Adding input and output names of the Keras model to `rmodel` object
While adding the input and output names of the Keras model, we need to make sure that we use the new layer iterator, otherwise the layer names would have been inconsistent again.

## How to make sure the parser has backwards compatibility with Keras version 2.x?
Along with parsing support for models trained with Keras 3, we also needed backward compatibility with Keras 2.x. Since Keras 3 introduced significant changes in attribute and layer names and storage formats, we conducted research on the updated versions. For example, the weight names in Keras 3 are no longer unique. Assume a model has 2 dense layers. Previously, with Keras 2.x, the layer weight names would have been 
```
dense/kernel:0
dense/bias:0
dense_1/kernel:0
dense_1/bias:0
```
but with Keras 3, the layer weight names are like this:
```
kernel
bias
kernel
bias
```
To remove the ambiguity, we used weight paths instead of weight names.

After these steps, the parser was in good shape and can be used to parse these layers:

- Add
- AveragePool2D channels first
- AveragePool2D channels last
- BatchNormalization
- Concat
- Conv2D channels first
- Conv2D channels last
- Conv2D padding same
- Conv2D padding valid
- Dense
- Elu
- Flatten
- GlobalAveragePool2D channels first
- GlobalAveragePool2D channels last
- LayerNormalization
- LeakyReLU
- MaxPool2D channels first
- MaxPool2D channels last
- Multiply
- Permute
- Relu
- Reshape
- Selu
- Sigmoid
- Softmax
- Subtract
- Swish
- Tanh

Along the way, we also fixed few minor bugs within SOFIE's ROperator header files.

## About JAX/FLAX parser
Initially, we aimed for JAX/FLAX Integration within SOFIE by researching about models built using its `nnx` and `linen` API, but after a careful discussion with the project mentors we came to the conclusion of focusing the Keras parser itself, by adding support to parse more layers and by writing unit tests for the same.

## Writing Unit Tests
Along with verifying the parsing capability to parse all the supported layers, we also needed to verify the correctness of the generated code. For this we created two functions: 

### 1. To generate and test the inference code
This function takes the file path of model built with keras. Then, it parses the same to the parser. After the parser returns the `rmodel` object, we generate the inference code. Now, we need to verify the correctness of the generated header file. For this, we need to pass a sample input to both the generated header file and the keras model. To avoid hardcoding the shape of the input for each and every model, we extract the input shapes from the Keras model and using it we create the sample input. After this, we pass the sample input and get the resultant output tensor. Since SOFIE always flattens the output tensor before returning it, we also check the output tensor shape from both Keras and SOFIE.

### 2. Validate the accuracy of the result
To validate the inference result from SOFIE, we compare the element-wise values in the output tensor of Keras and SOFIE and make sure that the difference between the results is within a specified tolerance.

## Unit tests
To write the unit tests, we used the `unittest` module within Python as it allows parametrizing those with minimum code repetition. There are two different sets of tests: 1. For models built using Keras' Functional API and 2. For models built using Keras' Sequential API. Within these, there are operator-specific tests which are invoked whenever a sub-test is called. While running the unit tests for both types of models, i.e. Functional and Sequential, temporary directories are created and torn down as soon as both are finished running.

## Pull request status

| Pull Request             | PR Number                               |   Status  |
|--------------------------|-----------------------------------------|-----------|
| New Keras Parser| [#19692](https://github.com/root-project/root/pull/19692) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Merged-orange?style=for-the-badge&logo=appveyor"> |

## Challenges faced and Learning Outcomes
- Faced difficulty while setting up the ROOT project with SOFIE enabled due to missing dependencies and incompatible versions of packages
- Navigated through SOFIE's complex code base 
- Got hands-on experince with Keras, its Functional and Sequential API, and the overall structure of its models
- Improved skills in reading documentation and solving bugs independently.
- Learned how to write concise and modular unit tests 

## Future work
In the future, I would love continuing my contributions to the SOFIE codebase beyond the GSoC period. My current focus is on adding support for parsing the `Conv2DTranspose`, `Dropout` and Recurrent layers.

## Conclusion
I am thankful for my project mentors, Sanjiban Sengupta and Dr. Lorenzo Moneta, for their kind guidance, which made my learning experience enriching and rewarding. They guided me whenever I felt any difficulty. I could ask them the silliest doubt, and they would still answer it happily. I am fortunate to be part of such a wonderful project and contribute to CERN-HSF this summer. I look forward to contributing to CERN-HSF beyond my GSoC project completion. 
Lastly, I would like to thank my seniors from the Open-Source community at my university, Project-X, for introducing me to GSoC and helping me in the pre-GSoC period.

#### Thanks and Regards

#### Prasanna Kasar




