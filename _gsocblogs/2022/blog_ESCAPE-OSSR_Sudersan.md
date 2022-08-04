---
project: ESCAPE-OSSR
title: Repository as a Service
author: Sudersan S
date: 04.08.2022
year: 2022
layout: blog_post
logo: OSSR-logo.png
intro: |
This blog entails my progress, learning and experience acquired during the GSoC period.
---

## Project Brief
##### Mentors: Enrique Garcia & Thomas Vuillame

Several physics communities with disciplines ranging from astronomy to particle physics use the Zenodo platform to publish digital research artefacts such as research papers, software, and datasets. Often researchers face difficulties in configuring the repositories for their use. This project seeks to eliminate that by building a JupyterLab extension that retrieves the required repository from Zenodo and automatically configures it in the JupyterLab interface


## Timeline

### Community Bonding Period

The community bonding period was the first phase of the Google Summer of Code. During the community bonding period, I got the opportunity to interact extensively with my mentors and learn more about the ESCAPE ecosystem, OSSR, and the Zenodo framework. I also got the opportunity to interact with the OSSR team and see its functioning. 

### Coding period

Once the coding period started, I worked to set up the development environment, learn from existing plugins and build 
sample extensions that mirror the required functionality. I also worked to construct a UI wireframe for the plugin. I then worked on the exercises the mentors gave to familiarise myself with the various backend operations required of the plugin. After which, I developed a small backend functionality that retrieves the list of repositories and the associated metadata and encodes it in a notebook. I then proceeded to start creating the front end of the plugin. I ran into some roadblocks there as I was unfamiliar with manipulating the Jupyter frontend and integrating React. With the help of my mentors, I was able to overcome it and proceed to develop the front end. Currently, the plugin has a primitive frontend retrieves all associated repositories from Zenodo per user queries. I have fallen behind on the proposed schedule due to a hectic work schedule and unfamiliarity with the Jupyter interface. Still, I believe I can wrap up the project by the deadline.

### Personal Experience

It has been a great learning experience, and I look forward to making more significant contributions. I am grateful to my mentors for their support and guidance.
Project Repository - https://gitlab.in2p3.fr/escape2020/wp3/ossr-jupyterlab-extension
Project Proposal - https://hepsoftwarefoundation.org/gsoc/2022/proposal_ESCAPE-repository-as-a-service.html


