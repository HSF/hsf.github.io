---
title: Add support for consteval and constexpr functions in Clad
layout: gsoc_proposal
project: Clad
year: 2023
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of
techniques to numerically evaluate the derivative of a function specified by a
computer program. Automatic differentiation is an alternative technique to
Symbolic differentiation and Numerical differentiation (the method of finite
differences).  Clad is based on Clang which provides the necessary facilities
for code transformation.  The AD library can differentiate non-trivial
functions, to find a partial derivative for trivial cases and has good unit test
coverage.

C++ provides the specifiers consteval and constexpr to allow compile time
evaluation of functions. `constexpr` declares a possibility, i.e the function
will be evaluated at compile time if possible, else at runtime; whereas
`consteval` makes it mandatory, i.e every call to the function must produce a
compile-time constant.
    
The aim of this project is to ensure that same semantics are followed by the
generated derivative function, i.e if the primal function is evaluated at
compile time (because of constexpr or consteval specifier), then the generated
derivative code should also have the same specifier to be evaluatable at compile
time.

This will enable clad to demonstrate the benefits of doing automatic
differentiation directly on C++ frontend to utilize the benefits of clang's
infrastructure.

After successful completion of the project the code snippet should work as
expected:

```cpp
    #include <cstdio>
    #include "clad/Differentiator/Differentiator.h"
    
    constexpr double sq(double x) { return x*x; }
    consteval double fn(double x, double y, double z) {
      double res = sq(x) + sq(y) + sq(z);
      return res;
    }

    int main() {
      auto d_fn = clad::gradient(fn);
      double dx = 0, dy = 0, dz = 0;
      d_fn.execute(3, 4, 5, &dx, &dy, &dz);
      printf("Gradient vector: [%.2f, %.2f, %.2f]", dx, dy, dz);
      return 0;
    }
```


## Project Milestones

* Add support for differentiation with respect to consteval and constexpr
  functions in the forward mode.
* Add support for differentiation with respect to consteval and constexpr
  functions in the reverse mode.
* Extend the unit test coverage.
* Develop tutorials and documentation.
* Present the work at the relevant meetings and conferences.


## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Mentors
* **[Vaibhav Thakkar](mailto:vaibhav.thakkar@cern.ch)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
