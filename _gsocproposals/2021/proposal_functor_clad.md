---
title: Add support for functor objects in clad
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). Clad is based on Clang which provides the necessary facilities for code transformation. The AD library is able to differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage.

Many computations are modelled using functor objects. Usually, a functor object is a lightweight C++ object which has state stored as members and has overridden call operator (operator()). For example:

     struct Functor {
       double x;
       double operator()() { return x * x ;}
     };

     int main () {
       Functor Fn;
       Fn.x = 2;
       double pow2 = Fn();
       auto dpow2_dx = clad::differentiate(Fn, /*wrt*/ 0); // unsupported
       return pow2;
     }

The goal of this project is to modify Clad to handle suhc cases.

## Task ideas and expected results
Implement functor object differentiation in both forward and reverse mode. The candidate should be ready to investigate performance bottlenecks, add test and benchmarking coverage and improve documentation for various parts of clad not only limited to the functor object differentiation support. The student should be prepared to write a progress report and present the results.


## Mentors

  * **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
  * [David Lange](mailto:david.lange@cern.ch)

## Links

  * [CLAD page](https://compiler-research.org/clad/)
  * [Cling](https://rawgit.com/root-project/cling/master/www/index.html)
  * [Clang](http://clang.llvm.org)
  
