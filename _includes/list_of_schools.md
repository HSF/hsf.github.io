

{% assign schools = site.categories.Schools | sort:"date" %}
{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}


## Current and Upcoming Training Schools
#### **Warning** : Application deadlines are **before the date shown**
{% for post in schools %}
  {% capture postdate %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if postdate > nowunix %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
  {% endif %}
{% endfor %}

## Past Schools
{% for post in schools reversed %}
  {% capture postdate %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if postdate < nowunix %}
  1. [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}})
  {% endif %}
{% endfor %}
