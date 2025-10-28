---
project: Intelligent Log Analysis for the HSF Conditions Database
title: Intelligent Logging Pipeline
author: Osama Ahmed Tahir
photo: blog_authors/OsamaTahir.jpeg
date: 27.10.2025
year: 2025
layout: blog_post
logo: BNL-logo.png
intro: |
    An intelligent logging pipeline for NopayloadDB that integrates log aggregation, anomaly detection, and monitoring. It improves reliability and maintainability in large-scale HEP experiments It is deployed on Minikube cluster while using a deep learning model for real-time anomaly detection.
---

<div align="center">
<img src="https://hepsoftwarefoundation.org/images/BNL-logo.png" width="500"/>
</div>

#### Mentors: Ruslan Mashinistov, Michel Hernandez Villanueva, and John S. De Stefano Jr
#### [Project Link (BNL Nuclear and Particle Physics Software Group) - Intelligent Logging Pipeline](https://github.com/BNLNPPS/intelligent-logging-pipeline)

### Introduction
<p align="justify">
As experiments grow more complex, the demand for efficient access to conditions data has increased. To address this, the HEP Software Foundation (HSF) proposed a reference architecture, NopayloadDB. It stores metadata and file URLs instead of payloads. However, NopayloadDB lacks a centralized logging subsystem. To address these limitations, this project proposes an intelligent logging pipeline integrated with NopayloadDB. The pipeline combines advanced log aggregation, scalable storage, and deep learning-based anomaly detection to reduce downtime and improve operation. The result is enhanced reliability, maintainability, and scalability of conditions database services in modern HEP experiments.
</p>

### Objectives
<p align="justify">
The project extended NopayloadDB, the HSF-referenced conditions database [1], by introducing a centralized and intelligent logging pipeline. The main goal was to provide centralized log aggregation, structured parsing and storage for easier querying, and anomaly detection using DeepLog to detect anomalies. The pipeline also aimed to support real-time monitoring and diagnostics for different stakeholders. It detected issues before escalation and provided insights for tuning system parameters. The design emphasized scalability, modularity, and compatibility with OpenShift deployments.
</p>

### Motivation
<p align="justify">
I am passionate about contributing to systems that are accessible and exist in both open-source and open-science settings. My background in distributed systems, cloud computing, and data-intensive applications aligns closely with this project. I am excited to contribute my skills that help to build a scalable and intelligent system and share the results with the broader community. This opportunity also allowed me to deepen my expertise in log analysis and machine learning while advancing my passion for technology and scientific knowledge to be openly available and accessible.
</p>

### Technical Walkthrough
<p align="justify">
The logging pipeline is deployed on Minikube and is implemented around three containerized modules: Process, Monitor, and Predict. Each component as shown in Figure 1 has been described below.
</p>
<div align="center">
<div style="text-align: center;">
<img width="1023" height="213" alt="intelligent_logging_pipeline" src="https://gist.github.com/user-attachments/assets/b833ae51-6a7c-4e3c-924a-f7717ef8432b" /></div>
<p align="center"><i>Figure 1: Intelligent Logging Pipeline</i></p>
</div>

#### Process
<p align="justify">
In the Process module, NopayloadDB generates log data, which includes both the Django application and the PostgreSQL database. This data is then collected, filtered, and parsed by Fluent Bit. The processed Fluent Bit logs are consumed by Kafka on a topic. Alloy is used as a forwarding agent that forwards a structured log from a Kafka topic to a Loki.
</p>

#### Monitor
<p align="justify">
The Monitor module focused on scalable storage and visualization. Loki is a distributed, horizontally scalable log aggregation system composed of several key components [2]. The Distributor receives logs from Alloy, validates them, and routes them to Ingesters while balancing the load. The Ingester temporarily stores logs in memory, compresses them, and forwards them to long-term storage in MinIO. The Querier retrieves the required logs from MinIO, forwarding them to Drain3 for prediction and Grafana for visualization. Figure 2 shows the flow of data within the customized Loki architecture.

</p>
<div align="center">
<div style="text-align: center;">
<img width="462" height="418" alt="custom_loki" src="https://gist.github.com/user-attachments/assets/8f29e922-ece8-425d-aca4-8f981c52e3a9" /></div>
<p align="center"><i>Figure 2: Customized Loki</i></p>
</div>

#### Predict
<p align="justify">
The Predict module added intelligence to the pipeline. Drain3 parsed raw logs into structured template IDs. These template IDs are consumed by Redis in sequence from Drain3. The template ID sequences are then processed by DeepLog for sequence-based anomaly detection. Any detected anomalies are visualized by Grafana for debugging and monitoring.
</p>

