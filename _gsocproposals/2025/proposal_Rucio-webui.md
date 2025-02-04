---
title: Rucio WebUI Revamp
layout: gsoc_proposal
project: Rucio
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-November
organization:
    - CERN
---

## Description

[Rucio](https://rucio.cern.ch) is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Originally developed to meet the requirements of the high-energy physics experiment ATLAS, Rucio has been continuously enhanced to support diverse scientific communities. Since 2016, Rucio has orchestrated multiple exabytes of data access and data transfers globally.

The [Rucio WebUI](https://github.com/rucio/webui) is a Next.js application utilized by various users within collaborating communities to access, monitor, and manage their distributed data. Key features of the Rucio WebUI include:

- **SDK for Streaming:** Facilitates seamless data streaming from the Rucio server to page components, ensuring a responsive user interface.
- **Typed in TypeScript with Generics:** Strict typing ensures code integrity and enhances development efficiency.
- **Accessibility and Responsiveness:** Designed with accessibility and responsiveness in mind, ensuring usability across various devices.
- **Testing and Stability:** Extensive testing ensures robustness and reliability in all components.
- **Feature Toggles:** Dynamic feature toggles provide flexibility in enabling or disabling specific functionalities as needed.
- **Component Library:** Utilizes Storybook and TailwindCSS to enhance development speed and consistency.

## Tasks

1. **Upgrade to Next.js 15, React 19, TailwindCSS 4.x:**
   - Migrate the existing codebase to Next.js 15 to leverage the latest features and performance improvements.
   - Utilize Server Side Rendering and React Query in Client Side Components to enhance data-fetching capabilities.
   - Migrate `tailwind.config.js` to new CSS based configuration for TailwindCSS 4.x. 

2. **Enhance User Experience for Site Administrators and Operators:**
   - Currently the WebUI focusses on List/Get views with the exception of allowing users to Create Rules. Add features to Create/Edit resources for site administrators and operational experts.
   - Investigate legacy views in the previous [Flask application]() and migrate them to the new WebUI.
   - Redesign these views to be more user-friendly, incorporating feedback from site administrators and operators.

3. **Migrate Authentication to NextAuth (Auth.js):**
   - Transition existing x509 and user/password authentication mechanisms to NextAuth.
   - Ensure compatibility with various authentication flows, including OAuth and OpenID Connect.
   - Develop an RBAC system to ensure users have access only to functionalities relevant to their roles, enhancing security and usability.

4. **Transition to a Monorepo Structure:**
   - Migrate the Rucio WebUI to a monorepo structure to improve code organization and facilitate the sharing of common components across different projects.

## Requirements

**Mandatory:**
- Proficiency in React.js and Next.js
- Experience with TailwindCSS
- Strong knowledge of JavaScript (ECMAScript 6) and TypeScript
- Familiarity with Python 3 and Flask
- Proficiency with Linux, Git, and Docker

**Good to Have:**
- Understanding of NX Monorepos
- Experience with AGGrid Data Tables
- Experience with GitHub Actions
- Knowledge of HTTP REST APIs
- Familiarity with OpenID Connect and x509 protocols

## Expected Results

By the end of GSoC 2025, we expect to have a revamped Rucio WebUI that:
- Is upgraded to Next.js 15 with integrated React Query.
- Utilizes both client and server-side components as per React 19's stable features.
- Supports TailwindCSS 4.0 for a modern design system.
- Offers enhanced user experiences tailored for site administrators and operators.
- Employs NextAuth for streamlined authentication processes.
- Implements a robust RBAC system.
- Adopts a monorepo structure for improved code organization and component sharing.

## Mentors

- **[Mayank Sharma](mailto:mayank.sharma@cern.ch)** (University of Michigan, Ann Arbor)
- [Martin Barisits](mailto:martin.barisits@cern.ch) (CERN)

## Links

1. [Rucio GitHub Repository](https://github.com/rucio/rucio)
2. [Rucio UI Presentation](https://docs.google.com/presentation/d/1mXw8Xo3bknO8Ahyd6RvKlNP0OwgXdKJxz6fWiuLYOdI/edit?usp=sharing)
3. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
4. [Rucio System Overview Journal Article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
5. [Rucio Operational Experience Article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
