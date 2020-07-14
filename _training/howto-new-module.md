---
title: Creating a HSF module from scratch
layout: plain
---

If...

* you want to create a new carpentry-style training lesson from scratch (or from material that is in another format)
* you have talked to us about it

then this is for you! If you already have a module of some kind and want to update it with the HSF style, see [here](howto-update-module-style).

Creating the repository and getting started
-------------------------------------------

**We recommend you to let us do this part, so that you can start with the content right away!**

Our training modules are mimicing the work of the [software carpentries](https://software-carpentry.org/), so we essentially follow their [guide](https://carpentries.github.io/lesson-example/) to set this up, but please be aware of the following changes:

* Please use our version of the styles repository to get started, that is ``https://github.com/hsf-training/hsf-styles `` instead of ``https://github.com/carpentries/styles``

We have probably recommended you to directly create your repository in our [github organization](https://github.com/hsf-training) and already selected a name for it, but of course you can also start development in your private github.

* Use ``git remote add template https://github.com/hsf-training/hsf-styles.git`` instead of the carpentry version

Resources
----------
Here are a few links to keep handy that can be helpful when building your module
  - [Our CONTRIBUTING.md](https://github.com/carpentries/lesson-example/blob/gh-pages/CONTRIBUTING.md)
  - [SWC Github flow](https://github.com/dmgt/swc_github_flow/blob/master/for_novice_contributors.md)

Filling in content
------------------

After the last section, you should have repository that creates a blank carpentry style lesson.

* Follow the "Jekyll Setup for Lesson Development" instructions of the [carpentry tutorial setup instructions](https://carpentries.github.io/lesson-example/setup.html).
* If you are interested to study the pedagogical concepts behind the carpentries approach, head [to their handbook](https://carpentries.github.io/curriculum-development/)
* [The technological section of their handbook](https://carpentries.github.io/curriculum-development/technological-introductions.html) is a good starting point to create content right away
* The [tutorial on creating content](https://carpentries.github.io/lesson-example/02-tooling/index.html) also gives a nice introduction (but perhaps a bit more from a technological standpoint)

What to not edit
----------------

* If you improve the HSF style and other general parts of the page, please commit your changes to the HSF style repository and then pull your changes from there (this way, all other modules benefit from the changes as well)

Additional steps
----------------

* Set the ``gh-pages`` branch as the default branch (``Settings`` > ``Branches`` > ``Default branch``)

* [optional] Enabling **continuous integration** with Travis. This means that every time you push to the gihub repository, a series of checks are performed that make sure that everything looks good (e.g. no spelling mistakes, etc.). Everything is set up already in ``travis.yml``, so you only need to go to your travis account and add the repository to be built. Then update the link in the build status badge of the readme.

FAQ
---

> This is so much to take in, I feel entirely overwhelmed and discouraged. 

This is entirely normal, if you're new to the technology stack that we're using (Markdown, Jekyll, git, github, ...). But don't despair, we're here to help you! Simply [write to us](mailto:hsf-training-wg@googlegroups.com) or [join our weekly meeting](https://indico.cern.ch/category/10294/), or join the [Mattermost educators space](https://mattermost.web.cern.ch/signup_user_complete/?id=t9zkdocffbbozqcdy193myre8y) and we'll help you get unstuck. We can also arrange a short meeting where we share screens and figure out problems.
