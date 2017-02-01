---
title: "CERN in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at CERN

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.pages %}{% if page.categories contains 'gsocproposal' and page.organization == "CERN" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %} 
{% endfor %}