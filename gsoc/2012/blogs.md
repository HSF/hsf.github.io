---
title: CERN Summer Thrills GSoC 2012
layout: plain
year: 2012
---

{:refdef: style="text-align: center;"}
![gsoc-logo](https://wiki.osgeo.org/w/images/a/a7/Gsoc-2012-logo-color.png){: width="600" }
{: refdef}


For the physics software development group at
[CERN](http://public.web.cern.ch/public/), our second year of *[Google
Summer of Code](http://code.google.com/soc/)* couldn't have come at a
better time. Motivated by CernVM\'s [awesome experience in
2011](http://google-opensource.blogspot.ch/2011/12/cernvms-fruitful-summer.html),
our colleagues from the [Geant4](http://geant4.cern.ch/) and
[ROOT](http://root.cern.ch) software projects joined us as mentors this
summer. And while physicists around the world snatched the first
evidence of a long-sought [Higgs
boson](http://cds.cern.ch/record/1459565) from the Large Hadron Collider
(LHC), our seven *Google Summer of Code* students worked on core parts
of the open source software engine that makes LHC data processing
possible.

Two of our students worked with the Geant4 team at CERN. Geant4 is a
toolkit for the simulation of the response of a material when
high-energetic particles are passing through it. Geant4 can be used to
model a gas detector, a gamma-ray telescope, an electronic device next
to an accelerator or the inside of a satellite. In order to keep up with
the rate of real data coming from the LHC detectors, Geant4 has to be
both accurate and fast.
 

-   Stathis Kamperis improved the speed of Geant4 by re-ordering the
    simulation of particles according to particle type. By simulating,
    for instance, first all electrons, than all photons, and so on, the
    number of instruction cache misses decreases. In the course of this
    work, Stathis also ported Geant4 to Solaris which gives us access to
    the very powerful [DTrace](http://dtrace.org/blogs/) profiling
    machinery.
-   Dhruva Tirumala Bukkapatnam contemplated Geant4 pointers and data
    structures. He developed code for a particle navigation algorithm
    optimized for use on GPU architectures.

\
Two more students were working together with the ROOT team. The ROOT
framework is the main working horse for LHC experiments to store,
analyze, and visualize their data.
 

-   Omar Zapata Mesa worked on an
    [MPI](http://www.mcs.anl.gov/research/projects/mpi/) interface for
    ROOT. On a cluster of machines, the MPI interface enables ROOT to
    toss around its C++ objects from node to node while also integrating
    with ROOT\'s C++ interpreter.
-   Eamon Ford worked on the CERN iOS App.The App brings CERN news and
    information on an iPad or iPhone. In case you can't sleep at night,
    you can now peek at the live display of particle collisions from
    inside the LHC.

For the CernVM base technology, we had three more students working with
us this summer. CernVM provides a virtual appliance used to develop and
run LHC data processing applications on the distributed and
heterogeneous computing infrastructure that is provided by hundreds of
physics institutes and research labs around the world.
 

-   Josip Lisec, back for his second *Google Summer of Code*, worked on
    the log analysis and visualization of CernVM Co-Pilot, the job
    distribution system which powers the [LHC\@home
    Test4Theory](http://lhcathome2.cern.ch/) volunteer computing
    project. Want to see the world map of active volunteers from the
    19th of November at 3:07pm?  Check out the [Co-Pilot
    dashboard](http://www.youtube.com/watch?v=UXHSXt9poCA).
-   Francesco Ruvolo worked on broken network services, such as
    misconfigured DNS or HTTP servers. Breaking such services in a
    controlled way comes in handy when simulating the behavior of a
    CernVM running on a hotel WiFi.
-   Rachee Singh programmed maintenance tools for the content
    distribution network that is used by the CernVM File System to
    distribute terabytes of experiment software to all the worker nodes.
    All the proxy servers of the content distribution network can now be
    plotted on a map and every CernVM can automatically find a close
    proxy by means of a [Voronoi
    diagram](http://en.wikipedia.org/wiki/Voronoi_diagram) produced by
    Rachee\'s code.


Overall, we were very glad to see so much interest and enthusiasm from
the student programmers in LHC software tools. We'd like to
congratulate all of our students on their hard work and on successfully
completing the program!

Sun, 09/30/2012 - 00:00
*By Jakob Blomer, CERN Organization Administrator*
[(original article on Google Open Source
Blog)](http://google-opensource.blogspot.fr/2012/12/cern-summer-thrills.html)
