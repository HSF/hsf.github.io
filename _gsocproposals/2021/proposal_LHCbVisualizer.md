---
title: Implementing an application for visualizing the LHCb DAQ network
layout: gsoc_proposal
project: LHCb
year: 2021
organization:
    - CERN
---

## Description

LHCb will operate the largest data acquisition network built today for any scientific instrument using state-of-the-art fast networks.
The supercomputer that is currently constructed at the LHCb will allegedly be the largest real-time data acquisition system in the World in 2021. 
In order to ascertain its real-time operation (thus avoiding losing critical physics data), some meticulous design of the network has to be made. 
The system has to optimally utilize the Remote Direct Memory Access (RDMA) cluster technology with such fabrics as InfiniBand or RDMA over Converged  Ethernet (RoCE v2).
This development process of this real-time network requires some additional utility tools to monitor and visualize the designs of networks. 
The purpose of this project is to develop a utility GUI application to "visualize" this high-speed network.
This is a notable difference from existing network monitoring tools that are targeting more classical IP over Ethernet.
This is to have some additional mechanisms to debug, design, and modify the LHCb data acquisition network.



## Task ideas

Starting from an existing application in Python, the program will be fed with network and routing data from the hardware.
In the GUI one must be able to clearly visualize:

 * the network topology
 *  the routing configuration in the switches
 *  conflicts with the relevant details in the network for a given input traffic patterns

## Expected results


 * Implemented GUI.
 * GUI must visualize large networks and traffic in a clear, optimized for ease of use for the end-user.
 * Embedding the GUI into the existing Python project that produces the input network configuration and routing tables.
 * Ascertaining ease of use of the application by feeding the GUI with existing network setups.
 * The final purpose is to have a helpful tool for the commissioning of the LHCb Event Builder.
 * Real-time network upgrades, during system runtime, is a very welcome bonus.
 
## Evaluation Task

Interested students please contact Rafal (see contact below) to ask questions and for an evaluation task.


## Requirements

 * C
 * C++
 * Python
 * Computer networks
 * Writing GUIs
 * Graphs
 * Git
 * Knowledge of InfiniBand and RoCE is optional but welcome


## Mentors
 * **[Rafal Dominik Krawczyk](mailto:rafal.dominik.krawczyk@cern.ch)**
 * [Niko Neufeld](mailto:niko.neufeld.cern.ch)

## Links
 * [LHCb intro](https://www.youtube.com/watch?v=rsmBMuTFdkA&ab_channel=CERN)
 * [LHCb experiment intro](https://www.youtube.com/watch?v=8lbQUa8z3M0&ab_channel=CERN)
 * [LHCb virtual visit](https://www.youtube.com/watch?v=bv-wFtA0gCQ)
 * [LHCb home page](https://lhcb-public.web.cern.ch/)
 * [LHCb DAQ ](https://indico.cern.ch/event/974424/contributions/4217589/attachments/2186332/3694141/DAQFEET_9_02_21_FINAL.pdf)
 * [InfiniBand intro](https://indico.cern.ch/event/218156/attachments/351724/490088/Intro_to_InfiniBand.pdf)

