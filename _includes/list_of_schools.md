

{% assign schools = site.data.training-schools | sort:"date" %}

{% capture now %}{{'now' | date: '%s' }}{% endcapture %}

## Current and Upcoming Training Schools
{% for post in schools %}
  {% capture date %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if date > now %}
  {% if post.deadline != blank %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} - **Deadline:** {{post.deadline | date: "%-d %b %Y"}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <span class="badge badge-success">{{ tag }}</span> {% endfor %}
  {% else %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <span class="badge badge-success">{{ tag }}</span> {% endfor %}
  {% endif %}
  {% endif %}
{% endfor %}

## Past Schools
{% for post in schools reversed %}
  {% capture date %}{{post.end_date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <span class="badge badge-success">{{ tag }}</span> {% endfor %}
  {% endif %}
{% endfor %}

## HSF only

{% for post in schools reversed %}
  {% capture date %}{{post.end_date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if post.tags contains "HSF" %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} 
  {% endif %}
  {% endif %}
{% endfor %}
