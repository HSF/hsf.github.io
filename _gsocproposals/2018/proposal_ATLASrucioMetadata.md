---
title: Rucio - Billion-row scalable and flexible metadata
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
 - CERN
 - UiO
---

## Description

Rucio is a data management system for modern large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way. Up to now, the close relationship between science metadata and the transactional state of the data management system was limiting the use of a scalable metadata catalogue, which has resulted in selected science metadata usage only. Previous attempts with non-relational database were prone to desynchronisation and inconsistency with the production system. Recent releases of the PostgreSQL and Oracle databases although provide an enticing new feature to support arbitrary JSON-encoded cells, which could allow the integration of a generic metadata component into the transactional state of Rucio directly. If you feel comfortable bringing databases to their knees with billions of rows, testing out new features at the forefront of technology, and eventually make a production-ready component out of it? Then this is the Google Summer of Code project for you!

## Expected results

### Objective 1 - Evaluate the JSON datatype in PostgreSQL up to several billion entries.

- We can provide PostgreSQL 9 installations at the necessary scale.

### Objective 2 - Evaluate the JSON datatype in Oracle  up to several billion entries.

- We can provide Oracle 12 installations at the necessary scale.

### Objective 3 - Implement a metadata component that integrates with core transactional model.

- We use the object-relational mapper SQLAlchemy for the transactional core. If necessary, support for the JSON-datatype needs to be extended there.
- The necessary distributed access via the REST interface will be provided by the team.

### Objective 4 - Implement the client interaction

- The necessary client-side libraries to interact with the REST servers.
- The necessary CLIs that use the client-side libraries for easy user

### Objective 5 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a 10 minute talk about the experience.

## Mentors

- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Cedric Serfon](mailto:Cedric.Serfon@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch){:data-proofer-ignore=""}
- [Rucio Github](https://github.com/rucio/rucio)
