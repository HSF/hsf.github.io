---
title: Summary of Mentors GSoC 2025
layout: plain
---


{% assign unique_mentors = "" %}

<!-- Loop through all pages and collect mentors with unique emails -->
{% for page in site.gsocproposals %}
  {% if page.layout == 'gsoc_proposal' and page.year == 2025 and page.project_mentors %}
    {% for mentor in page.project_mentors %}
      {% comment %}
      Build mentor info as:
      last_name,first_name,email,organization
      (last_name is first so that sorting works correctly)
      {% endcomment %}
      {% assign mentor_info = mentor.last_name | append: "," | append: mentor.first_name | append: "," | append: mentor.email | append: "," | append: mentor.organization %}
      {% unless unique_mentors contains mentor.email %}
        {% assign unique_mentors = unique_mentors | append: mentor_info | append: "|" %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

<!-- Split the mentors into an array and sort by last name -->
{% assign mentor_array = unique_mentors | split: "|" %}
{% assign sorted_mentors = mentor_array | sort %}

<ul>
  {% for mentor in sorted_mentors %}
    {% if mentor != "" %}
      {% assign mentor_details = mentor | split: "," %}
      <li>
        <strong>{{ mentor_details[1] }} {{ mentor_details[0] }}</strong> 
        - <a href="mailto:{{ mentor_details[2] }}">{{ mentor_details[2] }}</a> - {{ mentor_details[3] }}
      </li>
    {% endif %}
  {% endfor %}
</ul>


