---
title: "HSF Training Modules"
layout: plain
---

<table>
<tr>
    <th>
        ID
    </th>
    <th>
        Name
    </th>
    <th>
        Description
    </th>
    <th>
        Status
    </th>
    <th>
    </th>
    <th>
    </th>
    <th>
    </th>
</tr>
{% for module in site.data.training-modules %}
<tr>
<td>
    {{ module.id }}
</td>
<td>
    {{ module.name }}
</td>
<td>
    {{ module.description }}
</td>
<td>
    {{ module.status }}
</td>
<td>
    {% unless module.webpage == "" %}
    <a href="{{ module.webpage }}">Webpage</a>
    {% endunless %}
</td>
<td>
    {% unless module.videos == "" %}
    <a href="{{ module.videos }}">Videos</a>
    {% endunless %}
</td>
<td>
    {% unless module.repository == "" %}
    <a href="{{ module.repository }}">Repo</a>
    {% endunless %}
</td>
</tr>
{% endfor %}
</table>
