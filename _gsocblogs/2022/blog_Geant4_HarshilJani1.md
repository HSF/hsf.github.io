# Week 1

Me and my mentors have settled for Weekly Progress calls about discussing the progress of the project and what next we should be looking into it. The Week starts with this call itself. Now that, I already had a rough progress set, It was more easier to pick more clear ideas based on it. 

Let me show you the minimal version of the site which I already had at the start of Week 1 and by the end of community bonding. 
This is still better than what I had for my very first progress. I misunderstood and took the perf text reports and stick them to the site. But then mentors corrected me saying, They don't actually need the Text or CSV report and it was all about converting the generated CSV report to HTML Tables. 

![Before Week 1](https://user-images.githubusercontent.com/79367883/174475695-4e1b9179-6c6c-4862-a625-6703bd76536d.png)

In this, the table has been loaded from a demo.csv file which was not much filled with data. It was just a sample data file with very less number of entries. Now, If you look closely, There is a threshold based filtering part which I had implemented based on a For loop looping through all the entries and returning the ones that falls under that particular range. It was working well. 

Let's get back to discussion in the weekly call. Now, I was expected to add colours to the Tables based on the Metrics and also we had further discussions about the project for each chart individually. I coloured whole row based on a single metric. But, then I was corrected and expected to colour not just whole row but each cell based on their metric measures. So, I changed it as well and made each cell coloured. 

Now, One part of the project was to convert the perf reports to csv file using the awk script which was done by my mentor **Guilherme Amadio**. There were now more than one CSVs and we should allow the user to visualize all the reports. So, Next thing which I did was generalizing the loading of CSV file into the site. Currently, All you have to do for adding a CSV file is to add it inside the `Data/` directory and add the name of file to array. That will load all sort of files. Later I am thinking to even generalize array and let it read files directly from the directory itself. 

Now, There was some real problem with the threshold. Since, last time I used perf on the reports and generated the CSVs, I got actual data which was quite large compared to my demo data. So, The for loop for threshold was taking much longer time. It was the best possible way to find the entries in threshold ! Because it was O(N) I thought like this. But, When I discussed this issue with my mentor he suggested me to apply the filters just using the d3 logic so that, It will get those things coloured during the transpilation of d3 to JavaScript. He shared a sample snippet of how it could be implemented. It helped me in drawing the idea for the same and I was able to implement the logic which was shifted to d3 and every time new thresholds are there, We need to load the whole CSV to Table reports. It was definitely helpful and worked really well as compared to my loop based logic.

The design of site was not so great, Because I had used view-height and view-width everywhere to adjust things. So, I was suggested to use Grid or Flex and make it more responsive. I was also shared tutorials based on it. I was more comfortable with Flex comparatively so I applied the flex to whole site. I think it now looks much better than what It was looking before.

Here is the Screenshot of the site at then end of Week 1. 

![After Week 1](https://user-images.githubusercontent.com/79367883/174476966-35ce971c-b1a1-4601-a0b7-09762046a0bc.png)


TLDR :
- Coloured the individual cells based on metric. 
- Converted perf Reports to CSV with the help of awk scripts (provided by Mentor).
- Converted Threshold Logic from a `for` Loop to d3.js logic.
- Generalized the file input for loading CSVs.
- Changed styling of the site using Flex-box.