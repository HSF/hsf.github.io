---
layout: plain
title: HEP Software Training Events
---

To add an event to this list, follow the instructions [on this page]({{site.baseurl}}/howto-website.html) ("Adding a training event").

{% capture list_of_upcoming_schools %}{% include list_of_upcoming_schools.md %}{% endcapture %}
{% capture test %}{{ list_of_upcoming_schools | strip }}{% endcapture %}
{% if test  != "" %}
## Current and Upcoming Training Events

{{ list_of_upcoming_schools }}
{% endif %}

## Past Events

{% include list_of_past_schools.md %}
