---

project: MadAnalysis 5 Multiweight Integration
title: Midterm evaluation blog post
author: Kyle Fan
date: 24.07.2022 
year: 2022 
layout: blog_post
logo: MadAnalysis5-logo.png
intro: Midterm progress report

---

<p> 

As of July 24th, 2022, with generous time and support from Jack and Benjamin, I have integrated a multiweight container with the analysis platform. It currently fills in cut-flows with multiweight data correctly. Changes are currently held in [multi_weight/multi_thread](https://github.com/kfan326/madanalysis5/tree/multi_weight/multi_thread).
  
</p> 

<p> 
  
After discussions with Jack and Benjamin, we have decided to implement the next phase (Cutflow and histogramming output structure) in SQLite3 database format, next steps are to create a SQL schema and database manager to handle the database input and output. The format is selected due to ease of use for the end user, portability, and long term compatibility. Target completion time is the week of August 15th, 2022. Upon completion of the multi-weight integration, I will be working on multi-threading. The current plan is to use std::threads to handle events simultaneously in a SIMD paradigm since each event is independent of another. We may have to modify the datastructure to avoid data races when multiple threads are updating the same variables.

</p>


## User guide for multiweight integration - Final evaluation blog post September 8th, 2022.

<p>

Draft pull request can be found here [multiweight_integration](https://github.com/MadAnalysis/madanalysis5/pull/125). Current version does not yet have interface/install scripts for SQLite3, it will be included in the final Pull Request. MacOS users will have it installed by default and do not need to be concerened with it's installation, Linux users will need to install SQlite3 to use the multiweight feature.
 
</p>

<p>

To use the multiweight feature, please update your analysis files to pass in the multiweight container in the execute function. An example is shown below. Notice the Manage()->InitializeForNewEvent() function must pass in two parameters: the MAdouble64 weight value and the WeightCollection.GetWeights() container. The current implementation will run both side by side until numerical validation is complete, at which time the single weight implementation will be deprecated. The WeightCollection object is a general container for holding the weight values as well as providing operators such as addition, subtraction, multiplication, division, and assignment. The GetWeights() method is used to obtain the actual std::map<int, double> weights.
 
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
	The multiweight feature will produce two new files (one for Cutflows and the other for Histograms). The output location will be in their respective SAF output directory. The cutfow file will be named "cutflows.db" and the histogram file will be named "histo.db".
	
</p>
