---
title: GeoModelExplorer, interactive 3D geometry visualization - Development of a visualization tool to interactively explore the geometry of a HEP detector
layout: gsoc_proposal
project: ATLAS
year: 2020
organization:
  - Pittsburgh
  - UMass
---

## Description

Interactive visualization is a key tool in High Energy Physics (HEP). Not only interactively visualizing data from particle collisions helps in understanding the physics involved in the interactions between fundamental particles; it is also a necessary tool to explore and verify the correctness of the detailed geometry description of the experimental apparatus, which is needed to correctly reconstruct collision data.

In the [ATLAS Experiment](https://atlas.cern) at [CERN](https://home.cern), interactive 3D visualization is typically performed with the use of an in-house tool running within the experiment's framework, [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/).
VP1 is the primary 3D event display for the ATLAS experiment, and has been used to produce some of the [iconic 3D images](https://twiki.cern.ch/twiki/bin/view/AtlasPublic/EventDisplayRun2Physics) of recent physics research successes at CERN, such as the Nobel-prize winning discovery of the [Higgs boson](https://atlas.cern/updates/atlas-feature/higgs-boson). VP1 is also used to debug physics analysis, the experiment geometry description, and reconstruction and simulation techniques, and so is a vital tool for many ATLAS developers and physicists. Recently, as part of the modernization effort of the ATLAS [geometry description software](https://gitlab.cern.ch/GeoModelDev/), a light version of VP1 has been developed, with a strong focus on the visualization of geometry data; it is used solely for geometry debugging and, as a consequence, it has less dependencies and is also easier to use and develop for. The new tool let ATLAS physicists and engineers interactively explore the geometry and check the correct description and placement of the volumes that compose the particle detector.


Current visualization tools in ATLAS, however, are based on old graphics libraries (OpenInventor/[Coin](https://bitbucket.org/Coin3D/coin/src/default/) and [SoQt](https://bitbucket.org/Coin3D/soqt)), which do not exploit the graphics and computing power of current GPUs and lack modern graphics algorithms. As the [Visualization](https://arxiv.org/abs/1811.10309) section of the *HSF Community White Paper* explained, the use of modern graphics libraries would open the way to new features and towards a better integration in  modern graphics pipelines. In additional to that---and probably more importantly---, the use of modern software libraries and techniques would also help the HEP experiments to more accurately and faster develop new particle detectors and leverage the physics discovery potential.


Thus, as part of the current software modernization effort in ATLAS, the replacement of the core 3D graphics engine is planned. The new [Qt3D toolkit](https://doc.qt.io/qt-5/qt3d-index.html), recently added to the official releases of the Qt framework, could be an excellent option. It would let developers easily integrate 3D graphics natively in the Qt GUI framework (already used in ATLAS for GUIs), *de-facto* removing the need of interface packages like SoQt.
In addition to that, new features will be developed: to interact with the 3D objects composing the detector geometry more effectively; to let physicists see the details of the apparatus by the use of a better volumes' rendering and of animated views; to export 3D data to common formats.


Development of new features will be performed in the context of the [new, standalone version](https://gitlab.cern.ch/GeoModelDev/geomodelvisualization) of the ATLAS visualization tools. That will let developers work outside the complex and specific software framework of the experiment, with a much faster development cycle. Moreover, that would leverage the experiment-independent character of the new tools, to potentially develop software solutions for the HEP community. In addition to that, new developments to the open source libraries used in the project could be eventually contributed back into the relevant code bases.  


## Task ideas

 * Develop a Qt3D testbed, to explore its possibilities
 * Survey the other needed functionality (*e.g.*, the *SoSwitch* or *SoSelection* classes found in OpenInventor) and look for the existence of viable equivalents in Qt3D. (The graphics tools in VP1 is a possible example of what should be aimed for)
 * Develop extended orbit controls
 * Develop better volumes filtering
 * Develop interactive picking of 3D geometry volumes
 * Improve the handling of Boolean volumes, polycones, and tessellated solids
 * Improve rendering of 3D volumes for detector geometry
 * Improve the export of 3D data to common formats
 * Animation and transitions between views of different parts of the detector geometry

## Expected results

The integration of a modern graphics engine, new software tools focusing on detector geometry, possibility to animate the views to better explore the volumes, the ability to export 3D data to common formats.

## Requirements

C++, Qt5 framework (3D graphics experience a bonus)


## Mentors

  * [Riccardo Maria Bianchi](mailto:riccardo.maria.bianchi@cern.ch)
  * [Edward Moyse](mailto:edward.moyse@cern.ch)
  * [Joseph Boudreau](mailto:boudreau@pitt.edu)

## Links

  * [ATLAS Experiment](https://atlas.cern)
  * [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/)
  * [ATLAS Public Event Displays](https://twiki.cern.ch/twiki/bin/view/AtlasPublic/EventDisplayRun2Physics)
  * [GeoModelDev](https://gitlab.cern.ch/GeoModelDev/)
  * [HSF "Visualization" Community White Paper](https://arxiv.org/abs/1811.10309)
  * [Qt3D](https://doc.qt.io/qt-5/qt3d-index.html)
