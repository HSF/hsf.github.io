---

project: HSF
title: Interfacing PODIO with Julia
author: Soumil Baldota
date: 28.07.2022 
year: 2022 
layout: blog_post
logo: podio-logo.png
intro: Midterm progress report

---
*About Me*
I am Soumil Baldota in my sophomore year in college with a few years of development experience in C++ and Python. For me Julia was a new language but I got acclimated quickly and have had a good time contributing to HSF organization. I am thankful to my mentors and the organization.

*Community Bonding*
In the community bonding period, with the help of Thomas and Benedikt, I setup my development environment along with local install of podio. To get familiar with podio and the contributing workflow. I worked on some minor issues.

*Issues raised:*
[clang-tidy](https://github.com/AIDASoft/podio/issues/297)
[pylint](ps://github.com/AIDASoft/podio/issues/298)

*Pull Requests:*
[Replace obj_needs_destructor by more general concept](https://github.com/AIDASoft/podio/pull/291)
[Review generator python code](https://github.com/AIDASoft/podio/pull/293)
[running pre-commit locally](https://github.com/AIDASoft/podio/pull/296)


Next I began to work on a prototype for the Interface which described how the generated code would look like. The prototype was created for classes with one to one relations, one to many relations and vector members. Then I made unittests for the prototype and added them to github actions for continuous integration. 
The prototype can be found at the below link
[Prototype](https://github.com/soumilbaldota/PODIO_Julia_Interface_Prototype.git)
  
*Coding Period*
After the prototype was created. I added an attribute to store the Julia type of a data member described in C++ to the MemberVariable Class and a function to [get the Julia type](https://github.com/AIDASoft/podio/pull/310/files#diff-c129698a9b29360c0e27c5e4f710981b4f99524ad44c039202d750bcf349c834) in [generator_utils.py](https://github.com/AIDASoft/podio/blob/julia/python/generator_utils.py), this was a necessary step to feed the jinja2 templates with the appropriate Julia type for code generation.
After Julia type was added I made some [unittests](https://github.com/AIDASoft/podio/pull/310/files#diff-61702c3a214182795b1d726c5dc1679a64a10274b7929e4ad4ceaf8dc87c203d) for the same and added them to [test_MemberParser.py](https://github.com/AIDASoft/podio/blob/julia/python/test_MemberParser.py).
I made jinja2 [templates](https://github.com/AIDASoft/podio/blob/aae66dce1096b1c61bad3b84a12e1678f1593ce3/python/templates/MutableStruct.jl.jinja2) for Julia code generation 


*Work in progress:*
Adding the necessary preprocessing logic for julia code generation to [podio_class_generator](https://github.com/AIDASoft/podio/pull/311/files#diff-4dd2bca85ef3468fc6ba4f2701bc3131d54a47d333c9fa2112e85dddd5de988c) 
Currently some of the code generation works but still needs some fixes and additional features.

*Issues I am facing:*
Mutually recursive type declarations which exist in seperate files. This has been a long standing [issue](https://github.com/JuliaLang/julia/issues/269) on the Julia github.
I have found some workarounds namely by using Parameteric Types and Abstract types in Julia and currently am trying to find a suitable one, hence it requires some additional work.

