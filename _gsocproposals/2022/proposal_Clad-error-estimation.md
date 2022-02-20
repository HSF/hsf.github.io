---
title: Broaden the Scope for the Floating-Point Error Estimation Framework in Clad
layout: gsoc_proposal
project: Compiler-Research
year: 2022
difficulty: high
duration: 175
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

Clad also possesses the capabilities of annotating given source code with 
floating-point error estimation code. This allows Clad to compute any 
floating-point related errors in the given function on the fly. This allows 
Clad to reason about the numerical stability of the given 
function and also analyze the sensitivity of the variables involved.

The idea behind this project is to develop benchmarks and improve the 
floating-point error estimation framework as necessary. Moreover, find 
compelling real-world use-cases of the tool and investigate the possibility 
of performing lossy compression with it.

## Task ideas

The project consists of the following tasks:
  * Add support for differentiation with respect to multidimensional arrays
    (and pointers) in the reverse mode.
  * Add support for differentiation with respect to multidimensional arrays
    (and pointers) in the forward mode.
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

On successful completion of the project, the framework should have a
sufficiently large set of benchmarks and example usages. Moreover, the framework
should be able to run the following code as expected:
```cpp
#include <iostream>
#include "clad/Differentiator/Differentiator.h"

// Some complicated function made up of doubles.
double someFunc(double F1[], double F2[], double V3[], double COUP1, double COUP2) {
  double cI = 1;
  double TMP3;
  double TMP4;
  TMP3 = (F1[2] * (F2[4] * (V3[2] + V3[5]) + F2[5] * (V3[3] + cI * (V3[4]))) +
  F1[3] * (F2[4] * (V3[3] - cI * (V3[4])) + F2[5] * (V3[2] - V3[5])));
  TMP4 = (F1[4] * (F2[2] * (V3[2] - V3[5]) - F2[3] * (V3[3] + cI * (V3[4]))) +
  F1[5] * (F2[2] * (-V3[3] + cI * (V3[4])) + F2[3] * (V3[2] + V3[5])));
  return (-1.) * (COUP2 * (+cI * (TMP3) + 2. * cI * (TMP4)) + cI * (TMP3 *
  COUP1));
}

int main() {
  auto df = clad::estimate_error(someFunc);
  // This call should generate a report to decide
  // which variables can be downcast to a float.
  df.execute(args...);
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
 * **[Garima Singh](mailto:garima.singh@cern.ch)** (Princeton/CERN)
 * [Vassil Vassilev](mailto:vvasilev@cern.ch) (Princeton)

## Links

[Compiler-Research](https://compiler-research.org)
[clad](https://github.com/vgvassilev/clad)
[clang-repl](https://root.cern/blog/cling-in-llvm/)
[llvm](https://llvm.org/)
[clang](https://clang.llvm.org/)
