---
title: "Fermilab in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at Fermilab

## Project Proposals

{:.table .table-hover .table-striped}
| Project | Title      |
| ------  | ---------- |
{% for post in site.categories.gsoc %}{% if post.organization == "Fermilab" %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{ post.url }} ) | {% endif %} {% endfor %}