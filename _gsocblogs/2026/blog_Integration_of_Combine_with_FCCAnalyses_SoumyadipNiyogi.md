---
project: HSF
title: Integration of CMS Combine with FCCAnalyses
author: Soumyadip Niyogi
photo: blog_authors/SoumyadipNiyogi.jpg  # Upload your square photo to the blog_authors directory
avatar: https://avatars.githubusercontent.com/captainvogon  # Replace with your GitHub avatar URL
date: 19.05.2026
year: 2026
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  This summer, as a Google Summer of Code contributor with the HEP Software Foundation at CERN, I am bridging the gap between FCCAnalyses and CMS Combine. My project aims to build a native Python interface that automates the generation of datacards and RooFit workspaces directly from RDataFrame histograms, streamlining the path from simulated events to physics results.
---

|  |  |
| --- | --- |
| Name | [Soumyadip Niyogi](https://github.com/captainvogon) |
| Organisation | [IISER Thiruvananthapuram](https://www.iisertvm.ac.in/), [CERN](https://home.cern/), [HSF](https://hepsoftwarefoundation.org/) |
| Mentor | [Juraj Smiesko](https://github.com/kjvbrt) (CERN), [Jan Eysermans](https://github.com/jeyserma) (MIT) |
| Project | [Integration of CMS Combine with FCCAnalyses](https://summerofcode.withgoogle.com/programs/2026/projects/FyDjzZ3Y) |

## Introduction
Hi! I am Soumyadip Niyogi, a third-year BS-MS Physics student at IISER Thiruvananthapuram, India, and this summer I will be working with the HEP Software Foundation as a Google Summer of Code contributor at CERN.

My research so far has lived mostly in cosmology: MCMC-based constraints on modified gravity, Bayesian inference on Gamma-Ray Burst datasets, and simulating relativistic electrons in galaxy cluster magnetic fields. This project is my first serious step into collider physics, and I could not have asked for a better starting point.

## The Project
The Future Circular Collider (FCC) programme at CERN uses FCCAnalyses as its primary analysis framework. Built on ROOT's RDataFrame, it efficiently processes simulated EDM4hep collision events into histograms. But the next step, turning those histograms into actual physics results like discovery significances or exclusion limits, requires CMS Combine. Combine is a separate statistical tool that FCC physicists currently have to interface with manually.

That manual step is what I am here to automate. By the end of the summer, the goal is to have a native Python interface inside FCCAnalyses that reads RDataFrame output histograms and automatically generates the datacards and RooFit workspaces that Combine needs. The first piece of work is packaging Combine itself inside the Key4hep software stack so it is available as a standard dependency, requiring no separate installation.

## Community Bonding: Getting Up to Speed
I have been using the community bonding period to understand the landscape on both sides of the bridge I am building. 

On the FCCAnalyses side, I have been working through the benchmark $Z(\mu\mu)H(bb)$ analysis tutorial. This involved configuring the histmaker, stacking signal and background processes with the plotting utilities, and migrating my workspace from AFS to EOS to handle larger ROOT files. Generating recoil mass plots and studying b-tagging score distributions has given me a concrete picture of exactly what data structures my integration code will need to consume.

On the Combine side, I have been reading through the datacard format documentation and studying how RooFit workspaces encode shape systematics-the machinery that will form the core of the later project phases. I also had to tackle my first technical hurdle: setting up the Combine environment on CERN's `lxplus9` clusters without conflicting with the host's Key4hep stack. By isolating the environment using a Singularity container (`--cleanenv`) and building a local CMSSW workspace, I successfully compiled the tool and ran my first asymptotic limits check!

I will also be attending the group meeting with the FCCAnalyses team to introduce myself to everyone else, which should be highly beneficial for my future workflow and collaboration.

## Acknowledgements
Thank you to my mentors, Juraj Smiesko (CERN) and Jan Eysermans (MIT), for their time and guidance during the bonding period. More updates to follow as the coding phase begins!