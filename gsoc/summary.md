---
title: Summary of GSoC 2017 Projects and Supervisors
layout: plain
---

## Full List of Proposals

{:.table .table-hover .table-striped}
{% for proposal in site.gsocproposals %}{% capture u_proposal_org %}{{ organization | upcase }}{% endcapture %}[ {{ proposal.title }} ]( {{ proposal.url }} ) |
{% endfor %}