---
title: GSoC 2017 in ROOT
layout: plain
---

## Project Proposals

{:.table .table-hover .table-condensed .table-striped}
{% for post in site.categories.gsoc %} {% if post.project == "TMVA" %} | [ {{ post.title }} ]( {{ post.url }} ) |{% endif %}
{% endfor %}