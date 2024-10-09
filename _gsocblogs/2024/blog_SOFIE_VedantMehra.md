---
project: ROOT - TMVA SOFIE
title: Inference Code Generation for Deep Learning models
author: Vedant Mehra
photo: blog_authors/VedantMehra.jpg
date: 09.10.2024
year: 2024
layout: blog_post
logo:
intro: |
    Implemented new Operator classes for SOFIE (System for Optimized Fast Inference code Emit) along with respective operator parsers, tests and onnx models.
    Worked on adapting existing operator classes to be able to parse parametrised shapes with dimension values of input tensors not specified at compile time.
---

# Final Evaluation Report for GSOC 2024

<div align="center">
<img src="https://user-images.githubusercontent.com/84740927/170821829-f631f5f7-c410-429a-acdc-d9cc81d13dd3.jpeg" alt="drawing" width="500"/>
</div> 


## Details

|  |  |
| --- | --- |
| Name | [Vedant Mehra](https://github.com/extint) |
| Organisation | [CERN HSF (Root Project)](https://github.com/root-project/root) |
| Mentor | [Dr. Lorenzo Moneta](https://github.com/lmoneta), [Sanjiban Sengupta](https://github.com/sanjibansg), [Neel Shah](https://github.com/neel-shah-29)|
| Project | [ROOT - TMVA SOFIE Developments - Inference Code Generation for Deep Learning models](https://summerofcode.withgoogle.com/programs/2024/projects/6DDnly0z) |


## Table of Contents

1. [Project Description](#project-description)
2. [SOFIE: System for Optimized Fast Inference code Emit](#sofie-system-for-optimized-fast-inference-code-emit)
3. [GSoC 2024 Objectives](#gsoc-2022-objectives)
4. [Work Accomplished](#work-accomplished)
   - [New Operator Implementations](#1-implementing-New-Operator-Classes)
   - [Extending Existing Operators](#2-adapting-existing-operator-classes-to-parse-parameterized-shapes)
5. [Challenges and Learning Outcomes](#challenges-and-learning-outcomes)
6. [Future Work](#Future-Work)
7. [Conclusion](#conclusion)

## Project Description

The Toolkit for Multivariate Analysis (TMVA) is a part of the ROOT Project, providing a machine learning framework used primarily in High-Energy Physics for tasks like multivariate classification and regression. Given the massive data output (often reaching petabytes daily) from research activities, and the need for fast, real-time predictions, a highly efficient inference engine is necessary for using trained machine learning models regularly. With this objective SOFIE (System for Optimized Fast Inference code Emit) was developed.

### SOFIE (System for Optimized Fast Inference code Emit)
ROOT/TMVA SOFIE generates C++ functions easily invokable for the fast inference of trained neural network models. It takes ONNX model files as inputs and produces C++ header files that can be included and utilized in a “plug-and-go” style.

```c
// This generates a .hxx file containing the C++ code for model inference.
using namespace TMVA::Experimental;
SOFIE::RModelParser_ONNX Parser;
SOFIE::RModel model = Parser.Parse("./example_model.onnx");
model.Generate();
model.OutputGenerated("./example_output.hxx");
```

SOFIE uses BLAS or Eigen for executing the inference and Protobuf3 to parse ONNX files. It features two main classes: ```RModel``` for holding model data and ```ROperator``` for handling ONNX operations and generating inference code. Another sub-directory, `sofie-parsers`, was added under TMVA to include the ONNX parser, RModelParser_ONNX. This parser reads ONNX files, loads their values into an RModel object, and returns it. It creates an intermediate representation of the model and outputs a C++ header file with an infer function that can be directly used in production environments.

![flowchart_sofie](https://raw.githubusercontent.com/extint/gsoc24-blog/main/assets/Blank%20board%20-%20Page%201.png)

## Objective for GSoC24

The two main objectives for my GSoC period were the following:
1. Implement operator classes for the missing operators from Transformer models used in LHC experiments used at CERN for eg. particle-net.
2. Extend existing Operator classes to support fully dynamic (parameterised shapes) eg. (`input1_dim1 x input1_dim2` + `input2_dim1 x input2_dim2` -> ```out_dim1 x out_dim2```)

## Work Accomplished
The initial time during the community bonding period was spent on understanding the codebase of specifically SOFIE and planning the priority of the operators and tasks to be implemented.
I began working on the high priority operators after discussing with my mentors. We would have biweekly meets wherein all teams at CERN who were contributing in the domain of machine learning would provide updates on the tasks achieved and so would I regarding my GSoC project. I maintained regular communication with my mentors via Mattermost and arranged Zoom meetings as needed to address and resolve any issues.

 ### 1. Implementing New Operator Classes

   #### Constant Operator
   - I began with the implementation of the `Constant` operator and wrote the initial tests, which ran successfully. However, I soon realized that the constant operator wasn't as simple as I thought. I expected the constant operator to be a simple operator where the input tensor was simply returned as the output tensor to the next node. I addressed this issue with my mentor Lorenzo, and we realized that the output of the constant operators is like initialized tensors and not intermediate output tensors, causing subsequent operators to fail to receive any input. 

   - The issue was fixed over a few iterations by introducing a new flag and checking it while initializing tensors. [[Code]](https://github.com/lmoneta/root/commits/tmva_sofie_constant_op/)

   - *ONNX Documentation*: [Constant](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Constant)


   | Pull Request             | PR Number                               |   Status  |
   |--------------------------|-----------------------------------------|-----------|
   | Constant Operator        | [#15837](https://github.com/root-project/root/pull/15837) | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

   - Alongside, existing issues with the `ConstantOfShape` and `Reduce` operators were also fixed by my mentor Lorenzo.

---

#### TopK Operator
- Next, I implemented the `TopK` operator class and its respective tests. This was one of the more challenging implementations since I was in the process of understanding the utility functions of SOFIE. The `ROperator_TopK` operator extracts the top `K` values and their corresponding indices along a specified axis from an input tensor. It can return either the largest or smallest values based on configuration and allows sorting of the results. The `Generate` method iterates over the specified axis, retrieves either the largest or smallest values based on configuration, sorts them if required, and stores the results in output tensors for both values and indices.

- *ONNX Documentation*: [TopK](https://github.com/onnx/onnx/blob/main/docs/Operators.md#TopK)

| Pull Request             | PR Number                               |   Status  |
|--------------------------|-----------------------------------------|-----------|
| TopK Operator            | [#16313](https://github.com/root-project/root/pull/16313/commits/dea1a482e4ebd1402ba13187769f90f9164aa6b5) | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

---

#### Tile Operator
- I then began working on the `Tile` Operator to parse the particle-net model. I completed the brute-force implementation of the operator class as parsing the model was a priority. The tests, along with the model, were also included. The `ROperator_Tile` replicates an input tensor based on a provided repeats tensor along each dimension. It calculates the shape of the output tensor by multiplying the dimensions of the input tensor by the corresponding values from the `repeats` tensor. The `Generate` method iterates over the output tensor, mapping each output element to the appropriate input element using index modulations, effectively "tiling" the input tensor over the output tensor.

- As per the ONNX Operator [documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#tile), the Tile Operator has two input tensors: `input` and `repeats`. My current implementation of the operator class requires the `repeats` tensor to be pre-initialized with data to compute the shape of the output tensor at compile time.

- *ONNX Documentation*: [Tile](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Tile)

| Pull Request             | PR Number                               |   Status  |
|--------------------------|-----------------------------------------|-----------|
| Tile Operator            | [#16313](https://github.com/root-project/root/pull/16313/commits/776f06fa90564e47d2be59021dd74e3c85e41b3f) | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

---

#### Split Operator
- I implemented the `Split` operator along with tests. The `ROperator_Split` divides a tensor along a specified axis into multiple output tensors. It checks the axis and determines the output shapes either by evenly splitting the tensor or using a "splits" tensor for unequal divisions. The `Generate` method handles the actual tensor splitting by iterating over the input tensor and assigning slices to the output tensors based on computed offsets along the specified axis.

- The particle-net model did not require the complete version of the implementation; hence, the basic 1D version of the `Split` operator was merged and used to parse the model. The complete version of the implementation can be found [here](https://github.com/extint/root/commit/a731822e7cf109b026be39606fbf89d7b8e76433).

- *ONNX Documentation*: [Split](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Split)

| Commit             | Link |   PR Status  |
|--------------------------|-----------|-----------|
| Split Operator           | [Code](https://github.com/extint/root/commit/a731822e7cf109b026be39606fbf89d7b8e76433)     |  <img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-yellow?style=for-the-badge&logo=appveyor"> |

---

#### Sin and Cos Operators
- After successfully parsing the particle-net model using SOFIE, I implemented the basic trigonometric operators: `sin` and `cos`, along with their tests. The `ROperator_Sin` and `ROperator_Cos` classes apply the sin and cos functions element-wise to an input tensor. During initialization, the shape and type of the input tensor are retrieved. The `Generate` function iterates over the elements of the input tensor, applying the sin or cos function to each element and storing the result in the output tensor, maintaining the same shape and type as the input tensor.

- *ONNX Documentation*: [Sin](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Sin) / [Cos](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Cos)

| Commit             | Link |   PR Status  |
|--------------------------|-----------|-----------|
| Sin, Cos Operator        | [Code](https://github.com/extint/root/commit/547953565036083429576f5970520b848d373596)       |  <img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-yellow?style=for-the-badge&logo=appveyor"> |

---

#### Clip Operator
- The `Clip` operator was straightforward to implement. It constrains the values of the input tensor within a specified range defined by minimum and maximum thresholds. The `Generate` function iterates over the input tensor, comparing each value against the defined limits and setting it to the minimum or maximum as needed, thus ensuring the output values fall within the specified range.

- *ONNX Documentation*: [Clip](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Clip)

| Commit             | Link |   PR Status  |
|--------------------------|-----------|-----------|
| Clip Operator            | [Code](https://github.com/extint/root/commit/1b5c92244ebd5074400fdc8e836f09c79bcf83d5)         |  <img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-yellow?style=for-the-badge&logo=appveyor"> |

---

#### RandomNormalLike Operator
- Lastly, I implemented the `RandomNormalLike` operator. The `ROperator_RandomNormalLike` class generates random values following a normal distribution based on the shape and type of an input tensor. During initialization, it retrieves the input tensor's shape, infers the output type, and sets a random seed if not provided. The `Generate` function uses `std::normal_distribution` to fill the output tensor with random values according to the specified mean and scale.

- *ONNX Documentation*: [RandomNormalLike](https://github.com/onnx/onnx/blob/main/docs/Operators.md#RandomNormalLike)

| Commit             | Link |   PR Status  |
|--------------------------|-----------|-----------|
| RandomNormalLike Operator | [Code](https://github.com/extint/root/commit/9c09312923e6dd8e94e82bc751910aef46ac12b2) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-yellow?style=for-the-badge&logo=appveyor"> |

---

### 2. Adapting Existing Operator Classes to Parse Parameterized Shapes

The main logic to parse the dynamic tensors involved shifting any computation requiring available input tensor data to runtime. This approach introduced overhead at runtime but seemed the only way to achieve the objective.

#### Binary and Unary Operators
- I began with something simpler and extended the operator classes for the `Binary` and `Unary` Operators. An issue I faced was supporting broadcasting at runtime, which was required as per the documentation, but I eventually managed it successfully and wrote appropriate tests for the same.

- *ONNX Documentation*: [Binary](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Add) / [Unary](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Abs)

| Pull Request             | PR Number                               |   Status  |
|--------------------------|-----------------------------------------|-----------|
| Binary and Unary Operators| [#16012](https://github.com/root-project/root/pull/16012) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Merged-orange?style=for-the-badge&logo=appveyor"> |

---

#### BatchNormalization Operator
- I also extended the `BatchNormalization` operator to parse parameterized input shapes. The entire computation required to calculate the expected output dimension from the input tensor shapes had to be shifted to runtime.

- *ONNX Documentation*: [BatchNormalization](https://github.com/onnx/onnx/blob/main/docs/Operators.md#BatchNormalization)

| Pull Request             | PR Number                               |   Status  |
|--------------------------|-----------------------------------------|-----------|
| BatchNormalization Operator | [#16012](https://github.com/root-project/root/pull/16012) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Merged-orange?style=for-the-badge&logo=appveyor"> |

---

#### Concat Operator
- I addressed an issue with the existing implementation of the `Concat` operator. I discovered it couldn't parse input tensors with parameterized shapes for all `axis` tensor values. Hence, I generalized the implementation and included the necessary tests and models. [Commit Link](https://github.com/extint/root/commit/51804d9c0c6c08378e81b1935ecd88c11821d9a5).

- *ONNX Documentation*: [Concat](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Concat)

---

## Challenges and Learning Outcomes

- Navigated a steep learning curve due to SOFIE's complex codebase
- Gained experience working in continuous integration environments
- Improved skills in clear commit and PR organization - overall git management
- Enhanced communication and presentation skills

## Future Work

As I look toward the future, I am committed to continuing my contributions to the SOFIE codebase beyond the GSoC period. My current focus is on the implementation of the `Einsum` operator, which will allow for concise and powerful tensor operations. This operator is critical for various machine learning tasks.

In addition to the `Einsum` operator, I also plan to implement the `Loop` and `Where` operators. The `Loop` operator will handle recurrent computations, allowing for more complex workflows with dynamic input sizes. The `Where` operator will enable conditional selection from tensors, making it useful for element-wise operations based on specific conditions.

I am keen to continue contributing to the project, going ahead beyond the GSoC period.

## Conclusion
Working at CERN this summer was both productive and rewarding. The learning curve for SOFIE was steep initially due to the complexity of the codebase, but with the guidance of my mentors, I gradually got into the flow. The project became more manageable as I progressed. Beyond the technical goals, I gained valuable experience working in a continuous integration environment, ensuring my commits and PRs were clear and well-organized, and maintaining effective communication with my mentors.

Knowing that the code we worked on will be used in real-life high-energy physics experiments at CERN was a huge motivator. Finally being able to parse models like ParticleNet was especially fulfilling.

I would like to express my heartfelt gratitude to my mentors for their patience and support throughout this process. They understood my university commitments and adjusted timelines accordingly. Additionally, I want to thank my friends and seniors at Project X, an Open-Source AI-ML club at my university (VJTI) for their guidance and encouragement, which helped me navigate through GSoC 2024.
 

**Thanks and Regards,**

**Vedant Mehra**