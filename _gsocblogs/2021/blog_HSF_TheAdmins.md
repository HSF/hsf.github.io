---
project: HSF
title: Writing a blog about your experience with HSF in GSoC
author: Andrei Gheata
[//]: # (photo: blog_authors/FirstLast.jpg)
date: 16.05.2021
year: 2020
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  If you would like to share your experience with GSoC, you can write a blog that we will review and maybe host on our HSF GSoC pages. Your experience is valuable for future GSoC candidates, but also for HSF mentors and administrators who are striving to improve the program every year. This article gives some guidelines for publishing your blog using the [HSF GitHub repository](https://github.com/HSF/hsf.github.io).
---

If you would like to share your experience with GSoC, you can write a blog that we will review and maybe host on our HSF GSoC pages. Your experience is valuable for future GSoC candidates, but also for HSF mentors and administrators who are striving to improve the program every year. This article gives some guidelines for publishing your blog using the [HSF GitHub repository](https://github.com/HSF/hsf.github.io).

### Size and content

While there is no formal limit, we recommend writing short articles, mainly for readability reasons. You should be focusing on your experience, rather than diving into the technical details of your project, but you could give (persistent) links to your work if you wanted to. Remember that you will anyway need to write a final technical report on the results of your project, the blog is something different. 

A common approach is to write useful information for future students, giving hints or shortcuts that you may have struggled to discover, describing how you tackled certain problems or difficulties, briefly, trying to help newcomers by sharing your own experience. It may happen that your project was not as successful as you have wished for, but this does not mean you cannot write a fantastic article! You just need to find the silver lining in your experience because ultimately what matters is what you've learned from the process and if it's worth sharing it. 

If you never wrote a blog, this is your opportunity to begin - there are plenty of good articles on the net for you to pick advice from, such as [this](https://smartblogger.com/how-to-write-a-blog-post/) one. Your article will be reviewed before being published on the HSF site, inappropriate content is not acceptable. You can write the article just after the final evaluation week, not to interfere with your GSoC work, but we will review it even earlier if you make a PR.

### Making a pull request for your blog

 * Fork git [repository](https://github.com/HEP-SF/hep-sf.github.io)
 * Add __gsocblogs/YEAR/blog_YOURPROJECT_FirstnameLastname.md_
 * Add a front matter, using the following labels:

**project:** HSF _<span style="color:grey"> [use your project idea name, matching the same label in _gsocprojects/YEAR/project_yourproject.md]</span>_<br/>
**title:** Your article title<br/>
**author:** Firstname Lastname<br/>
**photo:** blog_authors/FirstLast.jpg _<span style="color:grey"> [Optionally upload a squared format photo, rendered as 100x100, othrwise don't use the label]</span>_<br/>
**date:** 16.05.2021 _<span style="color:grey"> [Use the date when you wrote the article]</span>_<br/>
**year:** 2021 _<span style="color:grey"> [Make sure the year is correct]</span>_<br/>
**layout:** blog_post<br/>
**logo:** hsf_logo_angled.png _<span style="color:grey"> [Use the same file name as in _gsocprojects/YEAR/project_yourproject.md]</span>_<br/>
**intro:** |<br/>
Short introduction that will appear alongside other blogs. It can match the beginning of the detailed article.<br/>
`---`<br/>
Start your detailed article using markdown from here...

 * Make a pull request (add as reviewers the admins: HSF/gsoc-admins)





