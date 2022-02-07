---
title: Ipopt (Interior Point OPTimizer) for ROOT
layout: gsoc_proposal
project: ROOT
year: 2019
organization:
  - CERN
  - OProject
---

## Description
Ipopt (Interior Point OPTimizer)[1] is a software package for large-scale ​nonlinear optimization. It is designed to find (local) solutions of mathematical optimization problems.
Ipopt is now integrated to ROOT framework providing a new set of tools for minization[2] through a ROOT plugin system in the math libraries.

## Task ideas
  * To write support for:
    * Constraint function g(x):Rn−>Rm
    * Gradient of the constraint function
    * Hessian
    * All solvers
    * Compilation under MS Windows with Visual Studio
  * Write tests for all solvers including some of then with Hessian and constrain function.
  * Measure performance comparing the current ROOT minimizers.

## Expected results
Fully integrated Ipopt with support for all solvers, hessian and constrain function. 
Documentation, tests and examples.

## Desirable Skills
  * C++ knowledge.
  * Experience with optimization problems.
  * Experience with ROOT is a plus.

## Mentors
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links
  1. [Ipopt](https://github.com/coin-or/Ipopt)
  2. [Github](https://github.com/oprojects/root/tree/master-ipopt/math/ipopt)
  4. [ROOT Ipopt](http://oproject.org/pages/Ipopt.html)
