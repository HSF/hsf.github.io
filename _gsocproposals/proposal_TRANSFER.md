---
title: Next generation of CMS data replication system
layout: plain
project: TRANSFER
organization: Cornell, Univ. of Bolognia
---

# Description

The CMS experiment at the LHC proton-proton collider developed PhEDEx as a
reliable and scalable dataset replication system. Designed in 2004, and written
mainly in Perl, it is still used today for managing multi-PB transfer loads per
week, across a complex topology of dozen of Grid-compliant computing centres.

Its architecture, instead of having a central brain making global decisions on
all CMS replica allocation, has a data management layer composed of a set of
loosely coupled and stateless software agents - each managing highly specific
parts of replication operations at each site in the distribution network -
which communicate asynchronously through a central blackboard architecture. The
system is resilient and robust against a large variety of possible failure
reasons, and it has been designed by assuming a transfer will fail (thus
implementing fail-over tactics) and being completely agnostic on the
lower-level file transfer mechanism (thus focusing on full dataset management
and detailed transfer bookkeeping). Collision data and derived data collected
at LHC that allowed to achieve the Higgs boson discovery by ATLAS and CMS
experiments at LHC were transferred in the CMS worldwide domain using this
toolkit.

## Tasks

The proposed project aims at reviewing the basic PhEDEX functionality in a
context of up-coming exa-byte HL-HLC era and exploring its implementation in Go
programming language.

The motivation for the effort is many fold:

  * even though current system is working well CMS lacks of support and
    expertise in perl programming language. We would like to leverage modern
    language such as Go to enhance concurrency model via native support in a
    language, and dependency free deployment;
  * the data volume expected in HL-HLC era will grow significantly to exa-byte
    level and we need to explore elasticity approach to handle variety of
    opportunistic resources; support ability to change access and transfer
    patterns, e.g. file data transfer vs event streaming, events vs individual
    objects, etc.;
  * implement support for user produced data in addition to centrally produced and manager by PhEDEx
  * take advantage of built-in concurrency model of the Go language and explore the scalability boundaries.

We propose the following steps:

  * built asynchronous, stateless agents which can discover and communicate with each other and thus lead to de-centralize approach for transfer system
  * implement and extend PhEDEx architecture in Go programming language
  * simulate broadcast of requests and possible failures in a system
  * integrate new Go-based agent(s) within existing PhEDEx infrastructure and assign a transfer requests to it

**Expected results**: working implementation of the system and fully tested in distributed
environment.

**Requirements**: Solid knowledge of Go-langauge, some knowledge of perl (be able to read legacy code
and translate it into Go), some knowledge of databases (Sqlite, MySQL, ORACLE), git

**Mentors**: 

  * V. Kuznetsov (vkuznet@gmail.com)
  * D. Bonacorsi (bonacorsi@bo.infn.it)
  * Paul Rossman (paulrossman@google.com)

**Links**:

  * https://github.com/vkuznet/transfer2go
  * https://www.researchgate.net/publication/228732867_Data_transfer_infrastructure_for_CMS_data_taking
