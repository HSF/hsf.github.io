---
project: HSF Rucio WebUI
title: Rucio WebUI Midterm Progress Report 
author: Nimish Bongale
photo: blog_authors/NimishBongale.jpeg
date: 18.08.2022 
year: 2022
layout: blog_post
logo: RUCIO-logo.jpg
intro: Let’s have a look at my progress, learning, and overall experience during the GSoC 2022 period, shall we?
---

## Project Synopsis

### Mentors: Mayank Sharma, Martin B, Mario Lassnig
### Project Proposal link: [https://summerofcode.withgoogle.com/proposals/details/U9JdPuHt](https://summerofcode.withgoogle.com/proposals/details/U9JdPuHt)
### Live storybook deployment: [https://rucio.cern.ch/webui](https://rucio.cern.ch/webui)

Rucio has proven its potential to be used for providing functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. What it needs is a revamped user-friendly UI. This will not only encourage existing users to get a feel of how Rucio continues to grow and reach new milestones but also increase the adoption of the Rucio WebUI. The desired outcomes of my stint would not only involve a complete revamp of the existing UI by building a UI library of our own but also presenting users with a new & intuitive dashboard, keeping the core functionality of Rucio in mind. Rucio also supports multiple types of users and their specific workflows. The first task would involve migrating the WEBUI to a pure REST’ful architecture would require identifying and implementing new REST endpoints on the Rucio Server and developing a dynamic cross-platform ReactJS application capable of consuming the REST API directly. The second task is to improve the overall user experience for different ‌users. The new dashboard would allow users to get a quick overview of the relevant activity and provide quick access to frequently used functionalities.

## Timeline

### Community Bonding Period

- Understand Rucio as an organisation, its work and related ethics.
- Have a look at Rucio’s GitHub repositories (mainly rucio/rucio) & (rucio/webui) and understand the code structure.
- Open Issues and PRs to get acquainted with the repository workflows.
- Interact with Mentors and establish the basic ideas regarding the project in question.
- Further research about the project's needs, and ponder its potential impact after implementation.

### Coding period

- Understand Rucio WebUI in greater depth and their existing components.
- Get a sample storybook running and deployed.
- Interact with mentors and other team members, and establish a rapport.
- Learn StorybookJS & NextJS

---

- Tackle queries regarding the page structure etc. and seek approval for the same.
- Begin to code the content which will need to fill up the Rucio landing site.
- Start replacing templating with the RESTful approach. Mock data and carry out a POC for authorization workflows.

---

- Finalize the approach.
- Keep the code ready for accepting storybook UI contents.
- Completely replace templating with modern TSX code.

---

- Begin to code UI components.
- Start developing the main Rucio landing page using our own UI library.
- Start working on replacing mock data with actual REST API calls.

---

- Get complete approval for the site contents.
- Work on more UI components within StorybookJS.
- Implement environment variable wrappers, fetch API calls.

---

- Write a mid-internship blog post describing work done and how the experience has been so far with Rucio.
- Completing the UI for all the basic components in Rucio.
- Make progress on the backend side of things, make connections.
- Progress on the auth workflows and complete the major ones.

### Personal Experience

It's been a great while so far contributing to the Rucio webui project under GSoC 2022. In the past couple of months, I've been able to understand Rucio, it's associated auth mechanisms, and complex workflows which are essential in developing a user-friendly UI. Learning from the deficits of the old webui has been key in bettering my understanding on an a comprehensive level. This has led to the development of a new up-to-the-standard UI library that is custom to Rucio while standing upon ui libraries like Bulma and Primer. Here is a gist of things I was able to do so far: <br />

- [Feature 52 alert notifications](https://github.com/rucio/webui/pull/55)

#55 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged 20 days ago• [Approved](https://github.com/rucio/webui/pull/55#partial-pull-merging)

- [Feature 53 initial auth workflow](https://github.com/rucio/webui/pull/54)

#54 opened 25 days ago by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+is%3Aopen+author%3Animishbongale)

- [Feature 47 login unit test cases](https://github.com/rucio/webui/pull/51)

#51 opened 25 days ago by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+is%3Aopen+author%3Animishbongale)

- [Create REST API wrapper utility](https://github.com/rucio/webui/pull/50)

#50 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged 26 days ago• [Approved](https://github.com/rucio/webui/pull/50#partial-pull-merging)

- [Feature 46 add org logos](https://github.com/rucio/webui/pull/49)

#49 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged 26 days ago• [Approved](https://github.com/rucio/webui/pull/49#partial-pull-merging)

- [Frontend Login Infrastructure complete](https://github.com/rucio/webui/pull/45)

#45 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 11 Jul• [Approved](https://github.com/rucio/webui/pull/45#partial-pull-merging)

- [Feature 37 Implement environment layer, add OIDC configuration, other cleanup](https://github.com/rucio/webui/pull/43)

#43 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 7 Jul• [Approved](https://github.com/rucio/webui/pull/43#partial-pull-merging)

- [Feature 38 client side routing](https://github.com/rucio/webui/pull/40)

#40 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 1 Jul

- [Feature 36 CI for React app](https://github.com/rucio/webui/pull/39)

#39 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 1 Jul

- [Feature 10 login page](https://github.com/rucio/webui/pull/35)

#35 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 27 Jun

- [Feature 10 login page components](https://github.com/rucio/webui/pull/34)

#34 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 27 Jun

- [Custom CI/CD pipeline replacing third party gh action](https://github.com/rucio/webui/pull/33)

#33 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 20 Jun• [Approved](https://github.com/rucio/webui/pull/33#partial-pull-merging)

- [Feature 13 custom cicd replace third party gh action](https://github.com/rucio/webui/pull/32)

#32 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was closed on 11 Jun

- [Initial Setup of Storybook, React App, CICD deploy to GitHub pages](https://github.com/rucio/webui/pull/16) [DevOps](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale+label%3ADevOps) [gsoc22](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale+label%3Agsoc22)

#16 by [nimishbongale](https://github.com/rucio/webui/issues?q=is%3Apr+author%3Animishbongale) was merged on 10 Jun• [Approved](https://github.com/rucio/webui/pull/16#partial-pull-merging) [1.0.0](https://github.com/rucio/webui/milestone/1)

There is still a lot of learning left, and some complex workflows to tackle, but given the foundation that has been built so far, I'm hoping for a blockbuster final evaluation!