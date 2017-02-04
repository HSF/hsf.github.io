---
title: Improvement of the TestU01 Suite for PseudoRandom Number Generation
layout: plain
project: TestU01
organization:
  - CERN
  - UMONTREAL
---

# Description
The TestU01 suite is an established suite of empirical tests for pseudorandom number generators. It has been used since 200x as a litmus test for potential PRNG algorithms and implementations.  Given the power of current computers, the length of the tests only probes number sequences which can be generated in tens of minutes on the fastest machines. The idea of this project is to select a larger set of configurations, improve the implementations and create a new 'standard' for tests of PRNGs.


## Potential project topics 
 * Creating a 64-bit version of the software, so that more than 32 bits of the output values are tested.
 * Use faster algorithms ot improve the implementation of certain tests.
 * Design and implement specific tests for parallel RNGs.
 * Construct a parallel version of TestU01, that can run on parallel  processors.

## References: 
[1] P. L'Ecuyer and R. Simard. TestU01: A C library for empirical  testing of random number 
generators. ACM Transactions on Mathematical Software, 33(4):Article 22,  August 2007. 

**Mentors**: 
 * John Apostolakis sft-gsoc@cern.ch
 * Pierre L'Ecuyer sft-gsoc@cern.ch
 
**Web page**: http://simul.iro.umontreal.ca/testu01/tu01.html 
**Source code:**  http://simul.iro.umontreal.ca/testu01/tu01.html
