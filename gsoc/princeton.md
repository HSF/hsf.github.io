---
title: "Princeton University in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals at Princeton University

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "Princeton" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
