---
title: GSoC 2017 in ROOT
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "ROOT" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}