### DeepLog 
<p align="justify">
DeepLog is an LSTM-based model that learns log patterns from normal execution [3]. It detects anomalies when log patterns deviate from the model trained from logs under normal execution. Over time, the DeepLog model adapts to new log patterns over time and constructs workflows from the underlying system log. This is because once an anomaly is detected, users can diagnose the detected anomaly and perform root cause analysis effectively. The deeplog configuration can be changed by the top K. The top K is how many of the most likely predictions will be considered "normal" by the model. If k is set to 2, you take the two events with the highest probabilities, and these will be the top k most probable next events.
</p>

<p align="justify">
Suppose a log system has several events, each represented by a unique ID. The model takes a sequence of past events and predicts what the next event is likely to be. For example, <i>Table 1: Set of Events</i> shows unique IDs for the set of events of a user trying to upload a file. From the past event, the DeepLog learns the upcoming event and gives a probability to each unique event. It is to be noted that these sets of events are consumed by DeepLog in a random sequence.
</p>

<div style="text-align: center;">
  <table style="
      border-collapse: collapse;
      margin: auto;
      width: 60%;
      font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
      font-size: 16px;
      text-align: center;
  ">
    <thead>
      <tr style="border-bottom: 2px solid #444; border-top: 2px solid #444;">
        <th style="padding: 8px 60px;">Unique ID</th>
        <th style="padding: 8px 60px;">Event</th>
        <th style="padding: 8px 60px;">Probability</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 8px 20px;">0</td><td style="padding: 8px 20px;">Login</td><td style="padding: 8px 20px;">0.7</td></tr>
      <tr><td style="padding: 8px 20px;">1</td><td style="padding: 8px 20px;">Upload File</td><td style="padding: 8px 20px;">0.4</td></tr>
      <tr><td style="padding: 8px 20px;">2</td><td style="padding: 8px 20px;">Select File</td><td style="padding: 8px 20px;">0.6</td></tr>
      <tr><td style="padding: 8px 20px;">3</td><td style="padding: 8px 20px;">Logout</td><td style="padding: 8px 20px;">0.25</td></tr>
      <tr><td style="padding: 8px 20px;">4</td><td style="padding: 8px 20px;">Submit File</td><td style="padding: 8px 20px;">0.3</td></tr>
    </tbody>
  </table>
  <p style="font-style: italic; margin-top: 6px;">Table 1: Set of Events</p>
</div>


<p align="justify">
Here the model thinks "Login" is most likely next event, then "Select File" and then "Upload File" etc. Hence, the sequence will be [Login, Select File, Upload File, Submit File, Logout] and with their respective unique IDs, it will be [0, 2, 1, 4, 3]. With k=2, the model predicts the top 2 event IDs as [Login, Select File], while the true event is Upload File. Since the true event does not appear in the top 2 predictions, this case is flagged as an anomaly. When k=3, the top 3 event IDs are [Login, Select File, Upload File], and the true event Upload File is included, so it is considered normal. In practice, the model checks whether the true event ID appears within the top-k predicted IDs: if the true event is not present, the sequence is labelled as an anomaly; otherwise, it is treated as normal.
</p>

### Results
<p align="justify">
The intelligent logging pipeline demonstrated log collection and aggregation for Kubernetes-based clusters. The heterogeneous logs were parsed and formatted into structured sequences. The DeepLog was integrated into the pipeline, showing the feasibility of automated real-time monitoring and anomaly detection. The Grafana dashboards provided tailored access for different user roles.
</p>

### Future Work
<p align="justify">
This research will establish a baseline for how the observability and diagnostics of a system can benefit the most from artificial intelligence. In addition, it will also be beneficial for the open source community, scientific research, and enterprise applications. From the experiment's point of view, it will provide more reliable and reproducible physics experiments. This will also enable HEP to efficiently allocate resources from insights gained from the system. In addition, it will also pave the way for how cutting-edge techniques can be applied beyond HEP, such as large-scale cloud applications and enterprise systems.
</p>

### Final remarks
<p align="justify">
I enjoyed my time working with my mentors Ruslan, Michel, and John. This project was the first time that I contributed to CERN and BNL to such an extent and provided me with a sense of accomplishment in my professional career. The consistent feedback on both the project and the publication helped me a lot in shaping the project. My mentors provided me with a path to present the project on a greater scale, and it resulted in the project reaching greater potential to be used for other experiments. I am happy to be mentored by such experienced and knowledgeable professionals.
</p>

### Links
#### [NoPayLoadClient](https://github.com/BNLNPPS/nopayloadclient)

### References

[1] Ruslan Mashinistov, L. Gerlach, P. Laycock, A. Formica, Giacomo Govi, and C. Pinkenburg, "The HSF Conditions Database Reference Implementation," EPJ Web of Conferences, vol. 295, pp. 01051–01051, Jan. 2024

[2] “Grafana Loki | Grafana Loki documentation,” Grafana Labs, 2025.

[3] M. Du, F. Li, G. Zheng, and V. Srikumar, “DeepLog, Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security”, Oct. 2017