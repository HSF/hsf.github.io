---
title: Graph Neural Networks for Charged Particle Tracking
layout: gsoc_proposal
project: iris-hep
year: 2023
organization:
- princeton
- iris-hep
difficulty: high
duration: 375
mentor_avail: May-October
---

## Description

[Charged particle tracking][tracking-wiki] reconstructs the trajectories ("tracks") of elementary particles traveling through a detector. 
This task is different from many other problems that involve trajectories: 

* there are several thousand particles that need to be tracked at once,
* there is no time information (the particles travel too fast),
* we do not observe a continuous trajectory but instead only around five points ("hits") along the way in different detector layers.

The task can be described as a combinatorically very challenging "connect-the-dots" problem, essentially turning a cloud of points (hits) in 3D space into a set of O(1000) trajectories.
Expressed differently, each hit (containing not much more than the x/y/z coordinate) must be assigned to the particle/track it belongs to.

Tracking algorithms are a crucial part of the software used at big high energy physics experiments and have a strong impact on their physics performance.
They are also computationally very expensive and can limit the rate at which data taking occurs.
For these reasons, tremendous development efforts have been spent on tracking software.
Historically, tracking software was mostly specific to individual physics experiments, but recent efforts such as [Acts][acts] have shown the potential of strong open-source community efforts.

Unlike traditional tracking algorithms that are built around [Kalman filters][kalman], this project uses [graph neural networks][gnn-wiki] for significant increases in speed.
A conceptually simple way to turn tracking into a machine learning task is to create a fully connected graph of all points and then train an edge classifier to reject any edge that doesn't connect points that belong to the same particle. 
In this way, only the individual trajectories remain as components of the initial fully connected graph.
However, this strategy does not lead to perfect results in practice, so it is usually combined with other steps.

While many of the model architectures are still actively explored and a variety of pipelines are under investigation, this project aims to build up a modular code base for many different GNN tracking studies.
By providing different models and common utility functions, the framework comes batteries-included while still remaining flexible for new ideas of any kind.
Our hope is that the code base will lower the entry-barrier for new studies and become a focal point of the community. 

The project code together with documentation and a reading list is available on [github][ghorganization].

## Objectives and Tasks

Depending on the candidate, two different areas can be explored:

Area 1: Software engineering. Example tasks: 

* Increase training efficiency and GPU utilization
* Port tracking metrics from `numpy`/`pandas` to `pytorch`
* Switch to a GPU-ready implementation of `DBSCAN`
* Improve use of hyperparameter optimization scripts (currently built around [ray tune][raytune]) on HPC clusters with the [SLURM][SLURM] workload manager
* General work on unit testing and maintenance tasks

Area 2: Machine learning & statistics. Example tasks:

* Investigate and contribute new model architectures
* Implement and investigate different clustering algorithms
* Run side-studies for variations of the existing architecture
* Run hyperparameter optimizations

Of course, students can also mix tasks from both areas.
Many of the concrete tasks are collected as [issues in the main GNN Tracking repository][issues].

## Requirements

For area 1:

* Excellent python skills, ideally including `pytorch` or `numpy`
* Working knowledge on git
* Dream candidate would specifically have experience with `pytorch`, GPU programming, or [ray][ray]

For area 2:

* High degree of mathematical understanding: candidate should be able to read general machine learning papers and implement the described architectures or loss functions
* General experience in data science and machine learning frameworks, preferably with `pytorch`
* Dream candidate would have some prior experience with graph neural networks, ideally with [`pytorch` geometric][pyg]

## Expected results

Example outcomes for area 1:

* Significantly faster training, making the best use of the available resources
* The whole pipeline should run on the GPU
* A user-friendly workflow that runs hyperparameter sweeps with [ray tune][raytune]) on a system with the [SLURM][SLURM] workload manager.

Example outcomes for area 2:

* Increased overall efficiency/performance of the default pipeline
* Detailed writeup of different architectures/algorithms and corresponding results
* Code available for every side-study, ideally in the main repository as a model that can be switched out with the current one, alternatively as a verbose Jupyter notebook.

## Mentors

* Kilian Lieret [kl5675@princeton.edu](mailto:kl5675@princeton.edu) Princeton University
* Gage deZoort [jdezoort@princeton.edu](mailto:jdezoort@princeton.edu) Princeton University

[SLURM]: https://slurm.schedmd.com/overview.html
[raytune]: https://docs.ray.io/en/latest/tune/index.html
[issues]: https://github.com/gnn-tracking/gnn_tracking/issues
[ray]: https://www.ray.io/
[ghorganization]: https://github.com/gnn-tracking
[pyg]: https://pytorch-geometric.readthedocs.io/
[tracking-wiki]: https://en.wikipedia.org/wiki/Tracking_(particle_physics)
[gnn-wiki]: https://en.wikipedia.org/wiki/Graph_neural_network
[acts]: https://github.com/acts-project/acts
[kalman]: https://en.wikipedia.org/wiki/Kalman_filter