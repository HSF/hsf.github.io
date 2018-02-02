---
title: Profiling reports data warehouse and presentation
layout: gsoc_proposal
project: HSF
year: 2018
organization: CERN
---

## Description

Profiling application performance is one of the critical tasks needed 
in order to optimise HEP workloads. This is usually done using well 
established tools like [Perf](https://perf.wiki.kernel.org/index.php/Main_Page), 
[Google Perf Tools](https://github.com/gperftools/gperftools), 
[Valgrind](http://valgrind.org); or in house tools like 
[igprof](https://igprof.org). Doing the profiling is only part of 
the job though, being able to easy navigate, analyse, correlate and share
the reports accumulated over time is another key factor.

We propose a project where the goal is to implement a prototype for a
HEP-scale, web based, multi-user service for storing, processing and 
visualising profiling reports.

## Task ideas
* Keeping in mind the format of reports, usually a DAG with counters 
  and source code lines associated to them, design a scalable data-warehouse 
  which can host and process time evolving reports from different users.
  This should include a REST based API to allow different users to
  import reports and navigate them.
* Provide a web based GUI, using the above mentioned REST API which 
  allows for ease of navigation of the different reports, overlaying 
  them with the associated project source code.

## Expected results
* A web service where performance profile data can be uploaded,
  visualised and compared.
* The service should be able to support at least IgProf and Google Perf Tools 
  reports. 
 
## Requirements
- Cloud based provisioning tools (e.g. [Kubernetes](https://kubernetes.io/){:_target="_kuberbnetes"})
- Dynamic web based visualisation technology
- Backend database layer

## Mentors 
- [Graeme Stewart](mailto:graeme.andrew.stewart@cern.ch)
- [Giulio Eulisse](mailto:Giulio.Eulisse@cern.ch)

