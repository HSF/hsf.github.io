---

project: PATATRACK
title: Implementation of a Python library that generalizes the CLUE clustering algorithm
author: Simone Balducci
date: 08.10.2022
year: 2022
layout: blog_post
logo: PATATRACK-logo.png
intro: |
  Description of the progress obtained in generalizing the CLUE clustering algorithm to N dimensions and binding it with Python.

---

## Introduction
Hello, I am Simone and I am currently working with the Patatrack team.  
The github repo for the project can be found [here](https://github.com/SimonB00/clue).  
The aim of the project I'm working on is to generalize the CLUE clustering algorithm to N dimensions, since it was initially designed to work in
2 dimensions. The following goal is to create a Python binding for the algorithm and deploy it as a Python library.

## Results obtained in the first period
So far, the generalization of the code has been fully implemented. Also, in order to make the algorithm more general it has been made independent of the
geometric properties of the detector.  
The Algorithm has been tested and it has been asserted that it works as expected. The output has been compared to that produced by the original algorithm,
and the two are compatible.  
The list of the commits can be found [here](https://github.com/SimonB00/clue/commits/main).

## The binding of the code
The CLUE algorithm has been binded into a python module created with pybind11.  
A problem that had to be solved was that the ClusteringAlgo is templated, where the template represents the number of dimensions, and the value of the template has to be known at compile time.  
The problem has been solved by writing several functions that execute the code for 10 possible dimensions, and the function mainRun, which is the the function that was eventually binded, runs the correct function depending on the number of dimensions that is passed in input.

## The clusterer class
The library contains a class named clusterer ([CLUEstering.py](https://github.com/SimonB00/CLUEstering/blob/main/CLUEstering/CLUEstering.py)) that reads the data, runs clue from the binded method in the pybind module and plots the data both in input and output, highlighting the different clusters and the ouliers in output. The output data can also be saved on csv files.  
The input data can either be from a csv file, a pandas dataframe, python lists or numpy arrays.  
The library also contains the method makeBlobs, which generates several 2D or 3D blobs and is intended as an easy way for the users to test the algorithm.
```
# Example
import CLUEstering as clue

clust = clue.clusterer(1,20,1.5)
clust.readData(clue.makeBlobs(1000,2))
clust.runCLUE()
clust.clusterPlotter()
```

The library has been called "CLUEstering" and has been officially uploaded to pypi (link at the end of the page).  
When a user downloads the library with the command "pip install CLUEstering", the wheel is built and the binding module is compiled locally, generating che .so file for the particular architecture of the user's machine.  
Building the wheel locally (thus using a source distribution instead of a source distribution) makes the installation slower, but is necessary, because the .so file has to be generated on the machine, otherwise the binded module wouldn't work.

![plot](https://raw.githubusercontent.com/SimonB00/GSOC_CLUE/main/images/blobwithnoise.png)

Useful links:  
[Link for the proposal](https://summerofcode.withgoogle.com/programs/2022/projects/h8Np6Hjm)  
[Link for the library on pypi](https://pypi.org/project/CLUEstering/)  
[Github repo of the library](https://github.com/cms-patatrack/CLUEstering)
