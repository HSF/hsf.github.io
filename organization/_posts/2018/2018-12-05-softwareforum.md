---
title: "Spark based analysis for LSST and HEP, December 5, 2018"
layout: meetings
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/754811/)

Introduction
------------
-   Reminder about the [*HSF/OSG/WLCG
    Workshop*](https://indico.cern.ch/event/759388/), 18-22 March 2019
    at JLab.
    -   We hope to open registration this week.
-   HSF intends to submit a short (1 page) paper to the European
    Strategy for Particle Physics Review Process.
    -   Will be circulated tomorrow for 1 week.
-   New working groups are up and running.
    -   Will have a report from the convenors in next week’s HSF
        Coordination meeting.

Analyzing astronomical data with Apache Spark
---------------------------------------------
-   Simulation data can be N-body simulations of the evolution of the
    universe.
-   An object for LSST is anything that can be “labeled” on the sky:
    -   Like a data frame row - with 100 or 1000 columns (position,
        redshift, spectra, …)
    -   Data is flatter than in particle physics (usually completely
        flat in the final catalogue).
-   FITS data does not fit “naturally” into Spark, but have written an adaptor.
-   Performance test was for \~small data elements (5 doubles); total
    size 100GB.
-   The schema for the dataset is fixed for each case; but see issues when
    many input files are used (causing the metadata bottleneck).
-   3D spatial data not well supported in Spark ecosystem.
    -   Most packages work with 2D data.
-   Re-partitioning in space is only one option - in general want to be
    able to repartition on arbitrary metrics:
    -   Need to build partition and then shuffle the data (2 phases).
    -   UDF = User Defined Function - this is difficult to optimise as
        it’s a black box for Spark.
-   For C/C++ interfaces how to serialise?
    -   Contact Christan Arnault for this.
-   Training - how can people run the tutorials?
    -   Targeting LSST people and they mostly have NERSC accounts where
        clusters are available. LAL cluster also available (which may
        expand if it proves popular).
-   For partitioning, isn’t Spark specifically designed for this kind of
    task?
    -   For a lot of cases Spark does do a good job, but if the data has
        structures that were not known at data loading time then the
        map/reduce workflow performs poorly when the output is as
        large as the input.
    -   Q. Problem with the memory usage? Is the algorithm optimal?
        - Default Spark partitioning is not doing so well, hence
          the O(N^2) scaling seen.

Distributed data analysis with ROOT RDataFrame and Spark
--------------------------------------------------------
-   Working with ROOT to establish working model for analysis for FCC
    levels of data.
-   In this case Spark does not do the reading - it’s the ROOT code
    running as a ‘black box’ on all of the mappers.
    -   Using Spark as a way of distributing work, so it’s quite simple;
        one advantage is not have to pump data through the JVM.
        -   Do get a ‘free’ way to reduce the results, plus monitoring
            and fault tolerance.
    -   Could a simpler backend be used? Like Dask, Parsel?
        -   Yes, it’s in the plan to try this and it is easy to adapt
             from the current codebase (no hard dependencies).
    -   Note, it is easy to read chunks of data in ROOT (even sub-file).
-   How to distinguish between communication time and working time?
    -   Each mapper really works independently, so no communication time
        during the processing, but problems with
        balancing the tasks.
    -   All the data processing needs to finish before the reduction
        phase can begin.
    -   Problem in HEP as events are inhomogeneous - hard to predict
        exactly how long processing will take.
-   Observation that analysing ROOT files from HDFS is slower than with
    EOS.
-   Want to avoid too much up-front tuning. Can you apply a task
    stealing approach, idle workers try to grab work from other busy
    tasks?
    -   Problem is that Spark is doing this part and it doesn’t know how
        to break apart the tasks.
-   ROOT is implemented as a UDF in Spark.
    -   Required about 2k lines to adapt.
    -   Can pass arbitrary C++ to the JIT engine; calls libraries
        pre-installed onto CVMFS.

AOB/Discussion
--------------
-   FITS original interface was in C. Could use a similar mechanism to
    that used by the ROOT team to implement an optimised file access,
    skipping the JVM.
