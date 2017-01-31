---
title: GSoC 2017 in ROOT
layout: plain
---

## Project Proposals

{:.table .table-hover .table-condensed .table-striped}
| Project   | Title      |
| ------ | ---------- |
{% for post in site.categories.gsoc %} {% if post.project == "TMVA" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ](  {{site.baseurl}}/{{ post.url }} ) |{% endif %}
{% endfor %}