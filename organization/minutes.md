---
title: "HSF Weekly Meetings"
layout: default
---

# HSF Weekly Meetings

## Meeting Minutes

The startup team runs a regular HSF meeting (nominally, and usually, weekly) which is open to all. Meeting announcements and minutes are posted to the HSF forum google group. Activity groups also hold their own meetings, for which minutes are usually posted here.

Please see [this page](future-events.html) for future meetings and events.

{:.table .table-hover .table-condensed .table-striped}
| Date   | Title      |
| ------ | ---------- |
{% for post in site.categories.organization %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{ post.url }} ) |
{% endfor %}
