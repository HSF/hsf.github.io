---
title: Image Explorer for ownCloud Infinite Scale
layout: gsoc_proposal
project: CERNBox
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-September
organization:
  - CERN
  - ownCloud
---

## Description of project

[CERNBox](https://cernbox.web.cern.ch) is a sync and share collaborative cloud storage solution used at CERN, the home of the LHC and the birthplace of the web. Used by more than 37K users, and storing over 15PB of data, it has been responding to the high demands of our diverse user community. CERNBox provides an easy and accessible cloud storage solution based on the [ownCloud](https://owncloud.com/) open source software, which recently launched their new flagship product, codenamed oCIS (ownCloud Infinite Scale).

Through visual perception, people are able to obtain information in a quicker and more productive way. Image types represent the most frequently stored data types in CERNBox with diverse use cases ranging from high resolution photos of the LHC detectors (i.e used for maintenance purposes) to document scans and data charts of the experiments' analysis. 

The aim of this project is to add an image explorer to the new ownCloud Infinite Scale frontend to simplify and accelerate working with the image data types.

## Task ideas
* Develop a gallery application to centralize the exploration of image data
* Allow filtering by image formats and metadata in the gallery view
* Develop a rich view of metadata (map, timeline, etc)
* Develop a slideshow view of the gallery
* Implement simple image editing functionalities
* /*Optional task*/ Enable detecting objects on the images automatically using a vision AI framework of your choice
* Document the developed components
* Test the components in the new CERNBox UI

## Related material
* [CERNBox project](https://cernbox.web.cern.ch/cernbox/)
* [Github of CERNBox web](https://github.com/cernbox/web) 
* [OCIS project](https://owncloud.dev/ocis/)
* [OCIS documentation](https://owncloud.dev/clients/web/getting-started/)

## Expected results
We expect at the end of GSOC ‘22, a well-documented VueJS component that can be enabled to explore and edit image data in the new Infinite Scale web interface.

## Experience required
HTML5, Typescript, ES6, VueJS, REST

## Evaluation Task
Interested students please contact Elizaveta (see contact below) to ask questions and for an evaluation task.

## Mentors
*  **[Elizaveta Ragozina](mailto:elizaveta.ragozina@cern.ch)** CERN
* [Diogo Castro](mailto:diogo.castro@cern.ch) CERN
* [Hugo Gonzalez Labrador](mailto:hugo.gonzalez.labrador@cern.ch) CERN
* [Benedikt Kulmann](mailto:bkulmann@owncloud.com) ownCloud
