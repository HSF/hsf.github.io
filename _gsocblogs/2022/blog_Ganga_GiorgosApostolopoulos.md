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
  Overview of the first half of the coding period in Ganga by Giorgos Apostolopoulos | GSoC 2022
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

### Coding Period

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

## Second Coding Period Plans

The goals until the end of the coding period are following:

- Migrate the rest of the job execution backends to be asyncio compatible.
- Improve DIRAC concurrency by using threadpools and utilizing its HTTPS services when available.
- Create a test suite for the new monitoring service.

## My Personal Experience So Far

I have only good things to say for my first half of this year GSoC program. Working for an organization like CERN has been
a lifelong dream of mine and the experience has not dissapointed. I have already learnt a great deal and really enjoy
working with the Ganga team.

I am really looking forward to the latter half of my time at this year's GSoC!

---

Reach out to me at: giorgosap@protomnail.com

---
