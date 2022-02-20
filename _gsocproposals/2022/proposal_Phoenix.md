---
title: Phoenix, interactive data visualization - Development of an experiment independent javascript event display framework and data format
layout: gsoc_proposal
project: Phoenix
year: 2021
organization: 
  - UMass
  - Pittsburgh
  - CERN
---

<!-- Phoenix visualisation URLs can't be validated by the checker, for some reason -->

## Description

Visualising HEP event data is currently typically done per experiment (e.g. [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/), [Iguana](https://doi.org/10.1016/j.nima.2004.07.036), [Fireworks](https://iopscience.iop.org/article/10.1088/1742-6596/219/3/032014/pdf)), and normally involves the installation of dedicated software. However modern browsers are more than capable of showing complex detector geometry, as well as representations of the underlying physics. As the [Visualisation](https://arxiv.org/abs/1811.10309) section of HSF Community White Paper explained, using an intermediate data format (e.g. JSON) makes it possible to separate the event display from the underlying (experiment-specific) software framework. 

[Phoenix](https://hepsoftwarefoundation.org/phoenix/) is a framework that can be used by any typical (e.g. colliding beam) High Energy Physics experiment. It was initially based on work done for the TrackML [Kaggle](https://www.kaggle.com/c/trackml-particle-identification)/[Codalab](https://competitions.codalab.org/competitions/20112) challenges (and internal use by ATLAS). 

In the recent Advanced Computing and Analysis Techniques (ACAT) 2021 [conference](https://indico.cern.ch/event/855454/), two submissions cited Phoenix:
* Open Data Detector (ACTS) [link](https://indico.cern.ch/event/855454/contributions/4596738/attachments/2352091/4013627/740_poster.pdf)
* New Web Based Event Data and Geometry Visualisation for LHCb [link](https://indico.cern.ch/event/855454/contributions/4598428/attachments/2352310/4013170/572_Andreas-Pappas_ACAT2021_poster.pdf)

GSOC students in 2019 and 2020 ported Phoenix to angular, wrote and implemented a new menu system and much more. Most base functionality now exists for the core display - the task now is to polish this, and develop better the VR display.

## Possible Tasks
### 3D menu for AR/VR
Phoenix currently supports (in a quite basic form) VR and AR and even with the limited functionality we have right now, this is a very exciting way to use the event display and it is something we would really like to improve.

However one current omission is there is no way to interact with the detector and event data visualisation: at the moment in AR/VR the user has no way to change what is shown,

Phoenix’s menu system was always intended to be extensible, and so it should be possible to add a 3D menu when in VR mode. The major complication here will be that visualising detectors and event data on a phone is a very different experience to using it in a dedicated headset (such as a Meta Quest). Much care will need to be taken to make the UI as intuitive as possible. Once this is made to work, we can investigate adding a simple menu for AR mode (AR is more difficult, since it is less stable).


#### Possible sub-tasks
* Investigate available open source menu packages (e.g. https://discourse.threejs.org/t/three-mesh-ui), and evaluate the feasibility of incorporating them in Phoenix.
* Decide what functionality should be available in which mode and how it should be best presented.
* Implement the above, and add the appropriate regression tests.
* Add new functionality, such as the ability to scale the view etc.
* Investigate whether a simple menu can also be added to AR.

### EDM4HEP loader
[Key4HEP](https://github.com/key4hep) is a new software stack being developed for future particle physics experiments. An important part of it is [EDM4HEP](https://github.com/key4hep/EDM4hep), “a generic event data model (EDM) for future High Energy Physics (HEP) collider experiments”. What this means in practice is it is a way of representing event data for potential future experiments, and we would like to be able to read this in Phoenix.

Phoenix is designed to be extensible via “loaders”, basically small interpreters that convert arbitrary data formats into Phoenix’s native event data model, so the concrete task would be to write a “loader” which understands EDM4HEP.

#### Possible sub-tasks:
* Investigate and understand the EDM4HEP format.
* Implement a loader to convert to Phoenix format.
* Write regression tests for the new functionality.

### Improved testing 

Phoenix consists of two packages:

* [phoenix-event-display](https://github.com/HSF/phoenix/blob/master/packages/phoenix-event-display) which is the UI independent library containing all the event display logic.
* [phoenix-ui-components](https://github.com/HSF/phoenix/tree/master/packages/phoenix-ng/projects/phoenix-ui-components) which is a library of Angular components that makes use of `phoenix-event-display` to provide UI for modifying the scene.

The current tests for both the packages are written using [Jasmine](https://jasmine.github.io/) and [Karma](https://karma-runner.github.io/). While Jasmine and Karma are fairly popular and feature-packed, the browser-oriented nature of Karma makes the tests very slow, especially for `phoenix-event-display` which doesn't necessarily need a browser.

In the case of `phoenix-ui-components`, the tests use the Angular testing setup which is based on Jasmine and Karma. While the setup is correct and the tests run fine, they need a serious revamp. The idea would be to update the current test setup and make sure it conforms to the latest Angular version. And (most of) the tests would need to be rewritten to follow [Behaviour Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) and be more meaningful.
Integration tests also need to be written for [phoenix-app](https://github.com/HSF/phoenix/tree/master/packages/phoenix-ng/projects/phoenix-app) which is the actual Phoenix application and uses `phoenix-ui-components`.

Phoenix does not have any end-to-end tests, so they also need to be set up and written. Possible options are Cypress and Protractor.

#### Possible sub-tasks:
* Investigate alternative JavaScript testing libraries for phoenix-event-display. For example [Jest](https://jestjs.io/).
* Revamp the unit and integration testing setup and rewrite tests for `phoenix-event-display` and `phoenix-ui-components`.
* Introduce and set up an end-to-end (e2e) testing framework and write e2e tests.
* Lay out a testing strategy for Phoenix and set up coverage thresholds to enforce and encourage testing.


## Requirements
Angular, Typescript, Web development (GUI design experience and [threejs](https://threejs.org) knowledge a bonus).

## Mentors
  * [Fawad Ali](mailto:m.fawaadali98@gmail.com)
  * [Riccardo Maria Bianchi](mailto:riccardo.maria.bianchi@cern.ch) 
  * **[Edward Moyse](mailto:edward.moyse@cern.ch)**

## Links
  * [Phoenix](https://github.com/HSF/phoenix)
  * [Kaggle challenge](https://www.kaggle.com/c/trackml-particle-identification)
  * [Codalab challenge](https://competitions.codalab.org/competitions/20112)

