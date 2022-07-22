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
I started working on this project from June 11, 2022, right after the community-bonding period. The first two weeks were hands-on period. I began with the [existing code](https://github.com/jblomer/iotools) that are capable to convert TTree containing simple data types to RNTuple. After being familiar with RNTuple APIs, I created my GitHub [repo](https://github.com/luozf14/TTreeToRNTuple) and started commiting my own code. 

Based on the data types supported by TTree, this project is divided into 5 parts with increasing difficulties, from simple C++ variables to nested collections. The status are summarized in the table below.

<table>
   <tr>
      <th>Part</th>
      <th>Subtopic</th>
      <th>Status</th>
   </tr>
   <tr>
      <td >Convert TTree containing simple variables </td>
      <td></td>
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
      <td>std::array<T, N></td>
   </tr>
   <tr>
      <td>std::vector<T> and ROOT::RVec<T></td>
   </tr>
   <tr>
      <td>std::pair<T1, T2></td>
   </tr>
   <tr>
      <td>std::tuple<T1, …, Tn></td>
   </tr>
   <tr>
      <td>Convert TTree containing user-defined classes</td>
      <td></td>
      <td>Expect by the end of Jul.</td>
   </tr>
   <tr>
      <td rowspan="2">Convert TTree containing branches of nested types</td>
      <td>std::vector<std::vector<T> ></td>
      <td rowspan="2">Expect by the end of Aug.</td>
   </tr>
   <tr>
      <td>…</td>
   </tr>
   <tr>
      <td>Tests and documentation</td>
      <td></td>
      <td >Except by Sep.</td>
   </tr>
</table>

## Approach
As a PhD student in experimental nuclear astrophysics, I have been using ROOT everyday for many years since nearly all experimental data are sotred in ROOT's legacy storage, TTree. 

