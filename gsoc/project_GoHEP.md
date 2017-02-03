---
title: GSoC 2017 in Go-HEP
layout: plain
---
[go-hep](https://go-hep.org) is a set of libraries and applications written in [Go](https://golang.org).
`go-hep` aims to provide robust, modular, easy to read and easy to install libraries for the HEP, astro-physics and cosmology communities.

## Project Proposals

{:.table .table-hover .table-striped}
{% for page in site.gsocproposals %}{% if page.project == "GoHEP" %} |[ {{ page.title }} ]( {{ page.url }} ) | {% endif %}
{% endfor %}
