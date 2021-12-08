---
title: "What are working groups?"
author: "Graeme Stewart"
layout: default
---

# Working Groups

HSF Working Groups are community led groups that organise activities
in particular domains with the aims of increasing communication
between developers, providing a platform for discussion of interesting
problems and novel solutions developments, and fostering the adoption
of common software between different communities.

Working groups have three conveners, to help share the workload, and
are appointed by the HSF (via an open nomination process and a search
committee) to serve for one year, with renewal possible by mutual
agreement. (In contrast, [interest groups and activity areas]({{ site.baseurl }}/what_are_activities.html)
are less formal.)

We strive for a diverse representation in the HSF working groups, so having
multiple conveners from the same experiment is very strongly discouraged.

If you want to form a working group, or want to put some community-wide
activity under the umbrella of the HSF,
just contact the
[HSF coordination team](mailto:hsf-coordination@googlegroups.com).

Working Groups are added to the website of the HSF, with 
description and contact information, and their own
[Indico category](https://indico.cern.ch/category/7972/).

<ul class="list">
{% for wg in site.workinggroups %}
  <li> <a href="{{ wg.url }}">{{ wg.title }}</a></li>
{% endfor %}
</ul>

## Being an HSF Working Group Convener

The HSF is extremely grateful to members of the community who take on the role
of convener in the working groups - *thank you*. Each working group engages
with a different subset of the developer and physics community and thus the
exact pattern of activities that are organised can vary. It is delegated to the
conveners to decide the way to organise so that it best serves the needs in
HEP software and computing as required. That said, organising an event every
4 to 6 weeks is usually a good cadence, although sometimes a series of related
events might happen bunched together more tightly, e.g., looking at one
specific topic from the point of view of several experiments.

HSF Working Group meetings in general should try to:

- be there to help encourage the exchange of ideas and techniques
- do not need to focus on "finished" items, but rather can be there
  to provide a community forum for unsolved problems
- should ensure there is plenty of time for discussion
- should take notes or minutes for important discussion points (attaching these
  to Indico is recommended)

We strongly encourage the use of common software in the HSF and opportunities
for common development and sharing should be seized when they exist. The HSF
exists as a [GitHub organisation](https://github.com/HSF) and is happy
to host projects to help them grow. This can include things like common
datasets used in development as well as actual code.

One focus that we encourage is to organise events together with other
groups, e.g., a special session at a workshop, a joint meeting with
a software development project, a cross-cutting topic that bridges
more than one HSF working group (our working groups are not intended to 
be silos). These meetings are excellent for bringing together
people that might not normally talk or know each other.

Our working group conveners should usually dedicate between 5% and 10% of their
time to running the working group. More than 10% is great, but we recognise
that people are busy with many other tasks. Less than 5% and the working group
can fall into an inactive state. Conveners should meet at least once a month to
plan. The HSF Coordination Group is always happy to attend to give feedback
and suggestions.

At least one of the working group conveners should attend the bi-weekly
[HSF Coordination Meetings](https://indico.cern.ch/category/7970/) and
give a short update on the group's recent and forthcoming activities.

When the HSF organises [workshops](https://indico.cern.ch/category/7971/)
working group conveners can give input to the organising team. If there
will be a session dedicated to the activities of any working group then
conveners will be asked to co-organise it.

### Recording Meetings and Minutes

In general, recording *is appropriate* for HSF meetings, which are there to
foster discussion and collaboration, so *we do recommend it*. There are a lot of
meetings and we have a worldwide community, so not everyone who is interested
can join a meeting and recordings can help people to catch-up.

However, you need to make it very clear with the speakers and to participants that:

- The meeting is being recorded and will be made public;
- And where the video will be posted ([YouTube]({{site.baseurl}}/organization/youtube.html), [CDS](http://cds.cern.ch/record/2289430), etc.);
  - Note that it is strongly recommended not to add video files directly into Indico, instead post a link to CDS.

In any case, *please also make sure that meetings are minuted in a concise way*
(it’s not always the case that people have the time to watch the 60 minute
video and they need a shorter summary). Minutes can be posted directly onto
Indico (easy) or to the [HSF website]({{site.baseurl}}/howto-website.html) (via a PR).
