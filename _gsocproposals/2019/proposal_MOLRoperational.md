---
project: Molr
title: Molr - Operational
year: 2019
layout: gsoc_proposal
organization: CERN
---

# Description

Connecting heterogeneous systems can pose difficulties due to different technologies and legacy code. In most of the cases in CERN LHC operations the requirements break down to triggering calculations or functionality of an existing system. Keeping in mind this scenario, the idea for Molr was born and a first implementation was developed. Molr is a remote execution and debugging framework based on a command-response communication protocol. It is designed to be easy to integrate into existing systems to expose operations via so-called Missions.
In the view of LHC Run 3, we want to extend the functionalities of Molr to finally use it in production to control various operational systems.

## Terminology
In contexts of remote code execution we often see the same terminology, whether it is agents, service managers, controllers, etc. For Molr we decided to introduce a new, funnier, terminology that is both different (and less confusing) from other similar approaches and well known by most people. By using the analogy of spy adventures, we call our agents Moles. A Mole can be included in a project to expose certain functionality. A Mole exposes its services through Missions (e.g. Java code that triggers a measurement). A Mole might be able to execute different kind of Missions (e.g. a Java Mole could execute any Mission expressed in Java). In order to reduce coupling in the system, we introduced the idea of Supermole that can be seen as a hub for Moles. A Supermole acts as a facade for multiple Moles and re-exposes their Missions. More detailed explanation of the Molr concepts can be found in the official web page [https://molr.io/](https://molr.io/).

## Tasks

We propose the following steps:

* Typed Molr missions: simplification of the mission concept when the input/output types are already known (much like a remote procedure call)
* Mission parameters sanitization and validation: at the moment only String and Doubles are allowed as mission parameters/results, this can be extended, e.g. to match the valid types of [JSON Schema](https://json-schema.org/).
* Persistence and runtime cleanup of the missions on the moles, e.g. `LocalSuperMole`: this kind of mole concentrates other moles and missions by re-offering their missions. It is important to persist the registered moles in the supermole and to be able to clean the missions state (preferably by keeping only the result) according to different policies.
* Registration of new mole instances at runtime. 

## Expected results

Providing a Molr version which is close to operational needs, and thus is able to support state persistence and recovery, supports diverse input/output parameters and that provides maintenance policies.

## Requirements

- Java
- Git
- Web technologies and protocols
- Bonus: Spring DI and Spring Web

## Mentors

  * [Andrea Calia](mailto:andrea.calia@cern.ch)
  * [Michi Hostettler](mailto:michi.hostettler@cern.ch)
  * [Kajetan Fuchsberger](mailto:Kajetan.Fuchsberger@cern.ch)

## Links

  * [Molr](https://molr.io/)
  * [Spring Framework](https://spring.io/)
