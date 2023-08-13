---
title: Summary of GSoC 2023 Proposals
layout: plain
year: 2023
---

[Click here for an overview of the GSoC program at
HSF.]({{ site.baseurl }}/activities/gsoc.html)

## Full List of Proposals

{:.table .table-hover .table-striped}
{% assign sorted_proposals = site.gsocproposals | sort: 'title' %}
{% for proposal in sorted_proposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}
{%- assign strings = proposal.url | split: '/' -%}
{%- assign proposal_year = strings[2] | plus: 0 -%}
{%- if proposal_year == page.year %} | [ {{ proposal.title }} ](
{{ proposal.url }} ) | {%- endif -%} {% endfor %}
