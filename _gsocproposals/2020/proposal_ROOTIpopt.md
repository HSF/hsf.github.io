---
title: Ipopt (Interior Point OPTimizer) for ROOT
layout: gsoc_proposal
project: ROOT
year: 2020
organization:
  - CERN
  - OProject
---

## Description
Ipopt (Interior Point OPTimizer)[1] is a software package for large-scale ​nonlinear optimization. It is designed to find (local) solutions of mathematical optimization problems.
Ipopt is being integrated to ROOT framework providing a new set of tools for minimization through a ROOT plugin system in the math libraries. 
The goal of the project will be to fully integrate in ROOT ipopt, to include the support for optimization with non trivial parameter  constraints and to provide tests and code examples showing users how to use the new optimizers. 

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
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)

## Links
  1. [Ipopt](https://projects.coin-or.org/Ipopt)
  2. [Github](https://github.com/oprojects/root/tree/master-ipopt/math/ipopt)
  3. [Ipopt MultiMin](http://clusteri.itm.edu.co/rootdoc/html/group__MultiMin.html)
  4. [ROOT Ipopt](http://oproject.org/pages/Ipopt.html)
  5. [Ipopt Solvers](https://www.coin-or.org/Ipopt/documentation/node51.html)
