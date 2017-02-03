---
title: "Cornell University in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals at Cornell University

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "Cornell" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
