---
title: "CERN in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at CERN

## Project Proposals

{:.table .table-hover .table-striped}
{% for post in site.categories.gsoc %}{% if post.organization == "CERN" %} | [ {{ post.title }} ]( {{ post.url }} ) | {% endif %} 
{% endfor %}