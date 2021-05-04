---
title: "HSF Training Modules"
layout: plain
---

<style type="text/css">
  table {
    padding: 0;
    width: 100%;
  }
  table tr {
    border: 1px solid #cccccc;
    background-color: white;
    margin: 0;
    padding: 0;
  }
  table tr:nth-child(2n) {
    background-color: #f8f8f8;
  }
  table tr th {
    font-weight: bold;
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px;
  }
  table tr td {
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px;
  }
  table tr th :first-child, table tr td :first-child {
    margin-top: 0;
  }
  table tr th :last-child, table tr td :last-child {
    margin-bottom: 0;
  }
</style>

This table of the HSF training modules is mostly meant for administrative purposes.
If you're a student and want to discover our training content, go [here](/training/curriculum.html).

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
    <th>Links
    </th>
</tr>
{% assign modules = site.data.training-modules | sort:"id" %}
{% for module in modules %}
<tr>
<td>
    <code>{{ module.id }}</code>
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
    <a href="{{ module.webpage }}"><span class="glyphicon glyphicon-book"></span></a>
    {% endunless %}

    {% unless module.videos == "" %}
    <a href="{{ module.videos }}"><span class="glyphicon glyphicon-film"></span></a>
    {% endunless %}
    {% unless module.repository == "" %}
    <a href="{{ module.repository }}"><span class="glyphicon glyphicon-wrench"></span></a>
    {% endunless %}
</td>
</tr>
{% endfor %}
</table>
