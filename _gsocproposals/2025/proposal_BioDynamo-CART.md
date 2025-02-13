---
title: Agent-Based Simulation of CAR-T Cell Therapy Using BioDynaMo
layout: gsoc_proposal
project: BioDynamo
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization: 
  - CERN
  - CompRes
project_mentors:
  - name: "Vassil Vassilev"
    email: "vvasilev@cern.ch"
  - name: "Lukas Breitwieser"
    email: "lukas.johannes.breitwieser@cern.ch"
---

## Description

Chimeric Antigen Receptor T-cell (CAR-T) therapy has revolutionized cancer treatment by harnessing the immune system to target and destroy tumor cells. While CAR-T has demonstrated success in blood cancers, its effectiveness in solid tumors remains limited due to challenges such as poor tumor infiltration, immune suppression, and T-cell exhaustion. To improve therapy outcomes, computational modeling is essential for optimizing treatment parameters, predicting failures, and testing novel interventions. However, existing models of CAR-T behavior are often overly simplistic or computationally expensive, making them impractical for large-scale simulations.

This project aims to develop a scalable agent-based simulation of CAR-T therapy using BioDynaMo, an open-source high-performance biological simulation platform. By modeling T-cell migration, tumor engagement, and microenvironmental factors, we will investigate key treatment variables such as dosage, administration timing, and combination therapies. The simulation will allow researchers to explore how tumor microenvironment suppression (e.g., regulatory T-cells, hypoxia, immunosuppressive cytokines) affects CAR-T efficacy and what strategies such as checkpoint inhibitors or cytokine support can improve outcomes.

The final deliverable will be a fully documented, reproducible BioDynaMo simulation, along with analysis tools for visualizing treatment dynamics. The model will provide insights into the optimal CAR-T cell dosing, tumor penetration efficiency, and factors influencing therapy resistance. This project will serve as a foundation for in silico testing of immunotherapies, reducing the need for costly and time-consuming laboratory experiments while accelerating the development of more effective cancer treatments.

## Expected plan of work:

- Phase 1: Initial Setup & Simple T-cell Dynamics
- Phase 2: Advanced CAR-T Cell Behavior & Tumor Interaction
- Phase 3: Integration of Immunosuppressive Factors & Data Visualization


## Expected deliverables

* A fully documented BioDynaMo simulation of CAR-T therapy.
* Analysis scripts for visualizing tumor reduction and CAR-T efficacy.
* Performance benchmarks comparing different treatment strategies.
* A research-style report summarizing findings.


## Requirements

* C++ (for BioDynaMo simulations) 
* Agent-based modeling (understanding immune dynamics)
* Basic immunology & cancer biology (optional but helpful)
* Data visualization (Python, Matplotlib, Seaborn)

## Links
* [Mapping CAR T-Cell Design Space Using Agent-Based Models](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2022.849363/full)
* [BioDynaMo: A Modular Platform for High-Performance Agent-Based Simulation](https://cds.cern.ch/record/2800211?ln=en)
* [Computational Modeling of Chimeric Antigen Receptor (CAR) T-Cell Therapy of a Binary Model of Antigen Receptors in Breast Cancer](https://ieeexplore.ieee.org/document/9669393)
* [Investigating Two Modes of Cancer-Associated Antigen Presentation in CAR T-Cell Therapy Using Agent-Based Modeling](https://www.mdpi.com/2073-4409/11/19/3165)
* [BioDynaMo: Cutting-Edge Software Helps Battle Cancer](https://home.cern/news/news/knowledge-sharing/biodynamo-cutting-edge-software-helps-battle-cancer)
