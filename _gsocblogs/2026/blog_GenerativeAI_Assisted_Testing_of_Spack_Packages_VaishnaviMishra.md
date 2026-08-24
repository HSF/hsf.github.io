---
project: HSF
title: "Generative-AI Assisted Testing of Complex Spack Packages"
author: Vaishnavi Mishra
photo: blog_authors/VaishnaviMishra.jpg
avatar: https://avatars.githubusercontent.com/VaishnaviOnPC
date: 25.08.2026
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
Hi! I am Vaishnavi Mishra, a Final Year B.Tech. student, and this summer I worked with the HEP Software Foundation as a Google Summer of Code contributor at CERN-HSF (Spack). 

The combinatorial explosion of build configurations in HPC package managers like Spack means that exhaustive testing is impossible. Package maintainers typically rely on CI pipelines that only test the default variants and the newest compilers. If a user on an HPC cluster tries to build an older version of a package with a non-default variant on a legacy compiler, they often hit undeclared incompatibilities or compiler regressions that the maintainers never saw. 

My project focused on automating the discovery of these hidden bugs by building a generative-AI testing pipeline packaged as a Spack extension (``spack ai-test``).

## The Project: What I Did
This project is a Spack extension that focuses on autonomous, off-leading-edge testing. It uses LLM to act as a combinatorial configuration generator that targets the high-risk configuration space regulated using a persistent knowledge base, multi-level contexting to prevent hallucinations and generate cases with higher failure rate during build processes.

The work involved building several interconnected core components:
1. **Schema Extraction:** The extension starts off with parsing Spack ``package.py`` recipes into canonical JSON schemas for valid boundaries, variants, and dependencies of the package.
2. **Multi-Level Context Assembly:** The extension uses a retrieval-augmented, data-driven context window to guide generation:
  * Structural Risk Metrics: Analyzes risks (e.g., unbounded version ranges, cross-major-version spans) to guide the LLM towards possible boundaries.
  * Version Gap Analysis: Identifies version gaps between the upstream releases and the versions in the Spack recipe.
  * Historical Failure Patterns: Focuses on specific variant flags or compilers that historically show high failure rates.
3. **LLM Configuration Generation:** Using this context, the LLM (supporting Gemini, Claude, OpenAI) acts as a targeted combinatorial generator, deliberately generating specs in the high-risk configuration space.
4. **Self-Correcting MAPE-K Loop:** The core architecture is a MAPE-K (Monitor, Analyze, Plan, Execute, Knowledge) control loop. The system never operates blindly. It reads past test history from a persistent Knowledge Base to identify unexplored or high-failure configuration regions. The LLM is then prompted to target those specific areas. After execution, outcomes (pass or fail) are written back to the Knowledge Base, allowing the system to refine its exploration strategy over time.

In addition to the core components, the extension also includes:
* **Automated Regression Bisection:** The ``--bisect`` flag that works on exponential galloping and binary search to locate the exact release where a deterministic build or test failure was introduced.
* **Decoupled HPC Workflows:** It supports offline compute nodes. The ``--plan-only`` mode generates specs on internet-connected login nodes, queuing them in a Knowledge Base, while ``--execute-queued`` processes them offline inside batch jobs (e.g., Slurm).

## Implementation Highlights (Pull Requests)
* **AI-Test Extension:** [VaishnaviOnPC/spack-ai-test](https://github.com/VaishnaviOnPC/spack-ai-test)
* **Documentation:** [spack-ai-test Documentation](https://VaishnaviOnPC.github.io/spack-ai-test/)

## Current State & What's Left to Do
The ``spack-ai-test`` extension is fully functional and successfully integrates into existing Spack installations. The core MAPE-K execution loop, the multi-provider LLM integration, and the automated bisection logic are operational. The project's documentation is live and hosted via GitHub Pages.

While the core development is complete, there is still future work planned:
* **E4S Knowledge Base:** Manually running the extension a few times for each package in the E4S (Extreme-scale Scientific Software Stack) to generate a baseline dataset. This history will be hosted centrally so users can pull it, solving the "cold start" problem for new installations.
* **Persistent Log Archival:** Adding a feature for the archival of full ``spack-build-out.txt`` and ``spack-build-env.txt`` files. Currently, only the failure status is recorded, archiving these logs will allow maintainers to get deep analysis of compiler errors.

## Challenges and Learnings
* **Preventing LLM Hallucinations:** The LLM initially hallucinated non-existent package versions and variants. I solved this by guiding the generation using multi-level context assembly and enforcing strict static validation against the extracted JSON schemas before specs reach the concretizer.
* **The "Cold Start" Problem:** The self-correcting MAPE-K loop requires historical data to intelligently target high-risk configurations. On a fresh installation, this history is empty. This can be prevented by E4S Knowledge Base.

## References
The architectural design of the MAPE-K loop and the context-aware generative testing pipeline was heavily informed by recent research in autonomous software engineering. The following papers were instrumental in shaping this project:
* [arXiv:2605.07062](https://arxiv.org/abs/2605.07062)
* [arXiv:2511.05626](https://arxiv.org/abs/2511.05626)
* [arXiv:2506.03691](https://arxiv.org/abs/2506.03691)

---

## Acknowledgements
Thank you to my mentor, Wouter Deconinck, for the guidance throughout this project. I am also very grateful to CERN, HSF and Spack for this opportunity.
