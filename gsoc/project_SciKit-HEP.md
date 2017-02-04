---
title: GSoc 2017 in SciKit-HEP
layout: plain
---

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "SciKit-HEP" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
