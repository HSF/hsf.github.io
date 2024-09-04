---
title: "What are activity areas?"
author: "Graeme Stewart"
layout: default
redirect_from: 
  - /what_are_WGs.html
---

# HSF Activities

HSF activities are focused mainly on community led groups that organise around
particular domains with the aim of increasing communication between developers,
providing a platform for discussion of interesting problems and novel solutions
developments, and fostering the adoption of common software between different
communities.

Activity areas have multiple conveners (typically three), to help share the
workload, and are appointed by the HSF (via an open nomination process and a
search committee) to serve for one year, with renewal possible by mutual
agreement. We have a [guide]({{ site.baseurl }}/activity-coordination.html) for
conveners about how to organise activities.

We strive for a diverse representation amongst the conveners and a broad
representation of experiments.

If you want to put some community-wide activity under the umbrella of the HSF,
just contact the [HSF Steering Group](mailto:hsf-steering@googlegroups.com) with
your proposal.

Activities are added to the website of the HSF, with description and contact
information, and their own [Indico
category](https://indico.cern.ch/category/7972/).

<ul class="list">
{% for act in site.activities %}
  <li> <a href="{{ act.url }}">{{ act.title }}</a></li>
{% endfor %}
</ul>

## Archive

The HSF has had a number of activities in the past which are no longer active,
but are kept for reference:

<ul class="list">
{% for act in site.activities-archive %}
  <li> <a href="{{ act.url }}">{{ act.title }}</a></li>
{% endfor %}
</ul>
