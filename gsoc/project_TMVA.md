---
title: GSoC 2017 in TMVA
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.pages %}{% if page.categories contains 'gsocproposal' and page.project == "TMVA" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %} 
{% endfor %}