---
project: AllpixSquared
title: Restructuring & Streamlining of the Allpix Squared Documentation
author: Sabita Rao
date: 02.12.2020
year: 2020
layout: blog_post
logo: ALLPIXSQUARED-logo.png
intro: |
  If you're a technical writer, [GSoD](https://developers.google.com/season-of-docs) is where you want to be. As a newbie, you'll learn all about open source methodologies and tech. As a seasoned writer, you'll showcase your expertise while finetuning your skills. Either way, you'll challenge everything ranging from your laptop's processors to your own capabilities. An absolute bonus is the experience of working with incredible mentors in trendsetting organizations.
---

## About GSoD and the project requirements

Here's a quick recap of how I got started with GSoD.

### About Google Season of Docs

If you're a technical writer, [GSoD](https://developers.google.com/season-of-docs) is where you want to be. As a newbie, you'll learn all about open source methodologies and tech. As a seasoned writer, you'll showcase your expertise while finetuning your skills. Either way, you'll challenge everything ranging from your laptop's processors to your own capabilities. An absolute bonus is the experience of working with incredible mentors in trendsetting organizations.

### Choosing the project

When the GSoD application phase opens, you're allowed to apply to 3 organizations. It's daunting to look at all those projects calling for 'technical'-technical writers. I hadn't even heard of the tools required by some projects. My advice? Fight off the imposter syndrome (if I can do it, anyone can!) and run through the list of organizations and their projects multiple times. I took approx. a week to finalize 2 orgs that I wanted to work with - CERN and mojaglobal. My primary reasons for choosing them were:

  * CERN, because well, they're CERN! But also because the project I was eyeing required skills that I hadn't mastered at the time of application; no better way to learn than on a live project, IMO. What caught my attention was how much thought the DESY mentors had put into their detailed project description. It was clear from their existing documentation that they took technical content writing seriously.
  * mojaglobal, because they're open source software for climate change. Who wouldn't want to be a part of that? :)

It was evident after I'd exchanged emails with both groups that CERN-DESY's project Restructuring & Streamlining of the Allpix Squared Documentation was it for me. (I intend to contribute to moja global as a volunteer after GSoD, so thank you for bringing us together, Google!)

It's risky going into the GSoD application phase with all your hopes pinned on a single org. But when you know, you know, I s'pose? :) I was excited enough to start working on a prototype for the DESY project way before Google even announced the selected candidates! It certainly helped channel my nervous energy as we waited for Google's list.

The first time I met the project mentors Paul Schütze and Simon Spannagel on a video call, I realized this was going to be a fun but hectic project! Thankfully, their sense of humor and professionalism made my job easy. We quickly established an informal agenda to meet on weekly calls, while using internal chat as frequently as required. I even got a temporary email ID srao@cern.ch(!) for easy access to CERN systems.

### Project requirements

The AP2 team was very clear on the **project requirements** from the start:
  * **Content:**
    * Separate the Allpix Squared documentation by user level: novice student, potential contributor, and seasoned developer.
    * Review the current user manual for potentially lacking information.
  * **Infrastructure:**
    * Streamline the documentation presentation, ideally with a fully-integrated website for news, manual and code reference.
    * Keep the current automatic deployment and workflow intact.
  * **Bonus task:**
    * Streamline examples to follow a tutorial-like workflow.

## Accomplishments and challenges

### My initial proposal

In my [GSoD application](https://developers.google.com/season-of-docs/docs/2020/participants/project-cernhsf-sabitar), I proposed the following deliverables:

  * A streamlined project website that integrates documentation, code reference, tutorials, and news.
  * A restructured and reviewed user manual that separates content intended for users and developers, and includes previously missing information.
  * A tutorials workflow from available examples of how-to documentation, FAQs, and commonly-faced issues.

### Accomplishments

Of my 3 proposed tasks, I've successfully completed the first 2, as seen in [this website](https://srao.web.cern.ch/srao/). The main features of this website are:

  * The user manual caters to users of different levels (novice, advanced, and developers).
  * The website allows seamless content search across the restructured user manual, code reference, and news articles.
  * The user manual content is in Markdown, and uses LaTeX only for the equations. This could encourage more contributions from novice users.

I had to revise my proposal and exclude the (bonus) tutorials task early in the project, as it needed more time than I'd originally planned.

### Challenges

  * **Working with multiple repositories:** being new to git and CMake, it took me the entire *Community Bonding phase* (Aug-Sep) to understand the current workflow and how to maintain it as far as possible.
  * **Running Allpix Squared on Windows Subsystem for Linux (WSL):** To test the existing documentation, I attempted to run AP2 on WSL, and ran into quite a few issues. Eventually, I did manage to run an instance of AP2 on Ubuntu for Windows. Happy to report that the existing documentation needed no fixing! There is scope for enhancing the content for Windows users, in future.
  * **Eliminating Pandoc from the workflow** This step turned out to be trickier than we'd anticipated.
    * It required converting the user manual content from LaTeX to Markdown for ease of use with static-site generators like Hugo and MkDocs.
    * We had to test multiple plugins to convert LaTeX to HTML, and eventually settled on Mathjax for MkDocs.
    * To ensure that the LaTeX equations were legible in both Gitlab as well as HTML, it was necessary to tweak the CMake files and edit the Markdown files at runtime only.

My mentors made it all possible!

If you are interested, more details on my project are available [here](https://github.com/sabitarao/gsod/wiki)