---
title: AI Assistance for CMS Computing Operations
layout: gsoc_proposal
project: CMS
year: 2026
organization:
  - CERN
  - MIT
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: h.ozturk@cern.ch
    first_name: Hasan
    last_name: Ozturk
    organization: CERN
    is_preferred_contact: yes
  - email: pmlugato@mit.edu
    first_name: Pietro
    last_name: Lugato
    organization: MIT
  - email: lavezzo@mit.edu
    first_name: Luca
    last_name: Lavezzo
    organization: MIT
---

# Description

Archi (AI Augmented Research Chat Intelligence) is an open-source, end-to-end framework for building AI agents to automate research and operational workflows. Various groups have already applied the system to their use case; the most advanced is the Computing Operations (CompOps) team at the Compact Muon Solenoid (CMS) experiment at CERN. CompOps has a private, constantly evolving, and scattered knowledge base, with scarce personnel on short term contracts. Archi puts together state-of-the-art, open-source tools like LangChain, knowledge graphs, and Model Context Protocol, and combines documentation, code, tickets, and live diagnostics to accurately retrieve relevant information, assisting operators in daily tasks, improving operator efficiency, and lessening the load on experts. Other groups at CMS deploying Archi for their use case include the Data Quality Monitoring (DQM) team and a group focusing on retrieval of the vast analysis code and documentation across the CMS landscape.

The goal of this GSoC project is to work on the development of autonomous agents to perform non-trivial computing operations at CMS, a task which integrates large language models with highly accurate retrieval, expert domain knowledge, heteregenous data sources, and agentic tools. The student will get familiarity with state-of-the-art and in-demand agentic tools like LangChain and MCP. like LangChain and MCP. 


## Task idea

- Identify operational tasks apt for automation
- Work with experts to define the specs of the agent: input data sources, actions it can take, desired outcomes
- Define sandbox limitations of the agent, policy of human review for first phase of roll-out
- Define metrics of success and data collection
- Implement, with the Archi framework, a prototype of the agent
- Deploy agent to operations and demonstrate impact


## Expected results and milestones

- Design report on the specs of agent
- Develop a prototype of the agent
- Integrate the agent into operations with domain experts
- Evaluate the performance of the agent based on desired outcomes

## Requirements

- Python programming skills
- Familiarity with Git and GitHub-based collaboration (PRs, code review)
- Basic Linux command-line skills
- Ability to communicate clearly and work iteratively with domain experts
- Familiarity with LLM tooling and agent frameworks (e.g., LangChain) and/or Model Context Protocol (MCP)
- Exposure to retrieval systems (vector search/embeddings), knowledge bases, or knowledge graphs
- Experience with containers (Docker/Podman) and/or CI testing
- Interest in (or prior exposure to) HEP/CMS computing operations workflows

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.


## Links

- https://github.com/archi-physics/archi