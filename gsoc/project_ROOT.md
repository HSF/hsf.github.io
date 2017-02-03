---
title: GSoC 2017 in ROOT
layout: plain
---
[ROOT](http://root.cern.ch) is a modular scientific software framework developed by [CERN](http://cern.ch) and other Particle Physics laboratories. 
It was originally designed for particle physics data analysis, but it is also used in other applications such as astronomy, bio-informatics, finances, etc.
It provides all the functionalities needed to deal with big data processing, statistical analysis, data visualisation and data storage.
It is mainly written in C++ but integrated with other languages such as Python and R.

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "ROOT" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}