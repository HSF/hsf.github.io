---
title: Manipulation of massive astronomical data using graphs
layout: gsoc_proposal
project: AstroLab
year: 2020
organization: IJCLab
---

## Description

Each observation night, telescopes all around the world issue alerts based on what they observe on the sky. These alerts are typically streamed to other places, where the streams are analysed and the relevance of each alert is asserted in order to take a decision on the next steps to perform. Such decisions include for example retrieving a set of previous observations and extract the scientific information, sometimes hidden on a longer time-scale than the alert itself (transient objects, new objects, ...).
Given the unprecedented precision of next generation of telescopes, the stream of alerts will be made of millions of alerts per night, reaching the TB per night, and decisions and actions must be taken extremely fast. In this context, the efficient manipulation and the visualisation of patterns in such a volume of data are real challenges for our community. 

Our group is investigating a broker solution, called Fink, based on Apache Spark structured streaming capabilities. Each night alerts are streamed from telescopes, analysed by the Fink broker, and redistributed to subscribers. But the processed data needs also to be stored for visualisation and post-processing. 


## Task ideas

The student will focus on JanusGraph, a scalable graph database, and Apache Spark, a cluster computing framework. The internship will have four steps:

- First the student will contribute to define and to implement the data structure for the graph, and s/he will test on the database prototype deployed on our University cloud. 
- S/he will then work on developing tools to enable a seamlessly integration of Apache Spark with JanusGraph to update the database. 
- S/he will then integrate and develop visualisation tools to enable scientists to perform efficient global graph data analytics and ETL on the alert dataset. 
- Finally s/he will develop a client to query the graph data using console and REST API.

## Expected results

Ultimately, the developments will be integrated in the Apache Spark-based Fink broker project developed by the group at IJCLab.

## Desirable Skills

* At least one of the following programming languages: Scala, Java, or Python.
* Knowledge of distributed computing (cluster and grid computing), and graph database.
* Being aware of the big data challenges and issues.
* Working with or willing to learn Apache Spark and JanusGraph.

## Mentors

* [Julien Peloton](mailto:peloton@lal.in2p3.fr)
* [Julius Hrivnac](mailto:hrivnac@lal.in2p3.fr)
* [Chris Arnault](mailto:arnault@lal.in2p3.fr)

## Links
1. [Fink](https://github.com/astrolabsoftware/fink-broker)
2. [Apache Spark](https://spark.apache.org/)
3. [JanusGraph](https://janusgraph.org/)

