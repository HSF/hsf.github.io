---
title: About the HSF newsletter website
author: Torre Wenaus
layout: default
---

## About the newsletter site

This site is maintained by the [HSF github repository people](https://github.com/orgs/HEP-SF/people). If you're interested to become one contact the HSF startup team or any team member. It was set up by Torre Wenaus.

## Implementation

This HSF newsletter website is implemented using [github's Pages service](https://pages.github.com/) which makes it easy to create a website associated with a github account or project. [Pages uses Jekyll](https://help.github.com/articles/using-jekyll-with-pages/), a tool to automatically build a website from source files (which are kept in github). It supports structured sites like blogs in a simple but powerful way. We all like to work in code editors; this lets you write content in a friendly editor using the easy [markdown syntax](http://daringfireball.net/projects/markdown/syntax) (which is used by github itself).

## How to post

To create a post you add a file in the [github repository of posting sources](https://github.com/HEP-SF/hep-sf.github.io/tree/master/_posts), so you need to be an [HSF github repository](https://github.com/HEP-SF) user. Talk to any member of the startup team.

If you wish (and it is recommended) you can easily set up a local instance of the newsletter site in order to preview submissions. See the [documentation on installing and running Jekyll](https://help.github.com/articles/using-jekyll-with-pages/). The newsletter uses user pages, ie use the master branch.

## What to post

Here's a template. This snippet covers the entire content of what should be in the post file. Note that the first lines enclosed by three dashes must be the first lines in the file. The format is markdown, see references below.

The file must be added to the [_posts directory](https://github.com/HEP-SF/hep-sf.github.io/tree/master/_posts) following the name convention `yyyy-mm-dd-title-goes-here.md`.

        ---
        title: HEP Software Foundation news, May 1 2015 (required)
        project: Project name if the post is about a particular project (optional)
        tags: tags for software category, etc. (optional)
        author: you (optional)
        ---

        HEP Software Foundation news this week: (include the sections for which you're giving updates)

        ## Packaging
        
        ## Software projects

        ## Training

        ## Development tools

        ## Knowledge base

        ## Technical notes

        ## Forum news

        ## Licenses

        ## Recent meetings

        ## Coming events
        
        You can also have subsections

        ### Subsection

        (you get the idea). You can include a link [here](http://path), use

        * bulleted
            * nested
        * lists

        and refer to `inline code` and

                include
                large
                code
                blocks.

        See the markdown doc for more. 


## Useful references

- [Jekyll](http://jekyllrb.com/) to build websites from plain text
- [The liquid template engine used by Jekyll](https://github.com/Shopify/liquid/wiki)
- [markdown syntax](http://daringfireball.net/projects/markdown/syntax)
