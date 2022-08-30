---
project: Geant4
title: Geant4 - Performance Data Visualization using d3.js 
author: Harshil Jani
photo: blog_authors/HarshilJani.jpg
date: 12.06.2022
year: 2022
layout: blog_post
logo: Geant4-logo.png    
intro: |
   GSOC 2022  : Performance Analysis and Data Visualization for Geant 4 
---
# Table of Contents
- [Getting into the Process](#getting-into-the-process)
- [My Process](#my-process)
- [Week 1](#week-1)
- [Week 2](#week-2)
- [Week 3](#week-3)
- [Week 4](#week-4)
- [Week 5](#week-5)
- [Week 6](#week-6)
- [Week 7](#week-7)
- [Week 8](#week-8)
- [Week 9](#week-9)
- [Week 10](#week-10)
- [Week 11](#week-11)


# Getting into the process
When the accepted projects were announced, I was part of CERN-HSF under Geant4 project with my project being Performance analysis and Data Visualization. So, Now before we actually get started with the project, There is a phase of time known as Community Bonding Period.

Each Organization have their own set of rules, workflows and hierarchy to follow. To get new contributors familiar with the organization this period is crucial.
In this time, Students get familiar with the work to be done in their community, know their mentors, plan their project in more details, receive guidelines for contribution, gets resources to gain knowledge on any topic etc. 

# My Process
Talking about my personal experience, On 20th May I got to know about the selection, Then I got a mail from mentor about an introductory call. In that, All of us Me and both of my mentors had a brief introduction. Further, We had more project oriented discussion about what part am I supposed to work on. Then I got some links to Guest Accounts in CERN which was to be used for further communication and activities. 
After, The first call, I was playing around the repository and had few errors and questions. So, We on the next week had another discussion call where they helped me get these things fixed. Then I was advised to start working on the project in order to get started. Mentors taught me how the reports were generated, How to generate CSV reports and I got to know more about perf. They shared few presentations and documentations by them which helped me in setting perf. Now, After this I generated the reports by myself, Converted them into HTML Table.  At first I used a Python script using Pandas but It was not a good idea because it doesn't allow much customization. So, I figured out by myself and got those table by using D3.js itself. Then once the tables were on the page, I worked for filtering out them. 

I also got cleared that we were working on CMS which is a general purpose detector at Large Hadron Collider (LHC). I visited the CERN website and had a virtual tour of the CMS. Everything seemed like a rocket science to me, But I was blissfull to have even a virtual tour of it. I wonder how great the people working there might be. Meanwhile, There was a GSOC Global Summit on 3rd June. So, I have attended the whole summit. I have noted few learnings which I took from the summit and they can be found here [GSOC 22 Summit Learnings](https://medium.com/@harshiljani2002/my-learnings-from-gsoc22-global-summit-dab3e9db392)

# Week 1

I already had a rough progress set,So it was more easier to pick more clear ideas based on it. 
Let me show you the minimal version of the site which I already had at the start of Week 1 and by the end of community bonding. This is still better than what I had for my very first progress. I misunderstood and took the perf text reports and stick them to the site. But then mentors corrected me saying, They don't actually need the Text or CSV report and it was all about converting the generated CSV report to HTML Tables. 

![Before Week 1](https://user-images.githubusercontent.com/79367883/174475695-4e1b9179-6c6c-4862-a625-6703bd76536d.png)

In this, the table has been loaded from a demo.csv file which was not much filled with data. It was just a sample data file with very less number of entries. Now, If you look closely, There is a threshold based filtering part which I had implemented based on a For loop looping through all the entries and returning the ones that falls under that particular range. It was working well. 

Now, I was expected to add colours to the Tables based on the Metrics and also we had further discussions about the project for each chart individually. I coloured whole row based on a single metric. But, then I was corrected and expected to colour not just whole row but each cell based on their metric measures. So, I changed it as well and made each cell coloured. 

Now, One part of the project was to convert the perf reports to csv file using the awk script which was done by my mentor **Guilherme Amadio**. There were now more than one CSVs and we should allow the user to visualize all the reports. So, Next thing which I did was generalizing the loading of CSV file into the site. Currently, All you have to do for adding a CSV file is to add it inside the `Data/` directory and add the name of file to array. That will load all sort of files. Later I am thinking to even generalize array and let it read files directly from the directory itself. 

Now, There was some real problem with the threshold. Since, last time I used perf on the reports and generated the CSVs, I got actual data which was quite large compared to my demo data. So, The for loop for threshold was taking much longer time. It was the best possible way to find the entries in threshold ! Because it was O(N) I thought like this. But, When I discussed this issue with my mentor he suggested me to apply the filters just using the d3 logic so that, It will get those things coloured during the transpilation of d3 to JavaScript. He shared a sample snippet of how it could be implemented. It helped me in drawing the idea for the same and I was able to implement the logic which was shifted to d3 and every time new thresholds are there, We need to load the whole CSV to Table reports. It was definitely helpful and worked really well as compared to my loop based logic.

The design of site was not so great, Because I had used view-height and view-width everywhere to adjust things. So, I was suggested to use Grid or Flex and make it more responsive. I was also shared tutorials based on it. I was more comfortable with Flex comparatively so I applied the flex to whole site. I think it now looks much better than what It was looking before.

Here is the Screenshot of the site at then end of Week 1. 

![After Week 1](https://user-images.githubusercontent.com/79367883/174476966-35ce971c-b1a1-4601-a0b7-09762046a0bc.png)

# Week 2

As you might have already seen the image from last week, The first task was to get the numeric columns before the comm, dso and Symbol. So, I made changes in the script which converted the perf reports to CSV to print the numeric columns first in order. This was easy fix.

Now, the current measures makes no sense to the readers. Raw data is not useful in any ways. So, We need to convert the data into some relative measures. For Example, In measuring the CPU metrics, If the data file consists of Cycles and Instructions then we need to also add a measure of CPI. Also the raw data must be formatted like The Cycles and Instructions must be percentage of total of the respective measures. Similarly for Cache Metrics if we have branches and branch misses then we must add a measure of Branch Miss Rate.There was an issue that some metrics were not calculated by the Intel processors so we couldn't extract those data (L1 instruction loads). So, I spent some time fixing the code for including new metrics and improving the existing ones.

I was expected to install the CVMFS which is Cern VM (Virtual Machine) FS (File System) and mount the geant4 public repository which would create the bare clone on my system and allow me to run the jenkins reports So, I can run the perf reports available in the CI for Geant4. This was important to do because the current flamegraph which I had was not showing up the actual measures. So, I had to set this up and run the jenkins script. Now, Let me describe a problem faced by me in doing this. I use Ubuntu 22.04. But CVMFS don't have the Fuse Libraries set up for 22.04 Jammy Jellyfish. So, I went to the GitHub repo and in one of the discussion saw that they are working currently for this. But there a simple work-around was suggested, Which was fetching the OpenSSL library by yourself and then using the Fuse for 20.04 as it is because the SSL was not packed by default in Jammy Jellyfish. While exploring this, I found out that the suggest work-around was upgraded to 2.15 form 2.13 and for some reason 2.13 was not existing any more on the umd mirror. So, I commented a new work-around in the issue itself and got the CVMFS settled on my system. Now, It was working fine and I mounted the Geant4 repo in it. Next was the CCACHE error while running the jenkins script. I fixed the report script of jenkins and made a pull to the original repo of g4run. And I started running the script. It was working fine, But meanwhile for some spooky reasons my perf got broke and it was running continuously. So, I was not actually able to run the jenkins script. 

Another task of project for the week was to implement the Tree-Maps from the data which was coming out from the perf reports using a script provided by Guillherme Amadio. So now, We had the treemaps in the site. But, One problem with them was, Initially When I tried loading the treemaps It won't get rendered. Because the treemap nodes were required to get the offset positions of their measure on the screen size. But, I had used a property of CSS to let the contents of the site being hidden and it was `display : none` So, All the coordinates were returning 0. It took me a while to figure out why the treeMaps are not loading but finally I found a way out of it to get the `display : none` property being mocked without actually hiding the elements. So, All I did was replaced it with `visibility : hidden` and `position : absolute`. This helped with the site being able to  render treemaps along with the other tab contents. It also improved the buffer performance of the site, Which I measured using performance analytics from the Chrome Dev Tools (Beta). I also added the Inverted Flamegraph but those will be soon replaced by The real working flamegraphs.

![After Week 2.1](https://user-images.githubusercontent.com/79367883/175816608-88eaaeb7-2f97-4f2f-b5a5-d3e17228252c.png)
![After Week 2.2](https://user-images.githubusercontent.com/79367883/175816632-fd9981ec-1699-4241-9f15-4e9a414d41f3.png)
![After Week 2.3](https://user-images.githubusercontent.com/79367883/175816641-cd957d58-748f-44de-94b6-66f39dcc26e3.png)

# Week 3

I had successfully mounted the geant4 on the CVMFS as stated last week. This week we tried running the jenkins script from the Geant4 hosted on CVMFS. Then the team needed the reports of Difference per function which I generated by hand and added it to reports. Main part was customizing the treemaps based on metric used for diving it in specific Area, Color or Tool-tip. It was implemented as well. But it considered many edge cases which were causing if else statements. But functionality comes first, And the performance of the software doesn't gets affected so it really doesn't matter. In future if we have time, We can think to make it more generic.

I also changed the colour all over the reports and treemaps to green white and red scheme which inititally was blue and red. It now improved it visually.

All of a sudden perf got broke on my laptop for no reason. Maybe it occurred since I was trying to compile another version of Kernel for learning kernel development. It was still working fine with the sudo But it might mess up ahead in the repo. Anyways, I ran the jenkins report but it was way too heavy for my PC to handle. Around 44 Gigs were occupied what was weird for me. So, I got to know that perf is memory hungry. It is common. But a fix to this was generating only the e- electron reports and exclude others.

[Link to my PR in the Week](https://github.com/amadio/g4run/pull/1)

![After Week 3.1](https://user-images.githubusercontent.com/79367883/177044505-e80b1f93-ed8d-42f1-814b-91dbd4b4266b.png)
![After Week 3.2](https://user-images.githubusercontent.com/79367883/177044534-66e6bee3-b5e6-462b-8530-00b9d85de752.png)

# Week 4
I am really enjoying learning more and more about LHC. I must not say learning but It is more like knowing. I find interesting to know more about LHC (Large Hedron Collider) and also about Higgs Boson particle. These things are way beyond my project work. They are really making an impact on this planet. And it have new possibilities and capabilities. I really love things at CERN. Meanwhile, I am also about to participate into WebFest which used to be a weekly hackathon but this year, It is stipulated over the month of time. And luckily, Their event theme is Environment and one of the project theme is Data Visualization. Thanks, To my GSOC Project, I will be having a good idea about the project compared to the case if I was not a part of GSOC under CERN.

This week we discussed a few thing about the statistics to be derived from the existing metrics and the new ones to be added soon to the web. I then got a sudden thought of breaking down the difference report separately from the raw data because the diff report was of more importance to the developers. And then I got a "YES" for doing so.

My mentor already provided me the extra data to be added. I included new reports, Updated the Colouring to come out more generically, Popped up a difference tab out from the main raw reports. Fixed the sizing of the the table cell's height. 
This is how I made the colouring more generic through the snippet.

```JavaScript

 const max_array = [];
        numeric_columns.forEach((i) => {
            const value_array= [];
            data.filter(d => {
                if(!isNaN(d[i]) && isFinite(d[i])){
                    value_array.push(d[i]);
                }
            })
            
            max_array.push(d3.extent(value_array));
        }

```

The above snippet is using a D3.JS property which is `d3.extent` which will return you with an array of two elements one which would be minimum of all the elements and other would be the maximum of all the elements.

Now the math which I currently use for colouring is Lower 5% of the values would be green and Upper 5% would be red and in between I use white. But I still feel there is something not so good with my math behind this. I am sharing the snippet below for reference. I will be fixing this as soon as I get to know more clear insight about this statistics.

```JavaScript
SOME_ELEMENT.style("background-color", d => {
            if(numeric_columns.indexOf(d.column)!=-1){
                const max_col = max_array[numeric_columns.indexOf(d.column)]
                return d3.scaleLinear()
                         .domain([5*max_col[0]/100,75*max_col[1]/100,95*max_col[1]/100])
                         .range(["green","white","red"])(parseFloat(d.value));
        }});
```

In the domain array, The 3 values comes with [ 5% of min, 75% of max, 95% of max ] and other two coming out from the extent with two values in [0] and [1] as min and max respectively. This comes over the case where I have If else loops for each metric in specific which was the worst idea for mankind. Currently this doesn't look good, But soon it will be definitely improved.

So, Next week we had already planned to bring out the scatter plot from the existing CSVs which we have with us.
![After Week 4.1](https://user-images.githubusercontent.com/79367883/178314121-251bc343-46c9-497b-9e01-d054555a666b.png)
![After Week 4.2](https://user-images.githubusercontent.com/79367883/178314262-c0ed6553-7564-44ab-ab7f-6cde31c3be08.png)

# Week 5

I made a simple version of Scatter Plot using just the raw data. Then I tried adding brush for selection to it. And slowly I progressed with it by adding fields to it like Selection for X-Axis and Y-Axis then Radius and Colour of dots. Also, I had a tooltip which in upcoming weeks will be helpful for showing up the Spider-Plot for specific data point.

Since, I had a brush selection and a tooltip both together so I need to draw out some idea about how can I make it both available. So, I decided to create a selection button, Which on turning ON will result into the selection mode and in OFF state it would turn out to become a tooltip mode. Creating this was not the actual problem. But once I created the button, There was problem while holding the state of the scatter plot when the selection changes. What I mean is that If I use Selection mode and change the measure area for the plot and then if I choose to use tooltip mode then the whole Scatter plot gets updated when you change the state of the Switch. This was real problem which I faced. But, In the end, I found a correct place to clear off the plot area only when you turn it back on for the second time. Also, With this I invented another bug where two entries of same scatter plot were being created. So, I approached this using `d3.selection` and targeted the second entry and removed it from the DOM. Also, I would like to share that, My brush feature works on event selection which has changed a lot from v3 to v7 of D3.js So, I had gone through the changes made to d3's v7 since v5 and found a way out of it to make this more compatible with D3 v7 and ES6 ECMAScript syntax. It was good insight knowing about the features which got deprecated due to bad architecture and other new ones which were included due to changes into ECMA Script.

![After Week 5.1](https://user-images.githubusercontent.com/79367883/179426141-0f49f9fc-bced-4ddc-bfd6-e57bae4645c1.png)
![After Week 5.2](https://user-images.githubusercontent.com/79367883/179426172-a919bc8d-6e60-4607-92ac-eddca25d4335.png)
![After Week 5.3](https://user-images.githubusercontent.com/79367883/179426242-17ec2f9f-42b3-4372-980c-6159eff1178d.png)

# Week 6

This is the final week before Mid-Evaluation. I asked about the ATLAS experiment if we have the GDML for the same. So in that regards we explored the FullSimLight which is an ATLAS equivalent for g4run as it is for CMS. I am still not sure about it. Maybe I can explore it a little bit and get myself comfortable with FulLSimLight as well. I then asked about WebFest at CERN and other stuffs. Final remarks from the meet were, Everything up to the Mid-Evaluation is being done. Just fix up small errors on the axes of Scatter-Plot and create the skeleton for Spider Plot.

So, I worked for a good amount of time to figure out how I can show another chart into the tooltip. It got me into a good amount of brainstorming and I ended up creating something which shows a chart as a tooltip on top of some existing chart.

I messed up when I used a property d3.extent() for getting the maximum and minimum of the values into the plot axes ranges. But I really had no idea that, I was not actually converting the data from string to number. So Let's say your data array is [2,30,99,1234,75432] and the extent now was returning with [2,99] as in string 9 comes big in strength over digits so this was the thing which really broke my plot. And from this I realized whether I messed up the same into the treemaps or reports. But the fix to this was really simple which I got from d3.js documentation. It was about adding `d3.autoType` function to the path where we loaded CSV. So, It would on its own format the data for us. And with just that everything started working perfectly.

![After Week 6](https://user-images.githubusercontent.com/79367883/180643015-8dd3d59e-e71f-4960-b84a-94206a95ea32.png)

# Week 7

I created really a javaScript Coordinate Geometry function and took the reference from Danny-Yang's Spider Plot for defining the geometry into the Spider Plot. Also I made the brushing tool to work in both the dimensions which until now was just X-Axis based. I actually wrote the working version of Spider Plot in my college library which is greately known as "The Central Library" Of SVNIT in between the classes. 
 
I got my Evaluation Passed into the GSOC for my Mid-Term and the Feedback which I got was :

> "Progress has been very good so far. I believe that all deliverables will be on time for this project, and the quality of the work is also quite good."

![After Week 7.1](https://user-images.githubusercontent.com/79367883/182231618-7a047b3f-0149-4cbf-9221-9f66a30871b4.png)
![After Week 7.2](https://user-images.githubusercontent.com/79367883/182231507-fdfc0559-d8a3-4ace-96d2-6aeecf77c5a9.png)

# Week 8

For this week, I worked for the Difference treeMap reports. There already existed the TreeMap report by Guilherme, I used the same and got integrated in my version with a little modifications. Meanwhile I also improved my old treeMaps a little bit.

![After Week 8](https://user-images.githubusercontent.com/79367883/183768820-86643b62-4b9f-454e-a136-7913500ee907.png)

# Week 9

While preparing the Sunburst for this week I found a silly mistake in stratifying the data for the Sunburst.I fixed it and I had created a Sunbust out of the existing data which is as same as for the TreeMaps but I still was facing the issues while labelling the Sunburst. But simple workaround was to just add the title on the hovering so we don't need to worry much about the label. We planned this Sunburst plot as a summary of the data file. 
  
My mentor suggested me that, It would be good to separate out the reports into two major parts one specifically for the Raw Reports and another for difference report. So for next week I would be doing this.

![After Week 9](https://user-images.githubusercontent.com/79367883/187046693-b74858ec-3536-4336-b9bd-7905071da5cc.png)

# Week 10

As written in the last week, I was expected to separate out the difference report into two different tabs.
Then , my mentor was working for finding a way about how can we integrate the existing reports into jenkins and he told me not to worry much about the report integration, He would mostly take care of it and once done, I can play with the Cmake file and adjust the JS variables out of it.

He also said It would be more helpful for the developers to actually sort the existing table files based on the column values. So, I worked for that part as well and implemented the sort feature when you click on the Table Head cell. Also, I was expected to change the Title of the Site from Peformatic Visuals to Geant4 Performance Reports.

I did all my changes and pushed them back to the repository. Now was the time for Jenkins Integration.

![After Week 10.1](https://user-images.githubusercontent.com/79367883/187047038-4deffb67-48b0-4d44-8861-72f1eb4ced29.png)
![After Week 10.2](https://user-images.githubusercontent.com/79367883/187047061-9319dafc-8ed5-4978-b670-97f299844b40.png)

# Week 11 

The week was officially for the Presentation and Blog Post. Since, All of my deliverables were completed, I was expected to do the Presentation. But I got busy with the CERN WebFest as it was the final week for submission. Moreover We approached the Completion of the Program and my project of g4Web got merged into the g4Run [PR for g4Web](https://github.com/amadio/g4run/pull/2). I am really thankful to my mentors and all the people who helped and will be helping further throughout the Entire Summer of Code. 

<!-- Presentation Link to be Added Soon ! -->