---
title: Creating a Metadata file format for Green Computing Practices in High Energy Physics and beyond
layout: gsoc_proposal
project: GreenMetaData
year: 2026
organization: 
  - GreenAlgorithms
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: caterina.doglioni@manchester.ac.uk
    first_name: Caterina
    last_name: Doglioni
    organization: University of Manchester
    is_preferred_contact: yes
  - email: bhogaljyoti1@gmail.com
    first_name: Jyoti
    last_name: Bhogal
    organization: Software Sustainability Institute Fellow 
    is_preferred_contact: yes
  - email: cb2374@cam.ac.uk
    first_name: Christina
    last_name: Bremer
    organization: University of Cambridge
    is_preferred_contact: no
  - email: dylan.powell@stir.ac.uk
    first_name: Dylan
    last_name: Powell
    organization: University of Stirling
    is_preferred_contact: no
  - email: LL582@medschl.cam.ac.uk
    first_name: Loïc
    last_name: Lannelongue
    organization: University of Cambridge
    is_preferred_contact: no
  - email: michael.sparks@manchester.ac.uk
    first_name: Michael
    last_name: Sparks
    organization: University of Manchester
    is_preferred_contact: no
  - email: William.Haese-Hill@glasgow.ac.uk
    first_name: William
    last_name: Haese-Hill
    organization: University of Glasgow
    is_preferred_contact: no
---

## Description

The [Green Algorithms](https://www.green-algorithms.org/) project aims to promote more environmentally sustainable computational science. It regroups calculators that researchers can use to estimate the carbon footprint of their projects, tips on how to be more environmentally friendly, training material, past talks etc.

The [GreenMetaData](https://github.com/GreenAlgorithms/GreenMetaData) File Format is the first step towards standardising the reporting of the environmental impact of computational research. It is a machine-readable file format that can be used to report the carbon footprint and other sustainability metrics of computational research projects. The format is designed to be flexible and extensible, allowing researchers to include additional information as needed.

[GreenMetaData](https://github.com/GreenAlgorithms/GreenMetaData) will feature a web-based tool that will help researchers create a GreenMetaData file for their projects. The tool will guide users through the process of filling out the required fields and will generate a downloadable metadata file in the appropriate format. 

This project aims to support the review and adoption of the GreenMetaData file format by the research community, by providing an easy-to-use tool for creating metadata files and by promoting the use of the format through outreach and engagement activities.

## Task ideas

- Review the fields and hierarchy of the existing metadata draft and confirm the fields.
- Develop the online tool for automatic generation of a metadata file, using the confirmed fields.
- Create a website for the GreenMetaData project for further community engagement and outreach.
- Create case studies around high energy physics (e.g. event generation, simulation, or analysis pipelines) as well as around wearable and digital health tech.
- Document the metadata format for a potential publication.

## Expected results and milestones

- Familiarisation with the existing GreenMetaData draft.
- Confirmation of the fields and hierarchy of the GreenMetaData file format.
- Design and implementation of the web-based tool (Django application) for generating GreenMetaData files.
- Creation of a website for the GreenMetaData project.

## Requirements

- Python programming skills
- Django fundamentals
- Familiarity with GitHub for project collaboration and open source development
- Technical writing skills

## AI Policy

AI assistance is allowed for this contribution, but its use will not be welcomed in the candidate selection exercise or for writing the initial proposal. 
The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). 
Routine tasks (grammar, formatting, style) do not require disclosure.

## How to apply

Please email the mentors with a brief background and interest in green computing and sustainable research. Include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [Green Algorithms](https://www.green-algorithms.org/)
- [GreenMetaData](https://github.com/GreenAlgorithms/GreenMetaData)
- [GSF Impact framework](https://if.greensoftware.foundation)
- [Pyscript](https://github.com/UofM-Green-Compute/GreenMeta)
- [Blog post from Collaborations Workshop 2025](https://jyoti-bhogal.github.io/about-me/blog/2025-05-25_cw25_hack_day/)
