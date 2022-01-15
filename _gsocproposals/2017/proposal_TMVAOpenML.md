---
title: Integration of TMVA and OpenML platform
layout: gsoc_proposal
project: TMVA
year: 2017
organization: 
 - ITM
 - CERN
---

# Description
[OpenML](https://www.openml.org/) is an open source project that aims to create a novel ecosystem for machine learning experimentation.  It is possible to integrate different machine learning tools through plugins and APIs to share datasets, experiments and results in the platform. The idea is to write an OpenML’s plugin in Java for ROOT, that allows the use TMVA in OpenML, and also create an C++ API for TMVA that lets permits the use of OpenML tools from within ROOT.


## Task ideas
 * Configure an [OpenML server](https://github.com/openml/OpenML/wiki/Local-Installation) in our servers
 * Write a plugin in Java to support ROOT in OpenML
 * Write a C++ API connect to OpenML server from ROOT

**Expected results**: 
 * Working implementation with tests and documentation
 * Server configured with OpenML using the plugin
 * A machine learning example using the plugin and the API
 
**Requirements**: Good skills in C/C++ and Java, experience with machine learning and OpenML.

**Mentors**: 
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Cesar Arias](mailto:cesararias@itm.edu.co)
  * [Diego Gutierrez](mailto:diegogutierez@itm.edu.co)


**Links**:
  * [http://root.cern](http://root.cern)
  * [https://www.openml.org/](https://www.openml.org/)
