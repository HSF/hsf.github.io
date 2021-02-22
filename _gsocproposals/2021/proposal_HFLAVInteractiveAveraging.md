---
title: Add support for in-browser interactive averaging of physics results
layout: gsoc_proposal
project: HFLAV
year: 2021
organization:
    - CERN
---

## Description
The Heavy Flavour AVeraging (HFLAV) group is responsible for collating measurements made at different High Energy Physics (HEP) experiments, at CERN and other particle physics laboratories, and combining them using robust statistical procedures. As a result, HFLAV provides a resource for all particle physicists seeking the 'state-of-the-art' results from across the field, in various categories of measurement. The 'Beauty to Charm' subgroup is responsible for combinations of measurements that involve the decay of a particle containing a b-quark to any final state where one of the particles involves a c-quark.

The HFLAV averages are published every two years (the latest are at https://arxiv.org/abs/1909.12524) and, whilst these peer-reviewed publications set the gold standard for the averages, it is essential for researchers to have online access to more frequently updated averages. The HFLAV website provides this: hflav.web.cern.ch, providing a 'live' snapshot of the averages that is updated after every new result is incorporated by an HFLAV representative. All code and data are stored in GitLab repositories and GitLab CI is used to perform the averaging automatically after each update and to manage deployment to the static website.

The HFLAV results could be of much greater value to the particle physics community, in three areas:
- accessibility: finding the specific measurement-average, from the hundreds collected.
- interactivity: a 'black-box' averaging has value, but to understand the impact of particular inputs, one needs to control which results enter the average.
- visibility: the result of the averaging is an intimidating array of measurement averages, of which only one (or a small number) are usually of interest. Users want hand-picked comparisons, not huge figures or long tables.

This project seeks to transform user interaction with HFLAV's 'Beauty to Charm' averages. We're not looking for a new website, but to implement effective, interactive, clear, user-led averaging.

## Task ideas
 * Understand the categories of 'Beauty to Charm' decays that enter the HFLAV averages, proposing a means to help the user navigate them as quickly as possible
 * Implement an in-website tool (perhaps using CERN's innovative Service for Web-based Analysis (SWAN)) that hands back control over averaging to the user
 * Allow the user to customise presentation of averages

## Expected results
The expected result is a web-portal, within the hflav.web.cern.ch website, that gives the user access to the heart of the averaging process, visualising the elements of the average results that they are interested in. The student should be prepared to write a progress report and present the results at the end of the summer.

## Evaluation Task
Interested students please contact Dan (d.j@cern.ch) for more details and an evaluation task.

## Requirements
 * Python, JavaScript, CSS, HTML5. Comfortable using Linux. Familiarity with Jupyter notebooks and matplotlib (or similar visualisation software suitable for web-based presentation) an advantage.

## Mentors
 * ***[Daniel Johnson](mailto:d.j@cern.ch)***
 * [Thomas Kuhr](mailto:Thomas.Kuhr@lmu.de)

## Links
 * [HFLAV](https://hflav.web.cern.ch/)
 * [SWAN](https://swan.web.cern.ch/)
 * [HFLAV 'Beauty to Charm' averaging code](https://gitlab.cern.ch/hflav/averaging)
