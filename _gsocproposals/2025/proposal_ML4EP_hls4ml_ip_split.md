---
title: Optimizing Model Splitting in hls4ml for Efficient Multi-Graph Inference
layout: gsoc_proposal
project: ML4EP
year: 2025
organization: CERN
difficulty: medium
duration: 350
mentor_avail: Flexible
---

# Description
hls4ml is an open-source tool that enables the deployment of machine learning (ML) models on FPGAs using High-Level Synthesis (HLS). It automatically converts pre-trained models from popular deep learning frameworks (e.g., Keras, PyTorch, and ONNX) into optimized firmware for FPGA-based inference.

Traditionally, the entire ML model is synthesized as a monolithic graph, which can lead to long synthesis times and complicated debugging, especially for large model topologies. Splitting the model graph at specified layers into independent subgraphs allows for parallel synthesis and step-wise optimization. However, finding the 'optimal' splitting points and optimizing FIFO buffers in between the subgraphs remains a challenge, especially when dealing with dynamic streaming architectures.

This project aims to investigate optimal splitting strategies for complex ML models in hls4ml, focusing on efficient FIFO depth optimization across multi-graph designs. The goal is to develop methodologies that can be integrated into hls4ml to enable automated and optimal graph splitting for improved performance.

## Task ideas
The contributor will start by familiarizing themselves with hls4ml and building ML models using multi-graph designs. They will implement profiling techniques (e.g., VCD logging) to measure FIFO occupancy and backpressure in order to develop a FIFO optimization strategy for multi-graph designs. They will also investigate multi-objective optimization algorithms to determine optimal splitting points based on subgraph resource usage or dataflow patterns. Finally, they will integrate these methodologies with hls4ml and run benchmarks to validate improvements in latency, resource utilization, etc.

## Expected results and milestones
 * **Familiarization with hls4ml**: Understand the hls4ml workflow, including synthesis, and simulation.
 * **Research and Evaluation**: Explore FIFO profiling and optimization strategies along with algorithms to partition the model graph given specific optimization objectives.
 * **Validation**: Benchmark against monolithic implementations and compare differences in latency and resource utilization.

## Requirements
  * Proficiency with computer architecture, FPGA design and simulation tools (e.g., Vivado)
  * Experience with Python
  * Understanding of ML concepts is beneficial.
  * Familiarity with version control systems like Git/GitHub.

## Mentors
  * **[Vladimir Loncar](mailto:vladimir.loncar@cern.ch)**
  * [Dimitrios Danopoulos](mailto:dimitrios.danopoulos@cern.ch)

## Links
  * [hls4ml documentation](https://fastmachinelearning.org/hls4ml/)
  * [hls4ml Repository](https://github.com/fastmachinelearning/hls4ml)
  * [Vivado Design Implementation](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Design-Implementation)
