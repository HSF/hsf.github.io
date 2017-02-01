---
title: GSoC 2017 in Geant4
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.pages %}{% if page.categories contains 'gsocproposal' and page.project == "Geant4" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %} 
{% endfor %}