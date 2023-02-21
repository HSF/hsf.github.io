---
title: Add support for differentiating with respect to multidimensional arrays (or pointers) in Clad
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

Clad currently only supports differentiation with respect to single-dimensional
arrays. Support for differentiation with respect to pointers is limited as well.
This project aims to add support for multi-dimensional arrays (and pointers) in
Clad.

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

After successful completion of the project the code snippet should work as
expected:
```
#include <iostream>
#include "clad/Differentiator/Differentiator.h"

double fn(double arr[5][5]) {
  double res = 1 * arr[0][0] + 2 * arr[1][1] + 4 * arr[2][2];
  return res * 2;
}

int main() {
  auto d_fn = clad::gradient(fn);
{% raw %}
  double arr[5][5] = {{1, 2, 3, 4, 5},
                      {6, 7, 8, 9, 10},
                      {11, 12, 13, 14, 15},
                      {16, 17, 18, 19, 20},
                      {21, 22, 23, 24, 25}};
{% endraw %}
  double d_arr[5][5] = {};
  d_fn.execute(arr, d_arr);
  std::cout << "Derivative of d_fn wrt arr[0][0]: " << d_arr[0][0] << "\n"; // 2
  std::cout << "Derivative of d_fn wrt arr[1][1]: " << d_arr[1][1] << "\n"; // 4
  return 0;
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
 * **[Vassil Vassilev](mailto:vvasilev@cern.ch)** (Princeton)
 * [Alexander Penev](mailto:alexander.p.penev@gmail.com) (University of Plovdiv Paisii Hilendarski)

## Links

[Compiler-Research](https://compiler-research.org)
[clad](https://github.com/vgvassilev/clad)
[clang-repl](https://root.cern/blog/cling-in-llvm/)
[llvm](https://llvm.org/)
[clang](https://clang.llvm.org/)
