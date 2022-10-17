---
project: CERNBox
title: Etherpad plugin as a ScienceMeshDocs editor
author: Mohammad Warid
photo: blog_authors/MohammadWarid.jpg
date: 13.09.2022
year: 2022
layout: blog_post
logo: cernbox-logo.png
intro: |
  An Etherpad plugin to support collaborative sync share across ScienceMesh Platform
---

# Introduction:
CERNBox is a sync and share collaborative cloud storage solution used at CERN, the home of the LHC and the birthplace of the web. Used by more than 37K users, and storing over 15PB of data, it has been responding to the high demands of our diverse user community. CERNBox has responded to the high demand in our diverse community for an easily and accessible cloud storage solution, which provides integrations with other CERN services for Big Science: visualization tools, interactive data analysis and real-time collaborative editing. For the latter, a number of applications have already been integrated, by leveraging the WOPI open specifications.
ScienceMesh is an emerging pan-European federated cloud infrastructure, which aims at bringing together several sync and share platforms across Europe. In the context of ScienceMesh the integration of CodiMD has been demonstrated through WOPI bridge extensions.

The goal of this proposal is to implement an Etherpad plugin that would leverage on the CS3 WOPI server bridge extensions and allow storing Etherpad files in sync & share storages connected in ScienceMesh. Particular focus is to be put on collaborative scenarios across federated sharing. Etherpad is a popular real-time collaborative editor that features an API and a rich ecosystem of plugins.
As the project is expected to deal with the CS3 WOPI server, it could be extended to include unit-testing the bridge extensions as well as integrating the WOPI validator test suite provided by Microsoft.

## Project Goals: 
- Analyze the Etherpad plugins system and APIs, and identify the operations required to fetch/push documents.
- Implement the connector in Etherpad and in the CS3 WOPI server.
- Test the integration, possibly writing appropriate unit tests for the WOPI server.
- Document the Etherpad connector and contribute it upstream
- Unit testing the bridge extensions. (optional)
- Integrating the WOPI validator test suite provided by Microsoft. (optional)

## Community Bonding Period
- This was my very first insight over how such huge codebases are managed at CERN. Since they deal with a lot of users and data, everything has to be structured and planned accordingly, so that it can scale if required as time progresses.
- During this time period, I managed to setup the different services that WOPI server interacts with, learn about their functionalities and witnessed REVA (which is a platform that connects storage, sync and share platforms and application providers using the CS3 APIS) to open a .txt file and .md files. 
- This made me aware about how the final implementation of my work in the upstream application would look like.
- Apart from this, I was introduced to CodiMD, a similar collaborative document editing platform but for markdown files. The integration for this application is already present in the codebase which I can take inspiration from and apply it to the Etherpad plugin.

## Coding Period
- So staring off, I experimented with the Etherpad API and hooks, to create a demo plugin called `ep_demo`, wherein there was not much of a functionality associated with it. As the name suggests, it was just a demo plugin to demonstrate basic Etherpad API calls and hooks (functions that are emitted on some specific events). (The documents in Etherpad are referred to as pads, which will be referenced to henceforth). 
- The challenge here was intercepting the data on the first padLoad event (which is the event that is triggered on creating of a new pad or opening of an existing pad), and passing it down to the WOPI server as a payload that in turn would carry out the necessary actions associated with the pad.
- Naturally, this would mean that the Etherpad would maintain some global data parameters which are then passed down to the API to carry out their respective functionality. Little did I know, how complex the working of Etherpad is under the hood. To support instantaneous read writes and to keep track of all the changes happening in the pad, the application uses websockets and NodeJS cache. The contents are not exposed publicly, so I dwelled in the codebase and found out the respective functions responsible for the data transfer.

The Etherpad application serves all pads at a URL like - `http://ETHERPAD_URL/p/padId`

- To branch out the functionality of the Etherpad with our custom functionality, we settled upon a URL like - `http://ETHERPAD_URL/sciencemesh/p/padId?metadata=some_data`
- After we have extracted the metadata from a custom endpoint on the server, we can store this data someplace safe. Luckily, I can use the same database that is used by the Etherpad plugin to push and retrieve information.
- After the above, I proceeded with making a `POST` request to the WOPI server endpoint, fetching the above data from the DB and passing it as parameters in the request headers.

This implementation served well for the project which meant that the metadata can now be passed down to a custom endpoint like `http://ETHERPAD_URL/sciencemesh/p/padId?metadata=some_data` without interacting with the in-app UI and then be retrieved back to pass in as a header argument to the WOPI server.

Currently, I am investigating the WOPI server functionality for receiving the metadata and handling it, after which, I will move towards testing the complete workflow.

# Post Midterm Period

## Support for multi-user collaboration
The main goal for the project was an `open file in app` workflow, targeted to enable users of a cloud storage opening and working with their files into Etherpad, each possessing a unique ID. This was achieved by fetching query parameters from a custom `/setEFSSMetadata` endpoint, thereby passing successful or error based responses to the wopiserver, which then allocated a new url to serve the etherpad user. 
The endpoint was protected against validation checks for bogus inputs like invalid `padID` and `API` key.

## Debouncing padUpdate event
The `padUpdate` event in etherpad is supposed to fire on every new change to the etherpad. This is more noticeable when dealing with every keystroke event. To lower the amount of requests at the wopiserver’s end, the `padUpdate` event was debounced by a factor of 3000 milliseconds. After this implementation, only the latest updated change was taken into account. 

## Triggering close event on window close or when user leaves the collaborative pad
In etherpad, if the user leaves or closes the browser tab, the     `userLeave` event is invoked. This was passed down to the wopsiserver as a `URL` parameter. The user content that existed inside the database was also cleared.

## User Notifications
The deliverables to this task were notifying users about ongoing events happening behind the scenes of the wopiserver and the etherpad lite client application. 
- The wopiserver can send responses containing parameters like the message, delay, statusCode etc.
To create a seamless user experience, the task was to generate appropriate notifications using the intercepted data.
- The main issue was integrating the client-side application (Etherpad UI) with the server-side application (Etherpad backend). Since client-side applications cannot access server-side properties and vice versa (for example, the window object, etc.), this implementation is currently attempted as a websocket request-response cycle using suitable etherpad APIs.
- The notifications should be sent from the server side, where the client receives them and extracts the notification data ( message, delay and statusCode) to invoke appropriate notification popups using `ejs` templates.
- Here, the sending of data from the server side is obtained through web sockets which is intercepted at the client side for displaying notification popups. The documentation of etherpad is inconsistent with handling data functionality at the client side without any examples. This was a substantial limitation in the achievement of this task.

## NPM package release and github actions workflow
- To test the packages by different users, the package was published to the NPM registry. Along with that basic github actions workflows were set up to auto-publish a new version over to NPM by tagging a package release.

## Future Work
- I’ll try to assist with future code contributions and development of the package, enabling the needful integration of the etherpad with the wopiserver.

## Personal Experience
It has been an enriching experience with a great learning curve that I have enjoyed. I am extremely grateful for all the support and guidance I have received from my mentors especially Giuseppe to familiarise me upon great software engineering practices that I never knew of before.
Project repository - https://github.com/waridrox/ep_sciencemesh
Link to Project idea - https://hepsoftwarefoundation.org/gsoc/2022/proposal_CERNBox-Etherpad.html
