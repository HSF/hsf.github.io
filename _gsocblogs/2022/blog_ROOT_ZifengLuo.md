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
For the past 25 years, high-energy physics (HEP) data have been stored with columnar structures in TTree, the ROOT’s legacy columnar storage that has been used to store more than 1 exabyte of HEP data. As the main data structure of ROOT v7, RNTuple classes provide ROOT’s new, experimental, high-speed I/O subsystem for HEP data. Given that RNTuple is a complete backward-incompatible redesign, the development of an automatic conversion tool that permits the migration of existing TTree data into RNTuple is a must. In this regard, both the schema (i.e., fields and their types) and the data will have to be migrated.

## Progress
I started working on this project on June 11, 2022, right after the community-bonding period. The first two weeks were a hands-on period. I began with the [existing code](https://github.com/jblomer/iotools/blob/master/gen_physlite.cxx) that is capable to convert TTree containing simple data types to RNTuple. After being familiar with RNTuple APIs, I created the project GitHub [repo](https://github.com/luozf14/TTreeToRNTuple) and started committing my own code. The length of the project is decided to be 14 weeks, ending at the beginning of October. 

Based on the data types supported by TTree, the project is divided into 5 parts with increasing difficulties, from simple C++ variables to nested collections. The status is summarized in the table below. 

<table>
   <tr>
      <th>Part</th>
      <th>Types</th>
      <th>Status</th>
   </tr>
   <tr>
      <td >Convert TTree containing simple variables </td>
      <td>int, float, bool, ...</td>
      <td>Completed <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/ConverterSimple.cxx">[Code]</a></td>
   </tr>
   <tr>
      <td rowspan="3">Convert TTree containing arrays</td>
      <td>Fixed-length array</td>
      <td rowspan="2">Completed <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/ConverterArray.cxx">[Code]</a></td>
   </tr>
   <tr>
      <td>Variable-sized array</td>
   </tr>
   <tr>
      <td>Multidimensional array (e.g., int myArry[16][8])</td>
      <td>Need RNTuple feature support</td>
   </tr>
   <tr>
      <td rowspan="5">Convert TTree containing STL types and collections </td>
      <td>std::string</td>
      <td rowspan="5">Completed <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/ConverterSTLContainer.cxx">[Code]</a></td>
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
      <td>Any user-defined class with dictionary</td>
      <td>Partially completed <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/ConverterUserDefClass.cxx">[Code]</a></td>
   </tr>
   <tr>
      <td rowspan="2">Convert TTree containing branches of nested types</td>
      <td>std::vector&lt;std::vector&lt;T> ></td>
      <td rowspan="2">Expected by the end of Aug.</td>
   </tr>
   <tr>
      <td>…</td>
   </tr>
   <tr>
      <td>Tests and documentation</td>
      <td></td>
      <td >Expected in Sep.</td>
   </tr>
</table>

Thanks to the [development](https://github.com/jblomer/iotools) that has been done by the ROOT I/O team, there are some programs that work as good references for me. I extended the ``gen_physlite`` program to be capable of converting TTree containing fixed-length arrays as well as variable-sized arrays. However, due to the limitation of data types supported by the current-stage RNTuple, the conversion tool is not able to deal with the multi-dimensional array. I/O team decided to mark this function as to-do until RNTuple supports multi-dimensional arrays.

For TTree containing STL containers, there is no good reference. The existing ``gen_atlas`` program is dedicated to std::vector\<T\> with some specific types. I not only extended it to deal with std::vector\<T\> with all RNTuple-supported data types but also included all other STL containers supported by RNTuple (see table above).

A dictionary consists of a C++ source file, which contains the type information needed by Cling and ROOT's I/O subsystem. RNTuple supports class that has a dictionary whose persistent members are themselves types with RNTuple I/O support. Currently, my code is able to migrate data stored in TTree containing user-defined classes with compiled dictionary embedded in library ``xx.so``, i.e., to do the conversion, the corresponding library must be existing. However, TTree has a feature that when it stores a class, the dictionary is also stored automatically. Hence, the next step is to find a way to load the dictionary from TTree in case the library does not exist.

Converting TTree containing branches of nested types is the most difficult part, and it is expected to be complete by the end of August. Upon completion of this, we will integrate all parts into a single program that can be run as a command line tool. It will also be used as a library for TTree-to-RNTuple conversion, hence we will be working on designing the API for the library upon the completion of the first 4 parts.

## Self evaluation
The project was initially carried out according to the timeline in the proposal. The first part "Convert TTree containing simple variables" went well and was completed on time. But the second part took two weeks longer than what was expected in the proposal. I met problems when dealing with variable-sized arrays: a) I didn't know how to migrate data of different types (e.g., int, float, ...) in a generic way instead of emulating cases; b) it was difficult to get the length of an array in each entry. My mentor Dr. Javier Lopez-Gomez helped me solve these problems. The third and fourth parts went well accordingly. Overall, the project is 2 weeks behind the initial schedule. But the proposal was based on a 12-week length, and we have extended it to 14 weeks. Therefore, the project is expected to be completed on time.

## Miscellaneous
As a Ph.D. student in experimental nuclear astrophysics, I have been using ROOT every day for many years since nearly all experimental data are stored in ROOT's legacy storage, TTree. When I heard about GSoC from friends, I instinctively looked for projects related to ROOT because I have always been dreaming to participate in ROOT project,  which is the most important infrastructure of high-energy physics. 

As mentioned in the beginning, TTree is the most important element of ROOT; a large amount of HEP data have been stored in TTree. Therefore, I was attracted by this TTree-To-RNtuple project because its deliverable will be the most commonly used tool among HEP scientists once ROOT v7 will be released. It would be really cool if everyone uses your tool frequently.

As a physicist without any computer science background, I meet a lot of troubles when I am working on this project. However, I am very lucky that I have the nicest mentor, Dr. Javier Lopez-Gomez. No matter how simple or naive my questions are, he is always considerate and full of patience to me. For example, he explained explicitly to me how the vector and array are stored in memory by drawing sketches, while others may just say "This is basic; you should have known it".






