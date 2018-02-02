---
title: Enabling Big Data Analytics on Physics Data with the "Hadoop-XRootD Connector" Library
layout: gsoc_proposal
project: XROOTD
year: 2018
organization: CERN
---

## Description
During the latest years, several efforts are ongoing in order to make it possible to perform analysis of High Energy Physics data with modern big data technologies from the Hadoop ecosystem, such as Apache [Spark](https://spark.apache.org/), an open-source software framework for large-scale data processing. One of the most important challenges to these efforts has been the need to effectively read data located in custom storage systems from within popular big data engines.

At CERN the vast majority of physics and infrastructure data reside in a system named EOS. [EOS](https://eos.web.cern.ch/) is a disk-based, low-latency storage service with a highly scalable hierarchical namespace, which enables data access via the [XRootD protocol](http://xrootd.org/).

In order to read files in the Hadoop ecosystem from EOS, the "[Hadoop-XRootD Connector](https://github.com/cerndb/hadoop-xrootd)" was created. This Java-based library connects to the XRootD Client of EOS via the Java Native Interface Framework ([JNI](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html)) and is capable of reading files directly, without the need to import or export files to HDFS.

The project aims to address the existing feature requirements of the "Hadoop-XRootD Connector" as well as expanding and optimizing the existing codebase of the library in order to make it production-ready. A successful outcome will allow researchers at CERN to perform analysis over PBs of physics and infrastructure data with Apache Spark and other popular big data technologies and, in addition, enable users, insitutions and citizen scientists outside CERN to easily access and analyze PBs of physics data in the Hadoop ecosystem via the EOS-based [CERN Open Data](http://opendata.cern.ch/) Project.

## Task ideas
 * Optimize the caching and request size features to minimize the performance gap between streaming files from EOS and reading natively from HDFS.
 * Expand the authentication mechanisms of the library by including GRID X.509 Certificates which are widely used by the WLCG.
 * Introduce globing support in order to allow users to include wildcards on the file input.
 * Make the library compatible with multiple versions of Hadoop and Spark and all popular file formats (parquet, avro, csv, root etc.).
 * Perform tests on physics analysis with the Hadoop-XrootD Connector over Apache Spark with real code coming from LHC experiments (mainly CMS).

## Expected results
A production-ready connection library between the EOS Storage Service of CERN and the Hadoop Ecosystem, working in a similar fashion as other existing connection libraries to popular file systems such as Amazon S3.

## Requirements
JAVA, JNI, C++, Spark, Hadoop

## Mentors
  * [Vaggelis Motesnitsalis](mailto:vaggelis.motesnitsalis@cern.ch)
  * [Zbigniew Baranowski](mailto:zbigniew.baranowski@cern.ch)
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)
  
## Links
  * [Hadoop-XRootD Connector](https://github.com/cerndb/hadoop-xrootd)
  * [EOS](https://eos.web.cern.ch/)
  * [Spark](http://spark.apache.org)
  * [Hadoop API FileSystem](https://hadoop.apache.org/docs/r2.8.2/api/org/apache/hadoop/fs/FileSystem.html)
  * [CERN Open Data](http://opendata.cern.ch/)
