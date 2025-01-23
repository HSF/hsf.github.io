---
title: MCnet/MCviz - graph and 3D-viewer tools for simulated particle collisions
layout: gsoc_proposal
project: MCnet
year: 2024
organization:
  - UofGlasgow
difficulty: medium
duration: 350
mentor_avail: June-October
---

# Description

Simulations are key to particle-physics research: many modern
theoretical models have such complex consequences that we test theory
not by comparing measurements of particle collisions to predicted
functional forms, but by _generating_ simulated collision-events from
the theory and analyzing them identically to the real ones from the
particle collider.

This means that event generators are incredibly important to particle
physics, as the most-used link between experiment and theory, and as a
crucial data format for exchange of ideas. They are also an excellent
way to introduce new researchers and the public to particle-physics
concepts. However, the toolset for MC event manipulation and
visualisation is less powerful and coherent than it should be, and
this project seeks to improve that situation!

## Task ideas

This project will pick up old ideas and code for MC-event
visualisation -- both of the interaction graph that illustrates the
internal theory computation, and the external appearance of the
resulting collision decay-products -- and produce a new set of tools
useful both to physicists and for public outreach.

## Expected results and milestones

 * Extend the mcgraph tool to be usable with both the HepMC and LHE MC-event formats.
 * Refactor mcgraph into a library capable of rendering to a web browser in a server app.
 * Interface the Phoenix event-viewer library to display 3D events (with and without a dummy detector model) to a web browsers.
 * Display interactive particle information and jet clustering in graph and 3D view interfaces.
 
## Requirements

 * Command-line tools
 * Python
 * Web technologies
 * Gitlab CI
 * git

## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**
 * [Chris Gutschow](mailto:chris.g@cern.ch)

## Links

 * [Phoenix event view library](https://github.com/HSF/phoenix)
 * [Old MCview web-based MC event viewer](https://gitlab.com/hepcedar/mcview)
 * [MC event-graph viewer](https://gitlab.com/hepcedar/mcutils/-/blob/master/bin/mcgraph?ref_type=heads)
 * [Old MCviz event-graph viewer](https://github.com/mcviz/mcviz)
 * [HepMC3 event format](https://hepmc.web.cern.ch/)
 * [LHE event format](https://arxiv.org/abs/hep-ph/0609017)
