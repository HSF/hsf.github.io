---
title: "Fermilab in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at SLAC

## Project Proposals

{:.table .table-hover .table-striped}
{% for post in site.categories.gsoc %}{% if post.organization == "SLAC" %} | [ {{ post.title }} ]( {{site.baseurl}}/{{ post.url }} ) | {% endif %} 
{% endfor %}