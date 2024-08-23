---
project: HSF Key4hep
title: Any collection in Data Model Explorer
author: Braulio Rivas
photo: blog_authors/BraulioRivas.jpg
date: 20.08.2024
year: 2024
layout: blog_post
logo:
intro: |
    Incorporated new features for eede (EDM4hep Event Data Explorer). Added a whole new set of collections that eede can visualize (according to the EDM4hep event
    data model) like Clusters, ParticleId or Tracks. Included visualization of relations between them and the previously developed MCParticle collection. Built a menu that allows users to filter out these objects according to their properties and tested using data from FCC simulations.
---

Welcome to my final blog post for the Google Summer of Code 2024 at CERN-HSF. I am Braulio Rivas, and I have been working on the project "Any collection in Data Model Explorer" for the Key4hep project.

![CERN-GSOC](https://hepsoftwarefoundation.org/images/CERN-HSF-GSoC-logo.png)

# The problem

eede (EDM4hep Event Data Explorer, which was previously called dmx) is a tool that allows physicists to **visualize** data in the EDM4hep format. [EDM4hep](https://edm4hep.web.cern.ch/) is a generic event data model for future HEP collider experiments. In High Energy Physics (HEP), accelerators like LHC collide many particles. In this context, an **event** refers to the collision of particles, which is later detected by detectors like CMS or ATLAS. However, several steps related to each other are taken to **reconstruct** these events. Every step of the event takes an input and produces an output. However, the internal functioning typically differs between tools and some software is necessary to ensure that this whole process is correct. This way, EDM4hep serves as an Event Data Model to represent data exchanged between different events, meanwhile eede allows us to analyze this data from EDM4hep visually.

However, eede had a problem. It only allowed to visualize a specific datatype, the `MCParticle`. This is a problem because the data model has many other datatypes that are relevant when analyzing an event, and being able to look at all of them allows to detect anomalies that we otherwise be hard to detect using other techniques. This is why the project "Any collection in Data Model Explorer" was created. The goal was to incorporate new features for eede, adding a whole new set of datatypes that eede can visualize (according to the EDM4hep event data model). This way, we can visualize not only the original simulated event, but also explore many types of relations that exists between reconstructed (as well as simulated) objects. Here we have a diagram that better represents the schema of available types of and how objects can be related among each other.

![EDM4hep Model](https://raw.githubusercontent.com/key4hep/EDM4hep/main/doc/edm4hep_diagram.svg)

# Proposed solution

The original [goal](https://hepsoftwarefoundation.org/gsoc/2024/proposal_Key4hepAnyCollectionInDataModelExplorer.html) was to allow to visualize all the remaining **datatypes** in EDM4hep, allow to filter collections and test on simulated FCC (Future Circular Collider) events. However, due to time constraints, together with mentors we decided to expand the functionality of eede to the most important set of datatypes than initially thought during the proposal development phase. After some discussion, we defined these goals:

1. Implement loading of Cluster, ParticleID, Reconstructed Particle, Vertex, and Track collections types from user provided JSON file(s).
2. Design appropriate graphical representations for every collection type defined by analyzing each type's properties.
3. Develop tools to filter, manipulate, highlight, and group related collections and objects to allow users to explore the visualized events easily.
4. Conduct testing to cover the new features using data from FCC events, either pre-generated or newly generated, to ensure that every version of EDM4hep can be handled correctly.
5. Incorporate CI/CD rules to automate the deployment of eede, enabling users to always access the tool's latest version.

# Coding period

**CI/CD rules**

At the very beginning, I started with new CI rules to automate development for eede. We wanted to do a few things: deploy a
preview of any pull request, so when making changes, in some way an URL will be available to use eede with the changes from the
PR, so its easier to review changes. It was harder than expected, but we finally were able to configure Github Actions to make
it work. Also, it was very simple to later add tests whenever running these previews, or before merging to main.

| Pull Request                                                          |                   PR Number                    | Description                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------- | :--------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated deploys via workflows                                       | [#16](https://github.com/key4hep/eede/pull/16) | I added 3 different workflow files: to deploy a "stable" version of eede. One to allow for pr previews and another to deploy a "release" version that has the latest features.                                                                                                          |
| Redirect from key4hep.github.io/dmx to key4hep.github.io/dmx/main #19 | [#19](https://github.com/key4hep/eede/pull/19) | Because we have two versions: release and main, we can't have a single url to eede. So we have a general link https://key4hep.github.io/eede/ of eede that automatically redirects to the stable `main` version. But there is also a button that allows to go to the `release` version. |
| Add testing for primitives, objects and tools                         | [#20](https://github.com/key4hep/eede/pull/20) | I added a basic test suite for some (now deprecated) graphing functions and for methods on objects.                                                                                                                                                                                     |
| Fix previews workflow                                                 | [#22](https://github.com/key4hep/eede/pull/22) | I had some problems incorporating previews, so this PR tries to solve this issue (unsuccessfully).                                                                                                                                                                                      |
| Configure previews with access tokens and check out to fork           | [#24](https://github.com/key4hep/eede/pull/24) | This PR finally fixed previews, by correctly configuring a GitHub environment that uses fined grained access tokens to checkout to the PR and deploy the code in the original repo.                                                                                                     |

**Loading**

After setting up the environment, I expanded the loading functionality. As explained above, at the beginning, eede could only
load one type of datatype. However, there are many more, so I created a function called [`loadObjects`](https://github.com/key4hep/eede/blob/32d50c7fab3fa244767aa012cdc5ba891339abef/js/types/load.js#L47-L226)
that can load **all** of the datatypes from EDM4hep. However, internally we deliberately limit this to load only those for which visualizations have been implemented. This loading can **also** deal with **different** schema versions of edm4hep and has tooling to facilitate adding a **new** version. Further
work its easier because it only will be necessary to expand other modules, and not loading in order to load all the datatypes.

**Loading**
| Pull Request| PR Number | Description |
| :--- | :----: | :--- |
| Load particles according to edm4hep | [#36](https://github.com/key4hep/eede/pull/36) | I developed a function that allows to load any kind of object into eede and a way to get the latest version of EDM4hep so it can load any file according to the latest version. |

**Visualizing**

Having the data loaded in memory, I was able to later develop the visualization of these new datatypes. For each new
datatype, a few properties have to be shown for an "object" belonging to a collection, and the whole collection has to be
placed around in a way its easy to understand. I discussed with mentors [what information](https://github.com/key4hep/eede/blob/main/js/types/objects.js) to show and most importantly,
**how** to visualize them, including relations. After throwing some ideas, I defined a set of common ["views"](https://github.com/key4hep/eede/tree/main/js/views/templates) that repeated across datatypes. So for
example, a `Cluster`, `Track` or `ReconstructedParticle` collection will be shown as a tree, connected to other objects of the
same type. But, if a `MCParticle` is related to a `ReconstructedParticle`, it will be shown as a large list going downwards.

| Pull Request                               |                   PR Number                    | Description                                                                                                                     |
| :----------------------------------------- | :--------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------ |
| Visualization of MCParticle + RecoParticle | [#43](https://github.com/key4hep/eede/pull/43) | Views for `RecoParticle` and existing relations between this and `MCParticle`.                                                  |
| Views for cluster and track                | [#48](https://github.com/key4hep/eede/pull/48) | I added a views for `Cluster` and `Track` plus relations that exists between `MCParticles`-`Cluster` and `MCParticles`-`Track`. |
| Initial views for particleID and vertex    | [#55](https://github.com/key4hep/eede/pull/55) | More views for `ParticleId` and `Vertex`.                                                                                       |

**Pixi**

eede is a static website. So we are using plain Javascript, HTML and CSS. But for visualization, we were using the Canvas API,
so all datatypes are drawn in a white canvas. However, when having many objects in one view, it was almost impossible
to scroll or drag objects around. So I [analyzed](https://github.com/key4hep/eede/pull/63) some of the weak points at that moment.
I came to the conclusion to change Canvas API to some more performant tool, and to find a way to render objects more efficiently.
After some research, I found [pixi.js](https://pixijs.com/), a library (which has a minified `js` version) that uses WebGL
to render any kind of content on a canvas very fast. After a bit of rework, I finally transferred everything to pixi.
The difference was big. Before, eede struggled to render a tree of `MCParticle` from this file https://fccsw.web.cern.ch/fccsw/eede/wzp6_ee_mumuH_ecm240_CLD_RECO.edm4hep.json
(by some reason, it was only possible in Firefox, but not on a chromium based browser). But it later had no problem, it
rendered everything fast without crashing.
Other very noticeable example is when rendering $15000+$ `MCParticle`s. When using Canvas API, the ram consumption went up by a lot
and froze the computer. But after using pixi and applying some techniques, like [culling](https://pixijs.com/8.x/guides/basics/scene-graph#culling)
it had no problem and takes only the necessary amount of memory.
| Pull Request| PR Number | Description |
| :--- | :----: | :--- |
| Use pixi | [#65](https://github.com/key4hep/eede/pull/65) | I changed the rendering engine from Canvas API to pixi.js. This PR also includes a few changes to make the rendering more efficient. |

**Filters**

One of the last tasks was to develop a set of filtering functionalities, because in one single event many
objects might exist, making it harder to visualize. So, I developed filters for every datatype, that allow to filter
any given view by e.g charge of a particle, momentum, energy, or to choose a subset of objects from a same datatype. This is fundamental, because anybody that wants to do research on their data, will be able to understand and
uncover complex relationships and patterns in the data that might not be apparent through traditional techniques.

| Pull Request                                     |                   PR Number                    | Description                                                                                                                                                                                                        |
| :----------------------------------------------- | :--------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add new filters for other collections            | [#70](https://github.com/key4hep/eede/pull/70) | I added filters for `Cluster`, `ParticleId`, `ReconstructedParticle`, `Track` and `Vertex` collections. Allow to filter by charge, mass, energy, type, etc. Everything depending on the properties of each object. |
| Allow to filter by collection name of the object | [#76](https://github.com/key4hep/eede/pull/76) | I added a filter that allows to filter by collection name of the object.                                                                                                                                           |

# Conclusion

eede has really changed a lot. The improvements made during GSoC have been very significant. Now, it is possible to visualize many types of collections, and to filter them according to their properties. This is a big step forward, as it allows physicists to analyze events in a more detailed way. In addition, some features related to UX like allowing to switch between versions of eede, upload a new file at any given time or to allow change between events make it easier to use. The CI/CD rules make it a more fluid development process. I am very happy with the results, and I hope that this tool will be useful for the HEP community.

I must say that GSoC is a great experience. I learned somethings about Physics, but most importantly, I learned a lot about software development. Talking, discussing and coding every day with my mentors really helped me to improve my skills. I don't have words to express my gratitude to them. I truly feel a more capable developer thanks to their help.

# Links

-   [eede repo](https://github.com/key4hep/eede/)
-   [eede release (stable) version](https://key4hep.github.io/eede/release/index.html)
-   [eede main development version](https://key4hep.github.io/eede/main/index.html)
-   [Proposal](https://drive.proton.me/urls/N74MP9JE34#VhJlh3ILFX7I)
-   [Initial blog explaining my thoughts about getting into GSoC](https://medium.com/@brauliorivas/google-summer-of-code-24-at-cern-hsf-cbbff64b025b)
-   [EDM4hep](https://edm4hep.web.cern.ch/)
-   [Podio](https://github.com/AIDASoft/podio)
-   [MonteCarlo Particle Numbering Scheme](https://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf)
-   [PDG IDs to names](https://github.com/iLCSoft/LCIO/pull/170/files#diff-ab79a6d4ac8ba0c3dc5f899a764751693e8f8117e7e972f8a157c9a5009739c5R18-R615)
-   [Generator Status](https://pythia.org/latest-manual/ParticleProperties.html)
-   [Pre defined bits for Simulation Status](https://github.com/key4hep/EDM4hep/blob/eddd0511f7d5e783f6c6c42910ce87bc042514a6/edm4hep.yaml#L293-L301)
-   [Presentation Jul 10](https://drive.proton.me/urls/7W6NGCFZ14#FhdIyQP7w90x)
-   [Final Work Product Submission](https://gist.github.com/brauliorivas/f1a4cb5dc84ee63182b8525ae0f581c5)
