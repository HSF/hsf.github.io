---
title: "University of Bologna in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals by University of Bologna

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "UNIBO" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
