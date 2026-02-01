---
title: S3 Backend for RNTuple
layout: gsoc_proposal
project: ROOT
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization: CERN
project_mentors:
  - email: jblomer@cern.ch
    first_name: Jakob
    last_name: Blomer
    organization: CERN
    is_preferred_contact: yes
---

## Description

The RNTuple I/O provides the data format and basic storage stack for HL-LHC data. It has been designed to allow for exchangeable storage backends for file system access and object stores. Proof-of-concept implementations for DAOS and S3 object stores exist but have not been further pursued. The goal of this project is to develop a robust (pre-release quality) implementation for storing RNTuple data in S3, the standard cloud storage protocol. In particular, the project needs to design and implement a URL scheme to address RNTuple objects and, secondly, an efficient HTTP base layer to access objects and byte ranges based on libcurl.



## Requirements

  * C++
  * Familiarity with HTTP protocols and object storage concepts
  * Experience with libcurl or similar networking libraries is a plus


## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.


## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentor with the string "gsoc26" in the subject. There will be a small evaluation task that we will email to you then.


## Links

  * [ROOT](https://root.cern/)
  * [RNTuple Overview](https://indico.cern.ch/event/773049/contributions/3474746/attachments/1937507/3211341/rntuple-chep19.pdf)
  * [RNTuple Code](https://github.com/root-project/root/tree/master/tree/ntuple/v7)
  * [RNTuple Tutorials](https://github.com/root-project/root/tree/master/tutorials/v7/ntuple)
  * [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)

