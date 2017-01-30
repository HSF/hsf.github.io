---
title: GSoC 2017 in TMVA
layout: plain
---


## Project Proposals

{:.table .table-hover .table-condensed .table-striped}
| Project   | Title      |
| ------ | ---------- |
{% for post in site.categories.gsoc %} {% if post.project == "TMVA" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{ post.url }} ) |
{% endif %}
{% endfor %}