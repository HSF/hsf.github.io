---
title: Automated Software Performance Monitoring for the ATLAS experiment
layout: gsoc_proposal
project: ATLAS
year: 2026
organization:
  - ANL
  - University of Washington
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: maciej.szymanski@cern.ch
    first_name: Maciej
    last_name: Szymanski
    organization: ANL
    is_preferred_contact: yes
  - email: tatiana.ovsiannikova@cern.ch
    first_name: Tatiana
    last_name: Ovsiannikova
    organization: University of Washington
    is_preferred_contact: yes
---

## Description

ATLAS is one of the particle physics experiments at the Large Hadron Collider (LHC) at CERN. The LHC Upgrade (the so-called High Luminosity phase) will allow for even more detailed exploration of fundamental particles and forces of nature. To ensure successful experiment operation in the unprecedented conditions, it is vital to systematically monitor software performance and guide optimization, especially in light of software paradigm shifts and detector upgrades. The Software Performance Optimization Team (SPOT) monitors software performance across the entire processing chain in the ATLAS experiment. The goal of this GSoC contribution is to enhance the SPOT framework by implementing automated, intelligent monitoring to detect anomalies, flag concerning patterns, and alert developers in real time.

## Task Ideas

- Implement automated performance monitoring using ML/statistical approaches
- Establish baselines and expected performance ranges
- Detect anomalies
- Generate automated alerts for significant changes or failures
- Improve visualization dashboards
- Modernize test orchestration scripts

## Expected Results and Milestones

- Familiarization with ATLAS and SPOT infrastructure and performance datasets
- Data exploration and algorithm evaluation
- Implementation of the automated monitoring pipeline
- Testing, validation, tuning
- Integration with alerting systems, documentation

## Requirements

- Python programming skills
- ML fundamentals
- Time series analysis or anomaly detection experience
- Interest in scientific software optimization

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in ML/particle physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [ATLAS Experiment](https://atlas.cern/)
- [SPOT Docs](https://atlas-software.docs.cern.ch/athena/performance/)
