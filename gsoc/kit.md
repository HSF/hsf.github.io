---
title: "Karlsruhe Institute of Technology in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals at KIT

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "KIT" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
