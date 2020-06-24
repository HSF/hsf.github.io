---
title: "How to update your educator profile"
layout: plain
---
This page explains how to update or create your educator profile for the [training community page](/training/community).

## Basics

Your educator profile corresponds to a text file in the ``_educators`` directory ([view on github](https://github.com/HSF/hsf.github.io/tree/master/_educators)). The file ``000_template.md`` tells you how this file should look like (it is shown below for convenience).

## If you don't have a profile yet

Simply copy the template at the bottom of this page and modify it to include your information. You can then either 

* send it to the conveners via email, or 
* (**preferred**) fork the github repository, put your profile in the ``_educators`` directory as ``first_name_last_name.md`` (don't worry about the exact form of the name) and open a pull request

## If you want to change your profile

Either

* Find your profile [on github](https://github.com/HSF/hsf.github.io/tree/master/_educators) (``first_name_last_name.md``), copy it to a text file, make your modifcations and send your new version to the conveners via email
* (**preferred**) fork the github repository, update your information in ``_educators/first_name_last_name.md`` and open a pull request

## The template

```
{% include_relative 000_template.md %}
```

### Notes

* The profile picture will be taken from your [github](https://github.com) profile (if specified). If the github profile is not specified, it will be taken from [gravatar](https://gravatar.com/) (a free service for global avatar synchornization). If the latter is not specified either, you will have a blank profile picture.
* The roles are explained [here](/training/educators). Valid examples: ``[convenor]``, ``[instructor, mentor]``.  **Invalid**: ``mentor`` (no brackets). Please keep the order of the roles as they are in the template. 

### Example

```
{% include_relative kilian_lieret.md %}
```

## FAQ

> I've added my profile, but it doesn't appear on the webpage

* The webpage takes a couple of minutes to update
* Make sure that the ``years`` information is correct and includes at least one year. **Valid** examples: ``[2020, 2019]``. **Invalid**: ``["2020"]``, ``2020``, ``[]``

>My profile picture doesn't show up

Make sure that your github link works or that you've added your gravatar ID

> I want to add/update my profile with git, but I'm stuck. Help?

Perhaps one of these links might help you:

* [short forking tutorial on guides.github](https://guides.github.com/activities/forking/)
* [a bit more overbose explanation on help.github](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)

If it doesn't, don't hesitate to ask us :)

> My file contained some (syntax) errors and destroyed the community page

Cool, that never happened before. But no worries, just write to the convenors, who apparently did a bad job at checking your file (if you can fix it quickly, a pull request would also be nice of course).