---
title: GSoC 2017 in Pythia
layout: plain
---
[Pythia](http://home.thep.lu.se/Pythia/) is the most widely used Monte Carlo event generator in particle physics. 

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "Pythia" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
