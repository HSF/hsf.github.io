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

In the GNN tracking project, we use [graph neural networks][gnn-wiki] (GNNs) to reconstruct trajectories ("tracks") of elementary particles traveling through a detector. 
This task is called ["tracking"][tracking-wiki] and is different from many other problems that involve trajectories: 

* there are several thousand particles that need to be tracked at once,
* there is no time information (the particles travel too fast),
* we do not observe a continuous trajectory but instead only around five points ("hits") along the way in different detector layers.

The task can be described as a combinatorically very challenging "connect-the-dots" problem, essentially turning a cloud of points (hits) in 3D space into a set of O(1000) trajectories.
Expressed differently, each hit (containing not much more than the x/y/z coordinate) must be assigned to the particle/track it belongs to.

A conceptually simple way to turn this problem into a machine learning task is to create a fully connected graph of all points and then train an edge classifier to reject any edge that doesn't connect points that belong to the same particle. 
In this way, only the individual trajectories remain as components of the initial fully connected graph.
However, this strategy does not seem to lead to perfect results in practice.
The approach of this project uses this strategy only as the first step to arrive at "small" graphs.
It then projects all hits into a learned latent space with the model learning to place hits of the same particle close to each other, such that the hits belonging to the same particle form clusters.

The project code together with documentation and a reading list is available on [github][ghorganization] and uses [pytorch geometric][pyg].

## Objectives and Tasks

Depending on the candidate, two different areas can be explored:

Area 1: Software engineering 

* Increase training efficiency and GPU utilization
* Port tracking metrics from `numpy`/`pandas` to `pytorch`
* Switch to a GPU-ready implementation of `DBSCAN`
* Improve use of hyperparameter optimization scripts (currently built around [ray tune][raytune]) on HPC clusters with the [SLURM][SLURM] workload manager
* General work on unit testing and maintenance tasks

Area 2: Machine learning & statistics

* Investigate different model architectures
* Investigate use of different clustering algorithms
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

For area 1:

* Significantly faster training, making the best use of the available resources
* The whole pipeline should run on the GPU
* A user-friendly workflow that runs hyperparameter sweeps with [ray tune][raytune]) on a system with the [SLURM][SLURM] workload manager.

For area 2:

* Increased overall efficiency/performance of the model
* Detailed writeup of different architectures/algorithms and corresponding results
* Code available for every side-study, ideally in the main repository as a model that can be switched out with the current one, alternatively as a verbose Jupyter notebook.

## Mentors

* Kilian Lieret [kl5675@princeton.edu](mailto:kl5675@princeton.edu) Princeton University
* TBD

[SLURM]: https://slurm.schedmd.com/overview.html
[raytune]: https://docs.ray.io/en/latest/tune/index.html
[issues]: https://github.com/gnn-tracking/gnn_tracking/issues
[ray]: https://www.ray.io/
[ghorganization]: https://github.com/gnn-tracking
[pyg]: https://pytorch-geometric.readthedocs.io/
[tracking-wiki]: https://en.wikipedia.org/wiki/Tracking_(particle_physics)
[gnn-wiki]: https://en.wikipedia.org/wiki/Graph_neural_network
