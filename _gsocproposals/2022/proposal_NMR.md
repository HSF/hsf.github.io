---
title: Decoding quantum states through nuclear magnetic resonance
layout: gsoc_proposal
project: NMR
year: 2022
organization:
 - Brown
 - Dartmouth
---

# Description
At low temperatures, many materials transition into an electronic phase which cannot be classified as a simple metal or insulator. So-called quantum phases of matter, like superconductors and spin liquids, are hard to study due to their fragile nature, making nonintrusive and indirect measurements important. We will explore the connection between electronic phases and nuclei in these materials via simulations of nuclear magnetic resonance (NMR). By using external magnetic pulses, the nuclear spins can be controlled, and their time-evolution (time-dependent magnetization) studied.

## Task ideas
  * Implement a classification model that determines the type of electronic interaction based on only the time-dependent curve. How sensitive is this classification to noise?
  * Utilize a neural network to predict the strength, range, and dissipation parameters of a given magnetization curve. 
  * Develop an algorithm which optimizes an applied pulse sequence to best estimate a specific physical parameter from a given material.
  
## Expected results
  * Comparison between ML algorithms to determine the ones best suited to the selected problem, including optimization of hyper parameters. When applicable, the gradients or important features of the model will be analyzed to determine what aspects of the experimental signal are most important.
   
## Requirements 
Python and some experience in Machine Learning. For using the NMR simulation code, familiarity with CUDA (GPU) and the Julia language will be helpful. 

## Mentors
  
  * [Stephen Carr](mailto:ml4-sci@cern.ch) (Brown University)
  * [Vesna Mitrovic](mailto:ml4-sci@cern.ch) (Brown University)
  * [Chandrasekhar Ramanathan](mailto:ml4-sci@cern.ch) (Dartmouth University)
  * [Brad Marston](mailto:ml4-sci@cern.ch) (Brown University)
  * [Charles Snider](mailto:ml4-sci@cern.ch) (Brown University)
  
Please DO NOT contact mentors directly by email, and instead please send project inquiries to [ml4-sci@cern.ch](mailto:ml4-sci@cern.ch) with Project Title in the subject and relevant mentors will get in touch with you. 
