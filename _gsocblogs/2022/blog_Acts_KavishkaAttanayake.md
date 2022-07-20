---  
project: Acts
title: Acts GPU R&D - Optimization of GPU tracking pipeline
author: Kavishka Attanayake
photo: Add
date: 20.07.2022
year: 2022
layout: blog_post
logo: Add
intro: |
  This blog summarizes what progress I have achieved, what I have learnt and my experiences during the GSoC period
--- 

## Project Description
Mentors: Beomki Yeo & Charles Leggett
Acts is a track reconstruction software toolkit for high energy physics experiments. With the increasing number of particle interactions in the HL-LHC 
experiemnts in the future the track reconstruction time will also increase. GPU R&D is conducted under traccc, vecmem and detray to accelerate the track 
reconstruction. Vecmem provides memory management tools for convinient GPU memory management and caching allocators, Detray is a geometry builder which 
translates the CPU geometry into GPU one (did not get my head around this one yet.) and finally Traccc demonstrates the gpu tracking pipeline.

This project mainly focuses on improving the throughput of the Traccc pipeline. This is achieved by using CUDA-MPS or CUDA-MIG and utilizing caching 
allocators provided by Vecmem.


### Communication 

#### Weekly meetings with the mentors

Weekly meetings were held every week (Thursdays) with the mentors starting from May 26th. Here my weekly progress, doubts and plans for the next week
were discussed.

#### Bi-weekly Acts Parallelization Group meeting

Bi weekly group meetings where contributors from different organizations and institutes discuss their updates. Moreover, dicussions on any new projects are
carried out. Understanding everything that is being discussed is a big challenge, nonetheless it is enjoyable listening to such an enthusiastic crowd.
This is a valuable oppotunity for me to grasp whats going on in the community and also learn from their discussions.
