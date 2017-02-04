---
title: GSoC 2017 in FALCON
layout: plain
---
## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "FALCON" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
