---
project: Phoenix
title: Revamping the testing infrastructure at Phoenix | Mid term progress report
author: Mohammad Humayun Khan
photo: blog_authors/MohammadHumayunKhan.jpg
date: 26.07.2022
year: 2022
layout: blog_post
logo: phoenix-logo.png
intro: |
  Hi all, I hope everyone is doing good. I'm Humayun and for the past couple of months, I've been working on the project Phoenix at CERN-HSF. This project aims to introduce a new testing strategy so that we encourage testing, especially Behaviour-driven Development here, at Phoenix.
---

### Community Bonding Period

> 20.05.2022 - 12.06.2022

This started with an introductory video call between me and my mentors, Edward Moyse and Fawad Ali in which we got to know each other and the work we do. It was really good to know about their experience in open-source software development and I straight away knew that this summer would be quite exciting and even a better learning experience for me. 

Community Bonding, in general, is all about reading the technologies that you are going to use in your project, figuring out any issues that may occur beforehand, setting up the development environment, dividing and finalizing the project milestones into deliverables, and making sure you and the mentor(s) agree on it.

Most of my time hence was spent doing the aforementioned things. I read about TypeScript, Angular, Jasmine, and Jest in detail - since these are the major ones that we would use throughout the project. I also read about the conventions that we use while implementing automated testing in projects and the Testing Pyramid.

### Writing unit tests for phoenix-event-display

> 13.06.2022 - 18.07.2022

We decided to use Jest in the unit tests for the [phoenix-event-display](https://github.com/HSF/phoenix/blob/master/packages/phoenix-event-display/README.md) library as it provides a lot of benefits viz a viz configuration, APIs, speed of execution and mocking over Jasmine and Karma which were creating troubles sometimes. 

In the start, we faced a problem as jest was not able to compile the `.jsm` files inside `threejs/examples`. With the help of Fawad, I was able to bypass this issue and then I went on to write the tests for `helpers` and `lib`. It is during this time that on a PR I realized a very important thing that is often misunderstood by beginners.

We write unit tests not solely to increase the code coverage but to test the behaviors of each of the modules (units) properly. Code coverage is achieved as a by-product and 100% code coverage is not always a guarantee that the concerned unit is tested correctly. 

Another problem was created later when I was writing tests for `loaders` and `managers` by the `WebGLRenderer` dependency as it didn't exist in NodeJS and we used it heavily inside the library. So, we needed to mock it and we added a helper function to create objects of `WebGLRenderer` in our tests. This is a well-known issue that we need a browser to create a `WebGLContext` and the jest environment jsdom, in our case does not have that, it just simulates one.

Also, I have to mention that the code reviews done by Fawad were actually superb. It led to a lot of improvements and I learned so many new things which would not have been the case otherwise. So, kudos to that. 

### Writing unit tests for phoenix-ng

> 19.07.2022 - 03.08.2022

Currently, I am doing the migration of the unit tests inside [phoenix-ng](https://github.com/HSF/phoenix/blob/master/packages/phoenix-ng/README.md) package from Jasmine and Karma setup to use Jest as well. This will eventually help us to use a single test runner for all our unit tests and it will also be easily maintainable by the developers. I hope that using Jest, we can find solutions to a lot of problems that we faced earlier with unit tests in Phoenix.

So, this is a short report of all the work that has been done in this project till the midterm evaluation. If you want to read in detail about the same, you can visit [my repo on GitHub](https://github.com/DamianArado/GSoC-2022-Phoenix/blob/main/PROGRESS.md).

Thanks a lot for reading and please feel free to connect over [LinkedIn](https://www.linkedin.com/in/damianarado) or [GitHub](https://github.com/DamianArado). Have a great week ahead!  ^_^