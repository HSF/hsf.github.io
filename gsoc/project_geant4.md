---
title: GSoC 2017 in Geant4
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
| Project | Title      |
| ------  | ---------- |
{% for post in site.categories.gsoc %}{% if post.project == "Geant4" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ](  {{site.baseurl}}/{{ post.url }} ) | {% endif %} {% endfor %}