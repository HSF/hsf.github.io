---
title: intelligent Data Delivery Service
author: Wen Guan
layout: plain
---

## Introduction

iDDS is an intelligent Data Delivery Service. It is an ATLAS/IRIS-HEP joint project. It is designed to intelligently transform and deliver the needed data to the processing workflow in a fine-grained approach for High Energy Physics workloads. It will not only reduce the need for replicas, but also enable benefits such as: decreasing the time period of caching transient data; transforming expensive replicas to cheaper format data at remote sites; and only cache cheaper new data for processing.

The iDDS will also work to orchestrate the WorkFlow Management System (WFMS) and the Distributed Data Management (DDM) systems to trigger them to process the data as soon as possible. In addition, the iDDS will have intelligent algorithms to adjust the lifetime of the cache, the format transformation and the delivery destination. The iDDS will increase the efficiency of data usage, reduce storage usage for processing and speed up the processing workflow.

## Main description

The iDDS is designed as a standalone experiment agnostic service. It is implemented based on a Work/Workflow structure, where Work is a transformation/processings and a Workflow is a collection of Work and their relationship(DAG). New use cases can be imported to iDDS by implementing a new Work item with some hook functions.

 * [Documents](https://idds.readthedocs.io/en/latest/index.html)
 * [Main page](https://idds.cern.ch)
 * [Repository](https://github.com/HSF/iDDS)

The iDDS has been used for several experiment exercises. Efforts are ongoning to support more use cases. 

## Contacts

More efforts are ongoing for different experiment exercises. Everyone is very much welcome to join! :)

To express general interests, please contact: atlas-adc-iddsATcern.ch
