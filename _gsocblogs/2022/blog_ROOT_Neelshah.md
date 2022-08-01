---
project: ROOT
title: Inference of Deep Learning models in TMVA/SOFIE
author: Neel Shah
photo: blog_authors/NeelShah.jpg 
date: 24.07.2022 
year: 2022 
layout: blog_post 
logo: ROOT-logo.png 
intro: |
   Currently, we are developing a fast inference system in TMVA, called SOFIE, that takes ONNX model as input and produces compilation-ready standalone C++ scripts as output. These scripts will then provide users an easy way to deploy their deep learning models in their physics software and analysis frameworks. This project focuses on the development of some missing deep learning operations which will allow to build more complex networks within TMVA. Specifically, we propose to implement the inference functionality of some ONNX operators in the code generation format. 
---

# Mid Evaluation Blog for GSOC 2022

## Pre-GSOC Period
Getting into GSOC was my dream since my college years, On May 20, I was so delighted when I got into my preferred Project in one of the most competitive Organisations. I will forever remember those sleepless nights spent solving those tasks, debugging, and building the project !!
I have prepared a detailed blog on how I got into GSOC 2022 at CERN HSF in detail [here](https://gist.github.com/Neel-Shah-29/3f04f05a8a353605068e32e55a5093c1)


## Community Bonding Period

<div align="center">
<img src="https://miro.medium.com/max/1200/1*YvvzCmO4dbCPeTPOq7_OKA.png" alt="drawing" width="500"/>
</div>

This is the period of time between when accepted GSoC contributors are announced and the time they are expected to start coding. This time is an excellent one to introduce your GSoC contributors to the community, get them on the right mailing lists, introduce them to the codebase, discuss how they will work with their mentors on their timeline for the program, etc.

Again I have written a very detailed blog on Community Bonding Period [here](https://gist.github.com/Neel-Shah-29/b2c887adaa118ba68b42e324d3b2a47a).

### Brief Description of Work Done\:

- For TMVA projects we usually have weekly meetings to discuss about the projects and solve the difficulties of everyone. So attending those meetings are mandatory as it involves your communication with other gsoc students of TMVA. Also the round table discussion solves all queries which you have as all the students and mentors give solutions and guidelines on it. Additionally we can also set a meeting with the mentor if required.

- In TMVA projects, we have a specific idea of presenting our projects with the detailed timeline of implementation in front of mentors and other Gsoc students so we can get familier with other's project as well and by that time our concrete strategy of project is also ready.

  Here is my presentation for reference\: [Inference Code Generation for Deep Learning models](https://docs.google.com/presentation/d/1bl1Xk5esr5TJEHKoro7o05pRQ2J997Qb1hc68XfU_0s/edit?usp=sharing)

- I built and set up the Root environment in my laptop as required. [Here](https://root.cern/install/build_from_source/) is the link to build Root from source.

- Finalised the evaluation dates so that i get enough time to complete my long term project. I chose a 16 weeks project after discussing with the mentor as my college reopens from July 18 and i will get less time to devote after that. 

- I have also contributed to fusing of Add and the MatMul operators in a Gemm Operator
 Our task was to Implement the capability to parse the MatMul and Add operators together and fuse them in a Gemm operator in the TMVA SOFIE parser (RModelParser_ONNX.cxx) .
So basically we take  the data of  MatMul operator and if we get Add operator exactly after the MatMul operator , we fuse both the Add and the MatMul operators and give their data to Gemm operator. Gemm operator is explained [here](https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/) in detail.
This improvement was added by my mentor Lorenzo Moneta in his PR , the link to my commit can be found [here](https://github.com/root-project/root/pull/10315/commits/fda26827ecfc76c23b2e4b634d8cf54c5cabf8dc).

- Lastly, I began coding part for one of the easy operator which is Leaky Relu so i get an headstart for the Project. Here is the link to the 
[PR](https://github.com/root-project/root/pull/10415).

**Pro-Tip** \: Use this Period very well to connect with your mentors, other Gsoc Candidates and the organisation as a whole!

## Coding Period 

#### 1) Finalise the **Leaky Relu PR** which was sent during Community Bonding Period. 
I have written a detailed blog for the Leaky Relu Operator implementation as well. [Here](https://gist.github.com/Neel-Shah-29/f0371566ca1e24a6b3a9b4097cdd44db) you can find the detailed description of the Operator.
Here, I will provide a brief Description about it.

- **Definition** \: [Leaky Relu ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#LeakyRelu)

- Fix warning related to length in compiled code when there are no initialized tensors
```
build/build/tmva/sofie/test/LinearWithLeakyRelu_FromONNX.hxx:24:8: warning: unused variable ‘length’ [-Wunused-variable]
```
It was general for all SOFIE operators not having a weight tensor. It is resolved by applying a small fix, we directly return when the tensors are not initialized.

``` 
if (fInitializedTensors.empty()) return;
```

- **PR Status**\:

| Pull Request| PR Number |   Status     |
| :---        |    :----:   |          ---: |
| Leaky Relu ONNX Operator | [#10415](https://github.com/root-project/root/pull/10415)       | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

#### 2) Fix the implementation of **Max Pool ONNX Operator for 1D and 3D cases.**

- **Definition** \: [Max-Pool ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#MaxPool)

- MaxPool ONNX Operator was only supported for the 2D case, i.e 4d tensors but i need to extend its support for the 1D and 3D cases as well.

- Earlier it was giving a runtime error for 1d and 3d cases of Max Pool operator.

- Error is described in the image mentioned below. I resolved the error by extending the support of Maxpool Operator for 3d and 5d tensors as well.

![image](https://user-images.githubusercontent.com/84740927/180577234-b23267c8-12b0-4970-a730-e22755fc0dcb.png)

- I also added the Unit Tests for MaxPool 1D, MaxPool 2D, MaxPool 3D and the Average Pool Operators.

- **PR Status**\:

| Pull Request| PR Number |   Status     |
| :---        |    :----:   |          ---: |
| Max Pool ONNX Operator | [#10768](https://github.com/root-project/root/pull/10768)       | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |


#### 3) Implemented all the 4 Basic Binary Operators\: Add,Sub,Mul and Div with the corresponding Unit Tests.

- **Definition** \: 
 1. [Add ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Add)
 2. [Sub ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Sub)
 3. [Mul ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Mul)
 4. [Div ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Div)
 
- I have implemented the four Basic Binary operators in a single file, they all are declared in an enum and we have used Type traits for making the code more modular and reusable. Below is the code sample for the same.

- I also implemented the **Multi-Directional Broadcasting** for SOFIE.

The following is the algorithm and its implemented in the SOFIE_common.cxx.
    
CASE-1\:The tensors all have exactly the same shape. : We support it already now

CASE-2\:The tensors all have the same number of dimensions and the length of each dimensions is either a common length or 1.
**Example\:** This is the example for two tensors as (2,3,4)  and (1,3,4) the result is (2,3,4)  

CASE-3\: The tensors that have too few dimensions can have their shapes prepended with a dimension of length 1 to satisfy CASE-2. **Example\:** This is the case for (3,4,5) and (2,1,1,1). Here we transform first tensor to (1,3,4,5) and the is like case 2 above. The result is (2,3,4,5)

So the algorithm should do: 
```
CASE-1\: Check if tensor have same shape - nothing special to do, we already supported it.

CASE-2 and CASE-3 \: If shape is different we call the multi-directional broadcasting function.

CASE-3 \: if shapeA .size() < shapeB.size() we insert in the shape vector values of 1 at the beginning of the tensor until shapeA.size() == shapeB.size()
CASE-2 \: We look then to the shape values, and if they are equal result is same, if shapeA[i] not equal to shapeB[i] we have the result shape equal to shapeA[i] if shapeB[i] = 1 or shapeB[i] if shapeA[i] = 1.
```

- **PR Status**\:

| Pull Request| PR Number |   Status     |
| :---        |    :----:   |          ---: |
| Basic Binary ONNX Operator | [#10822](https://github.com/root-project/root/pull/10822)       | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

#### 4) Implemented the Tanh ONNX operator with the corresponding unit tests.

- **Definition\:** [Tanh ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Tanh)

- For tanh activation function we require `cmath` library to support the tanh operator. So we add the required libraries in `RModelParser_ONNX.cxx` in the Parse method.
```C++
  if (op_type == "Tanh")
    rmodel.AddNeededStdLib("cmath");
```

- **PR Status**\:

| Pull Request| PR Number |   Status     |
| :---        |    :----:   |          ---: |
| Tanh ONNX Operator | [#10913](https://github.com/root-project/root/pull/10913)       | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

#### 5) Implemented the Neg ONNX operator with the corresponding unit tests.

- **Definition\:** [Neg ONNX Documentation](https://github.com/onnx/onnx/blob/main/docs/Operators.md#Neg)

- **PR Status**\:

| Pull Request| PR Number |   Status     |
| :---        |    :----:   |          ---: |
| Neg ONNX Operator | [#10946](https://github.com/root-project/root/pull/10946)       | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

## Some Useful Blogs written by me.
1) [Python Tutorials for various C files of Tutorials/TMVA](https://gist.github.com/Neel-Shah-29/7e46bee55f7c09a18e94696a0a3e5ccf)
2) [Documentation on RModelParser_ONNX.cxx](https://gist.github.com/Neel-Shah-29/5c1399ccd23903928128822c6f3e0957)
3) [Getting into GSOC 2022](https://gist.github.com/Neel-Shah-29/3f04f05a8a353605068e32e55a5093c1)
4) [All about Community Bonding Period](https://gist.github.com/Neel-Shah-29/b2c887adaa118ba68b42e324d3b2a47a)
5) [Implementing the Operators in Sofie](https://gist.github.com/Neel-Shah-29/f0371566ca1e24a6b3a9b4097cdd44db)
6) [Mid Evaluation Detailed Report](https://gist.github.com/Neel-Shah-29/d51a9038dd07ef096127a62a92113fa0)

## Proposal Link \: [Inference Code Generation for Deep Learning models](https://docs.google.com/document/d/1tvTY9Rq5j0XW8KFfvkWHWlmE__-94h-Nj0tCkMjYnzs/edit?usp=sharing)

## Conclusion
I enjoyed a lot working on this project! I would like to really thank my mentors **Lorenzo Moneta, Sitong An, Omar, Ahmat Hamdan, and Sanjiban Sengupta** for always being a great support for me. Whenever I wanted any help or guidance, they were always with me! I am very proud to be associated with so many bright minds surrounding me, and every single day I learn something new from them. In the end, I am able to achieve all of my success because of the best wishes of my parents, seniors, and friends so a big thanks to them as well.

Hope you all enjoyed reading my blog and learnt a lot.

**Thanks and Regards,**

**Neel Shah**