---
title: GSoC 2017 in CMS
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "CMS" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}