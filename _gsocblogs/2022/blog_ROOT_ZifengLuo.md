---
project: ROOT
title: Automatic conversion of data stored in TTree form to RNTuple
author: Zifeng Luo
photo: blog_authors/ZifengLuo.jpg
date: October 04, 2022
year: 2022
layout: blog_post
logo: ROOT-logo.png
intro: |
  This project consists of the implementation of an automatic conversion tool that migrates both the schema (i.e. fields and their types) and the data of a TTree to RNTuple.
---
This is a blog as part of the final evaluation of GSoC 2022 project: ROOT - Automatic conversion of data stored in TTree form to RNTuple.

## Overview of the project
For the past 25 years, high-energy physics (HEP) data have been stored with columnar structures in TTree, the ROOT’s legacy columnar storage that has been used to store more than 1 exabyte of HEP data. As the main data structure of ROOT v7, RNTuple classes provide ROOT’s new, experimental, high-speed I/O subsystem for HEP data. Given that RNTuple is a complete backward-incompatible redesign, the development of an automatic conversion tool that permits the migration of existing TTree data into RNTuple is a must. In this regard, both the schema (i.e., fields and their types) and the data will have to be migrated.

The goal of this project is to develop a TTree-to-RNTuple conversion tool which works in form of a C++ library as well as a command-line tool.

