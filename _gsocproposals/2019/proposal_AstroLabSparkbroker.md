---
title: Fast and reactive broker for astronomy based on Apache Spark
layout: gsoc_proposal
project: AstroLab
year: 2019
organization: LAL
---

## Description

Each observation night, telescopes all around the world issue alerts based on what they observe on the sky (see figure below). These alerts are typically streamed to other places, where the stream is analysed and the relevance of each alert is asserted in order to take a decision on the next steps to perform. Such decisions include for example retrieving a set of previous observations and extract the scientific information, sometimes hidden on a longer time-scale than the alert itself (transient objects, new objects, ...).
Given the unprecedented precision of next generation of telescopes, the stream of alerts will be made of millions of alerts per night, reaching the TB per night, and decisions and actions must be taken extremely fast. 

![broker](/images/system_design.png){:height="200px"} 

_Typical flow of alerts in astronomy. Raw data are collected by the telescope every nights, and alerts are issued by the Alert System. These alerts are streamed to other places, and treated by brokers (red). Brokers need to assess the relevance of the alerts, correlate corresponding alert data with external data (raw data or previous processed alerts for example) if needed, and produce scientific products for further analyses. Dashed lines represent stream processes._

## Task ideas

Our group is investigating a broker solution based on Apache Spark streaming capabilities. First, the student will develop a prototype for prompt handling of the received and accepted alerts. The prototype will store those alerts in a temporary storage, receive related data, pre-process them and send notifications (via Slack, sms, Twitter, ...) in case of alerts considered as urgent. 
Second, the student will focus on optimizing communications and data transfer between the broker and external databases, allowing fast correlation between alerts (and data alerts) at different timescales. S/he will specifically work on developing tools to enable fast detection of transients in telescope images (signal correlated in time) at different timescales. Finally if time allows, we propose to the student to focus on the input side of the broker and particularly the fast decoding and manipulation of the stream of alerts. S/he will develop tools to optimize the Apache Spark broker interface with Kafka used by our alert system, and tools to reduce latency in asserting the relevance of the alerts.
Datasets will be mock data specifically simulated for this project by our group.

## Expected results

Ultimately, the developments will be integrated in the Apache Spark-based broker solution developed by the group at LAL.

## Desirable Skills

* At least one of the following programming language: Scala, Java, or Python.
* Knowledge of distributed computing (cluster and grid computing), and streaming.
* Being aware of the Big Data challenges and issues.
* Working with or willing to learn Spark.

## Mentors

* [Julien Peloton](mailto:peloton@lal.in2p3.fr)
* [Julius Hrivnac](mailto:hrivnac@lal.in2p3.fr)
* [Chris Arnault](mailto:arnault@lal.in2p3.fr)

## Links
1. [Apache Kafka](https://kafka.apache.org/)
2. [Apache Spark](https://spark.apache.org/)
3. [AstroLab Software](https://astrolabsoftware.github.io/)

