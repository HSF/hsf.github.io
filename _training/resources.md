---
layout: plain
title: "HSF Training Talks & Papers"
---

Additional material about us:

<div class="training">
    <table>
    <tr>
        <th>Date</th>
        <th>Type</th>
        <th>Title</th>
        <th>Note</th>
    </tr>
    {% assign material = site.data.training-material %}
    {% for m in material %}
    <tr>
        <td>{{m.date}}</td>
        <td>{{m.type}}</td>
        <td><a href="{{m.url}}">{{m.title}}</a></td>
        <td>{{m.note}}</td>
    </tr>
    {% endfor %}
    </table>
</div>