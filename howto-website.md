---
title: About the HSF newsletter website
author: Torre Wenaus
layout: default
---

## About the HSF website

This site is maintained by the HSF GitHub [contributors](https://github.com/orgs/HEP-SF/people). If you're interested to become one contact the HSF startup team or any team member. It was set up by Torre Wenaus and Benedikt Hegner.

## Implementation

This website is implemented using [GitHub's Pages](https://pages.github.com/) service which makes it easy to create a website associated with a GitHub account or project. Pages uses [Jekyll](https://help.github.com/articles/using-jekyll-with-pages/), a tool to automatically build a website from source files (which are kept in GitHub). It supports structured sites like blogs in a simple but powerful way.
The site content is written using the easy [Markdown syntax](http://daringfireball.net/projects/markdown/syntax) (which is used by GitHub itself).

A [HSF documentation](/jekyll-beginners.html) provides some useful hints to make using Jekyll in the HSF context easier.

## How to add and edit information

For adding information to this page or improving it, we follow the *[pull request](https://help.github.com/articles/using-pull-requests/)* workflow in GitHub.

Just fork our HSF [website repository](https://github.com/HEP-SF/hep-sf.github.io), edit the
files you want to edit, push them to your fork, and open a pull request.

If you wish (and it is recommended) you can easily set up a local instance of the newsletter site in order to preview your submissions. See the [documentation](https://help.github.com/articles/using-jekyll-with-pages/)
on installing and running Jekyll.
The website uses the master branch of the hep-sf.github.io repository.

If you are not familiar with GitHub and Git, you can read our [survival kit](/github-beginners.html)!

### General structure of website content files
All Markdown files of this site start with a section surrounded by `---`. This
so-called *front-matter* contains metadata about the content. Such metadata are
e.g. the author of the document or the title of the document.

### Adding contents from GoogleDoc

It is sometimes handy to use GoogleDoc to produce some contents for the web site. For example, if taking minutes
during a meeting, it allows several people to contribute to the effort of note taking and other persons who attended the
meeting to validate/update them. It is then easy to convert a properly formatted GoogleDoc (using standard heading
levels) to Markdown for inserting it into the website. Look at our [documentation](/jekyll-beginners.html) on how to
do it.

### Adding to the newsletter

Add a new file in `newsletter/_posts` and follow the front-matter of the
other files in there. The list of news will be updated automatically.

### Adding a working group

Add a new file in `workinggroups/_posts` and follow the front-matter of the
other files in there. The navigation bar will be updated automatically.

### Adding an event

Add a new file in `events/_posts` and follow the *front-matter* (see above) of the other files
in there. The [Events](http://hepsoftwarefoundation.org/events.html) page and the ``Upcoming Events`` sidebar will be updated automatically. 

### Adding breaking news

Add a new file in `announcements/_posts` and follow the front matter of the other files in there. The front page will
get a new box with all information.

Please don't forget adding an event ``until`` in the *front-matter*: this is used for ordering events **and** as the end date
for adding the event in the ``Upcoming Events`` sidebar.

## Technical details

### Page templates

As of writing, this website contains the following page templates for wider usage:

 * default - every page inherits from this
 * event - to be used for events
 * newsletter - to be used for news items
 * plain - to be used for standard contents
 * main - the main page w/ boxes

### Menu bar and automatization
The menu bar is defined in `_includes/navbar.ext`, from which all page layouts inherit.
The layout is hard-coded except for the addition of working groups. A new post
in the `workinggroups/_posts` directory automatically adds the group to the drop
down menu `Working Groups`.

### Main page automatization
The main page contains three dynamic blocks:

 * breaking news, triggered by writing an item in `announcements/_posts`
 * a list of minutes
 * a list of newsletters
 
They are filled with *[Liquid](https://github.com/Shopify/liquid/wiki)* snippets.

## Useful references

- [Jekyll](http://jekyllrb.com/) to build websites from plain text
- The [Liquid](https://github.com/Shopify/liquid/wiki) template engine used by Jekyll
- [Markdown](http://daringfireball.net/projects/markdown/syntax) syntax
