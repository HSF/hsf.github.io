---
project: Geant4
title: Symplectic Integrators
author: Divyansh Tiwari
date: 27.07.2022
year: 2022
layout: blog_post
logo: Geant4-logo.png
intro: |
  Implementing Symplectic Integrators 
---

## Introduction

Hello Everyone! This is Divyansh. I was accepted to take part in GSoC 2022 under CERN-HSF and I am contributing to Geant4. My project is about implementing symplectic integrators into the Geant4 codebase. Many applications require the use of integrator method that preserve evergy over the course of a simulation.
Hence, the aim of this project is to implement multiple methods which do not accumulate errors in energy and phase space volume over a large number of integration steps.A famous class of methods which fulfill the above criteria are the symplectic integrators.

## Getting Into The Program

After going through the list of projects, I decided upon the one I was going to apply, pretty early on. I was really interested in the physics behind the symplectic integrator. I also had some prior experience of working on implementing them. I mailed the mentors with my interest in the project, following which I received a qualification task. I submitted my solution to the task and after that, worked with my mentors to develop a project proposal. The projects were announced in may and I was selected!

## Starting Off - The Community Bonding Period

This was a very essential period. I had my first meet with my mentors and I got to know a bit about their works. We figured out the logistics of how we'll be planning out the 3 month long coding period. I also got to attend the GSOC'22 Global Summit and learnt about the importance of open source. The rest of the community bonding period was utilized on brushing up my basics as well as learning to use the Geant4 toolkit.

## Coding Period - Kick Off

Before starting work on the actual methods, it was important develop up a test bed application that could be used to test the steppers and drivers. Hence, I started off my coding period by implementing a geant4 application to track a particle in a geometry initialized with a magnetic field. This was really interesting and exciting for me as I had done my homework during the community bonding period. The test bed is comprised of a detector constructor class, a physics list class and a primary action generator class. The magnetic field of the geometry and the stepper used for tracking the particle can defined in the detector constructor. The physics list is used to define various particles and physical processes. Finally, the primary generator was used to initialize the particle. I utilized the test bed to test out various steppers already present in the codebase to profile them.

## First Method

After implementing the above application, we started deliberating on the first method that we'll implement. We ultimately decided on the Boris Algorithm for its excellent performance in electromagnetic field. The same was implemented by using the familiar driver and dtepper design used in Geant4. The stepper(`G4BorisScheme`) implements the actual Boris Algorithm and the driver(`G4BorisDriver`) is used to manage the stepper.

## Some Links

1. [Mid-Term Report](https://docs.google.com/document/d/1LMNU8qvVKALE9EH1Hc5ROZeL-fl60gFf81KE4QsBj0M/edit?usp=sharing)
2. [Project Proposal](https://docs.google.com/document/d/1gLeoJs8HuCoLsN0AeceiVCH1QyNXHK9V3zmpyA0v0QM/edit?usp=sharing)
3. [Merge Request](https://gitlab.cern.ch/geant4/geant4-dev/-/merge_requests/2930)