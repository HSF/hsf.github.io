---
title: "HSF Software Forum, 6 June, 2018"
layout: meetings
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/733268/) 

DD4hep and DD\* tools
=====================
-   Tommaso - any comparison numbers for speed with other geometry
    toolkits? 
    - A. Actually mostly delegated - very dependent on ROOT toolkit speed, or the handling in
      G4.
-   Alberto - what about memory consumption? 
    - A. Yes, we have two representations after conversion to G4 and we
      do keep them right now. However, it is possible to drop an unused representation
      if that's required.
-   Are the XML files the only way to persistify the description?
    - A. Compact description is the "native" way to populate the geometry. However
      there are other plugins, e.g., LHCb or CMS plugins that can read
      from the experiment detector databases and build the geometry from
      there. Could have other ways too, e.g., CAD importer.
-   Dario - Visualisation is really useful on the web. three.js on the web is great
    and optimised for GPUs -
    could you translate into JSON to use that? 
    - A. Yes, via ROOT
      description and export. Noted
      that ROOT visualisation uses WebGL, so when GPUs are available they do get used.
    - Philosophy is that DD4hep not intending to replace visualisation that exists in ROOT,
      where a good job is done already. 
    - LHCb experience was that when ROOT to three.js conversion was done,  it was a bit limited compared
      to ROOT's javascript. Simplified geometry
      better for the web anyway - not all details useful or needed.
-   How to handle sensitive detectors from other sources? 
    - A. This is done
      via the plugin, if it populates things properly. Seems quite easy
      to do.
    - IOV alignment corrections are for reconstruction. Simulation uses global
      re-alignments. TGeo can do sanity checks for you for overlap and there are
      other toolkits that can help to.
-   Ben M - For a small experiment to evaluate I would need to write a
    converter from the current description to DD4hep. 
    - A. Yes.

CMS Migration
=============
-   First exercise to try DD4hep went very well, thanks to support from
    Markus and the other developers.
-   Now want to convert in time to do Run3 production in 2019.
-   Added unions and subtractions (booleans) - now validating. Truncated
    tube, etc. These are all converted into correct primitive shapes after
    input.
-   Pere - Are there 2M Volumes? 
    - No, actually 2M nodes, only about 4k independent
      volumes.
-   For memory use, could remove the TGeo geometry as
    it's is not needed to do simulation, but it's only
    15-20MB.
-   Some concerns about loss of precision between representations.
-   Some caution needed to be consistent with units (cm vs. mm). CGS was
    the "original" HEP units. Geometry doesn't care, but density and
    radiation length matters! Could offer updated code in ROOT, using
    mm? (Global switch?)
-   Foresee that ROOT can use VecGeom, but would need a lot of new
    functionality to fully exploit it, e.g., to support navigation.
-   What's the motivation to move to DD4hep? 
    - A. Can review and revise the code (that's 20 years old).
    - Daniel - as well as some CMS internal reasons that make now a
      good time to change, we want to have sustainability and support into the future.
      We want to support common software as the way to go forwards.   
