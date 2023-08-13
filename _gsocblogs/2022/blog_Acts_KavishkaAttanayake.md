---
project: Acts
title: Acts GPU R&D - Optimization of GPU tracking pipeline
author: Kavishka Attanayake
photo: blog_authors/KavishkaAttanayake.jpeg
date: 26.07.2022
year: 2022
layout: blog_post
logo: ACTSlogo.gif
intro: |
  This blog summarizes what progress I have achieved, what I have learnt and my experiences during the GSoC period. Improving throughput can be achieved by attempting to reduce compute times as well as improving hardware utilization. In this project I aim to utilize caching allocators to reduce data reading times as well as utilize CUDA MPS to maximize the GPU utilization of the parallelized CUDA algorithm and compare it against the multicore CPU algorithm.
---

# Acts GPU R&D - Optimization of GPU tracking pipeline

### Dear future readers

Hey all! As of starting GSoC 2022 I am a third year undergraduate from the
University of Moratuwa, Sri Lanka. GSoC program was an excellent way to get
started with open source and explore technology/fields that interest you with
the help of experienced mentors. Personally, astrophysics was something I was
really curious about since I was a little kid, this was one main reason I chose
to contribute under CERN. Moreover CUDA was not completely new to me therefore,
I found this project a good fit. It's okay to not know about everything, there
were many new concepts to me which I understood along the way.

If you are a potential future contributor, I suggest that communication is the
most important skill that's required. If you are having a difficulty your
mentors are always willing to help you out!

## Project Description

##### Mentors: Beomki Yeo & Charles Leggett

Acts is a track reconstruction software toolkit for high energy physics
experiments. With the increasing number of particle interactions in the HL-LHC
experiments in the future the track reconstruction time will also increase. GPU
R&D is conducted under traccc, vecmem and detray to accelerate the track
reconstruction. Vecmem provides memory management tools for convenient GPU
memory management and caching allocators, Detray is a geometry builder which
translates the CPU geometry into GPU one (did not get my head around this one
yet.) and finally Traccc demonstrates the gpu tracking pipeline.

This project mainly focuses on improving the throughput of the Traccc pipeline.
This is achieved by using CUDA-MPS or CUDA-MIG and utilizing caching allocators
provided by Vecmem.

Comprehensive introduction and progress :

