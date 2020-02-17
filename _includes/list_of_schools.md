

{% assign schools = site.data.training-schools | sort:"date" %}

{% capture now %}{{'now' | date: '%s' }}{% endcapture %}

## Current and Upcoming Training Schools
#### **Warning** : Application deadlines are **before the date shown**
{% for post in schools %}
  {% capture date %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if date > now %}
  {% if post.deadline != blank %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} - **Deadline:** {{post.deadline | date: "%-d %b %Y"}} ]({{post.source}})
  {% else %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
  {% endif %}
  {% endif %}
{% endfor %}

## Past Schools
{% for post in schools reversed %}
  {% capture date %}{{post.end_date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
  {% endif %}
{% endfor %}
