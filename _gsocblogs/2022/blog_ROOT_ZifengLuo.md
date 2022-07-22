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
  This project consists of the implementation of an automatic conversion tool that migrates both the schema (i.e. fields and their types) and the data of a TTree to RNTuple.
---
This is a blog as part of the mid-term evaluation of GSoC 2022 project: ROOT - Automatic conversion of data stored in TTree form to RNTuple.

## Overview of the project
For the past 25 years, high-energy physics (HEP) data have been stored with columnar structures in TTree, the ROOT’s legacy columnar storage that has been used to store more than 1 exabyte of HEP data. As the main data structure of ROOT v7, RNTuple classes provide ROOT’s new, experimental, hight speed I/O subsystem for HEP data. Given that RNTuple is a complete backwards-incompatible redesign, the development of an automatic conversion tool that permits the migration of existing TTree data into RNTuple is a must. In this regard, both the schema (i.e., fields and their types) and the data will have to be migrated.

## Progress
I started working on this project from June 11, 2022, right after the community-bonding period. The first two weeks were hands-on period. I began with the [existing code](https://github.com/jblomer/iotools) that are capable to convert TTree containing simple data types to RNTuple. After being familiar with RNTuple APIs, I created the project GitHub [repo](https://github.com/luozf14/TTreeToRNTuple) and started commiting my own code. The length of the project is decided to be 14 weeks, ending in the beginning of Oct. 

Based on the data types supported by TTree, the project is divided into 5 parts with increasing difficulties, from simple C++ variables to nested collections. The status are summarized in the table below. 

<table>
   <tr>
      <th>Part</th>
      <th>Types</th>
      <th>Status</th>
   </tr>
   <tr>
      <td >Convert TTree containing simple variables </td>
      <td>int, float, bool, ...</td>
      <td>Completed</td>
   </tr>
   <tr>
      <td rowspan="3">Convert TTree containing arrays</td>
      <td>Fixed-length array</td>
      <td rowspan="2">Completed</td>
   </tr>
   <tr>
      <td>Variable-sized array</td>
   </tr>
   <tr>
      <td>Multidimensional array (e.g., int myArry[16][8])</td>
      <td>Need RNtuple feature support</td>
   </tr>
   <tr>
      <td rowspan="5">Convert TTree containing STL types and collections </td>
      <td>std::string</td>
      <td rowspan="5">Completed</td>
   </tr>
   <tr>
      <td>std::array&lt;T, N></td>
   </tr>
   <tr>
      <td>std::vector&lt;T> and ROOT::RVec&lt;T></td>
   </tr>
   <tr>
      <td>std::pair&lt;T1, T2></td>
   </tr>
   <tr>
      <td>std::tuple&lt;T1, …, Tn></td>
   </tr>
   <tr>
      <td>Convert TTree containing user-defined classes</td>
      <td></td>
      <td>Expect by the end of Jul.</td>
   </tr>
   <tr>
      <td rowspan="2">Convert TTree containing branches of nested types</td>
      <td>std::vector&lt;std::vector&lt;T> ></td>
      <td rowspan="2">Expect by the end of Aug.</td>
   </tr>
   <tr>
      <td>…</td>
   </tr>
   <tr>
      <td>Tests and documentation</td>
      <td></td>
      <td >Except in Sep.</td>
   </tr>
</table>

Currently each part has its own cimpilible code. Our final goal is to integrate all of them into a command-line tool as well as a class of RNTuple. 

## Miscellaneous
As a PhD student in experimental nuclear astrophysics, I have been using ROOT everyday for many years since nearly all experimental data are sotred in ROOT's legacy storage, TTree. When I heard about GSoC from friends, I instinctly looked for projects related to ROOT because I have always been dreaming to contribute to this wonderful opensource project,  which is the most important infrastructure of high-energy physics. 

As mentioned in the beginning, TTree is the most important element of ROOT; a large amount of HEP data have been stored in TTree. Therefore, I was attracted by this TTree-To-RNtuple project because its deliverable  will be the most commonly-used tool among HEP scientists once ROOT v7 will be released. Wouldn't it be a nice thing that everyone uses the tool built by you?

As a physicist without any computer sicence background, I meet a lot of troubles when I am working on this project. However, I am very lucky that I have the nicest mentor, Dr. Javier Gomez. No matter how simple or naive my questions are, he is always considerate and full of patience to me. For example, he explained explicitly to me that how the vector and array are stored in memory by drawing sketch, while others may just said "you should have known this".







