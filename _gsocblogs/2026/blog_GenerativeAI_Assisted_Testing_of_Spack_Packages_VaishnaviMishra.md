---
project: HSF
title: "Generative-AI Assisted Testing of Complex Spack Packages"
author: Vaishnavi Mishra
photo: blog_authors/VaishnaviMishra.jpg
avatar: https://avatars.githubusercontent.com/VaishnaviOnPC
date: 2026-08-25
year: 2026
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  Traditional Continuous Integration (CI) test suites typically validate only "leading-edge" software configurations (the newest package versions, default variants, and the latest compilers). This project aims to build a Spack extension that leverages Large Language Models (LLMs) and a self-adaptive feedback loop to autonomously explore and test high-risk, off-leading-edge configurations, discovering undeclared incompatibilities and compiler regressions that traditional pipelines miss.
---

|  |  |
| --- | --- |
| Name | [Vaishnavi Mishra](https://github.com/VaishnaviOnPC) |
| Organisation | [CERN](https://home.cern/), [HSF](https://hepsoftwarefoundation.org/), [Spack](https://spack.io/)|
| Mentor | [Wouter Deconinck](https://github.com/wdconinc) |
| Project | [Generative-AI Assisted Testing of Complex Spack Packages](https://hepsoftwarefoundation.org/gsoc/2026/proposal_Spack_AIAssistedTesting.html) |

## Introduction
The combinatorial explosion of build configurations in HPC package managers like Spack means that exhaustive testing is impossible. Package maintainers typically rely on CI pipelines that only test the default variants and the newest compilers. If a user on an HPC cluster tries to build an older version of a package with a non-default variant on a legacy compiler, they often hit undeclared incompatibilities. 

This project focuses on automating the discovery of these hidden bugs by building a generative-AI testing pipeline packaged as a Spack extension (``spack ai-test``).

## The Project
``spack ai-test`` focuses on autonomous, off-leading-edge testing. It uses an LLM to generate high-risk configurations, guided by a persistent knowledge base and multi-level context to prevent hallucinations.

The work involved building several interconnected core components:
1. **Schema Extraction:** The extension parses Spack ``package.py`` recipes into canonical JSON schemas that define valid boundaries, variants, and dependencies.
2. **Multi-Level Context Assembly:** The extension uses a retrieval-augmented, data-driven context window to guide the LLM (supporting Gemini, Claude, OpenAI) that acts as the generator:
    * Structural Risk Metrics: Analyzes risks like unbounded version ranges, cross-major-version spans, etc.
    * Version Gap Analysis: Identifies version gaps between the upstream releases and the versions in the Spack recipe.
    * Historical Failure Patterns: Focuses on specific variant flags or compilers that have high failure rates.
3. **Self-Correcting MAPE-K Loop:** The core architecture is a MAPE-K (Monitor, Analyze, Plan, Execute, Knowledge) control loop. The system reads past test history from the Knowledge Base to identify unexplored or high-failure configuration regions, target them, and record the new outcomes to refine future exploration.

In addition to the core components, the extension also includes:
* **Automated Regression Bisection:** A ``--bisect`` flag that uses exponential galloping and binary search to pinpoint exactly which release introduced a build failure.
* **Decoupled HPC Workflows:** Supports offline compute nodes by generating specs on login nodes (``--plan-only``) and executing them offline in batch jobs like Slurm (``--execute-queued``).

## Implementation Highlights (Code & Documentation)
* **AI-Test Extension Repository:** [VaishnaviOnPC/spack-ai-test](https://github.com/VaishnaviOnPC/spack-ai-test)
* **Official Documentation:** [spack-ai-test Documentation](https://VaishnaviOnPC.github.io/spack-ai-test/)

## Current State & What's Left to Do
The extension is fully functional and successfully integrates into existing Spack installations. The core MAPE-K loop, LLM integration, and bisection logic are operational.

Planned future work:
* **E4S Knowledge Base:** Manually running the extension across the E4S (Extreme-scale Scientific Software Stack) to generate a baseline dataset. This centrally hosted history will solve the "cold start" problem for new installations.
* **Persistent Log Archival:** Archiving full ``spack-build-out.txt`` and ``spack-build-env.txt`` files for specific failures to allow maintainers to perform deep post-mortem analysis.

## Challenges and Learnings
* **Preventing LLM Hallucinations:** The LLM initially hallucinated non-existent package versions. I solved this by grounding the generation using multi-level context assembly and enforcing strict static validation against the JSON schemas before reaching the concretizer.
* **The "Cold Start" Problem:** The MAPE-K loop requires historical data to intelligently target configurations, but a fresh installation has an empty history. This challenge motivated the curated E4S Knowledge Base strategy.

## References
The design of the MAPE-K loop and generative testing pipeline was inspired by recent research in autonomous software engineering:
* [From Assistance to Agency: Rethinking Autonomy and Control in CI/CD Pipelines](https://arxiv.org/abs/2605.07062)
* [LLMs as Packagers of HPC Software](https://arxiv.org/abs/2511.05626)
* [LogSage: An LLM-Based Framework for CI/CD Failure Detection and Remediation with Industrial Validation](https://arxiv.org/abs/2506.03691)

---

## Acknowledgements
Thank you to my mentor, Wouter Deconinck, for the guidance throughout this project. I am also very grateful to CERN, HSF and Spack for this opportunity.