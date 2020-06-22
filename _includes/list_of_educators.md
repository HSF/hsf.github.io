<ul>
  {% for post in site.educators | sort:"title" %}
  {% assign nroles = post.roles.size %}
  {% if nroles >= 1 %}
    <li>
    	<a href="{{post.url}}">{{ post.title }}</a>
    	{% for role in post.roles %}
    		<span class="badge badge-secondary">{{ role }}</span>
    	{% endfor %}
		{% if post.twitter %}<a href="https://twitter.com/{{ post.twitter }}">twitter</a>{% endif %}
		{% if post.github %}<a href="https://github.com/{{ post.github }}">github</a>{% endif %}
		{% if post.orcid %}<a href="https://orcid.org/{{ post.orcid }}">orcid</a>{% endif %}
    </li>
  {% endif %}
  {% endfor %}
</ul>
