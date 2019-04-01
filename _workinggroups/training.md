---
title: Training
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/training.html
  - /activities/training.html
---

The HSF Training & Tutoring initiative is aimed at helping the research community (in various disciplines) to bridge the gap in computing skills existing nowadays between University level courses and what is required by scientist to produce high quality, sustainable software.

## Github Organization

The [HSF-Training GitHub Organization](https://github.com/hsf-training) has [Analysis Essentials](https://hsf-training.github.io/analysis-essentials/), a course on basic computing required for HEP, and [PyHEP resources](https://github.com/hsf-training/PyHEP-resources), a page of Python-focused training resources.

## WikiToLearn - collaborative textbooks

To achieve this goal, we adopted an already existing and successful platform. [WikiToLearn](http://en.wikitolearn.org/Main_Page). Originally developed in Italy, it was intended to allow University students to deploy our tutoring in software. It has now a growing usage also outside Italy.

The basic principle of this initiative is that researchers can seldom afford to spend time writing down training material. The same applies for professors when it comes to transcribing their courses for the benefit of students in general. On the other hand, students often take notes during lessons or during their own academic research. The goal of the platform is to make easy for them to publish these notes and reports in a publicly visible site.

WikiToLearn is a wikimedia-based content management system, pretty much like Wikipedia, were anybody can add new material or complete already existing one. To strengthen the quality of published material, scientists and researches can furthermore sign a particular version to enhance it's quality level. The platform is currently officially backed by Wikimedia and the KDE organization, and has received support from the University of Milano-Bicocca and the University of Pisa.

Under the category 'Physics/Software', WikiToLearn now has a [branch](http://it.wikitolearn.org/Main_HSF_Page) dedicated to the HSF effort. We plan, in the coming months, to recruit as many volunteers as possible to publish there training material in various software domains relevant to HSF.


## Other training activities in HSF

Many ideas are being discussed and are tracked down in the HSF training and education [notebook](https://docs.google.com/document/d/1E85vhzgFs37VOlTC6XTqvQOOmLEgAvamyvl4Iz-Sqm4/edit#heading=h.pstok39wu9vm).

Other actions in progress include:

* A [Training section](http://hepsoftware.org/e/training) in the HSF knowledge base intended to collect training related events, organizations, software packages... **Please contribute to the knowledge base to help enriching the content**

### Upcoming Training Schools
 **Warning** : Application deadlines are **before the date shown**
{% assign sorted = site.categories.Schools | sort:"date" %}

{% for post in sorted limit:20 %}
{% if post.date > site.time %}
1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
{% endif %}
{% endfor %}

### Past Schools
{% assign past = site.categories.Schools | sort:"date" | reverse %}

{% for post in past limit:20 %}
{% if post.date < site.time %}
1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
{% endif %}
{% endfor %}

 For full list of Upcoming and Past Schools enter [here](/Schools/events.html)


## How to participate ?

Everybody is welcome to join the [forum](https://groups.google.com/forum/#!forum/hsf-training-wg) dedicated to HSF training activities. This is the place where ideas and proposals are discussed and actions decided!
