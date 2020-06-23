<script src="{{ "/assets/js/lazysizes.min.js" | relative_url }}" async=""></script>

<link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>

<style>
.img-circle {
    border-radius: 50%;
    width: 128px;
    height: 128px;
}

.anchor-offset {
    padding-top: 50px;
    margin-top: -50px;
}



.team-member {
    margin-bottom: 50px;
    text-align: center;
}

.team-member img {
    margin: 0 auto;
    border: 7px solid #fff;
}

.team-member h4 {
    margin-top: 25px;
    margin-bottom: 0;
    text-transform: none;
}

.team-member p {
    margin-top: 0;
}

.list-inline {
    padding-left: 0;
    list-style: none;
    margin-left: -5px;
}

.list-inline>li {
    display: inline-block;
    padding-left: 5px;
    padding-right: 5px;
    font-size: 20px;
}

</style>


{% for person in site.educators | sort:"title" %}

{% assign nroles = post.roles.size %}


{% assign loopindex = forloop.index | modulo: 4 %}

{% if loopindex == 1 %}
<div class="row">
{% endif %}

<!-- to do delayed loading etc., see https://www.ratanparai.com/jekyll/Responsive-image-on-jekyll/ and then the original carpentries template -->

<div class="medium-3 columns">
<div class="team-member anchor-offset" id="{{ person.github }}">
  {% if person.github %}
  <img data-src="https://avatars.githubusercontent.com/{{ person.github }}" class="img-circle lazyload" alt="GitHub profile photo of {{person.title}}">
  {% else %}
  <img data-src="https://www.gravatar.com/avatar/{{ person.gravatar }}?d=mp" class="img-circle lazyload" alt="Gravatar profile photo of {{person.title}}">
  {% endif %}
  <h3>{{ person.title }}</h3>
  <ul class="list-inline social-buttons">
      {% if person.twitter %}<li> <a href="https://twitter.com/{{ person.twitter }}"> <i class="fab fa-twitter"></i> </a> </li> {% endif %}
      {% if person.github %}<li> <a href="https://github.com/{{ person.github }}"> <i class="fab fa-github"></i> </a> </li> {% endif %}
      {% if person.orcid %}<li> <a href="https://orcid.org/{{ person.orcid }}"> <i class="fab fa-orcid"></i> </a> </li> {% endif %}
      {% if person.url and person.url != "" %}<li> <a href="{{ person.url }}"> <i class="fas fa-link"></i> </a> </li> {% endif %}
  </ul>
  {% unless person.country == "" %}
  <!-- <img width="64" src="/files/flags/{{ person.country | downcase }}.svg"/> -->
  {% endunless %}
</div>
</div>


{% if loopindex == 0 %}
</div>
{% endif %}
{% endfor %}

