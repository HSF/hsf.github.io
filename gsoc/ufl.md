---
title: "University of Florida in GSoC"
author: "Omar Zapata"
layout: default
---
# Project Proposals at UFL

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.organization == "UFL" %} | [ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
