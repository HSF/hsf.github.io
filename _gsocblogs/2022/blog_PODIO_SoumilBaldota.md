---

project: Interfacing PODIO with Julia
title: Midterm evaluation blog post
author: Soumil Baldota
date: 28.07.2022 
year: 2022 
layout: blog_post
logo: podio-logo.png
intro: Midterm progress report

---


In the community bonding period, with the help of Thomas and Benedikt, I setup my development environment and began to work on a prototype for the Interface which described how the generated code would look like. The prototype was created for classes with one to one relations, one to many relations and vector members. Then I made unittests for the prototype and added them to github actions for continuos integration. 

The prototype can be found at the below link

[Prototype](https://github.com/soumilbaldota/PODIO_Julia_Interface_Prototype.git)
  

After the prototype was created. I added an attribute to store the Julia type of a data member described in C++ to the MemberVariable Class and a function to get the Julia type in [generator_utils.py](https://github.com/AIDASoft/podio/blob/julia/python/generator_utils.py) and added some unittests for the same.

Work in progress:

Adding the necessary preprocessing logic for code generation to [podio_class_generator](https://github.com/AIDASoft/podio/pull/311/files) and adding preprocessing steps necessary for code generation.
Currently some of the code generation works but still needs some fixes and additional features.
