---

project: PATATRACK
title: Implementation of a Python library that generalizes the CLUE clustering algorithm
author: Simone Balducci
date: 08.08.2022
year: 2022
layout: blog_post
logo: PATATRACK-logo.png
intro: |
  Description of the progress obtained in generalizing the CLUE clustering algorithm to N dimensions and binding it with Python.
  
---
  
## Introduction
Hello, I am Simone and i am currently working with the Patatrack team. The github repo for the project can be found here: https://github.com/SimonB00/clue.
The aim of the project I'm working on is to generalize the CLUE clustering algorithm to N dimensions, since it was initially designed to work in 
2 dimensions. The following goal is to create a Python binding for the algorithm and deploy it as a Python library.
  
## Results obtained
So far, the generalization of the code has been fully implemented. Also, in order to make the algorithm more general it has been made independent of the
geometric properties of the detector.
The Algorithm has been tested and it has been asserted that it works as expected. The output has been compared to that produced by the original algorithm,
and the two are compatible.
The binding is under development.
The list of the commits can be found here: https://github.com/SimonB00/clue/commits/main
  
## Next steps
Once the binding will be fully implemented, the code will be tested. In particular, the performance of the code will be compared to those of similar 
algorithms, like HDBScan. 
In the end the algorithm will be deployed as a Python library, making it available for the general public.

The proposal can be found at the link: https://summerofcode.withgoogle.com/programs/2022/projects/h8Np6Hjm
