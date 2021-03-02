---
title: Season of Docs 2020 Technical writer blogs
layout: plain
year: 2020
---

{% assign sorted_blogs = site.gsdocs-blogs | sort: 'title' %}
{% for blog in sorted_blogs %}
{%- if blog.year == page.year %}
{% assign blog_intro = blog.intro | strip_newlines | markdownify %}
<H2>
<table class="table table-hover table-striped">
  <tbody>

  <tr>
    <td><img src="/images/{{ blog.logo }}" alt="{{ blog.project }}" width="100px"></td>
    <td>{{ blog.title }}</td>
  </tr>
  </tbody>
</table>
</H2>
<p style="text-align: right; font-weight: bold;"> by {{ blog.author }}</p>

{{blog_intro}}

[ Read more ... ]( {{ blog.url }} )
<hr>
{%- endif -%}
{% endfor %}
