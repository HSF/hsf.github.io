---
title: Support for Rucio Users with Native Language Processing
layout: gsoc_proposal
project: Rucio
year: 2020
organization:
    - CERN
---

## Description

Rucio is an open source software framework that provides scientific collaborations with the functionality to organize, manage, and access their volumes of data. Data in Rucio is organized using Data Identifiers (DIDs) which have three levels of granularity viz.: files, datasets and containers, respectively. Datasets are used to organise sets of files in groups and to facilitate bulk operations such as transfers or deletions. Users are permitted to perform certain actions on the DIDs such as downloads, uploads or transfers. Several escalation levels of expert support is available for users in case of problems. When satisfying answers are not found at lower support levels, a request from a user or a group of users can be escalated to the Rucio support. Due to the vast amount of support requests, we are looking into methods to assist the support team in answering these requests. Ideally, the support would be provided by an intelligent bot able to process and understand the user’s requests and finally trigger appropriate action. 
The Native Language Processing (NLP) is a fairly developed technique used nowadays in many fields requiring the analysis of large chunks of text and automation of actions to be taken. Processing questions from users and providing satisfying answers is an important activity in the Rucio project. This activity could be optimised by prototyping a bot capable to handle user's requests up to a certain level of complexity, and forwarding only the remaining ones to the experts. Developing this prototype requires in a first phase reaching the following milestones.

## Milestones for GSoC Student

 * Input Data: 
   * Creation of text corpus or use of existing one.
   * Extraction of emails from the support mailing lists, preferably through IMAP client.
 * Extraction of the meanings of the input data and transformations needed for further analysis, preferably with the Natural Language Toolkit (NLTK).
   * Creation of a training set and a valdiation set from the input data. 
   * Development of a tool capable to extract the information from the emails relevant to the data management.

## Ideas for Extension

 * Sorting out possible solutions from provided sources (e.g. documentation, docstrings, table of answers) and triggering a response to the user.
 * Analysis of the acquired data:
   * Processing feedbacks from users (Determining a sentiment with NLTK, filtering out unrelevant feedbacks, etc.). 
   * Data popularity (Spotting the names of the DIDs in the emails and counting them).
   * Most frequent questions/answers (Sorting and caching FAQs for further use.)

## Expected Results

Note that the whole Rucio Bot project demands full engagement for the time period longer than the GSoC timescale. The essential requirements for declaring success of the work of a GSoC student are explicitly written in the section of 'Milestones'. Especially the second bullet requires deep expertise with NLTK including creation of both the training set and the validation set and running the developed bot on them. The validation set provides us with the neccessary statistics to demonstrate the reliability of the bot.

Achievable, but not mandatory, developments are listed in the section 'Ideas for Extension'.

## Requirements

Good python programming skills. Previous experience with NLTK, ML and data analysis is a plus.

## Mentors
 * [Tomas Javurek](mailto:tomas.javurek@cern.ch)
 * [Mario Lassnig](mailto:mario.lassnig@cern.ch)
 * [Thomas Beermann](mailto:thomas.beermann@cern.ch)
 * [Martin Barisits](mailto:martin.barisits@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Rucio web](https://github.com/rucio/rucio)
 3. [Journal article](https://doi.org/10.1007/s41781-019-0026-3)
