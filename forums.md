---
title: "HSF Lists and Forums"
author: "Benedikt Hegner"
layout: default
---

# Discussion Forums

Discussions and activities in the HEP Software Foundation rely on several mailing lists and forums, some of them for general discussions, others for topical ones. All these forums are open to anybody interested and archives are publicly available but they generally require that you register in order to participate.

*Most of these forums are hosted by Google Groups. To register to them with your preferred email, simply send a mail to
`forum_name+subscribe@googlegroups.com` (with `forum_name` replaced by the actual name, e.g. `hsf-tech`): subject and contents
are ignored and can be empty. If you want to register with your Google account, you can also use the web page associated with the forum
(see below).*


## General Discussion Forums
-----

### General Information about HSF: hsf-forum@googlegroups.com

The [hsf-forum](http://groups.google.com/d/forum/hsf-forum) is the general announcement and discussion forum for the HSF. Our meeting announcements are posted here, as are meeting minutes. The forum is intended for discussion, not just announcements. And everybody interested into the HSF, even though it is only for specific topic, is encourage to register to this forum to get all announcements.

### HSF Technical Forum: hsf-tech-forum@googlegroups.com

The [hsf-tech-forum](https://groups.google.com/forum/#%21forum/hsf-tech-forum) is the general open forum for technical discussions on HEP Software Foundation topics (e.g., software tools or experiment frameworks). Anyone subscribing here should be prepared for technical emails, so posters should not be shy about posting technical issues. Topics can be forked off to dedicated forums as appropriate.

### HEP S&C community mailing list: hep-sw-comp@googlegroups.com

This is not strictly an HSF mailing list. The [HEP S&C community mailing list](http://groups.google.com/d/forum/hep-sw-comp) is intended for occasional HEP software and computing community mailings. Everyone involved or interested in HEP S&C is encouraged to sign up to this list. It will be used for occasional mailings of community wide interest, such as announcements of HEP S&C conferences, workshops and schools not strictly related to the HSF.


## Dedicated Activity Areas
-----

Each of the HSF Activity Areas maintains a dedicated page where contact
information for that group can be found:

<ul class="list">
{% for activity in site.activities %}
  <li> <a href="{{ activity.url }}">{{ activity.title }}</a></li>
{% endfor %}
</ul>
