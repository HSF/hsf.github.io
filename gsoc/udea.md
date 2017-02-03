---
title: "University of Antioquia in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals at UdeA

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "UdeA" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
