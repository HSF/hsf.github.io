---
title: "CERN in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at CERN

## Project Proposals

{:.table .table-hover .table-striped}
| Project | Title      |
| ------  | ---------- |
{% for post in site.categories.gsoc %}{% if post.organization == "CERN" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{site.baseurl}}/{{ post.url }} ) | {% endif %} {% endfor %}