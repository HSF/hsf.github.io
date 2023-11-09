---
title: "Season of Docs"
author: "Andrei Gheata"
layout: default
current_year: 2023
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

### Previous HSF Season of Docs Results 

  * 2020 Season of Docs Technical writer [blogs]({{ site.baseurl }}/gsdocs/2020/blogs.html)
  * 2022 Season of Docs [summary]({{ site.baseurl }}/gsdocs/2022/Outcome.pdf) and [proposal]({{ site.baseurl }}/gsdocs/2022/proposal_analysis.html)
  
### For technical writers

For candidate technical writers interested in our project proposal, please take your time to first read it thoroughly and visit the links advertised. In case the content attracts your interest and you have ideas on how you may contribute, contact by mail directly the mentors listed at the end of each proposal. Please introduce yourself and attach your curriculum, which ideally contains references to some of your notable technical writing contributions. Note that all our projects require some previous experience in this area.

## Our {{page.current_year}} Project

{% assign sorted_proposals = site.gsdocs-proposals | sort: 'title' %}
{% for proposal in sorted_proposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}
{%- assign strings = proposal.url | split: '/' -%}
{%- assign proposal_year = strings[2] | plus: 0 -%}
{%- if proposal_year == page.current_year %}
* [ {{ proposal.title }} ]( {{ proposal.url }} ) 
{%- endif -%}
{% endfor %}

###  {{page.current_year}} Mentors (Name, Email, Org)

* Valentin Volkl [Valentin.Volkl@cern.ch](mailto:Valentin.Volkl@cern.ch) CERN
* Jakob Blomer [Jakob.Blomer@cern.ch](mailto:Jakob.Blomer@cern.ch) CERN

* HSF Season of Docs Administrators*: Valentin Volkl.

[Contact the HSF Season of Docs administrators](mailto:valentin.volkl@cern.ch) and use this [general e-mail to contact all mentors](mailto:hsf-gsod-mentors-{{page.current_year}}@cern.ch)

