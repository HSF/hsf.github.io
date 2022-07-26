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
##### Mentors: Beomki Yeo & Charles Leggett

Acts is a track reconstruction software toolkit for high energy physics experiments. With the increasing number of particle interactions in the HL-LHC 
experimnts in the future the track reconstruction time will also increase. GPU R&D is conducted under traccc, vecmem and detray to accelerate the track 
reconstruction. Vecmem provides memory management tools for convenient GPU memory management and caching allocators, Detray is a geometry builder which 
translates the CPU geometry into GPU one (did not get my head around this one yet.) and finally Traccc demonstrates the gpu tracking pipeline.

This project mainly focuses on improving the throughput of the Traccc pipeline. This is achieved by using CUDA-MPS or CUDA-MIG and utilizing caching 
allocators provided by Vecmem.

Comprehensive introduction and progress : [here]( https://medium.com/@attanayakekavishka/optimization-of-gpu-tracking-pipeline-for-acts-gpu-r-d-part-1-4b7e9ac6379d )

### Communication 

#### Weekly meetings with the mentors

Weekly meetings were held every week (Thursdays) with the mentors starting from May 26th. Here my weekly progress, doubts and plans for the next week
were discussed.

#### Bi-weekly Acts Parallelization Group meeting

Bi weekly group meetings where contributors from different organizations and institutes discuss their updates. Moreover, dicussions on any new projects are
carried out. Understanding everything that is being discussed is a big challenge, nonetheless it is enjoyable listening to such an enthusiastic crowd.
This is a valuable oppotunity for me to grasp whats going on in the community and also learn from their discussions.

### Progress
#### Weeks 1-4 Ending on 16.06.2022

CUDA-MPS was something relatively new to me at the time, I had tested CUDA-MPS during application period and continued this work over during community bonding. Joined my first parallelization group meeting. Meanwhile started working on porting SYCL clusterization code to CUDA and was able to create a [PR (PR-206)]( https://github.com/acts-project/traccc/pull/206 ). This PR was not merged in as it was outdated at the time, nevertheless it was a great starting point and got valuable feedback from the community.

### Weeks 5-8 Ending on 14.07.2022

Modified the PR-206 to fit in with the latest version and added suggested changes, this was merged in [PR-209]( https://github.com/acts-project/traccc/pull/209 ).
My mentors provided access to a server at Lawrence Berkeley National Laboratory to conduct the benchmarking. Benchmarked overall throughput for the CPU algorithm and CUDA algorithm with and without MPS [logs here]( https://drive.google.com/drive/folders/15QFPNNwgh75RoRZ2au2_WybCuIMbUQpQ ). 
Currently I am in the process of analysing the kernel level throughput. 
Using caching allocators will be postponed for a while as binary paged memory resource did not produce the expected improvement in performance. Meanwhile, a way to use Contiguous memory resource as an alternative will be explored.



