---
title: "HSF Training Modules"
layout: plain
---
This table of the HSF training modules is mostly meant for administrative purposes.
If you're a student and want to discover our training content, go [here](/training/curriculum.html).

<div class="training">
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
</div>