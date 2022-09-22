---
project: Phoenix
title: Revamped Testing Infrastructure for Phoenix
author: Mohammad Humayun Khan
photo: blog_authors/MohammadHumayunKhan.jpg
date: 24.09.2022
year: 2022
layout: blog_post
logo: phoenix-logo.png
intro: |
  Hello dear reader, I hope you're doing well. During the summer of 2022, I worked on project Phoenix at CERN-HSF as a Google Summer of Code contributor. My project aimed to introduce a new testing infrastructure for Phoenix.
---

### Community Bonding Period

> 20.05.2022 - 12.06.2022

This started with an introductory video call between me and my mentors, Edward Moyse and Fawad Ali in which we got to know each other and the work we do. It was really good to know about their experience in open-source software development and I straightaway knew that this summer would be quite exciting and even a better learning experience for me. 

Community Bonding, in general, is all about reading the technologies that you are going to use in your project, figuring out any issues that may occur beforehand, setting up the development environment, dividing and finalizing the project milestones into deliverables, and making sure you and the mentor(s) agree on it.

Most of my time hence was spent doing the aforementioned things. I read about TypeScript, Angular, Jasmine, and Jest in detail - since these are the major ones that we would use throughout the project. I also read about the conventions that we use while implementing automated testing in projects and the Testing Pyramid.

### Writing unit tests for phoenix-event-display

> 13.06.2022 - 18.07.2022

We decided to use Jest in the unit tests for the [phoenix-event-display](https://github.com/HSF/phoenix/blob/master/packages/phoenix-event-display/README.md) library as it provides a lot of benefits viz a viz configuration, APIs, speed of execution and mocking over Jasmine and Karma which were creating troubles sometimes. 

In the start, we faced a problem as Jest was not able to compile the `.jsm` files inside `threejs/examples`. With the help of Fawad, I was able to bypass this issue and then I went on to write the tests for `helpers` and `lib`. It is during this time that on a PR I realized a very important thing that is often misunderstood by beginners.

We write unit tests not solely to increase the code coverage but to test the behaviors of each of the modules (units) properly. Code coverage is achieved as a by-product and 100% code coverage is not always a guarantee that the concerned unit is tested correctly. 

Another problem was created later when I was writing tests for `loaders` and `managers` by the `WebGLRenderer` dependency as it didn't exist in NodeJS and we used it heavily inside the library. So, we needed to mock it and we added a helper function to create objects of `WebGLRenderer` in our tests. This is a well-known issue that we need a browser to create a `WebGLContext` and the jest environment jsdom, in our case does not have that, it just simulates one.

### Writing unit tests for phoenix-ng

> 19.07.2022 - 14.08.2022

During this period, I did the migration of the unit tests inside [phoenix-ng](https://github.com/HSF/phoenix/blob/master/packages/phoenix-ng/README.md) package from Jasmine and Karma setup to use Jest as well. This eventually helped us to use a single test runner for all our unit tests and Jest did a great job in providing faster execution time of tests, consistent test runs (no flaky tests), easy to understand reasons in the events when the tests fail with the only downside that we had to mock a lot of things as we are running tests in a browser-less environment.

### Writing e2e tests for Phoenix app

> 15.08.2022 - 26.08.2022

The task at hand was to introduce a new end-to-end testing setup for the [Phoenix application](https://hepsoftwarefoundation.org/phoenix/#/) and I did that using Cypress. In the start, I went the wrong way checking for elements inside the DOM heavily but after being prompted correctly by Fawad, I removed that and used snapshot testing for each experiment to test the different visual changes properly. 

### Making sure that the new setup is stable

> 27.08.2022 - 20.09.2022

At this point, all the unit tests and e2e tests were running fine locally. But, I encountered a strange problem that the unit tests were failing on GitHub CI and not locally. First, I tried changing the environment in which I ran tests as our CI environment was on Ubuntu, then I tried installing the necessary packages as I used the [headless-gl](https://github.com/stackgl/headless-gl) library to mock WebGLRenderer but then, we decided to mock the WebGLRenderer completely as we intended to test only our code and not WebGLRenderer itself. 

After this change, all the tests passed on the CI but still, I got a non-zero exit code on the execution of tests which also lead to a lot of confusion as we were not sure as to why we were getting this but [after a lot of digging](https://github.com/HSF/phoenix/pull/492/#issuecomment-1249671624), I got to know that it is due to the fact that Jest uses a single worker process while executing the tests on the CI and we just needed to add one more worker for it to stop showing the non-zero exit code. And, the tests then ran fine on the CI! ^_^

This culminated in the end of the GSoC project timeline for me but I would be glad to continue working and add enhancements to Phoenix in the future as well. Thanks a lot to Edward, Fawad and HSF GSoC admins for selecting my project and giving me an opportunity to work here, at CERN-HSF. I am truly grateful. I would especially like to mention that the code reviews done by Fawad throughout the project work were actually fantastic and detailed. It led to a lot of improvements and I learned so many new things which would not have been the case otherwise so, kudos to that as well. 

#### Relevant Links

- Project Work Summary: https://github.com/DamianArado/GSoC-2022-Phoenix/blob/main/SUMMARY.md
- Project Roadmap: https://github.com/DamianArado/GSoC-2022-Phoenix/blob/main/ROADMAP.md
- Project Progress: https://github.com/DamianArado/GSoC-2022-Phoenix/blob/main/PROGRESS.md

Thanks a lot for reading and I wish you a great year ahead.
