---
title: Season of Docs 2020 Technical writer blogs
layout: plain
year: 2020
---

{% assign sorted_blogs = site.gsdocs-blogs | sort: 'title' %}
{% for blog in sorted_blogs %}
{%- if blog.year == page.year %}
{% assign blog_intro = blog.intro | strip_newlines | markdownify %}
<div class="blog-header" style="text-align: left">
  <div class="row">
    <div class="col-md-2">
      <img src="{{ site.baseurl }}/images/{{ blog.logo }}" alt="{{ blog.project }}" width="100px">
    </div>
    <div class="col-md-8">
      <h1>{{ blog.title }}</h1>
    </div> 
    <div class="col-md-2" style="text-align: right;">
      {% if blog.photo %}
      <img src="{{ site.baseurl }}/images/{{ blog.photo }}" alt="{{ blog.author }}" width="100px">
      {% endif %}
      <p style="font-weight: bold;"> by {{ blog.author }}</p> 
    </div>
  </div>
</div>
{{blog_intro}}

[ Read more ... ]( {{ blog.url }} )
<hr>
{%- endif -%}
{% endfor %}
