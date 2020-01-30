---
title: "What are activity areas?"
author: "Graeme Stewart"
layout: default
---

# Activity Areas and Interest Groups

HSF Activity Areas and Interest Groups are led by enthusiasts and
advocates for a particular area of work or of technology
interest and provide a focal point for organising dicussions
in the HEP community. They can also cover engagement with
external projects, like Google's Summer of Code.

They are less formal, in the HSF, than [working groups](/what_are_WGs.html)
and any relevant and reasonable activity for HEP can spawn
an interest group. If you want to put some community-wide
activity under the umbrella of the HSF as an activity areas or interest group
just contact the
[HSF coordination team](mailto:hsf-coordination@googlegroups.com).

Activity areas are added to the website of the HSF, with 
description and contact information and will have a dedicated mailing list
and, if appropriate, an Indico category.

<ul class="list">
{% for activity in site.activities %}
  <li> <a href="{{ activity.url }}">{{ activity.title }}</a></li>
{% endfor %}
</ul>
