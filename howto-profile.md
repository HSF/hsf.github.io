---
title: "How to update your profile"
layout: plain
---
This page explains how to update or create a profile/"floating head" as e.g. shown on the [training community page]({{ site.baseurl }}/training/community.html).

## Basics

Your profile corresponds to a text file in the ``_profiles`` directory ([view on github](https://github.com/HSF/hsf.github.io/tree/master/_profiles)).

## If you don't have a profile yet

Simply copy the template at the bottom of this page and modify it to include your information. You can then either

* send it to the conveners via email, or
* (**preferred**) fork the github repository, put your profile in the ``_profiles`` directory as ``first_name_last_name.md`` (don't worry about the exact form of the name) and open a pull request.

## If you want to change your profile

Either

* Find your profile [on github](https://github.com/HSF/hsf.github.io/tree/master/_profiles) (``first_name_last_name.md``), copy it to a text file, make your modifications and send your new version to the conveners via email
* (**preferred**) fork the github repository, update your information in ``_profiles/first_name_last_name.md`` and open a pull request

## The template

```
{% include_relative _profiles/000_template.md %}
```

### Notes

* If you have specified your [gravatar](https://gravatar.com/) (a free service for global avatar synchornization), we will take your profile picture from there. Else, the profile picture will be taken from your [github](https://github.com) profile (if specified). If the latter is not specified either, you will have a blank profile picture showing an [octocat](https://en.wikipedia.org/wiki/GitHub#Mascot).
* If you don't know your gravatar email hash, you can [use this page](https://en.gravatar.com/site/check/) (or look [here](https://en.gravatar.com/site/implement/hash/) for more background information about the hashing)

### Activity Area specific settings

* To be listed as "educator" on the [training community page]({{ site.baseurl }}/training/community.html) or the [educators page]({{ site.baseurl }}/training/educators.html):
  * Set the `training_roles` field: Zero or more of `instructor`, `mentor`, `facilitator`, `author`. The first three ``training_roles`` are explained [here]({{ site.baseurl }}/training/educators.html). You are an `author` if you've made not-completely-trivial contributions to our training material. Valid examples: ``[]``, ``[instructor, mentor]``.  **Invalid**: ``mentor`` (no brackets).
  * Set the `training_years` field: This should be a list of years that you were actively contributing to the HSF Training efforts. Valid examples: `[2012]` , ``[2012, 2014]``. **Invalid**: ``["2012"]``.

### Example

```
{% include_relative _profiles/kilian_lieret.md %}
```

## If you want to include a specific selection of people on your page

Use this:

{% raw %}
```
{% assign persons = "Kilian Lieret, Sudhir Malik, Sam Meehan" | split: ", " %}
{% include list_of_selected_profiles.html %}
```
{% endraw %}

## FAQ

> I've added my profile, but it doesn't appear on the webpage

* The webpage takes a couple of minutes to update
* If you don't find yourself on the list of educators/training people, make sure that the ``training_years`` information is correct and includes at least one year. **Valid** examples: ``[2020, 2019]``. **Invalid**: ``["2020"]``, ``2020``, ``[]``

>My profile picture doesn't show up

Make sure that your github link works or that you've added your gravatar ID.

> I want to add/update my profile with git, but I'm stuck. Help?

Perhaps one of these links might help you:

* [short tutorial on from github](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
* [a bit more overbose explanation on help.github](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

If it doesn't, don't hesitate to ask us :)

> My file contained some (syntax) errors and destroyed the community page

Cool, that never happened before. But no worries, just write to the convenors, who apparently did a bad job at checking your file (if you can fix it quickly, a pull request would also be nice of course).
