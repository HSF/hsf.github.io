{% assign schools = site.data.training-schools | sort:"date" %}
{% capture now %}{{'now' | date: '%s' }}{% endcapture %}
{% for post in schools reversed %}
  {% capture date %}{{post.end_date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <a href="/training/our-events.html" title="Organized/supported by HSF"><span class="badge badge-success">{{ tag }}</span></a> {% endfor %}
  {% endif %}
{% endfor %}
