---
title: "Fermilab in GSoC"
author: "Benedikt Hegner"
layout: default
---
# Project Proposals at SLAC

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if post.organization == "SLAC" %} | [ {{ page.title }} ]( {{site.baseurl}}/{{ page.url }} ) | {% endif %}
{% endfor %}