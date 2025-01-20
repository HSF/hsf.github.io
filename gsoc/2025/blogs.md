---
title: HSF student pages for GSoC 2025
layout: plain
year: 2025
---

{% assign sorted_blogs = site.gsocblogs | sort: 'title' %}
{% for blog in sorted_blogs %}
{%- if blog.year == page.year %}
{% assign blog_intro = blog.intro | strip_newlines | markdownify %}
<div class="blog-header" style="text-align: left">
  <div class="row">
    <div class="col-sm-2">
      <img src="/images/{{ blog.logo }}" alt="{{ blog.project }}" width="80px">
    </div>
    <div class="col-sm-7" style="text-align: left;">
      <h2>{{ blog.title }}</h2>
    </div> 
    <div class="col-sm-3" style="text-align: center;">
      {% if blog.avatar %}
      <img src="{{ blog.avatar }}" alt="{{ blog.author }}" width="100px">
      {% else %}
        {% if blog.photo %}
        <img src="/images/{{ blog.photo }}" alt="{{ blog.author }}" width="100px">
        {% endif %}
      {% endif %}
      <p style="font-weight: bold; text-align: center; font-style: oblique;"> {{ blog.author }}</p> 
    </div>
  </div>
</div>
{{blog_intro}}

[ <span style="color:blue">Read more ...</span> ]( {{ blog.url }} )
<hr>
{%- endif -%}
{% endfor %}
