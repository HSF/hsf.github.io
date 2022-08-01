---
project: Compiler-Research
title: Add Initial Integration of Clad with Enzyme 
author: Manish Kausik H
photo: blog_authors/ManishKausik.jpg
date: 24.07.2022
year: 2022
layout: blog_post
logo: compiler-research-logo.png   
intro: |
  A blog that summarises my experience with GSoC so far and also gives a brief of the work I've done. 
---
## What Interested me to apply for this Project?
Ever since as I was introduced to compiler design as a part of my university course work, I have been fascinated by this subject and was always eager to explore more about it. Naturally
I came across the [LLVM compiler](https://llvm.org) Infrastructure and was interested in learning more about it. I found the [Compiler-Research](https://compiler-research.org/) group while looking out for some exciting projects related to the Clang and LLVM. As soon as the GSoC Organizations were announced, I got in touch with the Group members hoping to contribute in their work. This project was suggested to me by my mentor Vassil, as its a nice fit for a beginners in the field of compiler design and implementation.

Here is my [Project Proposal](https://compiler-research.org/assets/docs/Manish_Kausik_H_Proposal_2022.pdf).

## GSoC Community Bonding Period
As the Community Bonding period started, I got into fixing a few bugs in the [Clad repository](https://github.com/vgvassilev/clad), just to get to know the codebase better. I was successful in fixing some, but was not successful in fixing a few others. Meanwhile I also presented my project proposal to the rest of the Compiler Research community([Slides](https://compiler-research.org/assets/presentations/CaaS_Weekly_01_05_2022_Manish_Add_Initial_Integration_of_Clad_with_Enzyme.pdf)) and got their feedback on how I intend to take the project forward. I started participating in the weekly meetings of the Community and learnt (and still learning) about the various projects that the community members are doing.

During my community bonding period, I also explored more about the core algorithms and concepts behind my project. The primary class of algorithms that concern my project is [Automatic Differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation)(AD). AD algorithms are primarily used for finding derivatives of functions that are expressed as computer programs(code), and they are mainly of two types- forward mode and reverse mode. Often AD algorithms are implemented in 2 ways, either by source code transformation or by operator overloading. Both [Enzyme](https://enzyme.mit.edu/) and Clad use source code transformation along with compiler parsing technologies to correctly differentiate computer programs. 

## Coding Period 1
Once the coding period started, I got into implementing what vision I had for proceeding in the project. With help from my mentors and a few other community members I achieved my first milestone, that is summarised in the pull request "[Detecting Request For Enzyme by Clad](https://github.com/vgvassilev/clad/pull/460)". This first PR primarily sets the stage for the integration of clad with enzyme, by correctly detecting when a user wants to use Enzyme as a backend in clad.

Now the next step would be to actually use Enzyme to differentiate a function using the Clad API. My second Pull Request "[Generate code for Enzyme autodiff for functions with Pointer/array arguments](https://github.com/vgvassilev/clad/pull/466)" deals with this, for a very specific function prototype. This PR not only generates Clad code that Enzyme can work on, but also integrates the Enzyme Source code and the build files into the clad workflow.
