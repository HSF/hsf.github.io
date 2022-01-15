---
title: Rucio - Extension with new ways to authenticate & authorize
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
 - UOslo
 - CERN
---

## Description

Rucio is a multi-location data management system for large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way. Currently, Rucio supports different kind of authorization credentials like SSH public keys, Kerberos, or passwords. This proposed extension is to empower Rucio with third party authentication services and libraries, from the authentication with Rucio to the operational authorization against the storage systems.

- The first part of the work would be to define a list of new and popular used authentication systems and evaluate their corresponding python libraries and its dependencies, .e.g., like Macaroons, OpenID, or signed URLs.
- The second part will be to extend Rucio and interface with these new credentials.
- Finally, the last part will be to implement the most common use cases like uploading or downloading data, and having all distributed service interactions from Rucio to storage with the new authentication and authorization mechanism.

## Expected results

### Objective 1 - Setup a Rucio development environment and familiarise with the Rucio code

### Objective 2 - Survey of authorization credentials mechanisms

 - Strong focus on OpenId and Macaroons.

### Objective 3 - Extend new authentication credentials within Rucio

### Objective 4 - Implement some basic data management workflows

- For example, uploading data from storage with different authorization credentials

### Objective 5 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a 10 minute talk about the experience.

## Requirements

- Python
- Linux development environment (bash, git, ...)

## Mentors

- [Vincent Garonne](mailto:vgaronne@gmail.com)
- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Github](https://github.com/rucio/rucio)
