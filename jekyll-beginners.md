---
title: Contributing to the HSF Web Site
author: Michel Jouvin
layout: default
---

# Contributing to the HSF Web Site
{:.no_toc}

* auto-gen TOC:
{:toc}

The HSF web site is hosted by [GitHub Pages](https://pages.github.com) which relies on a framework called 
[Jekyll](https://jekyllrb.com). This page documents a few useful hints that help contributing to the web site 
and assessing the result of your contributions. Refer to the linked documentations for details about [
GitHub Pages](https://pages.github.com) and [Jekyll](https://jekyllrb.com).



## Content Format

Jekyll expect the web site contents to be written in [Markdown](https://guides.github.com/features/mastering-markdown/) with 
a special section at the beginning of the file called `frontmatter`. This section contains attribute definitions used to render the file. It is delimited by a pair of `---` lines. A typical frontmatter section is:

```
---
title: Contributing to the HSF Web Site
author: Michel Jouvin
layout: default
---
```

After the frontmatter section, you have to write in markdown (or generate markdown from another format, see below).


### File Name Format

Markdown files are organized by categories: events, newsletter, organization (meeting notes)...
Markdown files in these categories are stored in a `_post` subdirectory. Jekyll expects the markdown file names 
in these `_post` directories to follow the following convention:

```
YYY-MM-DD-some-text.md
```

with:

* `YYYY`: the year
* `MM`: the month number
* `DD`: the day number


### Adding a TOC

To generate a table of contents of the file, you need to add the following lines where you want to insert it:

```
* auto-gen TOC:
{:toc}
```

If you don't want a heading, for example the page title (heading level 1), to be inserted into the TOC, you need to insert the following line right after the heading:

```
{:.no_toc}
```

Look at the source of this page for an example.


### Converting Contents from Word or GoogleDoc

[pandoc](http://pandoc.org) is the swiss-army knife for the conversion between text formats. In particular it supports a very good conversion from Microsoft Word (`docx`) format to Jekyll markdown. The typical command to do this conversion is:

```
pandoc -t markdown_github --base-header-level=2 --atx-headers -o organization/_posts/2016-05-19-startup.md document.docx
```

This method can be used to convert a GoogleDoc document to markdown. To do it, use the GoogleDoc menu `File->Download as` and expoert the GoogleDoc document as a `docx` file. Then use the command above to convert to markdown.


## Checking the Results of Your Contribution

It is often desirable to assess the result of changes before publishing them. There is no services at GitHub to do that: 
you can only render the markdown contents, without all the CSS and other things. To achieve this, you need to install 
Jekyll on your local machine. Detailed instructions can be found on Jekyll [web site](https://jekyllrb.com/docs/installation/) 
but the short story is:

* Install [Ruby](https://www.ruby-lang.org/en/downloads/) and [RubyGems](https://rubygems.org/pages/download)
* Install Jekyll with:

    ```bash
    gem install jekyll
    ```

* Create a directory where the web site files will be generated: in this documentation we assume that it is 
`$HOME/hep-sf.github.io`

Assuming that you have a clone of GitHub HSF repository `hep-sf.github.io` in `$HOME/git/hep-sf.github.io`, launch Jekyll with:

```bash
jekyll serve --base '' --source $HOME/git/hep-sf.github.io -d $HOME/hep-sf.github.io
```

Once Jekyll has been started you can view the web site by connecting to `localhost:4000`.

