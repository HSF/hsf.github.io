---
title: Improve robustness of dictionary to module lookups in ROOT
layout: gsoc_proposal
project: Compiler-Research
year: 2022
difficulty: high
duration: 175
mentor_avail: May-September
organization: princeton
---

## Description

The LHC smashes groups of protons together at close to the speed of light: 40
million times per second and with seven times the energy of the most powerful
accelerators built up to now. Many of these will just be glancing blows but some
will be head on collisions and very energetic. When this happens some of the
energy of the collision is turned into mass and previously unobserved,
short-lived particles – which could give clues about how Nature behaves at a
fundamental level - fly out and into the detector. Our work includes the
experimental discovery of the Higgs boson, which leads to the award of a Nobel
prize for the underlying theory that predicted the Higgs boson as an important
piece of the standard model theory of particle physics.

CMS is a particle detector that is designed to see a wide range of particles and
phenomena produced in high-energy collisions in the LHC. Like a cylindrical
onion, different layers of detectors measure the different particles, and use
this key data to build up a picture of events at the heart of the collision. The
[CMSSW](https://github.com/cms-sw/cmssw/) is a collection of software for the
CMS experiment. It is responsible for the collection and processing of
information about the particle collisions at the detector. CMSSW uses the
[ROOT](https://root.cern/) framework to provide support for data storage and
processing. ROOT relies on Cling, Clang, LLVM for building automatically
efficient I/O representation of the necessary C++ objects. The I/O properties of
each object is described in a compileable C++ file called a /dictionary/. ROOT's
I/O dictionary system
[relies on C++ modules](https://github.com/root-project/root/blob/master/README/README.CXXMODULES.md)
to improve the overall memory footprint when being used.

The few run time failures in the modules integration builds of CMSSW are due to
dictionaries that can not be found in the modules system. These dictionaries are
present as the mainstream system is able to find them using a broader search.
The modules setup in ROOT needs to be extended to include a dictionary extension
to track dictionary<->module mappings for C++ entities that introduce synonyms
rather than declarations (`using std::vector<A<B>> = MyVector` where the
dictionaries of A, B are elsewhere)


## Task ideas

The project consists of the following tasks:
  * If an alias declaration of kind `using std::vector<A<B>> = MyVector`, we
    should store the ODRHash of it in the respective dictionary file as a
    number attached to a special variable which can be retrieved at symbol
    scanning time.
  * Track down the test failures of CMSSW and check if the proposed
    implementation works.
  * Develop tutorials and documentation.
  * Present the work at the relevant meetings and conferences.

## Technology

C/C++, Clang, LLVM, ROOT

## Desirable Skills

 * Necessary knowledge: C++ programming; data structures and algorithms.
 * Basic knowledge of Clang and LLVM
 * Experience with ROOT would be an asset.

## Expected results

Develop functionality in ROOT's `TCling` and `rootcling` classes which is
capable of storing the `ODRHash` of a `clang::Decl`.

## Candidate Guidelines and Evaluation

If you have interest in working on the project there is a list of things to do
in order to maximize your chances to get selected:

1. Contact the mentors and express interest in the project. Make sure you attach
   your CV;
2. Download the source code of the project, build it and run the demos;
3. Start familiarizing yourself with the codebase;
4. If you have questions you can always contact a mentor.

For an evaluation task please contact the mentors.

## Mentors
 * **[Vassil Vassilev](mailto:vvasilev@cern.ch)** (Princeton)
 * [Alexander Penev](mailto:alexander.p.penev@gmail.com) (University of Plovdiv Paisii Hilendarski)
 * [David Lange](mailto:david.lange@cern.ch) (Princeton)

## Links

[ROOT](https://github.com/root-project/root)
[CMSSW](https://github.com/cms-sw/cmssw/)
[Compiler-Research](https://compiler-research.org)
[clad](https://github.com/vgvassilev/clad)
[llvm](https://llvm.org/)
[clang](https://clang.llvm.org/)
