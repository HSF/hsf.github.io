---
title: Summary of Season of Docs 2019 Projects and Supervisors
layout: plain
year: 2019
---

## Full List of Proposals

{:.table .table-hover .table-striped}
{% assign sorted_proposals = site.gsdocs-proposals | sort: 'title' %}
{% for proposal in sorted_proposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}
{%- assign strings = proposal.url | split: '/' -%}
{%- assign proposal_year = strings[2] | plus: 0 -%}
{%- if proposal_year == page.year %}
| [ {{ proposal.title }} ]( {{ proposal.url }} ) |
{%- endif -%}
{% endfor %}
