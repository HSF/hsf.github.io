---
title: Enable CUDA compilation on Cppyy-Numba generated IR
layout: gsoc_proposal
project: Cppyy
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Cppyy is an automatic, run-time, Python-C++ bindings generator, for calling C++ from Python and Python from C++. Initial support has been added that allows Cppyy to hook into the high-performance Python compiler, Numba which compiles looped code containing C++ objects/methods/functions defined via Cppyy into fast machine code.

Since Numba compiles the code in loops into machine code it crosses the language barrier just once and avoids large slowdowns accumulating from repeated calls between the two languages. Numba uses its own lightweight version of the LLVM compiler toolkit (llvmlite) that generates an intermediate code representation (LLVM IR) which is also supported by the Clang compiler capable of compiling CUDA C++ code.

This project aims to demonstrate Cppyy's capability to provide CUDA paradigms to Python users without any compromise in performance. Upon successful completion a possible proof-of-concept can be expected in the below code snippet:

```python
import cppyy
import cppyy.numba_ext

cppyy.cppdef('''
__global__ void MatrixMul(float* A, float* B, float* out) {
    // kernel logic for matrix multiplication
}
''')

@numba.njit
def run_cuda_mul(A, B, out):
    # Allocate memory for input and output arrays on GPU
    # Define grid and block dimensions
    # Launch the kernel
    MatrixMul[griddim, blockdim](d_A, d_B, d_out)	
```

## Project Milestones

* Add support for declaration and parsing of Cppyy-defined CUDA code on the Numba extension.
* Design and develop a CUDA compilation and execution mechanism.
* Prepare proper tests and documentation.

## Requirements

* C++ programming and familiarity with CUDA C++
* Python programming
* Knowledge of LLVM IR is an advantage

## Mentors
* **[Aaron Jomy](mailto:aaron.jomy@cern.ch)**
* [Wim Lavrijsen](mailto:wlavrijsen@lbl.gov)
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/wlav/cppyy)
