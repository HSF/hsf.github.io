---
title:  Event Streaming Service - A new approach to event processing
layout: gsoc_proposal
project: ATLAS
year: 2017
organization:
  - BNL
---

## Description

Over the past 2-3 years ATLAS has developed an innovative new approach to HEP data processing, the ATLAS Event Service (AES), which dispenses with the decades-old file-based processing model in favor of fine grained, dynamic workflows controlled and managed at the event level (~10min processing time quanta). The AES streams fine grained processing assignments to workers and streams out the data in quasi-real time such that the full processing allotment of a slot can be fully and efficiently used, ensuring full resource utilization particularly on opportunistic resources with transient or unpredictable worker lifetimes, such as commercial cloud spot markets and HPCs. The AES is built on the foundation of ATLAS' PanDA distributed workload management system and the powerful fine grained workload tailoring capabilities of its JEDI subsystem.

The proposed project is concerned with the next major step in this development program, the Event Streaming Service (ESS). With the AES in hand to stream event processing assignments, we have the possibility to intelligently stream the input data itself to workers. The value of this is that distributed dynamic data flows across the WAN at the highest possible efficiency are vital for the future of ATLAS computing. Storage is by far the largest cost component of our computing, and growing data volumes over the next decade will make it impossible to sustain our present computing model and how it uses storage. We will need to reduce replica counts, make ever greater use of transient caches, and make full use of our high bandwidth networking, delivering just the data needed to a worker, when it is needed, and without the application payload seeing WAN latencies. The ESS is designed to do this, intelligently pre-fetching the data needed asynchronously from the payload, in quasi-real time. Its development -- presently at the early prototyping stage -- is foreseen in several steps at increasing levels of sophistication:

### ESS V1

ESS V1, the simplest incarnation of the ESS, performs asynchronous data pre-fetch for the events assigned by AES. Analogous to how outputs are streamed off the worker, the worker's supervisor (pilot) runs a data pre-fetcher process asynchronous from the payload, performing WAN (or local) reads to fetch the data and creating small input files corresponding to event ranges that are consumed by the application. A first prototype of ESS V1 exists.

### ESS V2

ESS V2 adds a server-side component to the system that receives the data streaming requests. Instead of the pre-fetcher reading a remote file, it interacts with a service, specifying the event processing assignment it has received. The service then can apply knowledge of the data needed by the client and its availability to choose an optimal means of acquiring, marshalling and streaming exactly the data needed by the client.

### ESS V3+

The ESS service of V2 can evolve progressively into a powerful CDN-like capability to apply central knowledge and intelligence to data delivery while presenting simple access methods to the client. Furthermore, the interface presented by the service -- when presented with a specific request for event data, deliver the data -- is well suited to the 'ultimate' step in storage optimized data delivery, 'virtual data', in which the data does not exist prior to the request at all, but is generated on demand. This approach trades off CPU (relatively cheap and plentiful) against expensive storage.

## Task ideas

With a first prototype of ESS V1 existing, the basic infrastructure to explore more sophisticated versions of ESS is in place. The GSoC objectives focus on exploring these more sophisticated approaches. A single GSoC program is likely to encompass one of the task ideas below, or a variation on them, to be decided with the candidate.

- Implement a ROOT data delivery service that marshals data for delivery over the wire depending on the event data requested by the client (event, branches used, filtering to be applied, ...).
- Implement a CDN-like web service that receives event data requests and interacts with the data management system and other information sources (such as data popularity) to produce a data delivery plan for the client: delivering to the client an access endpoint for the data, and taking decisions such as whether to cache or replicate the data close to the client based on popularity and concurrent usage, so that subsequent requests for related data come from a source close to the client.
- Implement a web service interacting with a 'knowledge base' database to receive event data requests and service them by generating the requested data on demand, delivering generated data to an ensemble of clients requesting related data.

## Expected results

A working server implementation of one of the ESS V2/V3 concepts for intelligent streaming data delivery via ESS to an event service client.

## Requirements

- C++
- python
- scripting
- familiarity with ROOT preferred
- some experience with relational (or other) databases preferred
- experience with real-time and/or distributed and/or concurrent software

## Mentors

 * [Vakho Tsulaia](mailto:tsulaia@cern.ch)
 * [Torre Wenaus](mailto:wenaus@gmail.com)