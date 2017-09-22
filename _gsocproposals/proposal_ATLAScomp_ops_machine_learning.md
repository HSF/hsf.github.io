---
title: Optimizing Computing Operations with Machine Learning algorithms
layout: gsoc_proposal
project: ATLAS
organization: CERN
---

## Description

ATLAS Computing Operations requires on-shift manpower to manage its complex infrastructure. This includes, but is not limited to, the Data Management system, Workload Management system, Conditions and Databases, or the interactive clients. Additionally, the participating computing centres are heterogeneous, providing various software and hardware, with different versions and configurations. We see an opportunity to support computing operations using machine learning algorithms, to automate the many different manual activities and decision processes that previously required human intervention.

With the ATLAS Open Analytics Platform (based on ElasticSearch, HDFS, Spark, Graphite and Jupyter) we now have in place a central system that collects critical metrics that can form the basis of automated operational decisions. With this project we propose to design, implement, and deploy a framework that is able to classify and cluster these metrics based on operational needs. The operator is notified upon a significant event, and potential resolutions are proposed. The framework will learn the decisions of the operator through reinforcement algorithms over time, yielding better classification of events and proposals for notification or automation.

For example, a broken network link between two data centres could trigger a ticket, the blacklisting of either data centres, or the rescheduling of data transfers. Such resolutions should be proposed by the system and automatically learnt over time based on the decisions of the operators.

## Task ideas

- Reduction of operational noise (i.e., target workflows that require human intervention)
- Contextualise operational situations (i.e, what is the root cause of the problem)
- Automate repair and recovery workflows based on machine learning response

## Expected results

The ATLAS Data Management system (Rucio) will serve as the experimental platform for the first iteration of these studies. Care must taken that the implementation is applicable to other ADC systems as well, as anomalous behaviour usually shows across multiple systems. For many of the proposed tasks there are already systems in place, and they should be exploited for this project. In detail, we propose the following:

### Milestone - Data aggregation
- Establish a method to process real-time system monitor data. Structured data is available in two principal backends, ElasticSearch (rucio-events, e.g., transfer-success/fail) and Graphite (performance measurements). Unstructured data (logfiles) is available on Hadoop.
- Filter and transform the historical monitoring data into input matrices, such that they can be used by machine learning toolkits. Many algorithms require numerical input, which must be mapped accordingly.
- Establish a datastore backend where these historical monitoring matrices can be stored efficiently.

### Milestone - Anomaly detection
- Establish a method to classify system behaviour into normal and anomalous behaviour. This can be accomplished either via thresholds (where known), or via more sophisticated methods for cases where spiking characteristics are irregular, but still valid.
- For systems with already existing anomaly detection, e.g., Prodsys-2, establish a method to include their anomaly markers.
- Store learnt anomaly markers in the datastore backend together with the historical monitoring matrices, for comprehensive input to a trigger.

### Milestone - Streaming trigger
- Establish a method to continuously monitor the current state of the system to automatically trigger upon anomalous behaviour, based on the thresholds and by using the learnt classifiers.
- Upon a trigger, select the n-best solutions based on a ranking and propose them to the operator on shift via email.
- Allow the operator to give feedback on the proposed solutions (good, wrong, not applicable).

### Milestone - Operator decision
- Establish a method to store operator decisions, including the root cause of the anomaly, the affected system, the executed solution, and the proposal feedback.
- Establish a method to rank solutions based on their effectiveness for selection.

### Milestone - Automation
- For highly effective solutions automatically trigger the best solution, e.g., file a ticket to a site, or create data movement rules.

## Requirements

- Knowledge of Machine Learning methods (preferably LSTMs)
- Proficiency with Machine Learning implementations (preferably TensorFlow + Keras)
- Python programming language (preferably with NumPy extensions)

## Mentors

- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Alessandro Di Girolamo](mailto:Alessandro.Di.Girolamo@cern.ch)

## Links
- [ElasticSearch](https://www.elastic.co/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Jupyter](https://jupyter.org/){:data-proofer-ignore} <!-- Unknown error from Travis HTML proofing -->
