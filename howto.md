---
title: About the HSF newsletter website
author: Torre Wenaus
layout: default
---

## About the HSF website

This site is maintained by the [HSF GitHub repository people](https://github.com/orgs/HEP-SF/people). If you're interested to become one contact the HSF startup team or any team member. It was set up by Torre Wenaus and Benedikt Hegner.

## Implementation

This website is implemented using [GitHub's Pages service](https://pages.github.com/) which makes it easy to create a website associated with a GitHub account or project. [Pages uses Jekyll](https://help.github.com/articles/using-jekyll-with-pages/), a tool to automatically build a website from source files (which are kept in GitHub). It supports structured sites like blogs in a simple but powerful way. We all like to work in code editors; this lets you write content in a friendly editor using the easy [markdown syntax](http://daringfireball.net/projects/markdown/syntax) (which is used by GitHub itself).

## How to add and edit information

For adding information to this page or improving it, we follow the *[pull request](https://help.github.com/articles/using-pull-requests/)* workflow in GitHub.

Just fork our [HSF website repository](https://github.com/HEP-SF/hep-sf.github.io), edit the
files you want to edit, push them to your fork, and open a pull request.

If you wish (and it is recommended) you can easily set up a local instance of the newsletter site in order to preview your submissions. See the [documentation on installing and running Jekyll](https://help.github.com/articles/using-jekyll-with-pages/).
The website uses the master branch of the hep-sf.github.io repository.
If you only do simple operations like the ones mentioned below, the GitHub
interface itself gives you all options to add and edit such files in the browser.
So no local checkout is required.

### Adding to the newsletter

Add a new file in `workinggroups/_posts` and follow the front-matter of the
other files in there. The list of news will be updated automatically.

### Adding a working group

Add a new file in `workinggroups/_posts` and follow the front-matter of the
other files in there. The navigation bar will be updated automatically.

### Adding an event

Add a new file in `events/_posts` and follow the front-matter of the other files
in there. The events page will be updated automatically. Please don't forget
adding a startdate. Only this allows a proper ordering

### Adding a job opening

Add a new file in `jobs/_posts` and follow the front-matter of the other files
in there. It is important to fill the field `open: true`. This field allows to
only show positions that aren't filled yet.

## Technical details

### Page templates

As of writing, this website contains the following page templates for wider usage:

 * default - every page inherits from this
 * event - to be used for events
 * job - to be used for job postings
 * newsletter - to be used for news items
 * plain - to be used for standard contents

### Menu bar and automatization
The menu bar is defined in `default.html`, from which all page layouts inherit.
The layout is hard-coded except for the addition of working groups. A new post
in the `workinggroups/_posts` directory automatically adds the group to the drop
down menu `Working Groups`.

### Side bar and automatization
The side bar contains two dynamic blocks - *upcoming events* and *current job
openings*. Both are filled with *liquid* snippets defined in `_includes`.



## Useful references

- [Jekyll](http://jekyllrb.com/) to build websites from plain text
- [The liquid template engine used by Jekyll](https://github.com/Shopify/liquid/wiki)
- [markdown syntax](http://daringfireball.net/projects/markdown/syntax)
