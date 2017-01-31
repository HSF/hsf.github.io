---
title: GSoC 2017 in Geant4
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for post in site.categories.gsoc %}{% if post.project == "Geant4" %} | [ {{ post.title }} ]( {{ post.url }} ) | {% endif %} 
{% endfor %}