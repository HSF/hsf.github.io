---
title: Probabilistic circuit for lossless HEP data compression
layout: gsoc_proposal
project: Baler
year: 2025
organization:
  - CERN
difficulty: medium
duration: 350
mentor_avail: June-October (with 3 weeks mentor vacation where student will work independently with minimal guidance)
project_mentors:
  - name: "Leonid Didukh"
    email: "ledidukh@gmail.com"
  - name: "Caterina Doglioni"
    email: "caterina.doglioni@cern.ch"
---
​
## Short description of the project
Neural data compression is an efficient solution for reducing the cost and computational resources of data storage in many LHC experiments.
However, it suffers from the ability to precisely reconstruct compressed data, as most of the neural compression algorithms perform the decompression with the information loosage.
On another hand, the lossless neural data compression schemas (VAE, IDF) have a lower compression ratio and are not fast enough for file IO.
This project's task is to overcome the disadvantages of the neural compression algorithm by using the probabilistic circuit for HEP data compression.

## Task ideas

* Implement the probabilistic circuit using the PyTorch
* Train and compress the HEP data (Higgs data, TopQuark Dataset)
* Measure the cost and quantify the optimal compression ratio of the probabilistic circuit
* Perform the benchmark, and compare the results with AE, Transformer

## Expected results

An improved compression performance with documentation and figures of merit that may include:
  * Implemented model of the probabilistic circuit
  * Documentation of the benchmark and experiment of compression of the HEP data

## Requirements

Required: Good knowledge of UNIX, Python, matplotlib, Pytorch, Julia, Pandas, ROOT. 

## Links

* Previous work:
  
   * [GSOC 2021 project: Zenodo entry by George Dialektakis](https://zenodo.org/record/5482611#.Y-I28S2l3fa)
   * [Baler -- Machine Learning Based Compression of Scientific Data
](https://arxiv.org/abs/2305.02283)

 * [ROOT](https://root.cern/)
 * [Jupyter](http://jupyter.org)
 * [Lossless compression with probabilistic circuits](https://arxiv.org/pdf/2111.11632)
 * [iFlow: Numerically Invertible Flows for Efficient Lossless Compression via a Uniform Coder](https://arxiv.org/pdf/2111.00965)
 * [Integer Discrete Flows and Lossless Compression](https://arxiv.org/pdf/1905.07376)
   


