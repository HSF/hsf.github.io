---
title: Implement vector mode in forward mode automatic differentiation in Clad
layout: gsoc_proposal
project: Compiler-Research
year: 2022
difficulty: high
duration: 350
mentor_avail: May-September
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of
techniques to numerically evaluate the derivative of a function specified by a
computer program. Automatic differentiation is an alternative technique to
Symbolic differentiation and Numerical differentiation (the method of finite
differences). Clad is based on Clang which provides the necessary facilities for
code transformation. The AD library is able to differentiate non-trivial
functions, to find a partial derivative for trivial cases and has good unit test
coverage.

Vector mode support will facilitate the computation of gradients using the
forward mode AD in a single pass and thus without explicitly performing
differentiation n times for n function arguments. The major benefit of using
vector mode is that computationally expensive operations do not need to be
recomputed n times for n function arguments.

For example, if we want to compute `df/dx` and `df/dy` of a function
`f(x, y)` using the forward mode AD in Clad, then currently we need to
explicitly differentiate `f` two times. Vector mode will allow the generation of
`f_d(x, y)` such that we will be able to get partial derivatives with respect to
all the function arguments (gradient) in a single call.

## Task ideas

The project consists of the following tasks:
  * Extend and generalize our ForwardModeVisitor to produce a single
    function with the directional derivatives.
  * Add a new mode to the top-level clad interface `clad::differentiate` for
    vector mode.
  * Extend the unit test coverage.
  * Develop tutorials and documentation.
  * Present the work at the relevant meetings and conferences.

## Technology

C/C++, Clang, LLVM

## Desirable Skills

 * Necessary knowledge: C++ programming; data structures and algorithms.
 * Intermediate knowledge of automatic differentiation;
 * Basic knowledge of Clang and LLVM
 * Experience with Clad would be an asset.

## Expected results

After successful completion of the project the code snippet should work as
expected:
```cpp
#include <clad/Differentiator/Differentiator.h>
#include <iostream>

double someComputationalIntensiveFn();

double fn(double x, double y) {
  double t = someComputationalIntensiveFn(); // should be computed only once
                                             // in the derived function.
    double res = 2 * t * x + 3 * t * x * y;
    return t;
  }

  int main() {
    auto d_fn = clad::differentiate(fn, "arr");
    double d_x = 0, d_y = 0;
    d_fn.execute(3, 5, &d_x, &d_y);
    std::cout << "Derivative of fn wrt d_x: " << d_x << "\n";
    std::cout << "Derivative of fn wrt d_y: " << d_y << "\n";
  }
```

## Candidate Guidelines and Evaluation

If you have interest in working on the project there is a list of things to do
in order to maximize your chances to get selected:

1. Contact the mentors and express interest in the project. Make sure you attach
   your CV;
2. Download the source code of the project, build it and run the demos;
3. Start familiarizing yourself with the codebase;
4. If you have questions you can always contact a mentor.

The mentors are interested in working with all candidates but unfortunately the
rules allow only one to be selected. There are a few tasks which give bonus
points to candidate's application:
 * Submit a valid bug -- demonstrates that the candidate has completed step 2
   and 3 from the previous section.
 * Fix a bug -- demonstrates the technical skills of the candidate and shows
   he/she can work independently on the project. The mentors can suggest looking
   into these [good first issues](https://github.com/vgvassilev/clad/labels/good%20first%20issue).
   Fixing one issue may be enough to become a successful candidate.

## Mentors
 * **[Alexander Penev](mailto:alexander.p.penev@gmail.com)** (University of Plovdiv Paisii Hilendarski)
 * [Vassil Vassilev](mailto:vvasilev@cern.ch) (Princeton)

## Links

[Compiler-Research](https://compiler-research.org)
[clad](https://github.com/vgvassilev/clad)
[clang-repl](https://root.cern/blog/cling-in-llvm/)
[llvm](https://llvm.org/)
[clang](https://clang.llvm.org/)
