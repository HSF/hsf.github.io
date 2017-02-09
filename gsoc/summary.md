---
title: Summary of GSoC 2017 Projects and Supervisors
layout: plain
---

## Full List of Proposals

{:.table .table-hover .table-striped}
{% assign sorted_proposals = site.gsocproposals | sort: 'title' %}
{% for proposal in sorted_proposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}[ {{ proposal.title }} ]( {{ proposal.url }} ) |
{% endfor %}