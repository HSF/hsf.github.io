---
title: "HSF Weekly Meetings"
layout: default
---

# HSF Weekly Meetings

## Meeting Minutes

The coordination team runs a regular HSF meeting (nominally, and usually, weekly) which is open to all.
Meeting announcements and minutes are posted to the HSF forum Google group.
Activity groups also hold their own meetings, for which minutes are usually posted here.

Please see [this page]({{ site.baseurl }}/future-events.html) for future meetings and events.

{:.table .table-hover .table-condensed .table-striped}
| Date   | Title      |
| ------ | ---------- |
{% for post in site.categories.organization %} | {{ post.date | date: "%d-%m-%Y" }} | [ {{ post.title }} ]( {{ post.url }} ) |
{% endfor %}
