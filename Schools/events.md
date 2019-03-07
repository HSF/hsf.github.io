---
layout: plain
title: Schools for HSF Training
---
### Upcoming Training Schools
 **Warning** : Application deadlines are **before the date shown**
{% for post in site.categories.Schools reversed %}
{% if post.date > site.time %}
1. [{{post.title}} - {{post.date | date_to_string}}]({{post.source}})
{% endif %}
{% endfor %}

### Past Schools
{% for post in site.categories.Schools %}
{% if post.date < site.time %}
1. [{{post.title}} - {{post.date | date_to_string}}]({{post.source}})
{% endif %}
{% endfor %}
