---
title: Tensorflow-TMVA GAN Interface Applied to NOvA Neutrino Events.
layout: gsoc_proposal
project: NOvA
organization:
 - NOvA
 - Fermilab
 - CERN
 - UFlorida
 - Google
 - KIT
---

# Description
[NOvA](https://www-nova.fnal.gov) is a neutrino oscillation experiment that measures the properties of neutrinos. These measurements rely on efficient identification and robust reconstruction of neutrino events. NOvA has already shown the [first use of CNNs] (http://inspirehep.net/record/1444342) in a HEP analysis. Now we are expanding the program of machine learning applications on NOvA events for their use in full event reconstruction and eventually event simulation applications.

The use of Generative Adversarial Networks (GANs) is of particular interest for potential applications for neutrino events and beyond. GANs are sets of generator networks, which produce simulated samples based of a training set, and classification networks, which discriminate events in a sample as real or simulated.

Generative Adversarial Networks (GANs) are sets of generator networks that produce simulated samples based of a training set, competing with classification networks that attempt to classify events as real or simulated. The use of GANs is of particular interest for potential applications focused on fast and accurate neutrino event simulation.

Because the data structures of many particle physics experiments are compatible with the ROOT scientific software framework, an interface that uses ROOT compatible analysis tools can be extended for multiple applications across experiments.

The focus of this project will be to integrate GANs in [Tensorflow] (https://www.tensorflow.org/), Google's open source machine learning library, with the ROOT-integrated Toolkit for Multivariate Analysis (TMVA). This will enable particle physicists easy access to deep learning algorithms, such as GANs, in Tensorflow for direct 
applications in HEP.


## Task ideas
 * Reproduce NOvA's existing classification applications of CNNs with an implementation on Tensorflow
 * Write an open-source interface between Tensorflow and TMVA, specifically for simulations with GAN.
 * Apply GANs in Tensorflow to neutrino events.


**Expected results**:
 * Develop an interface between Tensorflow GANs and TMVA
 * At least one proven application of Tensorflow-TMVA interface for NOvA neutrino event simulations.

**Requirements**:
Strong C++ skills
Familiarity with ROOT and TMVA applications.
Experience with the particle physics simulations.
Experience with deep learning frameworks (Tensorflow encouraged).
Experience with the ART framework is preferable but not indispensable.

**Mentors**:
  * [Fernanda Psihas](mailto:psihas@fnal.gov)
  * [Sergei Gleyzer](mailto:sergei@cern.ch)
  * [Paul Rossman](mailto:paulrossman@google.com)
  * [Stefan Wunsch](mailto:stefan.wunsch@student.kit.edu)


**Links**:
  * [Tensorflow](https://www.tensorflow.org/)
  * [NOvA](https://www-nova.fnal.gov)
  * [CNNs and NOvA Events] (https://arxiv.org/pdf/1406.2661v1.pdf)
