---
title: Training
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/training.html
  - /activities/training.html
  - /training/
  - /training/index.html
excerpt: none
---

The HSF Training Working Group aims to help the research community to provide training in the computing skills needed for researchers to produce high quality and sustainable software. The group works with experiment training groups, HEP initiatives (such as [IRIS-HEP](https://iris-hep.org/) and [FIRST-HEP](https://first-hep.org/)) and organisations like [Software Carpentry](https://software-carpentry.org/) to coordinate training activities.

The group aims to develop a training program that can be pursued by researchers to achieve the level of required knowledge. This ranges from basic core software skills needed by everyone to the advanced training required by specialists in software and computing.

## Sitemap

* I'm a student and want to **learn** about HEP Software:
  * [The HSF training curriculum](/training/curriculum.html)
  * [List of upcoming training events](/Schools/events.html)
* I want to **teach** software:
  * Training events:
    * [How to organize a software training event](/training/howto-event.html)
    * [The different roles in an HSF-training event](/training/educators.html)
  * Training modules:
    * [The HSF training curriculum](/training/curriculum.html)
    * [Guidelines for HSF training content](/training/module-guidelines.html)
    * [How to create a HSF training module from scratch](/training/howto-new-module.html)
    * [How to update a carpentry-style module with the HSF style](/training/howto-update-module-style.html)
* I want to learn more **about the HSF Training WG**:
  * [Our mission](/workinggroups/training.html#our-mission)
  * [HSF training White paper](https://arxiv.org/abs/1807.02875)
  * [List of HEP training events](https://indico.cern.ch/category/11386/)
  * The Community
    * [The HSF training community](/training/community.html)
    * [Participating & Contributing](/workinggroups/training.html#how-to-participate-and-contribute)
    * [Convenors](/workinggroups/training.html#convenors)
* **Meta**:
  * [How to add your profile to the HSF training community pages](/training/howto-educator-profile.html)

## Our mission

The long term sustainability of the research software ecosystem is important for HEP as [HL-LHC](https://home.cern/science/accelerators/high-luminosity-lhc) and other facilities of the 2020s will be relevant through at least the 2030s. Meeting this challenge requires a workforce with a combination of HEP domain knowledge and advanced software skills.

The software skills required fall into two groups. Nearly all researchers need basic programming skills (Python, C++), basic software engineering skills (Unix, git/GitHub/GitLab, continuous integration, performance evaluation), and skills in the core data tools in HEP (e.g., the [ROOT data format and analysis framework](https://root.cern.ch/)).

More advanced training is then needed (with domain examples!) in parallel programming, efficient software implementations, performance optimization, and machine learning and data science tools. A workforce trained in this range of software skills is the critical ingredient from which the solutions to the computing challenges can grow.

Today's graduate students will be the young faculty members driving HEP research in the 2020s. Investing in their software skills is not only important to actually build the requisite software infrastructure, but will also change community norms, create role models and promote career paths for computational scientists within the HEP research community. Computation is a central element of 21st century science, and clearer career paths will provide a virtuous cycle of feedback to enhance the vibrancy of the training and workforce development activities.

<div style="text-align:center; padding:25px; float:center">
<img src ="/images/training/training-pyramid.png" alt="HSF Training Pyramid" />
</div>

## How to participate and contribute?

Everybody is welcome to join the [forum](https://groups.google.com/forum/#!forum/hsf-training-wg) dedicated to HSF training activities. This is the place where ideas and proposals are discussed and actions decided! 

Weekly meetings are usually held at 16h00 CERN time on Mondays. Everyone is welcomed to discuss! Check [Indico](https://indico.cern.ch/category/11294/) for details.

We are always looking for volunteers from the community to help us with our training events. [This page](/training/educators.html) lists the different roles that you can take. We have also prepared [recommendation for organizing your own workshop](/training/howto-event.html).

## Towards a full HEP Software Curriculum

Our long term goal is to compile standardized HEP Software training modules into a full curriculum. More about this project can be found [here](/training/curriculum.html).

## Github Organization

The [HSF-Training GitHub Organization](https://github.com/hsf-training) hosts the training modules from our [HEP software curriculum](/training/curriculum.html). It also has [Analysis Essentials](https://hsf-training.github.io/analysis-essentials/), a course on basic computing required for HEP, and [PyHEP resources](https://github.com/hsf-training/PyHEP-resources), a page of Python-focused training resources.

## The community

The HSF training group relies on a growing list of proactive and dedicated educators that help us with our mission. Head to [this page](/training/community.html) to meet them!

## Current and Upcoming Training Schools

{% assign schools = site.data.training-schools | sort:"date" %}

{% capture now %}{{'now' | date: '%s' }}{% endcapture %}

{% for post in schools %}
  {% capture date %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if date > now %}
  {% if post.deadline != blank %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} - **Deadline:** {{post.deadline| date: "%-d %b %Y"}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %}

    {% else %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %}

    {% endif %}
    {% endif %}
{% endfor %}

[**Full list of Upcoming and Past Schools**](/Schools/events.html)

## Convenors

Kilian Lieret (LMU), Sudhir Malik (Puerto Rico), Sam Meehan (CERN)

{% assign persons = "Kilian Lieret, Sudhir Malik, Sam Meehan" | split: ", " %}
{% include list_of_selected_training_people.html %}

---

Former Convenors:
- Dario Menasce (INFN Milano)
