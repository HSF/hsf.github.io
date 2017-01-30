---
title: GSoC 2017 in ROOT
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
| Project | Title      |
| ------  | ---------- |
{% for post in site.categories.gsoc %}{% if post.project == "ROOT" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{ post.url }} ) | {% endif %} {% endfor %}