---
title: "Season of Docs"
author: "Andrei Gheata"
layout: default
current_year: 2022
---

# ![CERN]({{ site.baseurl }}/images/CERN-HSF-GSdocs-logo.png){:height="100px"} Season of Docs {{page.current_year}}

## Introduction

[Season of Docs](https://developers.google.com/season-of-docs/) is a program that brings technical writers and open source projects together for a few months to work on open source documentation.

Particle physics is an exciting field where large collaborations of scientists collect
and analyze petabytes data from high-energy physics experiments, such as the Large Hadron Collider,
hosted at the CERN laboratory in Geneva, Switzerland.
Some of the questions that we collectively ask are:

- what are the fundamental blocks that make up our Universe?
- what is the nature of dark matter and dark energy?
- what is the nature of the asymmetry between matter and antimatter?
- what was early Universe like?

To answer these questions, particle physicists build software to simulate and analyze what happens in particle physics detectors.

Since 2011, CERN has participated in other Google initiatives such as Google Summer of Code (GSoC), first as a small organization (CERN-SFT) and later as an umbrella organization (CERN-HSF) to involve the high-energy physics community. Given the good results in the past under the GSoC program, CERN-HSF is eager to participate in this year and future editions of Season of Docs.

### Blogs from previous participants

Technical writer [blogs]({{ site.baseurl }}/gsdocs/2020/blogs.html)

### For technical writers

For candidate technical writers interested in our project proposals, please take your time to first read them thoroughly and visit the links they advertise. In case the content attracts your interest and you have ideas on how you may contribute, contact by mail directly the mentors listed at the end of each proposal. Please introduce yourself and attach your curriculum, which must contain references to some of your notable technical writing contributions. Note that all our projects require some previous experience in this area.

<!---
### For HSF projects and mentors

 Detailed instructions for mentors and organizations on how to apply, including links to other relevant Season of Docs resources are [available here]({{ site.baseur l }}/gsdocs/guideline.html). Please use the administrators contact at the bottom of this page (not the general to ask us any questions concerning your application.
-->

## Our {{page.current_year}} Project

{% assign sorted_proposals = site.gsdocs-proposals | sort: 'title' %}
{% for proposal in sorted_proposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}
{%- assign strings = proposal.url | split: '/' -%}
{%- assign proposal_year = strings[2] | plus: 0 -%}
{%- if proposal_year == {{page.current_year}} %}
* [ {{ proposal.title }} ]( {{ proposal.url }} ) 
{%- endif -%}
{% endfor %}

###  {{page.current_year}} Mentors (Name, Email, Org)

* David Lange [David.Lange@cern.ch](mailto:David.Lange@cern.ch) Princeton University
* Vassil Vassilev [Vassil.Vassilev@cern.ch](mailto:Vassil.Vassilev@cern.ch) Princeton University
* Andy Buckley [andy.buckley@cern.ch](mailto:andy.buckley@cern.ch) University of Glasgow

<!---
We have one project, so just remove the indirection for {{page.current_year}}
[HSF GSoD Projects]({{ site.baseurl }}/gsdocs/2022/summary.html)

[Full list of Mentors]({{ site.baseurl }}/gsdocs/2022/mentors.html)
 -->
---

*HSF Season of Docs Administrators*: David Lange.

[Contact administrators](mailto:david.lange@cern.ch) / [General e-mail for mentors](mailto:hsf-gsod-mentors-{{page.current_year}}@cern.ch)
