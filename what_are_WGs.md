---
title: "What are working groups?"
author: "Benedikt Hegner"
layout: default
---

# Working Groups

Working Groups can be ad-hoc formed groups of people interested in
tackling a problem together
as well as by the HSF setting strategic directions.
If you want to form a working group or want to put some community-wide
activity under the umbrella of the HSF,
just contact the
[HSF coordination team](mailto:hsf-coordination@googlegroups.com) and we will
announce your activities here.

Working Groups will be added to the activities listing of the HSF,
can add material to the website and can have a dedicated mailing list
and Indico category.

<ul class="list">
{% for wg in site.workinggroups %}
  <li> <a href="{{ wg.url }}">{{ wg.title }}</a></li>
{% endfor %}
</ul>
