---
project: Belle II
title: Belle II Event Display with Phoenix
author: Hieu Le Cong Minh
photo: blog_authors/HieuLeCongMinh.jpg
date: 25.08.2023
year: 2023
layout: blog_post
logo: belle2-logo.png
intro: |
    I am excited to share my journey and insights from taking part in the Belle II Event Display with Phoenix project during Google Summer of Code 2023. This project aimed to create an accessible and user-friendly web application for Belle II event displays by harnessing the capabilities of the Phoenix framework.
---

# About Me

My name is Hieu Le Cong Minh, a third-year undergraduate student at the Tokyo Institute of Technology. I was both thrilled and honored to be selected to participate in the **Belle II Event Display with Phoenix** project during the Google Summer of Code 2023.

# Project Description

The Belle II software plays a crucial role in analyzing extensive datasets acquired through the international Belle II collaboration. To visualize events, the Belle II software employs ROOT TEve. However, this necessitates installing the complete Belle II software on a local machine for execution. Unfortunately, this approach proves unsuitable for contemporary client-server-based systems, posing challenges for users seeking efficient access to the necessary information.

As proposed by the organization in GSoC 2023, the project aims to address this issue by developing a web application that utilizes the Phoenix framework-based event display for Belle II. This application will allow users to view detector geometry, recorded signals, and reconstructed objects from Belle II data in a web browser. By doing so, it enhances accessibility and user experience while ensuring data security.

# Technologies

* `typescript`, `angular-cli`
* `phoenix`
* `JSRoot`

# Project Procedure

Throughout the project, I followed a carefully planned procedure comprising five distinct steps: **[Preparation](#preparation--community-bonding-period)**, **[Data Extraction and Visualization](#data-extraction-and-visualization--official-coding-phase-begins)**, **[User Experience Improvement](#user-experience-improvement)**, **[User Feedback Collection](#user-feedback-collection)**, and **[Documentation](#documentation--user-and-developer-guides)**.

## Preparation – Community Bonding Period

The initial phase involved approaching the Belle II community and gaining a fundamental understanding of the Belle II software, particularly the event display component.

During this phase, I tackled the challenge of installing and configuring the Belle II software on my local machine. The complexity of this task underscored the importance of the project, further fueling my motivation. With the software in place, I conducted a preliminary event display to grasp the project's scope and potential as an alternative to the existing software.

Once I had a clear grasp of the Belle II event display structure, I created a preliminary version of the Phoenix event display. Drawing on my prior experience, I had already developed a Phoenix application to display a cube and sphere during the proposal process. By applying this knowledge and learning how to use `JSRoot`, I successfully extracted and displayed the Belle II detector geometry within a Phoenix web application during the community bonding period. This accomplishment significantly accelerated the progress of the project.

A screenshot of the detector geometry display conducted during this period is shown below.

![image](https://github.com/HieuLCM/gsoc2023_belle2_display/blob/main/docs/source/assets/detector.png?raw=true)

## Data Extraction and Visualization – Official Coding Phase Begins!

Building upon the successful extraction and display of the detector geometry, I transitioned smoothly into the coding phase.

The Belle II event display involves showcasing two crucial components: the detector geometry and reconstructed objects.

For the detector geometry, I developed a simplified version based on the work done during the **Preparation** step.

Extracting and utilizing the necessary data to render objects on the web browser presented a unique challenge due to Belle II's distinct format for storing data in `.root` files. Overcoming this challenge was made possible with invaluable support and guidance from my mentors. Through a systematic approach, I successfully extracted and displayed the reconstructed objects.

## User Experience Improvement

With the focus on showcasing vital data accomplished in the previous step, attention turned to addressing multiple user interface issues.

Regular weekly meetings with my mentors played a pivotal role. Collaboratively, we identified and discussed the shortcomings of the existing event display, proposing necessary improvements. I subsequently implemented these changes and presented them in subsequent meetings. This iterative process led to significant enhancements, particularly in terms of user experience.

## User Feedback Collection

Once I had resolved the issues identified in the weekly mentor meetings and received their approval, I showcased the project to Belle II software developers during a weekly meeting. Here, I introduced the project, demonstrated its functionality, and actively sought feedback and suggestions.

The users' experience provided valuable insights, resulting in constructive feedback and suggestions. Armed with this input and after further discussions with mentors, I fine-tuned the application to align with the users' needs. The receipt of numerous positive feedback messages was an incredibly gratifying moment.

## Documentation – User and Developer Guides

With the application refined based on user feedback, I proceeded to create comprehensive documentation catering to both users and developers.

For users, the documentation focuses on effectively navigating and utilizing the application. Meanwhile, the developer-oriented documentation provides guidance for those interested in extending the application's capabilities, such as adding new event objects or modifying existing features.

After all, I presented again at the Belle II software developer meeting, discussing the improvements and introducing the documentations.

Through these meticulous steps, the **Belle II Event Display with Phoenix** project has evolved into a user-friendly, feature-rich, and well-documented tool, contributing to the accessibility and utility of Belle II's event display capabilities.

# Deliverables

After more than three months of working on the project, I successfully created a web application for the Belle II event display, accompanied by documentation. 
An event displayed by the application, along with a brief UI explanation, is shown below.

![image](https://github.com/HieuLCM/gsoc2023_belle2_display/blob/main/docs/source/assets/event_display.png?raw=true)

The web application serves as a tool that allows scientists and physicists to import events from mdst `.root` files, which contain data, and then view them directly in a web browser. By leveraging the Phoenix framework and adding custom features, the application provides a user-friendly environment for event display, complete with intuitive user interface controls.

Comprehensive user and developer documentation is also provided to ensure efficient utilization of the application and to support future development.

*Link to the application repository implemented during GSoC 2023: **[github.com/HieuLCM/gsoc2023_belle2_display](https://github.com/HieuLCM/gsoc2023_belle2_display)**
I have also initiated a new repository for further development beyond GSoC 2023 at **[github.com/belle2/display](https://github.com/belle2/display)***

*A demo version of the application was deployed and accessed via **[gsoc2023-belle2-display](https://gsoc2023-belle2-display.netlify.app/#/)**.
The corresponding documentation: **[gsoc2023-belle2-display-docs](https://gsoc2023-belle2-display-docs.netlify.app/)***

# Future Plans

The **Belle II Event Display with Phoenix** project still holds potential for further development beyond GSoC 2023. Plans include implementing a server for the application and integrating it into the current Belle II software ecosystem. Additionally, in terms of the frontend, along with the development of Phoenix, the application can be further enhanced in the future. This necessitates developers to continuously maintain and improve the app. Furthermore, depending on the different usage purposes, each developer can also customize the code based on their preference.

I am personally enthusiastic about continuing my involvement and contribution to the project if my schedule permits. Moreover, I will continue to follow the development of the application and will always be pleased to answer questions and provide support for any related issues.

# Personal Experience

Participating in the Belle II project during GSoC 2023 presented me with a precious opportunity to apply and elevate my programming skills within a meaningful context, making a contribution to the advancement of particle physics, even at a modest level. Belle II not only stands as an open-source coding organization but also a vast intellectual community. Being part of it has been a remarkable journey for me.

Throughout the project, I delved into multiple new technologies and effectively applied them to a real-world project. This experience was an excellent learning opportunity for me.

Additionally, I would like to extend a heartfelt thank you to my mentors, Thomas Kuhr (LMU) and Giacomo De Pietro (KIT), for their unwavering support, which has been instrumental in helping me complete the project.
