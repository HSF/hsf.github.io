{% assign schools = site.data.training-schools | sort:"date" %}
{% capture now %}{{'now' | date: '%s' }}{% endcapture %}
{% for post in schools %}
  {% capture date %}{{post.end_date | date: '%s' }}{% endcapture %}
  {% if date > now %}
  {% if post.deadline != blank %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} - **Deadline:** {{post.deadline | date: "%-d %b %Y"}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <a href="{{ '/training/our-events.html' | relative_url }}" title="Organized/supported by HSF"><span class="badge badge-success">{{ tag }}</span></a> {% endfor %}
  {% else %}
  * [**{{post.date | date: "%-d %b"}} - {{post.end_date | date: "%-d %b %Y"}}** - {{post.title}} ]({{post.source}}){% if post.url_proof_ignore %}{:data-proofer-ignore=""}{% endif %} {% for tag in post.tags %} <a href="{{ '/training/our-events.html' | relative_url }}" title="Organized/supported by HSF"><span class="badge badge-success">{{ tag }}</span></a> {% endfor %}
  {% endif %}
  {% endif %}
{% endfor %}
