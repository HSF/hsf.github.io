---
title: "Licensing WG Meeting, February 21, 2017"
layout: default
---

# Licensing Working Group Meeting, February 21, 2017

Present: Pere Mato, John Harvey, Liz Sexton Kennedy, Michel Jouvin, Dave Dykstra, Grigory Rybkin, Jim Pivarski, Andrea Valassi, Giacomo Tenaglia, Graeme Stewart, Andrew MacNab, and Nick Ziogas and Myriam Ayass from CERN KT

[*Agenda*](http://indico.cern.ch/event/614901/)

## CERN/IT Licensing Status - G. Tenaglia

Current situation from the Open Source License Task Force

-   GPLv3 is the default license for SW developed at CERN, with LGPLv3 as an alternate one (in particular recommended for libraries) and Apache 2 as an exception

-   Each source file must contain a “Copyright $year CERN”, the license and an acknowledgment of CERN as an intergovernmental organisation (impact on courts that can be used to solve conflicts).

-   Non OS license possible as part of specific collaboration agreements

Giacomo is a point of contact for licensing issues at CERN. Trying to raise developer awareness.

-   A CERN-FOSS group created with people outside IT, maybe our HSF licensing group should try to partner with this group, and find other similar groups.

Inventory of CERN SW in progress: probably some of the SW should be registered into the HSF SW&C knowledge base

## CMS Licensing Status - L. Sexton Kennedy

Since July 2011, CMS collaborators writing SW to take, simulate, reconstruct and analyze CMS data give up ownership of that SW when they commit it to the CMSSW.

-   Similar to what happens for HW put in the detector…

-   CERN offered to act as the legal entity for the benefit of CMS

-   This applies also to older SW: may be challenged in court but an experience with HW property rights brought to court in Germany by a postdoc was won by CMS...

But not agreement yet on the license to use… currently blocked

-   Would prefer a permissive license but depends on some GPL SW that we link to, in particular generators… Probably partly due to some misunderstanding of the CERN recommendations, and about the licensing implications by generator developers.

-   Andrew: nothing prevents using an Apache license for the CMS-developed SW and relicensing it to GPL on the fly when producing a binary distribution linked against GPL libs. Liz will pursue this within CMS.

-   Partly related to packaging issues: if packaging allows an opt-out of a GPL component (for example it is possible to remove MathMore lirbraries from the ROOT distribution) , the packaging options may offer a possibility to fix the viral license issue.

## BNL Licensing Status - B. Viren

Initially some push for a modified BSD but there is a recent move to keep to standard licenses (as recommended by this group) like GPL/LGPL

-   Recent contact with LLNL to discuss their experience with LGPL for Spack which has been proposed as a solution by the HSF packaging working group.

## ATLAS Licensing Status - G. Stewart

Very similar to CMS now… All the code copyrighted to CERN as the ATLAS Collaboration is not a legal entity

-   Important work was done to not claim code that other people wrote (some in Athena)

-   There has been no public release of the code so far

Recent question to the collaboration about objections to a permissive license, and a public release of the code: none so far

-   Most people comfortable with Apache 2

-   The GPL license of Fastjet remains a problem that is being worked on… No clear solution yet (even dynamic linking is not a firewall from the GPL)

## Discussion

We need to explain to developers, in particular the generator community, the difference between (viral) licensing and recognition, and in particular the problems resulting from using a GPL license for small pieces of work, inserted into larger multi-purpose frameworks.

-   Plan specific meetings or a workshop

-   A European project about generators, MCNET, recommended to use GPL to ensure that the code is not broken down into different parts and that there is recognition for the work done by the developers… Probably impacted the decision by several projects...

Nick says license is defined by the copyright owner, not the author. So it depends on where and when the code was written and which institution employed the author. Nick also confirmed that industry groups do not like to work with GPL’d software due to its viral nature. Liz provided a specific example of that in email after the meeting, see below.

## INFN Views - F. Giacomini

*(Input received after the meeting, sent by email to HSF Forum list on 23/2, added to the summary for reference. INFN view has thus not been discussed during the meeting).*

- the analysis and the conclusions are in line with the (much more thorough) work produced by the Open Source Task Force established at CERN

- INFN is leaning towards the adoption of the [*European Union Public License*](https://joinup.ec.europa.eu/page/eupl) (EUPL) 1.2, which is a copyleft license created on the initiative of the European Commission, compatible with the legislation of the EU and all the EU Countries and officially available in all the EU languages
- the choice of a copyleft license instead of a permissive one helps when dealing with Technology/Knowledge Transfer matters, because it protects better against third-party appropriation
- the EUPL is the **\*default\*** license, in case there are no other constraints or obligations, for example because one is part of CMS or ATLAS

*Note: INFN is aware that EUPL cannot be adopted by CERN who as an international organization cannot be brought in national courts.*

*Note also that in the context of experiment collaborative software (where appropriation is not a concern), a permissive license may make collaboration with industry easier. Liz wrote email to HSF Forum list on 06/03, sharing an instance when CMS participation in an Nvidia hackathon had to be abandoned because Nvidia was not sure if collaborating with CMS would endanger its own IP.
*
