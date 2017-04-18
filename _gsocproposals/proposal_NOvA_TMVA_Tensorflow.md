---
title: Tensorflow-TMVA GAN Interface Applied to NOvA Neutrino Events.
layout: gsoc_proposal
project: NOvA
organization:
 - NOvA
 - Fermilab
---

# Description
[NOvA](https://www-nova.fnal.gov) is a neutrino oscillations experiment whose measurement of this particle's properties relies on efficient identification and robust reconstruction of events. NOvA has already shown the first use of CNNs (convolutional neural networks) for [event classification] (http://inspirehep.net/record/1444342) in a HEP result. Now we are expanding the program of machine learning applications on NOvA events for their use in full event reconstruction and eventually event simulation applications.

[Tensorflow] (https://www.tensorflow.org/) is Google's open source machine learning library which enables collaboration between developers using machine learning algorithms for different applications.

GANs are sets of generator networks, which produce simulated samples based of a training set, and classification networks, which discriminate events in a sample as real or simulated. <They are cool to simulate events and such>

<TMVA and tensorflow and why we care>



## Task ideas
 * Reproduce NOvA's existing classification applications of CNNs with an implementation on Tensorflow
 * Apply GANs in Tensorflow to neutrino Events.
 * Write an open-source interface between Tensorflow and TMVA, specifically for simulations with GAN.


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
  * [Stefan Wunsch](mailto:)


**Links**:
  * [https://www.tensorflow.org/](https://www.tensorflow.org/)
  * [https://www-nova.fnal.gov](https://www-nova.fnal.gov)
  * [https://arxiv.org/pdf/1406.2661v1.pdf] (https://arxiv.org/pdf/1406.2661v1.pdf)
