---

project: Dataset-manipulation tools for simulated collider events
title: Midterm evaluation blog post
author: Kalp Shah
date: 9.08.2022 
year: 2022 
layout: blog_post
logo: UGlasgow-logo.png
intro: A software package that provides tools for manipulation of HEP specific datasets 

---

## Introduction

This project aims to make the process of performing any form of modification to the simulated collider events a much simpler one. Examples of such changes include slicing, converting, merging, splitting, and any combination of such processes.

The scope of the project changed during the middle, and implementation of a pileup tool was added to it. It is a tool that generates signal events superimposed with min-bias events, resulting in an event-generator-level approximation to the presence of pileup in high-luminosity collisions.

## Progress

It was decided to split the modification toolkit as a collection of small python programs that perform a particular task which can then be used together for performing a combination type process. Till the mid-evaluation, the functions that are implemented are the following :

- Conversion of file formats
- Slicing out the top n events from the file, equivalent to the `head` command
- Slicing out the top n events from the file, equivalent to the `tail` command

On the other hand, progress on the pile up tool was made. The tool is called pilemc which was previously a C++ tool last updated in 2015.

The pilemc code is to be rewritten in python. Most of the algorithm is implemented except the case when a signal file is not provided.

## Work Left

For the dataset manipulations, the following functionality is remaining :

- Merging of Files
- Filtering of events

Another task that is remaining is to provide the same functionality as a python library.

For pilemc, the tasks remaining are :
- Complete the replication in python
- Implement additions to the program that allow different modes of operation for memory allocation. The possible modes being :
    - Load the entire file into memory at once
    - Sample events from the file and close it as per requirement
- Change the working of the pile-up files from cross sections to bias value (&mu;)

## Links

The codes are dataset manipulation are present here : https://github.com/Blizzard57/data-manipulation

The codes for pilemc are present here : https://gitlab.com/hepcedar/pilemc