- [mid report](https://medium.com/@attanayakekavishka/optimization-of-gpu-tracking-pipeline-for-acts-gpu-r-d-part-1-4b7e9ac6379d)
- [complete report](https://chamodya-ka.github.io/blog/GSOC-2022/)

### Communication with the mentors and the community

#### Weekly meetings with the mentors

Weekly meetings were held every week (Thursdays) with the mentors starting from
May 26th. Here my weekly progress, doubts and plans for the next week were
discussed.

#### Bi-weekly Acts Parallelization Group meeting

Bi weekly group meetings where contributors from different organizations and
institutes discuss their updates. Moreover, discussions on any new projects are
carried out. Understanding everything that is being discussed is a big
challenge, nonetheless it is enjoyable listening to such an enthusiastic crowd.
This is a valuable opportunity for me to grasp what's going on in the community
and also learn from their discussions.

## Progress

#### Weeks 1-4 ( including community bonding )

> Ending on 16.06.2022

CUDA-MPS was something relatively new to me at the time, I had tested CUDA-MPS
during the application period and continued this work over during community
bonding. Joined my first parallelization group meeting, gave me the opportunity
to see and listen to the developers and introduce myself as well. Meanwhile
started working on porting SYCL clusterization code to CUDA and created a
[PR (PR-206)](https://github.com/acts-project/traccc/pull/206). This PR was not
merged in as it was outdated at the time, nevertheless it was a great starting
point and got valuable feedback from the community. Moreover, my mentors
provided access to a server at Lawrence Berkeley National Laboratory to conduct
the benchmarking.

#### Weeks 5-8

> Ending on 14.07.2022

Modified the PR-206 to fit in with the latest version and added suggested
changes, this was merged in
[PR-209](https://github.com/acts-project/traccc/pull/209). Tests were done using
caching allocators, and there were issues along the way
([issue with contiguous memory resource](https://github.com/acts-project/vecmem/issues/180)
and issue with
[binary page memory resource](https://github.com/acts-project/vecmem/issues/182)),
Once the issues were fixed by the Vecmem developers. I carried out benchmarks
using contiguous memory resource and got expected results. Sadly, using binary
page memory resource did worse than using any caching allocation at all.
Therefore, benchmarking throughput with caching allocators was postponed.
Meanwhile, a way to use Contiguous memory resource as an alternative will be
explored. In addition, prepared the bash scripts and modified the CUDA algorithm
to be suitable for benchmarking and comparing against the CPU algorithm.

#### Weeks 9-10

> Ending on 28.07.2022 (Mid Evaluation)

Benchmarked overall throughput for the CPU algorithm and CUDA algorithm with and
without MPS
[logs available here](https://drive.google.com/drive/folders/15QFPNNwgh75RoRZ2au2_WybCuIMbUQpQ).
Speed up by using MPS can be expected only from this kernel execution and memory
transfer portion. Therefore, significant improvement was not observable by using
MPS, since CUDA kernel execution only takes up ~10% of the entire process. As
advised by my mentors I started benchmarking kernel level throughput with and
without MPS. Currently I have completed benchmarking and in the process of
analyzing the kernel execution times. After this analysis it will provide more
insight into how the number of processes will affect the individual kernel
throughput.

Following are two comparisons between using MPS and not using MPS each process
computes 10 and 150 events respectively. X axis is the number of processes that
are running concurrently. Y axis is the throughput in events/second

![10_events](https://user-images.githubusercontent.com/58067288/181102393-bf893de6-492d-4c5c-8187-3c3db2eeff49.jpg)
![150_events](https://user-images.githubusercontent.com/58067288/181108051-5f3bdd22-6d23-46cc-b764-4ccb6661a169.jpg)

#### Weeks 11-14

> Ending on 25.08.2022

The plots on the kernel level execution were cluttered as there was no
synchronization before each kernel execution among the concurrent processes.
During the first two weeks, I worked on using shared memory to implement inter
process communication to synchronize the concurrent processes and obtained the
execution times. However, interpreting the results required help from my
mentors, this will be discussed later. Moreover, benchmarks were carried out on
the overall pipeline using vecmem caching allocators and multiple memory
resources. Similar benchmarks were conducted to find how many events per process
would give the peak throughput. The results will be discussed below. I was given
the opportunity to present my progress and contributions at the ACTS
parallelization group meeting as well.

### Results

#### Throughput benchmarks

Comparison between different memory resources is shown below.

![mem_res_mps_comparision](https://user-images.githubusercontent.com/58067288/189314296-e8d48284-69ab-4b9a-9664-36eb237fdba4.jpg)

By utilizing contiguous memory resource with CUDA pinned memory upstream, the
effect of CUDA mps is significant compared to when using only managed memory(see
the plots under week 9-10).
![c_mr_mps_comp](https://user-images.githubusercontent.com/58067288/189314610-236667f5-956b-465f-aa68-ab5d6e12321c.png)

The plot below shows a throughput comparison between multicore CPU and CUDA-MPS.
![mps_cuda_cpu](https://user-images.githubusercontent.com/58067288/189314831-08131ba8-1f8d-4da2-a683-965f503f387b.png)

#### Kernel level benchmarks

The following is a single kernel execution time plot for the spacepoint
formation kernel against the number of concurrently running processes.
![form_spacepoints](https://user-images.githubusercontent.com/58067288/189314421-87f4c0ac-391b-445b-be53-1b2647f811b5.png)

The sudden increase in times from 2 to 3 processes can be explained as there are
2 GPUs and introducing a third process can cause a single GPU to work almost
twice as long stretching the wait time for all 3 processes. Similar case when
there are 4 processes, now each GPU works twice as long. However this trend does
not continue over when the number of processes increase further, this can be
explained as a one time overhead as GPU context switching is introduced for the
first time.

### Conclusion

This concludes my GSoC adventure, I got the opportunity to contribute to CERN as
well as learn CUDA further. Moreover the interaction with my mentors was helpful
to improve my soft skills too!
