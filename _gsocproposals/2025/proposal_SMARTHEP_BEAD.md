---
title: Background Enrichment augmented Anomaly Detection (BEAD) for new physics searches at LHC
layout: gsoc_proposal
project: BEAD
year: 2025
organization:
  - SMARTHEP
  - UManchester
difficulty: medium
duration: 350
mentor_avail: June-August 
project_mentors:
  - name: "Pratik Jawahar"
    email: "pratik.jawahar@cern.ch"
    organization: "CERN"
  - name: "Sukanya Sinha"
    email: "sukanya.sinha@cern.ch"
    organization: "CERN"
  - name: "Caterina Doglioni"
    email: "caterina.doglioni@cern.ch"
    organization: "CERN"
    role: "Backup Mentor"
---
​
## Short description of the project
A long-standing mystery of fundamental physics is the existence of dark matter (DM), 
a type of matter that has little interaction with ordinary matter but is supported by 
various astrophysical and cosmological observations and is six times more abundant
than ordinary matter in the universe. 
Several Large Hadron Collider (LHC) experiments are conducting 
searches aimed at detecting dark matter.  Unsupervised and semi-supervised 
learning outlier detection techniques are advantageous to these searches, 
for casting a wide net on a variety of possibilities for how dark 
matter manifests, as they impose minimal constraints from specific physics 
model details, but rather learn to separate characteristics of rare signals 
starting from the knowledge of the background they’ve been trained on. 
Developing innovative search techniques for probing dark matter signatures 
is crucial for broadening the DM search program at the LHC, and BEAD 
is a Python package that uses deep learning based methods for anomaly detection 
in HEP data for such new physics searches. BEAD has been designed with modularity in 
mind, to enable usage of various unsupervised latent variable models for any task.

BEAD has five main running modes:

   1. Data handling: Deals with handling file types, conversions between them and 
pre-processing the data to feed as inputs to the DL models.

   2. Training: Trains a model to learn implicit representations of 
the background data that may come from multiple sources(/generators)
to get a single, encriched latent representation of it.

   3. Inference: Using a model trained on an enriched background, the user can
feed in samples where to detect anomalies in.

   4. Plotting: After running Inference, or Training, one can generate plots. 
These include performance plots as well as different visualizations of the learned data.

   5. Diagnostics: Enabling this mode allows running profilers that measure
a host of metrics connected to the usage of the compute node to
help optimization of the code (using CPU-GPU metrics).

The package is under active development. 
The student in this project will work on the machine learning models available 
in BEAD, and implementing new models to perform anomaly detection, initially on simulated data.

## Task ideas

Possible projects include:

  * New auto-encoder models could be developed, 
better identifying correlations between data objects in a given particle physics dataset entry 
(containing event level and/or physics object level information). 
New models could also improve performance on live / unseen data. 
These could include transformer, GNN, probabilistic and other tiypes of networks.
  * Existing models could be tested on different datasets, 
potentially identifying distinct latent spaces populated by the different 
LHC physics processes, that can enable improved anomaly detection.

Ideas from the student working on this project are also welcome.

## Expected results

An improved performance of selected models, with documentation and figures of merit that may include:
  * Plots made in matplotlib that demonstrate the performance of the new models compared to the old
  * Documentation of the design choices made for the improved models
  * Documented evaluation of a physics analysis on data before and after compression

## Requirements

   * Python
   * Linux environment
   * ML / unsupervised algorithms key concepts 
   * PyTorch

   * Desired skills: transformers and/or graph neural networks, particle physics theory and experiments, particle physics simulations


## Links
  * [Paper on unsupervised ML algorithms using HEP datasets](<https://arxiv.org/abs/2105.14027>)
  * [Review of LHC searches using unsupervised learning](<https://arxiv.org/abs/2312.14190>)
  * [BEAD GitHub repository (WIP)](<https://github.com/PRAkTIKal24/BEAD>)
  * [ROOT](<https://root.cern/>)
  * [Jupyter](<http://jupyter.org>)
  * [PyTorch](http://pytorch.org)
