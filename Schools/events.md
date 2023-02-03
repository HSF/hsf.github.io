---
layout: plain
title: HEP Software Training Events
---

{% capture list_of_upcoming_schools %}{% include list_of_upcoming_schools.md %}{% endcapture %}
{% if list_of_upcoming_schools != "" %}
  ## Current and Upcoming Training Events

  {{ list_of_upcoming_schools }}
{% endif %}

## Past Events

{% include list_of_past_schools.md %}
