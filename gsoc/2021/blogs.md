---
title: HSF student blogs for GSoC 2021
layout: plain
year: 2020
---

{% assign sorted_blogs = site.gsocblogs | sort: 'title' %}
{% for blog in sorted_blogs %}
{%- if blog.year == page.year %}
{% assign blog_intro = blog.intro | strip_newlines | markdownify %}
<div class="blog-header" style="text-align: left">
  <div class="row">
    <div class="col-md-2">
      <img src="/images/{{ blog.logo }}" alt="{{ blog.project }}" width="100px">
    </div>
    <div class="col-md-7" style="text-align: left;">
      <h1>{{ blog.title }}</h1>
    </div> 
    <div class="col-md-2" style="vertical-align: bottom;">
      {% if blog.photo %}
      <img src="/images/{{ blog.photo }}" alt="{{ blog.author }}" width="100px">
      {% endif %}
      <p style="font-weight: bold; text-align: center;"> by: {{ blog.author }}</p> 
    </div>
  </div>
</div>
{{blog_intro}}

[ Read more ... ]( {{ blog.url }} )
<hr>
{%- endif -%}
{% endfor %}
