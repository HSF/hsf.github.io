---
title: Add initial integration of Clad with Enzyme
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
coverage. Enzyme is a prominent autodiff framework which works on LLVM IR. 

Clad and Enzyme can be considered as a C++ frontend and a backend automatic
differentiation framework. In many cases, when clad needs to fall back to
numeric differentiation it can try configuring and using Enzyme to perform the
automatic differentiation on lower level.


## Task ideas and expected results

Understand how both systems work. Define the Enzyme configuration requirements
and enable Clad to communicate efficiently with Enzyme. That may require several
steps: start building and using the optimization pass of Enzyme as part of the
Clad toolchain; use Enzyme for cross-validation derivative results; etc. The
student should be prepared to write a progress report and present the results.

## Necessary skills

Intermediate C++; Understanding basic differential calculus; intermediate
knowledge of clang and llvm.

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
  * **[William Moses](mailto:wmoses@mit.edu)** (MIT)
  * [Vassil Vassilev](mailto:vvasilev@cern.ch) (Princeton)

## Links
  * [clad](https://github.com/vgvassilev/clad)
  * [clad gsoc page](https://github.com/vgvassilev/clad/wiki/GSoC-2022)
  * [enzyme](https://github.com/EnzymeAD/Enzyme)
  * [enzyme web](https://enzyme.mit.edu)
  * [clang](http://clang.llvm.org/)
  * [llvm](http://llvm.org/)
