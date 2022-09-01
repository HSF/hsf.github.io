---
project: HSF
title: Writing a blog about your project with HSF in GSoC
author: Andrei Gheata
[//]: # (photo: blog_authors/FirstLast.jpg)
date: 08.06.2022
year: 2022
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  Student blogs are mandatory for CERN-HSF starting with GSoC 2022 edition! This is now common practice and it is an efficient way to track the activity within the different GSoC projects. For students: consider this your own GSoC page. You should publish all relevant information about the activity: links to proposals, presentations, reports, and also your experience with GSoC.
---

Student blogs are mandatory for CERN-HSF starting with GSoC 2022 edition! This is now common practice and it is an efficient way to track the activity within the different GSoC projects. For students: consider this your own GSoC page. You should publish all relevant information about the activity: links to proposals, presentations, reports, and also your experience with GSoC. 

Your experience is invaluable for future GSoC candidates and for improving the program every year. There are some guidelines for publishing your blogs using the [HSF GitHub repository](https://github.com/HSF/hsf.github.io).

### Size and content

We are still experimenting this year, so there are no formal rules. The idea is that we offer a one-page placeholder that can be used for a short project description and links to all relevant materials. Some links are mandatory, such as the link to your project proposal and the links to the GSoC reports that you have to provide in the program. Few things to consider: the size of inlined text should not be exhaustive for readability reasons, and links should not point to temporary pages. 

### Making a pull request for your blog

 * Fork git [repository](https://github.com/HSF/hsf.github.io)
 * Add __gsocblogs/YEAR/blog_YOURPROJECT_JaneDoe.md_
 * Add a front matter, using the labels as below
 * Commit to your fork and make a pull request, asking a review from your mentor(s)

---
**project:** HSF _<span style="color:grey"> [replace with the project label as in _gsocprojects/YEAR/project_yourproject.md]</span>_<br/>
**title:** Your article title<br/>
**author:** Jane Doe<br/>
**photo:** blog_authors/JaneDoe.jpg _<span style="color:grey"> [Optionally use this label and upload a squared format photo as images/blog_authors/FirstLast.jpg]</span>_<br/>
**date:** 16.05.2022 _<span style="color:grey"> [Use the date when you wrote the article]</span>_<br/>
**year:** 2022 _<span style="color:grey"> [Make sure the year is the current one]</span>_<br/>
**layout:** blog_post<br/>
**logo:** hsf_logo_angled.png _<span style="color:grey"> [Use the same file name as in _gsocprojects/YEAR/project_yourproject.md]</span>_<br/>
**intro:** |<br/>
Short introduction that will appear alongside other blogs. It can match the beginning of the detailed article.<br/>
`---`<br/>
Start your detailed article using markdown here...
