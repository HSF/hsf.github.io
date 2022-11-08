---
project: Ganga
title: An updated concurrency model for job monitoring in Ganga
author: Giorgos Apostolopoulos  
photo: blog_authors/GiorgosApostolopoulos.jpg
date: 29.08.2022
year: 2022
layout: blog_post
logo: ganga_logo_150dpi.png
intro: |
  My GSoC 2022 experience working with the Ganga team | Giorgos Apostolopoulos
---

## Introduction

### About Me

My name is Giorgos Apostolopoulos and I am a 23 year old software developer from Greece. I was happy and honored to be
selected by the Ganga team to work on their GSoC 2022 project.

### What is Ganga?

Ganga is a CERN project that was built to tackle the problem of processing system heterogeneity in scientific computing.
It enables specifying and managing computational tasks for a variety of backends using the same programmatic interface
for all of them. It is a widely used tool, mostly within CERN and the LHCb experiment.

## The Project Challenges

This year's project revolves around monitoring the jobs submitted via Ganga. The main goals are the following:

1. To rewrite Ganga's job monitoring service using modern Python concurrency features.
2. To improve monitoring performance, especially focusing on the DIRAC backend which is the one that quickly becomes underperformant.

Throughout the course of the coding period, it has become a side objective to also improve the project's coding standards.
I have therefore taken up the challenge of improving and enriching the CI workflows and continuously submitting code style improvements.

## Midterm Project Timeline

### Community Bonding Period

#### Overview

During this period I focused on becoming familiar with the project codebase. I took up a few good first issues that included writing unit tests
and making small improvements. The Ganga team was very helpful guiding me through the process.

[My Pull Requests during this period](https://github.com/ganga-devs/ganga/pulls?q=is%3Apr+author%3Ajoj0s+is%3Aclosed+closed%3A%3C2022-06-01+)

### First Coding Period

#### Overview

During the first half of the coding period there has been steady progress towards the goals of the project.

The basis of the new monitoring service based on asyncio has been created and the Local backend has been migrated to use
async APIs for its monitoring. Besides that, a base requirement for the new service was that it also had to support non async
monitoring. This has also been achieved by using ThreadPoolExecutors within it.

However, there has been a wrench thrown in the original project plans. My proposal included migrating all DIRAC monitoring
communication to the newly developed REST API it exposes so that it can be handled by asyncio. We later found out though
that the REST API is experimental and that most of the DIRAC services still use the old DISET protocol to expose their endpoints.
Therefore, the latter part of this coding period has been focused on profiling DIRAC monitoring and researching other ways of speeding it up.

During coding we also discovered that the project is suffering from a significant amount of PEP8 violations. Part of my
work has been focused on tackling this problem. To that end, I submitted a few grooming PRs and I also introduced a new
CI workflow that features enriched linting and automatic formatting PR creation.

[My Pull Requests during this period](https://github.com/ganga-devs/ganga/pulls?q=is%3Apr+author%3Ajoj0s+is%3Aclosed+closed%3A%3E2022-06-01+)

## Second Coding Period

The second half of the coding period was all about finding the right solution to our DIRAC monitoring problem. As mentioned before, my originally proposed solution proved to be not yet ready for adoption.

The new solution was a product of combining multiple concurrency options to achieve the best performance possible while still making sure that the original requirement of running DIRAC monitoring in an isolated subprocess held true. If you would like to see the technical side of things, I would refer you to the [wiki page](https://github.com/ganga-devs/ganga/wiki/Ganga-Monitoring-Service-Guide) I wrote outlining the new monitoring service, with a detailed mention of the DIRAC solution.

We then ironed out the service functionality and made sure that the new monitoring solution would work as expected in all environments, which was no easy task due to the fact that Ganga is meant to run in a wide variety of computing ecosystems. The LHCb environment proved particularly troublesome to get working properly, so the final weeks of the coding period was all about getting that part right.

[My Pull Requests during this period](https://github.com/ganga-devs/ganga/pulls?q=+is%3Apr+author%3A%40me+created%3A%3E2022-08-29)

## Project Outcome and Future Plans
I am very happy to say that the end of this year's GSoC finds the Ganga project with a newly developed, very performant and functional monitoring service.

The original project's goals of bringing Ganga's monitoring solution up to date with modern tools and coding practices, as well as fixing the significant bottlenecks that came with DIRAC monitoring have been met. As a simple metric, we found that the new monitoring service decreased the time needed to update the status of 25 remotely executing DIRAC computing jobs **from 16 seconds to 0.7**!

The plan now is to subject the new monitoring solution to rigorous testing by the Ganga team and include it in the next project release.

As for myself, I will be happy to remain available to the Ganga team to make sure that the process goes smoothly and hopefully continue contributing to the project beyond the GSoC timeline.

## My Personal Experience

### First Coding Period
I have only good things to say for my first half of this year GSoC program. Working for an organization like CERN has been
a lifelong dream of mine and the experience has not disappointed. I have already learnt a great deal and really enjoy
working with the Ganga team.

I am very much looking forward to the latter half of my time at this year's GSoC!

### Second Coding Period Update

The second coding period came with its own unique set of difficulties. Due to the challenges mentioned in the second period outline, my problem solving and debugging skills had to be put to the test. Thankfully, and thanks to the help of my GSoC mentors those challenges were overcome and through that I feel like I greatly improved as a developer.

### Final Takeaways

All in all, my experience in GSoC 2022 was everything I hoped it would be. I got to be participate and help improve a project used by a tremendous amount of people in the scientific computing community and I couldn't be more thankful and proud for that.

I would like to thank my GSoC mentors, [Ulrik](https://github.com/egede), [Mark](https://github.com/mesmith75) and [Alex](https://github.com/alexanderrichards) whose help and communication have been invaluable for me during this year's program.

Lastly, to anyone reading this blog who might be thinking about participating in GSoC, I couldn't recommend it enough! I got the opportunity to be part of an amazing organization, meet brilliant people of diverse technical and personal backgrounds and exponentially improve my skills as a software developer. That is simply an opportunity that doesn't come easily, and I would encourage everyone to go for it.

---

Reach out to me at: giorgosap@protomnail.com

---
