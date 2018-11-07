---
title: "HSF Working Groups Mandate"
layout: plain
---

v1.0, 2018-10-11
================

*The mandate for the new HSF Working Groups was widely publicised to the
HEP software and computing
community, developed with input from experiments and others and was
agreed on in the
[open HSF meeting](/organization/2018/10/11/coordination.html) of 2018-10-11.*

----

The mandates are based around the CWP, [**A Roadmap for HEP Software and
Computing R&D for the 2020s**](https://arxiv.org/abs/1712.06982) and the
plans laid out therein.

Three convenors will be appointed for each group. Nominations for
convenorships are open for HEP experiments and members of the HSF
community to make. To properly reflect the full diversity of the
community, the HSF Coordinators will propose convenors from the
nominated candidates, which will then be made public and open for
comment before being finalised.

Appointments as convenors are for one year, renewable.

Group Activities
================

The specific activities of each group are based on the HSF Roadmap and
should ensure that:

-   There is an inventory of active R&D areas, with identification of
    possible overlaps.
-   Areas which lack effort are identified.

To help build a community for collaboration each group should:

-   Look for synergistic R&D areas and try to identify/orchestrate
    collaborative R&D goals out of those.
    -   Groups are encouraged to promote work towards collaborative
        funding proposals as a means of setting R&D directions.
    -   Groups should report on public R&D and plans from the various
        communities (e.g. different experiments) as a mean of
        discussing future directions towards the goals of the roadmap,
        and alert the HSF community of interesting discussions within
        the community.
-   Interact with the broader HSF community via occasional reports at
    the HSF weekly meetings, via the annual HSF workshop, and other
    fora.
-   Hold meetings or topical workshops as necessary to help disseminate
    information and allow for discussion, including making
    presentations to particular communities or experiments if invited.

-   Maintain whatever other discussion and communication channels are
    useful.

The group convenors will organise sessions for their activity areas and
possible joint sessions as part of annual HSF workshops.

Areas of Study and Interest
===========================

The [*HSF Roadmap*](https://arxiv.org/abs/1712.06982) is the primary
document laying out the working domains of each group, but a short
summary is provided for reference below.

Detector Simulation
-------------------

The Detector Simulation Working Group will consider approaches to making
detector simulation faster and more accurate for HEP experiments.
Simulation that produces a traditional digitised detector output, as
well as more radical approaches to generate reconstruction or analysis
level outputs directly are within the remit of the group. Improvements
to physics models, faster particle transport options and using machine
learning and other approximate techniques can be considered. The
adaption of simulation techniques to modern computing hardware
(covering, e.g., multithreading, vectorisation and different accelerator
technologies) are an important area of work.

Reconstruction and Software Triggers
------------------------------------

The Reconstruction and Software Triggers Working Group will consider
approaches and solutions to common challenges across HEP in the area of
event reconstruction and software triggering (e.g., algorithms and data
structures designed for online and offline processing of raw detector
data). The working group targets challenges identified during the CWP
process as well as new ones arising as the state of R&D advances. This
forum should foster collaboration on design and implementation
challenges, the adoption of common approaches, and raise awareness of
existing solutions known to the community. Topics of interest include
the evaluation of new foundational libraries; techniques for track and
calorimetric-object reconstruction and identification; pattern
recognition and clustering; new approaches, including applications of
machine learning techniques and real-time analysis techniques; the
effective use of modern computing hardware through threading,
vectorisation and use of accelerator technologies; and the application
of profiling and quality assurance toolkits.

Data Analysis
-------------

The Data Analysis Working Group considers developments and approaches
that will make the analysis of HEP data towards final physics results
faster and more scalable in the future. One new approach to be
considered is the development of expressive functional interfaces for
analysis. The meshing of HEP specific tools with those found in the
larger data science community is another area of interest, where
database approaches or formats optimised for high-speed processing may
be profitable. The development of test beds for high performance
analysis clusters, that may speed-up turn-around and efficiency is a
major area of R&D. The group should help coordinate activities and
communication here between experiments and IT experts. The integration
of such systems into the end-to-end data flow, with caching and
distribution policies, are important. Optimising the actual content of
analysis formats is a boundary condition to discuss with physics groups,
but can bring major gains.
