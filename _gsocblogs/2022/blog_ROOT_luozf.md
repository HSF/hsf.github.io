---
project: ROOT
title: Automatic conversion of data stored in TTree form to RNTuple
author: Zifeng Luo
[//]: # (photo: blog_authors/FirstLast.jpg)
date: July 20, 2022
year: 2022
layout: blog_post
logo: ROOT_logo.png
intro: |
  TTree is the ROOT’s legacy columnar storage that has been used to store more than 1 exabyte of high-energy physics data during the last 25 years. RNTuple classes provide ROOT’s new, experimental I/O subsystem for HEP data. This project will consist of the implementation of an automatic conversion tool that migrates both the schema (i.e. fields and their types) and the user data.
---
This is a blog as part of the mid-term evaluation of GSoC 2022 project: ROOT - Automatic conversion of data stored in TTree form to RNTuple.

## Overview of the project
For the past 25 years, high-energy physics (HEP) data have been stored with columnar structures in TTree, the ROOT’s legacy columnar storage that has been used to store more than 1 exabyte of HEP data. As the main data structure of ROOT v7, RNTuple classes provide ROOT’s new, experimental, hight speed I/O subsystem for HEP data. Given that RNTuple is a complete backwards-incompatible redesign, the development of an automatic conversion tool that permits the migration of existing TTree data into RNTuple is a must. In this regard, both the schema (i.e., fields and their types) and the data will have to be migrated.

 
