---
title: GSoC 2017 in GeantV
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "GeantV" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
