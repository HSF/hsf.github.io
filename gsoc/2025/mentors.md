---
title: Summary of Mentors GSoC 2025
layout: plain
---

**Note for contributors:** entries must be sorted in **last name** alphabetic order

{% assign all_mentors = "" %}

<!-- Initialize an empty string to store unique mentors -->
{% assign unique_mentors = "" %}

<!-- Loop through all pages and collect mentors with unique emails -->
{% for page in site.gsocproposals %}
  {% if page.layout == 'gsoc_proposal' and page.year == 2025 and page.project_mentors %}
    {% for mentor in page.project_mentors %}
      {% assign mentor_info = mentor.name | append: "," | append: mentor.email | append: "," | append: mentor.organization %}

      {% unless unique_mentors contains mentor.email %}
        {% assign unique_mentors = unique_mentors | append: mentor_info | append: "|" %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

<!-- Split the mentors into an array -->
{% assign mentor_array = unique_mentors | split: "|" %}


<!-- Create an array of mentor objects with last name as the sorting key -->
{% assign mentor_objects = "" %}
{% for mentor in mentor_array %}
  {% assign mentor_details = mentor | split: "," %}
  {% assign full_name = mentor_details[0] %}
  {% assign first_name = full_name | split: " " | first %}
  {% assign last_name = full_name | split: " " | last %}
  {% assign mentor_objects = mentor_objects | append: last_name | append: "," | append: first_name | append: "," | append: mentor_details[1] | append: "," | append: mentor_details[2] | append: "|" %}
{% endfor %}

<!-- Sort mentors by last name -->
{% assign sorted_mentors = mentor_objects | split: "|" | sort %}

<ul>
  {% for mentor in sorted_mentors %}
    {% assign mentor_details = mentor | split: "," %}
    <li>
      <strong>{{ mentor_details[0] }} {{ mentor_details[1] }}</strong> 
      - <a href="mailto:{{ mentor_details[2] }}">{{ mentor_details[2] }}</a> - {{ mentor_details[3] }}
    </li>
  {% endfor %}
</ul>

