---
title: "HSF Generator Meeting #15, 17 June 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #15, 17 June 2021

*Agenda: <https://indico.cern.ch/event/1042656>*

Present (remote): Efe Yazgan, Josh McFayden, Andrea Valassi, Graeme Stewart, Simon Plaetzer, Andrzej Siodmok, Patrick Kirchgaesser, Andreas Papaefstathiou, Aidin Masouminia, Michal Kreps, Zach Marshall

Apologies: Alexander Grohsjean, Gurpreet Singh Chahal, Peter Richardson, Stefan Gieseke

## News

Josh: virtual Les Houches ongoing this week, unfortunately this means lower attendance for us today. And there are many other experiment events.

## Herwig report for LHCC review 
Speaker: S. Plaetzer

Simon presents the slides describing the answers from the Herwig team to the question received for the second phase of the LHCC review of HL-LHC computing.
- Emphasis is on showers to be ready for NNLO matching.
- Some slides come from a recent CMS tutorial, documentation (as well as physics papers) is an important part of the work. Physics papers is what guarantees the funding to the Herwig authors.
- One change compared to Herwig++ was disentagling building the event generator from sending off jobs to the Grid (a bit similar to what Sherpa or also Madgraph can do).
- Under the hood, there are software components that essentially match the different factors in the cross section factorization formula (except for multi parton interactions). There is also a large ME library, and interfaces to MadGraph, OpenLoops and other ME providers.
- A very delicate point is the shower evolution, how to switch it off at the right scale.
- A lot of new work on logarithmic accuracy and other theory developments. Many hooks added for reweighting.
- BSM support, with good agreement to MG5aMC.
- Sudakov algorithm is the workehorse of shower emissions, but it is a troublemaker for on-the-fly weights and new shower improvements because it results in prohibitive weight distributions. After a few emissions, things almost diverge. You need a resampling algorithm. After each emission you try to compress the weight distribution (~resampling).
    - Josh: is this alphas scale variations for instance? Simon: yes, precisely.
- Coming to the direct questions. 
    - Funding is a serious issue. Any funding for generator development must be strongly linked to a very strong physics case. In some cases this may not be what the experiments need. To fund the bread and butter of what the experiments need, one would need different specific funding.
    - To improve on NLO EW and NNLO, need some physics changes in the showers.
    - Refactoring/rebuilding some parts of the ThePEG framework is needed. Maybe the HSF can help with this? This was an innovative framework at the time, but now is very old.
        - Josh: discussed with Sherpa weeks ago about better interfaces to allow plugging in different components. Stefan Hoeche seemed to be on board with this idea. Was this the initial idea behind ThePEG? Simon: yes this was an idea at the time. Andrzej: the idea of ThePEG was tempting, but essentially the other generators were not interested. It is difficult, even more difficult than LesHouches file format, which was difficult in itself. Andrea: strongly support the idea of identifying and agreeing on some interfaces.
        - Efe: why is ThePEG dropped in the first place.
            - Andrzej/Simon: Mainly because of sociological reasons. 
            - Simon: Scientifically and technologically there is no question ThePEG or something like ThePeg will be very useful. 
        - Efe: was there also an issue of licensing for ThePEG? Simon: this is GPL, in CMS there was an issue of GPL2 vs GPL3.
        - Andrea: who is using this? Simon: there was an attempt to pull in Pythia but they are not in it. It is used also in Ariadne. For Herwig it is absolutely essential.
    - Port to GPU, no plans. Things like showering are clearly no good for SIMD. 
        - Andrea: the ME calculation is vectorizable, could you consider interfacing to that part in a GPU/vector implementation? Simon: matchbox actually already heavily relies on interfacing to MG5aMC for MEs.

Additional comments/discussion:
- Andrzej: might have a student who could work on GPUs, but very limited knowledge. How could we supervise him/her? Andrea: in general, the Compute Accelerator Forum in HSF.  More specifically, the MG on GPU activity, we have meetings on Monday every one or two weeks. Can send you some pointers.
- Josh: thanks for highlighting the issue of funding. You made this much more explicit than other generator groups. If a FA accepted the argument that they fund one person to do half physcs and half software, would you accept that and be able to supervise them? Andrzej: actually we might hire a computer scientist. It would be very interesting to have a common project with software engineers! It could be interesting to work with HSF on these things.
- Andrea: what are the prospects of KrkNLO for reducing negative weights? Andrzej: it has no ngeative weights, but it is limited to only two processes for the moment. It can be used in Herwig.

## AOB

- The next meeting will be on June 24, discussing POWHEG.
