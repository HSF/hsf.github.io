---
title: "HSF Generator WG Meeting #23, 7 July 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1146150/>

Event Generation with Julia

Discussion:
* Liz: Are you collaborating with computational experts, or do you still need domain expertize, how do you do this? (Josh had the same question.)
    * Uwe: This is an excellent question. Something like ALPAKA or low level things are written by IT people, programming experts; actually compiler constructors. This is what we need here and we have a colleague of mine who is a compiler constructor. In our institute we have two levels; one is scientist, i.e. domain experts like me, the other is people like, for example, who can make ulia usable in different architectures, programmers, compiler constructors. 

* Josh: Something along the same lines. Funding is for a fraction of a person? Is that how it works? A lot of people take different projects 
    * Uwe: Professional support is not bounded to a project, so these are full time positions. Job is to help scientists in their software projects. But you can actually also bound people to projects up to work 100%. This means that the payment model is different than that of scientists. 
    * Josh: It sounds like it is kind of research software engineer.
    * Uwe: Yes, something like that. It is also something like the engineers who help build the experiments. They are not technicians and they are not scientists either. And they are not paid like postdocs. 
* Graeme: Is parallelization all being done through DAG? So, is it able to see which parts depending on the dagger and throw bunch of different threads and do them in parallel?
    * Uwe: This is an actual work in progress but we have written a paper on that; how to actually schedule function calls. It just starts with throwing tasks into executor. In Julia you know how many calls you have. You know how many floats you will multiply when you do a function call. This is like the heuristic dagger. Dagger schedules things down to the float multiplication. We are also working on a different way of doing it but it is not published yet.  
    * Graeme: I would not say this is super user-friendly code to write because they have to do the decomposition themselves.
    * Uwe: But on slide 20 what you see here is the optimized code. What you can do in Julia: you can start with the Feynman diagram itself (left of side of slide 19) and do all the optimization. The other step is to do the diagram generation itself which is deduced from the previous step. 
    * Graeme: Yes, this is a much better way of doing it. You give the user a high level interface 
* Graeme: Do you use any sort of vectorization? Does Julia have an easy way to access vector types as well or is that something not explored at the moment? 
    * Uwe: Yes. Julia fully supports SIMD. It uses SIMD as a macro that finds what type of vectorization is available in your architecture and then you can internally write vectorizations if you need. This is actually depended on the memory model used but things I showed here are agnostic to the memory model. We have not yet decided what is the best way to do that. But Julia is generic enough. This is to be explored a bit more. 
* Josh: What you showed is all about QED. Is it philosophyically complicated to expend this to other Feynman rules, e.g. QCD even at the perturbative level, or QED+weak interactions etc. 
    * Uwe: We have this in mind as a far away project for other interactions as well. We started with QED and laser physics side etc. because of our backgrounds. Not easy but doable because you can write the interfaces quite generic for instance in QED model.  
    * Josh: May be one can start with a very simple process (e+e- -> mu+mu-) even there you can do QED and then you can compare this to other generators to compare CPU usage and things like that. That would be very interesting already.  
    * Uwe: All design is motivated from MG5_aMC and Sherpa et al. So it did not come out of nowhere. But we do not want to re-write MG but we can compare and use some parts of MG. 
