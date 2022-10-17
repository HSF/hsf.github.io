---
project: Compiler-Research
title: Add Initial Integration of Clad with Enzyme 
author: Manish Kausik H
photo: blog_authors/ManishKausik.jpg
date: 09.09.2022
year: 2022
layout: blog_post
logo: compiler-research-logo.png   
intro: |
  A blog that summarises my experience with GSoC 2022. 
---
## What Interested me to apply for this Project?
Ever since as I was introduced to compiler design as a part of my university course work, I have been fascinated by this subject and was always eager to explore more about it. Naturally
I came across the [LLVM compiler](https://llvm.org) Infrastructure and was interested in learning more about it. I found the [Compiler-Research](https://compiler-research.org/) group while looking out for some exciting projects related to the Clang and LLVM. As soon as the GSoC Organizations were announced, I got in touch with the Group members hoping to contribute in their work. This project was suggested to me by my mentor Vassil, as its a nice fit for a beginners in the field of compiler design and implementation.

Here is my [Project Proposal](https://compiler-research.org/assets/docs/Manish_Kausik_H_Proposal_2022.pdf).

## GSoC Community Bonding Period
As the Community Bonding period started, I got into fixing a few bugs in the [Clad repository](https://github.com/vgvassilev/clad), just to get to know the codebase better. I was successful in fixing some, but was not successful in fixing a few others. Meanwhile I also presented my project proposal to the rest of the Compiler Research community([Slides](https://compiler-research.org/assets/presentations/CaaS_Weekly_01_05_2022_Manish_Add_Initial_Integration_of_Clad_with_Enzyme.pdf)) and got their feedback on how I intend to take the project forward. I started participating in the weekly meetings of the Community and learnt (and still learning) about the various projects that the community members are doing.

During my community bonding period, I also explored more about the core algorithms and concepts behind my project. The primary class of algorithms that concern my project is [Automatic Differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation)(AD). AD algorithms are primarily used for finding derivatives of functions that are expressed as computer programs(code), and they are mainly of two types- forward mode and reverse mode. Often AD algorithms are implemented in 2 ways, either by source code transformation or by operator overloading. Both [Enzyme](https://enzyme.mit.edu/) and Clad use source code transformation along with compiler parsing technologies to correctly differentiate computer programs. 

## Coding Period 1
Once the coding period started, I got into implementing what vision I had for proceeding in the project. With help from my mentors and a few other community members I achieved my first milestone, that is summarised in the pull request "[Detecting Request For Enzyme by Clad](https://github.com/vgvassilev/clad/pull/460)". This first PR primarily sets the stage for the integration of Clad with enzyme, by correctly detecting when a user wants to use Enzyme as a backend in Clad.

Now the next step would be to actually use Enzyme to differentiate a function using the Clad API. My second Pull Request "[Generate code for Enzyme autodiff for functions with Pointer/array arguments](https://github.com/vgvassilev/clad/pull/466)" deals with this, for a very specific function prototype. This PR not only generates Clad code that Enzyme can work on, but also integrates the Enzyme Source code and the build files into the Clad workflow. However, this PR was not merged before the end of this coding period.

## Coding Period 2
Initially my second Pull Request integrated Enzyme within Clad as a shared object, but upon some discussion with my mentors, we decided to statically link Enzyme with Clad. My mentor helped me with this. Statically linking did bring up some issues in scheduling the Enzyme Passes correctly, which took some time for me to figure out. Thus the second PR did take some time for me to achieve, but when it was successfully merged, it was a milestone in the project as it gave a platform to call Enzyme within Clad.

Now the stage was set to add support for differentiating different function prototypes with Enzyme in Clad. This was achieved by my third Pull Request [Add Support for Differentiating functions with both pointer/array type and primitive type parameters with Enzyme](https://github.com/vgvassilev/clad/pull/486). This PR completes initial Enzyme Reverse Mode integration with Clad. 

Now that I had integrated Enzyme within Clad, to comprehensively complete my Project, I contributed to a few other Pull Requests which are mentioned here:

+ [Benchmark Clad and Enzyme](https://github.com/vgvassilev/clad/pull/491): This PR compares the execution time of Clad generated derivatives with Enzyme Generated derivatives with Google's Benchmark library.
+ [Treat Request to use Enzyme for Differentiating a Function to be different from a Clad differentiation](https://github.com/vgvassilev/clad/pull/492): This PR was a bug fix.
+ [Add Documentation for Integration of Enzyme with Clad](https://github.com/vgvassilev/clad/pull/494): This PR adds a page in the Clad Documentation explaining the details of the Project as well as the calling convention to use the features added by the project.
+ [Add tests to verify enzyme results with clad](https://github.com/vgvassilev/clad/pull/495): This PR verifies if the Gradients generated by Enzyme and Clad match to a certain fixed level of accuracy.

## My Experience with GSoC
This project gave me a good insight into Software Engineering practices used by the Open Source Community and a great experience in learning some State of the Art Compiler Libraries like Clang and LLVM. It was also a great opportunity to meet members of both Clad and Enzyme communities. Honestly, not everything about the Project went smoothly, as there were some unexpected delays in code reviews and I did face several coding challenges during the project. But thanks to timely help from my mentors and other members of the community I was able to achieve most deliverables that I had proposed in my GSoC Proposal. Overall, it was a great learning experience!

## Future Work
I had proposed to add support for forward mode AD with Enzyme within clad, but  currently forward mode AD is under development in Enzyme. Once a stable release of the same is available, we can add support for forward mode AD with Enzyme within Clad.