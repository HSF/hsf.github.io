---
title: "Google Summer of Code"
author: "Benedikt Hegner"
layout: default
---

# ![CERN](/images/CERN-logo.jpg){:height="100px"} ![HSF](/images/hsf_logo_angled.png){:height="100px"} Google Summer of Code

## Introduction

[Google Summer of Code](https://developers.google.com/open-source/gsoc/) is a program that allows students to contribute to development of open-source projects, mentored by participating organizations.

Particle physics is an exciting field where large collaborations of scientists collect 
and analyze petabytes data from high-energy physics experiments, such as the Large Hadron Collider, 
hosted at the CERN laboratory in Geneva, Switzerland. 
Some of the questions that we collectively ask are: 

- what are the fundamental blocks that make up our Universe? 
- what is the nature of dark matter and dark energy?
- what is the nature of the asymmetry between matter and antimatter? 
- what was early Universe like? 

To answer these questions, particle physicists build software to simulate and analyze what happens in particle physics detectors.

The CERN software for experiments (CERN-SFT) group has participated in the GSoC since 2011. 
Since 2017 the program has expanded to involve the high-energy physics community under the umbrella of the HEP Software Foundation.

Information from last year's GSoC can be found [here](/gsoc/2017/index.html). For 2018 the 
HSF is again applying for participation in the program. If you are 
interested in the GSoC program contact us using the HSF GSoC mailing list: [hep-software-foundation-google-summer-of-code@googlegroups.com](mailto:hep-software-foundation-google-summer-of-code@googlegroups.com).

Instructions for participating projects and mentors can be found [here](/gsoc/guideline.html).

## Projects in 2018

{% assign project_collection = 'gsocprojects' %}
{:.table .table-hover  .table-striped}
{% for project in site[project_collection] %}| ![{{ project.project }}](/images/{{ project.logo }}){:width="100px"} | {%if project.summary %}{{ project.summary | strip_newlines }}{%else%}{{ project.description | strip_newlines }}{%endif%} | [List of proposals](/gsoc/projects{{ project.path | remove_first: '_' | remove_first: project_collection | replace: '.md', '.html' }}) |
{% endfor %}

## Participating Organizations in 2018

{% assign org_collection = 'gsocorgs' %}
{:.table .table-hover  .table-striped}
{% for org in site[org_collection] %}| ![{{ org.organization }}](/images/{{ org.logo }}){:width="100px"} | {%if org.summary %}{{ org.summary | strip_newlines }}{%else%}{{ org.description | strip_newlines }}{%endif%} | [List of proposals](/gsoc/organizations{{ org.path | remove_first: '_' | remove_first: org_collection | replace: '.md', '.html' }}) |
{% endfor %}


## Summary

[Full list of Proposal Ideas](/gsoc/2018/summary.html)

[Full list of Mentors](/gsoc/2018/mentors.html)

---

*HSF GSoC Administrators*: [Sergei Gleyzer](mailto:sergei@cern.ch), [Enric Tejedor Saavedra](mailto:etejedor@cern.ch) and [Antoine Perus](mailto:perus@lal.in2p3.fr).
