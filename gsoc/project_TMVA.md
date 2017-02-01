---
title: GSoC 2017 in TMVA
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "TMVA" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}