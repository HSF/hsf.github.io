project: _gsocprojects/2022/project_MadAnalysis5.md
title: Midterm evaluation blog post
author: Kyle Fan
//photo: blog_authors/JaneDoe.jpg [Optionally use this label and upload a squared format photo as images/blog_authors/FirstLast.jpg]
date: 24.07.2022 
year: 2022 
layout: blog_post
logo: hsf_logo_angled.png [Use the same file name as in _gsocprojects/YEAR/project_yourproject.md]
intro: Midterm progress report



<p> 

As of July 24th, 2022, with generous time and support from Jack and Benjamin, I have integrated multiweight container with the analysis platform. It currently fills in cutflows with multiweight data correctly. Changes are currently inside the multi_weight/multi_thread branch in my fork https://github.com/kfan326/madanalysis5/tree/multi_weight/multi_thread 
  
</p> 

<p> 
  
After discussions with Jack and Benjamin, we have decided to implement the next phase (Cutflow and histogramming output structure) in SQLite3 database format, next steps are to create a SQL schema and database manager to handle the database input and output. The format is selected due to ease of use for the end user, portability, and long term compatibility. Target completion time is the week of August 15th, 2022. Upon completion of the multi-weight integration, I will be working on multi-threading. The current plan is to use std::threads to handle events simultaneously in a SIMD paradigm since each event is independent of another. We may have to modify the datastructure to avoid data races when multiple threads are updating the same variables.

</p>

