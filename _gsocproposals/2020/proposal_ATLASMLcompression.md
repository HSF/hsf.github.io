---
title: Deep autoencoders for ATLAS data compression
layout: gsoc_proposal
project: ATLAS
year: 2020
organization: CERN
---

## Short description of the project 

Storage is one of the main limiting factors to the recording of information from proton-proton collision events at the [Large Hadron Collider](https://home.cern/science/accelerators/large-hadron-collider), at [CERN](https://home.cern) in Geneva. Hence, the [ATLAS](https://atlas.cern) experiment at the LHC uses a so-called [trigger system](https://atlas.cern/discover/detector/trigger-daq), which selects and sends interesting events to the data storage system while throwing away the rest. 

However, if interesting events are buried in very large backgrounds and difficult to identify as signal by the trigger system, they will also be discarded together with the background. To alleviate this problem, we plan to reduce the size of the data that is recorded, and study compression algorithms that can be used directly within the trigger system. A variety of compression algorithms is already in use in high energy physics (see e.g. [Zhe Zhang and Brian Bockelman. Exploring compression techniques for ROOT IO. CoRR (2017)](https://arxiv.org/abs/1704.06976)). 

A machine learning (ML) approach will be used to compress ATLAS data, specifically a method using autoencoder (AE) neural networks. In short an AE is a neural network which tries to implement an approximation to the identity, _f(x) ≈ x_, by using one or more hidden layers with smaller size than the input and output layers. If this is possible, it means that all the information necessary to reproduce the input, x, is contained in the hidden layer, and the data has been compressed. The idea is then to only save this smaller hidden layer representation instead of the current data format, along with the neural network that can recreate the original data. 

Moreover, an AE can be used for anomaly detection. This is perhaps the most common use of AEs and works as follows. The AE is first trained on data which is known not to be anomalous. If then the network is presented with a new data point that differs in some significant way from the training data, the AE will not be able to provide a faithful reconstruction at the output layer and hence the data point is considered anomalous. In other words, if the reconstruction error of a data point is larger than some threshold, it is considered anomalous. 

The aim of this project is to understand the standalone performance of an existing AE network, and whether this network can be used in combination with standard compression methods. Furthermore, a byproduct of this project is that the student will gain expertise in cutting-edge machine learning techniques, and learn to use them in the context of both data compression and detection of anomalous events. 

It will also be interesting to treat this study as a proof-of-principle for future data compression techniques for the ATLAS experiment. For the planned experimental upgrades in 2026, the techniques used in this report may help solving the problem of needing much more storage space than in the past due to the increase of the size of the dataset. 

## Project Milestones 

   * Run and benchmark an existing autoencoder network to compress ATLAS data.
      * Benchmarking includes and is not necessarily limited to:
         * The costs of training and decompressing the data in the context of a resource-constrained system such as the ATLAS trigger;
         * The fidelity of decompressed data with respect to original inputs, in terms of impact on the quality of the physics analysis with de-compressed objects; 
         * The dependence of the quality of the output on the similarity between training sample and test sample.
   * Understand whether the network can be used in combination with other compression algorithms already used at the LHC, and whether this can increase the compression factor overall.
   * The performance of combinations of compression algorithms will be evaluated using the same figures of merit as above. 
   * If time allows, study the performance of the network as an anomaly detection algorithm, injecting simulated signal data into background data. 

## Expected results

The first milestone will lead to a set of plots made in MatPlotLib/ROOT that should demonstrate the performance of the existing network on a different sample of ATLAS data with respect to what was used before for prototyping the network. 
The second milestone will lead to the same plots as above, but in the case when the network is fed variables to compress that have already been compressed with another algorithm beforehand. Particular attention will be paid to CPU cost and speed of the network.  Ideally, these plots will point to a configuration that is viable for use on already-compressed data. 
The third milestone will lead to a set of plots of the reconstruction error of a signal that is very different from the high-rate backgrounds that are being compressed, and increase the understanding of how the network treats anomalous signals when compressing it. 

## Requirements

Required: Good knowledge of UNIX, Python, MatPlotLib or ROOT, ability to install software and run a Jupyter notebook locally

Desirable: Knowledge of ROOT and PyTorch, batch submission algorithms

## Evaluation tasks

Jupyter and pyTorch exercise. 

Running the existing NN. 

Making plots in MatPlotLib/ROOT. 

## Links
  * [ROOT](https://root.cern/)
  * [Jupyter](http://jupyter.org)
  * [PyTorch](http://pytorch.org)

## Mentors
  * [Caterina Doglioni](mailto:caterina.doglioni@cern.ch)
  * [Antonio Boveia](mailto:antonio.boveia@cern.ch)
  * [Lukas Heinrich](mailto:lukas.heinrich@cern.ch)
