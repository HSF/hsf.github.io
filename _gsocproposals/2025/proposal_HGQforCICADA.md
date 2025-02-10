---
title: Highly Granular Quantization for CICADA
layout: gsoc_proposal
project: CICADA
year: 2025
organization: princeton
---

## Description

The CICADA (Calorimeter Image Convolutional Anomaly Detection Algorithm) project aims to provide an unbiased detection of new physics signatures in proton-proton collisions at the Large Hadron Collider's Compact Muon Solenoid experiment (CMS). It detects anomalies in low-level trigger calorimeter information with a  convolutional autoencoder, whose behaviour is transferred to a smaller model through knowledge distillation. Careful quantization of the deployed model allows it to meet the requirement of sub-500ns inference times on FPGAs. While CICADA currently employs Quantization Aware Training with different quantization schemes for each layer of the distilled model, a new gradient-based quantization optimization approach published in 2024 offers the possibility of optimizing quantization at the individual weight level. This project would explore implementing this highly granular quantization method to CICADA's distilled model and evaluating its effects on both model performance and resource consumption on FPGAs. The work would involve implementing the new quantization approach, comparing it with the current implementation, and investigating the impact on both detection performance and hardware resource utilization while maintaining the strict timing requirements.

## Task ideas
 * Transition CICADA's quantization tool from QKeras to HGQ 
 * Optimize student model's quantization with higher granularity
 * Compare resulting model's performance with legacy model
 * Emulate deployment on FPGA w/ Vivado to evaluate resource consumption  

## Expected results
 * Extend existing training / quantization scripts to use HGQ in addition to QKeras
 * A trained student model with highly granular quantization
 * Estimates of that model's performance and resource consumption on an FPGA

## Requirements
Python, Tensorflow, Quantization

## Mentors
  * [Lino Gerlach](mailto:lino.oscar.gerlach@cern.ch)
  * [Isobel Ojalvo](mailto:iojalvo@princeton.edu)
  
## Links
  * [CICADA (homepage)](https://cicada.web.cern.ch/)
  * [CICADA (code)](https://github.com/Princeton-AD/cicada)
  * [HGQ (Paper)](https://arxiv.org/pdf/2405.00645)
  * [HGQ (code)](https://github.com/calad0i/HGQ)
