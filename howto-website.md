---
title: About the HSF newsletter website
author: Torre Wenaus
layout: default
---

## About the HSF website

This site is maintained by the HSF GitHub [contributors](https://github.com/orgs/HSF/people). If you're interested to become one, contact the [HSF Steering Group]({{ site.baseurl }}/organization/team.html) or any team member. It was set up by Torre Wenaus and Benedikt Hegner.

## Implementation

This website is implemented using [GitHub's Pages](https://pages.github.com/) service, which makes it easy to create a website associated with a GitHub account or project. Pages uses [Jekyll](https://help.github.com/articles/using-jekyll-with-pages/), a tool to automatically build a website from source files (which are kept in GitHub). It supports structured sites like blogs in a simple but powerful way.
The site content is written using the easy [Markdown syntax](http://daringfireball.net/projects/markdown/syntax) (which is used by GitHub itself).

A [HSF documentation]({{ site.baseurl }}/jekyll-beginners.html) provides some useful hints to make using Jekyll in the HSF context easier.

## How to add and edit information

For adding information to this page or improving it, we follow the *[pull request](https://help.github.com/articles/using-pull-requests/)* workflow in GitHub.

Just fork our HSF [website repository](https://github.com/HSF/hsf.github.io), edit the
files you want to edit, push them to your fork, and open a pull request.

If you wish (and it is recommended) you can easily set up a local instance of the newsletter site in order to preview your submissions. See the [documentation](https://help.github.com/articles/using-jekyll-with-pages/)
on installing and running Jekyll.
The website uses the main branch of the [hsf.github.io](https://github.com/HSF/hsf.github.io) repository.

If you are not familiar with GitHub and Git, you can read our [survival kit]({{ site.baseurl }}/github-beginners.html)!

### General structure of website content files

All Markdown files of this site start with a section surrounded by `---`. This
so-called *front-matter* contains metadata about the content. Such metadata are,
e.g., the author of the document or the title of the document.

In the *front-matter* (but not in the text itself), you need to replace any `&` characters (which has a special meaning in HTML) by `&amp;`. This is particularly important for the `title` attribute.

### Adding content from collaborative tools (live notes)

#### Markdown file

The recommended way to host a collaborative note book, e.g. for taking meeting minutes (live notes),
is to use a collaborative editing tool utilising Markdown directly.  This makes it trivial to move the content into the HSF website for archiving.

[CodiMD](https://hackmd.io/c/codimd-documentation/%2Fs%2Fcodimd-documentation) is the suggested choice as it has been designed for collaboraitve editing of Markdown files. Unfortunately, the [Hackmd](https://hackmd.io) free service is now restricted to 4 editors. Another possibility, if you have a CERN account, is to use CERNBox which makes CodiMD available to edit Markdown files: you can then define a public link to the document (similar to Google Docs public links) to allow those without a CERN account to edit the file.

We find that *recycling* the same document for a series of meetings is extremely useful
as the *live notes* link can be copied and cloned from one meeting to the next.

#### GoogleDocs

Google Docs can also be used for shared notebooks, but in this case there is a need to convert
the document to Markdown before it can be added to the website. This is less convenient, but
we have [documentation]({{ site.baseurl }}/jekyll-beginners.html) on how to do it.


### Adding coordination meeting minutes

HSF Coordination minutes are produced using the live notes approach described above. The content of the live notes are preformatted to be suitable for direct injection into Jekyll, after minimal edits described in the [running-meetings]({{ site.baseurl }}/organization/running-meetings.html) page. The minutes file must be placed into Jekyll `organization/_posts` directory.

### Adding an Activity Area

*Before adding any new activity or proposing a new Activity Area please discuss with the
[HSF Steering Group]({{ site.baseurl }}/organization/team.html)!
We will make sure it gets proposed in an HSF meeting for approval.*

Then, for the technical creation, add a new file in the `_activities` directory. Follow the front-matter of the
other files in there. The `Activities` menu in the navigation bar will
be updated automatically: the menu entry text is the `title` attribute in the *front-matter* section.

### Adding an event

Add a new file in `events/_posts` and follow the *front-matter* (see above) of the other files
in there. The [Events](http://hepsoftwarefoundation.org/events.html) page and the ``Upcoming Events`` sidebar will be updated automatically.

### Adding a training event

For *training events* we have a special handling that lists all of these together on the 
[Training Activity Area page]({{ site.baseurl }}/workinggroups/training.html). To create a new
entry you can either:

1. Run the interactive script ``scripts/add_training_event.py`` (recommended)
2. Directly edit the ``_data/trainning-schools.yml`` file and add another entry following the structure of the existing entries (note that events are sorted chronologically by starting date)
    - There is one very rare thing you may need to do if the URL for the training event
      will not validate in the link checker, which is to add the tag `url_proof_ignore: true`
      to the YAML file (an example is a school that used a web technology that insists
      on setting cookies and issues continual redirects without this)

### Adding news or announcements

Add a new file in `announcements/_posts` and follow the front matter of the other files in there. The front page will
get a new box with all information.

Please don't forget adding an event ``until`` in the *front-matter*: this is used for ordering events **and** as the end date
for adding the event in the ``Upcoming Events`` sidebar.

### Adding a newsletter

[Newsletters]({{ site.baseurl }}/newsletter.html) are occasional longer articles we publish. Each of these lives in `newsletter/_posts`.
The format is very similar to the other
content on the website, follow the front matter of the other files in there.

You can highlight a newsletter by updating the centre column of the frontpage of the website (see below).

### Adding your profile

Some pages, like the [training community page]({{ site.baseurl }}/training/community.html) feature "floating heads"
corresponding to profiles of community members.
See [howto profile]({{ site.baseurl }}/howto-profile.html) for how to create your profile and how to include
selected profiles into a page.

## Technical details

### Page templates

As of writing, this website contains the following page templates for wider usage:

- default - every page inherits from this
- event - to be used for events
- newsletter - to be used for news items and announcements
- plain - to be used for standard contents
- main - the main page w/ boxes
- minutes - used for meeting minutes (the template adds forward / backward navigation links)

### Menu bar and automatization

The menu bar is defined in `_includes/navbar.ext`, from which all page layouts inherit.
The layout is somewhat hard-coded, but activities are generated
automatically.

### Main page

The main page contains three blocks, mostly hard-coded:

- A *meetings* block, with links to the minutes of the last three meetings
    auto-generated
- A news item that holds a small snippet of current important information
    (currently this is hard-coded, but it would be better if it were more
      dynamic)
- An *activities* block, that serves as an entry point to the main sections
    of the website

They are filled with *[Liquid](https://github.com/Shopify/liquid/wiki)* snippets.

## Useful references

- [Jekyll](http://jekyllrb.com/) to build websites from plain text
- The [Liquid](https://github.com/Shopify/liquid/wiki) template engine used by Jekyll
- [Markdown](http://daringfireball.net/projects/markdown/syntax) syntax
