---
project: FASER
title: Real-time data compression for FASER experiment
layout: gsoc_proposal
year: 2023
difficulty: medium
duration: 175
mentor_avail: June-October
organization:
  - Geneva University
  - CERN
---


## Description
The [FASER experiment](https://arxiv.org/abs/2207.11427) is an LHC experiment located in a tunnel parallel to the LHC ring and is considerably smaller and low-budget compared to the titan LHC experiments such as ATLAS and CMS. The experiment seeks to detect new long-lived particles that have travelled half a kilometer from a LHC proton-proton collision site, escaping the major ATLAS experiment undetected. The only other proton collision "background" particles reaching FASER's faraway location are muons and neutrinos.
During proton running, the FASER experiment records up to 1500 events per second using an open source data acquisiton (DAQ) software framework developed at CERN. The DAQ software receives dedicated data fragments from subcomponents on the detector, packs them into a single event and writes completed events to file.
FASER currently records its data as raw bit stream to disk but is hitting storage space limitations. The project aim is to explore methods of real-time data compression to reduce FASER's output data size.

## Task ideas
The project will explore the use of standard C++ compression libraries to compress raw data read out of the FASER detector in real-time and decompress data for event analysis. The task will need to explore the best method of implementation, considering at which level of event building data compression can be most effectively implemented. It will need to be ensured that the implementation causes no undue bottlenecks during data acquisition, and that data can be easily decompressed for physics analysis.

## Expected results
 * Determine a suitable C++ library/method for data compression and decompression in the context of FASER's DAQ model.
 * Study ways of most effective data compression, acquiring knowledge of how the FASER data recording stream works at different levels.
 * Test final implementation methods on the full FASER DAQ system by running high event rate tests to measure and compare recording speed and verify no bottlenecks in throughput are caused.

## Evaluation Task
Please contact [Claire Antel](mailto:claire.antel@cern.ch) for more details.

## Requirements
 * Good knowledge of C++

## Mentors
 * **[Claire Antel](mailto:claire.antel@cern.ch)**

## Links
* [FASER DAQ git repo](https://gitlab.cern.ch/faser/online/faser-daq)
* [FASER DAQ docs](https://faserdaq.web.cern.ch/faserdaq/)
* [Publication on FASER TDAQ system](https://arxiv.org/abs/2110.15186)

