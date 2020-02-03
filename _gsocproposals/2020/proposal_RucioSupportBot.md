---
title: Support for Rucio Users with Native Language Processing
layout: gsoc_proposal
project: Rucio
year: 2020
organization:
    - CERN
---

## Description

Rucio is an open source software framework that provides scientific collaborations with the functionality to organize, manage, and access their volumes of data. Data in Rucio is organized using Data Identifiers (DIDs) which have three levels of granularity viz. Files, datasets and containers, respectively. Datasets are used to group a set of files to facilitate bulk operations on them eg. in transfers, deletions, and organizational purposes. Users are permitted to perform certain actions on the DIDs such as downloads, uploads, transfers, etc. Expert support, through different escalation levels, is offered to the users in case of problems.. In case when satisfying answer was not found at previous support levels, a request from a user or a group of users can reach the Rucio support. Due to the vast amount of support requests we are looking into methods to assist the support team in answering these requests. Ideally, the support would be provided by an intelligent Bot able to process and understand user’s requests and finally trigger appropriate action. 
The Native Language Processing (NLP) is nowadays fairly developed technique used in many fields with need of analyzing large chunks of text and automate actions on them. Next to a few other use cases in Rucio project, an important one is to process responses and questions of users and to provide satisfying answers - development of a prototype of a Bot that is capable to handle user requests until certain complexity. The request would be handled by experts only in case when the bot can not provide a reliable answer. Such a complex task consists of the following milestones.

## Milestones

 * Input Data: 
   * creation of corpora or use of existing one 
   * getting emails from the support mailing lists, preferably through IMAP client
 * Extracting meanings of the input data and acquiring the data for further analyses, preferably with the NLTK.
   * Creation of a training set and valdiation set from the input data. 
   * Development of a tool capable to extract the meanings.
 * Sorting out possible solutions from provided sources (e.g. documentation, docstrings, table of answers) and triggering a response to the user.
 * Fallback to the Rucio experts in case that no answer could be found.
 * Analysis of the acquired data:
   * Feedbacks from users.
   * Data popularity.
   * Most frequent questions/answers.

## Expected results

Note that the whole Rucio Bot project regards full engagement for time period longer than the GSoC timescale. A minimal success of the project would be declared in case when the first two bullets of the milestones are done and suggestions for the rest is provided. Especially the second bullet requires deep expertise with NLTK including creation of both the training set and the validation set and performing the developed bot on them. The validation set provides us with statistics necessary to demonstrate reliability of the bot. The other bullets are at least as advanced as the second one. Providing a prototype of a code capable to process the tasks from the last three bullets would be considered as advanced goals of the GSoC project. Working out the most optimal solution can again mean analyzing text from documentation or docstrings, while for easy requests, there can be a list of pre-defined answers or cached answers from the previous cases.

## Requirements

A candidate suitable for this project should be a good python programmer. Previous experience with NLTK, ML and data analysis is appreciated. The candidate will be patiently guided through the Rucio and the NLTK in order to gain knowledge necessary for this project.

## Mentors
 * [Tomas Javurek](mailto:tomas.javurek@cern.ch)
 * [Mario Lassnig](mailto:mario.lassnig@cern.ch)
 * [Thomas Beermann](mailto:thomas.beermann@cern.ch)
 * [Martin Barisits](mailto:martin.barisits@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Journal article](https://doi.org/10.1007/s41781-019-0026-3)
