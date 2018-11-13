---
title: "HSF Software Forum on HEP analysis in the Numpy ecosystem, November 7, 2018"
layout: meetings
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/745288/)

Introduction
============
-   News on upcoming workshops, procedure and timeline for selection of
    HSF WG convenors, next Software Forum meetings.

HEP analysis in the Numpy ecosystem
===================================
-   Uproot-methods define behaviour of what you can do with certain
    classes, which is not encoded in the data itself.
-   Awkward Array - how well does HEP analysis map into this array
    language?
    -   Interfaces like MATLAB/R will not work.
    -   Will need to rethink the way the analysis is expressed.
    -   LPC group using a distributed processing engine - array centric
        python:
        -   What pieces are missing? This will be interesting - will
            probably need new primitives.
    -   Is there a direct mapping between the analysis on Slide 24?
        -   No, not in general.
        -   It’s a bit like VMSIMD.
-   Uproot is very good for teaching.
    -   Quick bootstrap for students.
-   Is nested data that rare?
    -   Yes, other sciences “clean” data, which is mapping into tables.
    -   Would other fields be interested in using the nested data if
        they had the tools? Maybe.
    -   In NOSQL there is more support for this nested data, like
        MongoDB (there is a query language, very SQL-like).
        -   SQL doesn’t deal well with that, but SparkSQL is trying to
            extend to add support.
-   BDTs deal better with “missing” data, could be a reason they are
    more popular than NNs?
    -   Or is was better performance? Maybe BDTs will die off in favour
        of DNNs.
-   How easy is it for people to understand JaggedArray operations?
    -   Explicit is clear, implicit might be less so.
    -   This is part of of the experiment.
        -   Selectors can help disambiguate a lot, to help understand
            masking.
-   Exploring the right solutions for expressing analysis is a very
    important part of this kind of evolution.
-   Original idea was not to give physicists array syntax, but to use
    numba JIT expressions; however physicists might like to use an
    array operation style...
    -   Xeonon-1T seem to have decent experience with this with new
        analysts.
-   Could a DSL hide the loopyness, but allow for clearer expression of
    the idea, then behind the scenes use arrays?
    -   Yes, this is on the table, there is a functor version.
-   Different expression syntaxes liked by different people!

AOB/Discussion
==============
-   Since XENON mentioned, if interested in interface scientific python
    stack and particle physics community software (working on common
    tools), check out this postdoc ad at Rice:
    [*https://jobs.rice.edu/postings/17226*](https://jobs.rice.edu/postings/17226).
-   Interested in following the HSF “Python in HEP” activities?
    Subscribe to the Gitter channel
    [*https://gitter.im/HSF/PyHEP*](https://gitter.im/HSF/PyHEP).
