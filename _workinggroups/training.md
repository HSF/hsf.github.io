---
title: Training
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/training.html
  - /activities/training.html
---

The HSF Training Working Group aims to help the research community to provide
training in the computing skills needed for researchers to produce high
quality, sustainable software. The group works with experiment training groups,
with HEP initiatives (such as IRIS-HEP and FIRST-HEP) and with organisations
like Software Carpentry to coordinate training activities.

The group aims to develop a training programme that can be followed by all
researchers to achieve the level of knowledge that they require. This ranges
from basic core skills, needed by everyone, to advanced training required by
specialists in software and computing.

A link to our training events can be found [HERE](https://indico.cern.ch/category/11386/)

A link to CWP report on training can be found here: [HEP Software Foundation Community White Paper Working Group - Training, Staffing and Careers](https://arxiv.org/abs/1807.02875)

<div style="text-align:center; padding:25px; float:center">
<img src ="/images/training/training-pyramid.png" alt="HSF Training Pyramid" />
</div>

Convenors: Kilian Lieret (LMU), Sudhir Malik (Puerto Rico), Sam Meehan (CERN)

## How to participate ?

Everybody is welcome to join the
[forum](https://groups.google.com/forum/#!forum/hsf-training-wg) dedicated to
HSF training activities. This is the place where ideas and proposals are
discussed and actions decided!

Weekly meetings are usually held at 15h30 CERN time on Mondays. Check
[Indico](https://indico.cern.ch/category/11294/) for details.

## Github Organization

The [HSF-Training GitHub Organization](https://github.com/hsf-training) has [Analysis Essentials](https://hsf-training.github.io/analysis-essentials/), a course on basic computing required for HEP, and [PyHEP resources](https://github.com/hsf-training/PyHEP-resources), a page of Python-focused training resources.

{% assign schools = site.data.training-schools | sort:"date" %}

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}

## Current and Upcoming Training Schools
#### **Warning** : Application deadlines are **before the date shown**
{% for post in schools %}
  {% capture date %}{{post.end_date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
  {% endif %}
{% endfor %}

#### For full list of Upcoming and Past Schools enter [here](/Schools/events.html)

---

Former Convenors:
- Dario Menasce (INFN)
