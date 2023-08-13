---
project: MadAnalysis 5 Multiweight Integration
title: MADAnalysis 5 Multiweight integration
author: Kyle Fan
avatar: https://avatars.githubusercontent.com/u/25071468?s=400&u=4a9c3d16631b63f5fea28cc2738b77dbaaa5fa37&v=4
date: 11.09.2022
year: 2022
layout: blog_post
logo: MadAnalysis5-logo.png
intro:
  Final blog post, Multiweight-integration User Guide and continued work plans.
---

## Multiweight Integration

This feature update will give users the ability to track theoretical
uncertainties during analysis.

## Midterm Evaluation

<p>

As of July 24th, 2022, with generous time and support from Jack and Benjamin, I
have integrated a multiweight container with the analysis platform. It currently
fills in cut-flows with multiweight data correctly. Changes are currently held
in
[multi_weight/multi_thread](https://github.com/kfan326/madanalysis5/tree/multi_weight/multi_thread).

</p>

<p> 
  
After discussions with Jack and Benjamin, we have decided to implement the next phase (Cutflow and histogramming output structure) in SQLite3 database format, next steps are to create a SQL schema and database manager to handle the database input and output. The format is selected due to ease of use for the end user, portability, and long term compatibility. Target completion time is the week of August 15th, 2022. Upon completion of the multi-weight integration, I will be working on multi-threading. The current plan is to use std::threads to handle events simultaneously in a SIMD paradigm since each event is independent of another. We may have to modify the datastructure to avoid data races when multiple threads are updating the same variables.

</p>

## User guide for multiweight integration - Final evaluation blog post September 8th, 2022.

<p>

Draft pull request can be found here
[multiweight_integration](https://github.com/MadAnalysis/madanalysis5/pull/125).
Current version does not yet have interface/install scripts for SQLite3, it will
be included in the final Pull Request. MacOS users will have it installed by
default and do not need to be concerned with it's installation, Linux users will
need to install SQlite3 to use the multiweight feature.

</p>

<p>

To use the multiweight feature, please update your analysis files to pass in the
multiweight container in the execute function. An example is shown below. Notice
the `Manage()->InitializeForNewEvent()` function must pass in two parameters:
the `MAdouble64 weight` value and the `WeightCollection.GetWeights()` container.
The current implementation will run both side by side until numerical validation
is complete, at which time the single-weight implementation will be deprecated.
The WeightCollection object is a general container for holding the weight values
as well as providing operators such as addition, subtraction, multiplication,
division, and assignment. The `GetWeights()` method is used to obtain the actual
`std::map<int, double> weights`.

</p>

```
bool atlas_susy_2018_31::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  MAdouble64 EvWeight;
  WeightCollection EvMultiweight;
  if(Configuration().IsNoEventWeight()) {
	  EvWeight=1.;
	  EvMultiweight=1.;
  }
  else if(event.mc()->weight()!=0.) {
	  EvWeight=event.mc()->weight();
	  EvMultiweight=event.mc()->multiweights();
 } else { return false;}

 Manager()->InitializeForNewEvent(EvWeight, EvMultiweight.GetWeights());
```

<p>
	An example of operator usage is shown below. 
</p>

```
if (MET<=250.)
  {
	Manager()->SetCurrentEventWeight(EvWeight*0.80);
	Manager()->SetCurrentEventWeight(EvMultiweight *= 0.80); //multiplication operator to scale all weight values by a float
  }
```

## Multiweight output files

<p>
The multiweight feature will produce two new files (one for Cutflows and the other for Histograms). The output location will be in their respective SAF output directory. The cutflow file will be named "cutflows.db" and the histogram file will be named "histo.db". These are SQLite3 files and can be transferred, stored, compressed and accessed independently of MADAnalysis 5. Users who are familiar with the basics of SQL queries can access the files through the terminal by the command: sqlite3 "file name"	
</p>

## Cutflow database schema and basic queries

The Cutflow database has 3 tables

- Cutflow
- Weights
- WeightDefinition

<p>
The Cutflow table contains a list of region name and cut name instances in the analysis. The Weights table contain all weight information, each weight row is uniquely identified by region name, cut name and weight id. The WeightDefinition table contains the name or description of the weights which are identified by their numerical ID. Some basic queries are shown below.
</p>

```
select * from Cutflow; // lists all region and their associated cuts in this analysis
select * from Weights; // lists all Cutflow data (# of positive/negative entries, positive sum, negative sum, positive squared sum, negative squared sum)
select * from Weights where id = 1; //same as above but only give the entry where weight id = 1, this is the same data as the SAF file for the non multiweight implementation
select * from WeightDefinition; // lists the weight definition for each weight

// note that you can select the columns individually instead of all of them by replace "*" with "column_name_1,.....,column_name_n" the where clause allows you to filter the rows based on a value for a column, in the above case weight id = 1
```

## Histogram database schema

The Histogram database has 3 tables

- HistoDescription
- Statistics
- Data

<p>

The HistoDescription table lists the name of the histograms associated with the
analysis and their restrictive attributes(number of bins, minimum value, maximum
value, associated regions). The Statistics table lists the statistical data
associated with each Histogram/weight pair. The Data table contains the positive
and negative values of each histogram bin. Examples of basic queries are shown
below.

</p>

```
select * from HistoDescription; // list all the histograms associated with the analysis and their general description
select * from Statistics where id = 1; // list all Histogram stats for weight id 1
select * from Data where id = 1; // List all bins including underflow/overflow for weight id 1
```

## When SQLite3 is unavailable

Without SQLite3, the program will not be able to output the multidimensional
data and thus, will continue to output in existing SAF format. A feature will be
added to merge weight information based on the weight description. Plots will
also be generated automatically during normal mode based on the merged weight
information.

## Continued work

The next milestone for this project is to enable multi-threading and optimize
the program for performance. Profiling will be used to identify the most compute
critical sections of the program that may benefit from optimizations. As
mentioned in the Mid-term blog, SIMD multi-threading will be used to parallelize
the program, the current plan is to duplicate the Cutflow and Histogramming
datastructures for N cores, then synchronize and collect the N "shards" of data
with one core. I believe this to be the most performant way of parallelization
since the datastructures themselves are not very memory hungry, duplicating them
N times will not exponentially increase memory usage.

Additional milestone after multi-threading is complete will likely be working on
a CI pipeline so that logic and numerical validation can be completed
automatically with each update, this will save significant time that developers
would need to spend on validation after each update.