## Approach
I started working on this project on June 11, 2022, right after the community-bonding period. The first two weeks were a hands-on period. I began with the [existing code](https://github.com/jblomer/iotools/blob/master/gen_physlite.cxx) that is capable to convert TTree containing simple data types to RNTuple. After being familiar with RNTuple APIs, I created the project GitHub [repo](https://github.com/luozf14/TTreeToRNTuple) and started committing my code. The length of the project is decided to be 14 weeks, ending at the beginning of October. 

Based on the data types supported by TTree, the project is divided into 7 parts with increasing difficulties, from simple C++ variables to nested collections. The status is summarized in the table below. 

<table>
   <tr>
      <th>Part</th>
      <th>Types</th>
      <th>Status</th>
   </tr>
   <tr>
      <td >Convert TTree containing simple variables </td>
      <td><code>int</code>, <code>float</code>, <code>bool</code>, ...</td>
      <td>Completed. Types are one-to-one mapped (e.g., <code>int</code>-><code>int</code>).</td>
   </tr>
   <tr>
      <td rowspan="3">Convert TTree containing arrays</td>
      <td>Fixed-length 1D array</td>
      <td>Completed. Mapped to <code>std::array&lt;T, N></code> (e.g., <code>int arry[10]</code>-><code>std::array&lt;int,10></code>)</td>
   </tr>
   <tr>
      <td>Variable-sized 1D array</td>
      <td>Completed. Mapped to <code>std::vector&lt;T></code> (e.g., <code>int arry[N]</code>-><code>std::vector&lt;int></code>)</td>
   </tr>
   <tr>
      <td>Multidimensional array (e.g., <code>int myArry[16][8]</code>)</td>
      <td>Depending on if the size is variable, currently it is mapped to 1D <code>std::array&lt;T, N></code> (fixed-size) or <code>std::vector&lt;T></code> (variable-size). In order to map it to corresponding dimensional vector, native RNTuple feature support is needed.</td>
   </tr>
   <tr>
      <td rowspan="5">Convert TTree containing STL types and collections </td>
      <td><code>std::string</code></td>
      <td rowspan="5">Completed. All types are one-to-one mapped except types that are not supported by RNTuple I/O. For example, <code>std::set&lt;T></code> will cause program crash. However, conversion of TTree containing branches of <code>ROOT::RVec&lt;T></code> is not stable in current stage (see section <b>Known issues and Future work</b>).</td>
   </tr>
   <tr>
      <td><code>std::array&lt;T, N></code></td>
   </tr>
   <tr>
      <td><code>std::vector&lt;T></code> and <code>ROOT::RVec&lt;T></code>*</td>
   </tr>
   <tr>
      <td><code>std::pair&lt;T1, T2></code></td>
   </tr>
   <tr>
      <td><code>std::tuple&lt;T1, …, Tn></code></td>
   </tr>
   <tr>
      <td>Convert TTree containing user-defined classes</td>
      <td>Any user-defined class with dictionary</td>
      <td>Completed. The dictionary of the user-defined class is required. It can be either a <code>*.so</code> file or a <code>*.a</code> file. If corresponding dictionary does not exist, <code>RFieldBase::Create()</code> should throw, thus aborting the conversion process.</td>
   </tr>
   <tr>
      <td rowspan="2">Convert TTree containing branches of nested types</td>
      <td><code>std::vector&lt;std::vector&lt;T> ></code></td>
      <td rowspan="2">Partially completed. User needs to manually generate the dictionaries of the nested types.</td>
   </tr>
   <tr>
      <td>…</td>
   </tr>
   <tr>
      <td rowspan="2">Integration</td>
      <td>Integrate the 5 parts above into a command-line tool</td>
      <td>Completed. <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/GenericConverter.cxx">[Code]</a></td>
   </tr>
   <tr>
      <td>A reusable library for TTree-to-RNTuple conversion as part of RNTuple module</td>
       <td>Completed. <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/src/TTreeToRNTuple.cxx">[Code]</a> </td>
   </tr>
   <tr>
      <td>Tests and documentation</td>
      <td></td>
      <td >Completed. This tool passed a <a href="https://github.com/luozf14/TTreeToRNTuple/tree/main/test">unit test</a> with with 1e8 entries and is tested with data from <a href="https://root.cern/files/RNTuple/treeref/">here</a>. Documentation can be found <a href="https://github.com/luozf14/TTreeToRNTuple/blob/main/README.md">here.</a></td>
   </tr>
</table>

*see section **Known issues and Future work**.

Thanks to the [development](https://github.com/jblomer/iotools) that has been done by the ROOT I/O team, there are some programs that work as good references for me. I extended the ``gen_physlite`` program to be capable of converting TTree containing fixed-length arrays as well as variable-sized arrays. However, due to the limitation of data types supported by the current-stage RNTuple, the conversion tool is not able to deal with the multi-dimensional array. For now such array is converted into 1D `std::array<T, N>` (fixed-size) or `std::vector<T>` (variable-size). I/O team decided to mark this function as to-do until RNTuple supports multi-dimensional arrays.

For TTree containing STL containers, there is no good reference. The existing ``gen_atlas`` program is dedicated to `std::vector<T>` with some specific types. However, thanks to ``TClass::GetClass()``, I not only extended ``gen_atlas`` to be capable to deal with `std::vector<T>` with all RNTuple-supported data types but also included all other STL containers supported by RNTuple (see table above). 

A dictionary consists of a C++ source file, which contains the type information needed by Cling and ROOT's I/O subsystem. RNTuple supports class that has a dictionary whose persistent members are themselves types with RNTuple I/O support. This tool can migrate data stored in TTree containing branches of user-defined classes with compiled dictionary embedded in library `xx.so` or `xx.a`, i.e., to do the conversion, the corresponding library must be existing. 

Nested types are more difficult to be converted since most of the time ROOT does not provide compiled CollectionProxy for those nested types. From TTree side, one needs to generate the dictionaries of the nested types so that their values can be retrieved, while there is no problem for RNTuple side to create fields of nested types thanks to ``TClass::GetClass()``. Currently, this tool is capable to convert TTree containing nested types if user generate and import the corresponding dictionaries.

The tool can be used as a command-line tool as well as a C++ library. More details can bee seen in the next section.

## Usage

- As a command-line tool

  ```bash
  $ ./GenericConverter -h
  Usage: ./GenericConverter -i <input.root> -o <output.ntuple> -t(ree) <tree name> [-d(ictionary) <dictionary name>] [-s(ub branch) <branch name>][-c(ompression) <compression algorithm>] [-p(rint conversion progress)]
  ```

- As a C++ library

  An example is shown below:

  ```c++
  std::string inputFile = "input.root";
  std::string outputFile = "output.ntuple";
  std::string treeName = "tree";
  std::string compressionAlgo = "none";
  int compressionLevel = 0;
  std::vector<std::string> dictionary = {"UserClass.so"};
  std::vector<std::string> subBranches = {"userClass", "branch1", "branch2"};
  
  // convert
  std::unique_ptr<TTreeToRNTuple> conversion = std::make_unique<TTreeToRNTuple>(inputFile, outputFile, treeName);
  conversion->SetCompressionAlgoLevel(compressionAlgo, compressionLevel);
  conversion->SetDictionary(dictionary);
  conversion->SelectBranches(subBranches);
  conversion->SetUserProgressCallbackFunc([](int current, int total)
                                          {if (current % 10 == 0)
                                          {
                                              fprintf(stderr, "\rProcessing entry %d of %d [\033[00;33m%2.1f%% completed\033[00m]",
                                                      current, total,
                                                      (static_cast<float>(current) / total) * 100);
                                          } }); //user-defined lambda function
  conversion->Convert();
  ```

## Self evaluation
The project was initially carried out according to the timeline in the proposal. The first part "Convert TTree containing simple variables" went well and was completed on time. But the second part took two weeks longer than what was expected in the proposal. I met problems when dealing with variable-sized arrays: a) I didn't know how to migrate data of different types (e.g., `int`, `float`, ...) in a generic way instead of emulating cases; b) it was difficult to get the length of an array in each entry. My mentor Dr. Javier Lopez-Gomez helped me solve these problems. The third and fourth parts went well accordingly. Due to some personal issues from both my mentor and I, the project was delayed a bit in August and early September. But finally we managed to make it and complete the rest of the parts. For now the tool is coded independently from the root-project. We may integrate it into ROOT in the post-GSoC period. 

## Miscellaneous
As a Ph.D. student in experimental nuclear astrophysics, I have been using ROOT every day for many years because nearly all experimental data are stored in ROOT's legacy storage, TTree. When I heard about GSoC from friends, I instinctively looked for projects related to ROOT because I have always been dreaming to participate in the ROOT project,  which is the most important infrastructure of high-energy physics. 

As mentioned in the beginning, TTree is the most important element of ROOT; a large amount of HEP data have been stored in TTree. Therefore, I was attracted by this TTree-To-RNTuple project because its deliverable will be the most commonly used tool among HEP scientists once ROOT v7 will be released. It would be cool if everyone uses your tool frequently.

As a physicist without any computer science background, I meet a lot of troubles when I am working on this project. However, I am very lucky that I have the nicest mentor, Dr. Javier Lopez-Gomez. No matter how simple or naive my questions are, he is always considerate and full of patience to me. For example, he explained explicitly to me how the vector and array are stored in memory by drawing sketches, while others may just say "This is basic; you should have known it".

## Summary
This is my first time participating in an open-source project. I learned a lot about collaboration in the field of computer science. Things go a little differently from the initial timeline, but the progress is within expectation. It has been a great learning experience and I'm grateful to have an awesome mentor and to be able to meet with the "real and alive" ROOT team.
