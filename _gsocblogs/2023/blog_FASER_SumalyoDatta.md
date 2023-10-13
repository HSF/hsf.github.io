---
project: FASER
title: Real-time lossless data compression for the FASER experiment
author: Sumalyo Datta
photo: blog_authors/SumalyoDatta.jpg
date: 04.10.2023
year: 2023
layout: blog_post
logo: faser-logo.png
intro: |
    I am sharing my GSoC 2023 journey, working with the FASER collaboration to develop a real-time compression module for the experiment that reduced file sizes by 50%. The module integrates with the FASER Data Acquisition System (DAQ) and can perform seamlessly at high event rates. 
---
![header](https://sumalyo.github.io/benchmarkFASER/FASERImages/banner.png)
![C++ Badge](https://img.shields.io/badge/Built_with-C_%2B%2B-purple?logo=cplusplus)
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?logo=plotly&logoColor=white)
![daqling Badge](https://img.shields.io/badge/Powered_By-daqling-green?link=https://gitlab.cern.ch/ep-dt-di/daq/daqling)

# Real-Time Lossless Data Compression for the FASER Experiment
## Introduction
The [FASER experiment](https://faser.web.cern.ch/index.php/) is an LHC experiment located in a tunnel parallel to the LHC ring. It is considerably smaller and low-budget compared to the titan LHC experiments such as ATLAS and CMS. The experiment seeks to detect new long-lived particles that have travelled half a kilometre from the LHC proton-proton collision site at the centre of the ATLAS experiment, escaping the ATLAS detector undetected. During proton collisions at the LHC, the FASER experiment records up to 1500 events per second using an open-source data acquisition (DAQ) software framework developed at CERN. The DAQ software receives dedicated data fragments from subcomponents on the detector, packs them into a single event and writes completed events to a file. The assigned total storage space for the experiment was, however, quickly met and already resulted in a doubling of the requested storage space. The challenge was to develop a compression engine that would compress data in real-time, __introducing minimal latency and performance overheads__. The compression engine would also have to decompress events transparently for data reconstruction for physics analysis. <p>

FASER has a trigger-based data acquisition model, and the DAQ software is developed using the DAQling framework.
>> DAQling is an open-source lightweight C++ software framework that can be used as the core of data acquisition systems of small and medium-sized experiments. It provides a modular system in which custom applications can be plugged in. It also provides the communication layer based on the widespread ZeroMQ messaging library, error logging using ERS, configuration management based on the JSON format, control of distributed applications and extendable operational monitoring with web-based visualization.

You can read more about the strategy in the [paper published by the FASER collaboration](https://arxiv.org/abs/2110.15186).

The first part of the project involved __the exploration__ of various open-source lossless compression libraries and the development of a standalone compressor for raw files, which can be used to record performance metrics (such as compression ratio and compression speed) to help determine the best compressor that could be used in the engine. You can read more about the exploration of compression algorithms in this [medium blog](https://medium.com/gsoc-2023-data-compression-faser/real-time-lossless-data-compression-for-the-faser-experiment-part-1-274025eb4079) <p>

After exploration of various algorithms, the next task was to __develop a compression engine module__ that could be integrated into the full FASER DAQ system and can be configured to obtain a compressed file for physics events directly from the acquisition system. The challenge was to design a module that could handle high throughput working at high event rates (as high as 4kHz). The module would publish relevant metrics on the Monitoring dashboard, such as the compression ratio.
<p>

| ![DashBoard1](https://sumalyo.github.io/benchmarkFASER/FASERImages/Compression%20Dashboard%20High%20Rate.png) | 
|:--:| 
| *Fig 1: A Glimpse of The Metrics Dashboard* |

## The Community Bonding Period
Before the coding period, the plan for contributions was roughly chalked out during the community bonding phase. The development setup was finalized during this phase. A Docker-based setup was planned as it helped replicate the production environment and made managing packages and dependencies much more manageable and streamlined. I found some issues with the existing docker image and worked with the mentors to add services like supervisord and reddis to the container configuration. To add support for data compression, additional dev packages were added to aid in building the prototype implementation. 
Code for the new Dockerfile can be found here : [master branch on faser-docker](https://gitlab.cern.ch/faser/docker)
<br>
Merge Request: [MR #2](https://gitlab.cern.ch/faser/docker/-/merge_requests/2)<br>
![MR_Merged](https://img.shields.io/badge/MR-Merged-green?style=for-the-badge&logo=appveyor)

## Raw File Compressor
In the first phase of the project, a standalone utility application `eventCompress` [Link to Code](https://gitlab.cern.ch/faser/faser-common/-/blob/compression_app/EventFormats/apps/eventCompress.cxx) was developed which can be used to compress existing raw data files and record performance metrics during the process. It can also do decompression tests and record metrics like decompression speed.
```
Usage: eventCompress [-n nEventsMax -l -d -s -o <output_file> -c <config_file> ] <input_raw_filename> 
   -n <no. events>:   Run Compression for n events only (optional)
   -l --enableLog:    Enable logging for metrics and benchmarks (optional) 
   -d --decomress:    Run Decompression tests (optional)
   -s --silent:       suppress logs (optional)
   -o --write:        specify file to write out to
   -c --config:       specify file to read compressor config
```
The idea here is to compress event-by-event reading from a raw file and alter the header information to indicate compression and specify the compression algorithm used. As each event was compressed individually, the time taken for compression and the ratio of the uncompressed size to the compressed size are recorded for each event. These are logged in a JSON file, which can be analysed with a Python notebook to visualise the data as graphs and to understand performance tradeoffs. You can view a sample report [here](https://cloud.datapane.com/reports/VkG8X2A/compression-report-an-overview/). 
<br>
Merge Request: [MR #50](https://gitlab.cern.ch/faser/faser-common/-/merge_requests/50)<br>
![MR_Merged](https://img.shields.io/badge/MR-Merged-green?style=for-the-badge&logo=appveyor)
<br>
The logs and the python-based analysis notebooks can be found at [this repo](https://gitlab.cern.ch/faser/online/compression-studies). Please refer to the README for additional information.

### The Best Candidate
| ![Chart](https://sumalyo.github.io/benchmarkFASER/FASERImages/FASER-Report-Compression.jpg) | 
|:--:| 
| *Fig 2 Average Compression Ratio vs Average Compression Speed* |

The approach for finding the best compressor is described below
- Events were divided into a set of 10 classes based on event size (Class 0 having events of smallest size)
- For each event class, the average compression speed and compression ratio were calculated (for each compressor)
- The resulting points were plotted on a graph, and this helped to visualize the tradeoff. The compressor configuration offering the highest average compression ratio at the highest compression speed was considered optimal.
<br>
After running several experiments with recorded physics data, it was determined that [ZSTD](https://github.com/facebook/zstd) was the best compressor. The __compression levels 3 and 5__ were observed to be the most optimal configuration for implementation. 

## The Compression Engine
| ![Chart](https://sumalyo.github.io/benchmarkFASER/FASERImages/Schematic.drawio.png) | 
|:--:| 
| *Fig 3 Schematic Diagram of the Implementation of the Compression Module* |

<br>
The final phase of the project was to develop a compression engine module with the DAQling framework that could be added to an existing configuration to compress physics events before they are written out. The EventBuilder module is responsible for collecting the data fragments from event sources (like the tracking detectors) and building events that are sent to the FileWriter Module. The Compression engine sits between these modules, receiving events from the Eventbuilder, compressing them and sending them out to the FileWriter module. 
<p>
It's designed in a non-blocking manner, with an internal buffer to store incoming events and then read events from it to compress and send out. It utilizes multithreading to achieve this by using the producer-consumer queues provided by the Folly library. Essential parts of the design are laid out in the following sections.

```C++
std::array<unsigned int, 2> tids = {threadid++, threadid++};
    const auto & [ it, success ] =
        m_compressionContexts.emplace(0, std::forward_as_tuple(queue_size, std::move(tids)));
    assert(success);

    // Start the context's consumer thread.
    std::get<ThreadContext>(it->second)
    .consumer.set_work(&CompressionEngineModule::flusher,this, // Threaded function
    std::ref(std::get<PayloadQueue>(it->second)), // Primary
    Compressor,m_buffer_size // Auxiliary Arguments;
    );
  assert(m_compressionContexts.size() == 1); // Only one context may be created
```
Here, the threads are spawned and associated with the queues, which would be used to store and compress events.

```C++
 for (auto & [ chid, ctx ] : m_compressionContexts) {
  std::get<ThreadContext>(ctx).producer.set_work([&]() {
  auto &pq = std::get<PayloadQueue>(ctx);
  auto receiverChannel = m_config.getConnections(m_name)["receivers"][0]["chid"];
  while (m_run)
  {
    DataFragment<daqling::utilities::Binary> blob;
    auto chid = receiverChannel; // set to 0 for Physics data
    while (!m_connections.receive(chid, blob) && m_run)
    {
      if (m_statistics) {
      m_payload_queue_size = pq.sizeGuess();
      }
      std::this_thread::sleep_for(1ms);
    }
    DEBUG(" Received " << blob.size() << "B payload on channel: " << chid);
    if (pq.sizeGuess() > 990)
    {
      WARNING("Payload Queue is filling up !!");
    }
    while (m_run && !pq.write(blob));
    if (m_statistics && blob.size()) {
      m_events_received++;
    }
  }
  });
```
Here, the section of the code is highlighted that is used to obtain events from the EventBuilder and write the payloads to the Producer queue.

```C++
compressorUsedFlush->setCompressionLevel(compressionLevel);
    auto senderChannel = m_config.getConnections(m_name)["senders"][0]["chid"];
  const auto flushVector = [&](std::vector<DataFragment<daqutils::Binary>> &eventBufferVector) {
    float uncompressed_size = 0;
    float compressed_size = 0;
    for (auto & blob : eventBufferVector)
    {
    eventGot = std::make_unique<DAQFormats::EventFull>(blob.data<uint8_t *>(), blob.size());
    uncompressed_size+=eventGot->payload_size();
    if(compressorUsedFlush->compress(eventGot) == false)
    {
      m_status = STATUS_ERROR;
    }
    compressed_size+=eventGot->payload_size();
    int channel = senderChannel; // Channel to send out compressed data 
    auto *bytestream = eventGot->raw();
    DataFragment<daqling::utilities::Binary> binData(bytestream->data(), bytestream->size());
    DEBUG("Sending event " << eventGot->event_id() << " - " << eventGot->size() << " bytes on channel " << channel);
    m_events_sent++;
    m_connections.send(channel, binData); // to file writer
    delete bytestream;
    }
    eventBufferVector.clear();
    if (compressed_size!=0)
    {m_compression_ratio.store(uncompressed_size/compressed_size);}
  };
  while (!m_stopWriters) {
    while (pq.isEmpty() && !m_stopWriters) { // wait until we have something to write
      flushVector(eventBuffer);
      std::this_thread::sleep_for(1ms);
    };

  if (m_stopWriters) {
    flushVector(eventBuffer);
    return;
  }

  auto payload = pq.frontPtr();
  DataFragment<daqutils::Binary> eventProcess(payload->data(), payload->size());
  eventBuffer.push_back(eventProcess);
  eventProcess = DataFragment<daqutils::Binary>();
  if(eventBuffer.size() > maxBufferedEvents )
  {
    flushVector(eventBuffer);
  }
  pq.popFront();
  
  }
```
This section of the code is used to send out the compressed events.
<br>

Merge Request: [MR #203](https://gitlab.cern.ch/faser/online/faser-daq/-/merge_requests/203)<br>
![MR_Merged](https://img.shields.io/badge/MR-Merged-green?style=for-the-badge&logo=appveyor)
<br>

### Decompression On-the-Fly
Another essential requirement of the project was to implement support for decompression in a way that would be abstracted from the user. The user should not bother about a file containing compressed events or raw events; all the software used for analysis and reconstruction should be compatible with the compressed files. For this, the loadPayload() method was altered to identify compressed events and decompress events on the fly. 
```C++
 void loadPayload(const uint8_t *data, size_t datasize) {
    std::vector<uint8_t> decompressed_data_vector;
    if (header.status & Compressed) // Compressed Event Detected
      { 
        // DEBUG("A Compressed Event is being read");
        
        // Detect Compression Algorithm And Decompress
        if (decompressPayload(header.compression_code,data,static_cast<size_t>(datasize),decompressed_data_vector ))
        {
          data = &decompressed_data_vector[0];
          datasize = decompressed_data_vector.size();
          processCompressedData(datasize);
        }
        else
        {
            THROW(CompressionDataException,"DECOMPRESSION FAILED SKIPPING EVENT READ");
        }
      }
    if (datasize != header.payload_size) {
    THROW(EFormatException, "Payload size does not match header information");
    }
    for(int fragNum=0;fragNum<header.fragment_count;fragNum++) {
        EventFragment *fragment=new EventFragment(data,datasize,true);
        data+=fragment->size();
        datasize-=fragment->size();
        fragments[fragment->source_id()]=fragment;
      }
    }
```
The offline reconstruction software [calypso](https://gitlab.cern.ch/faser/calypso) was recompiled with support for handling compressed events and tested. It performed quite smoothly with compressed files passed as input.


## High Event Rate Tests
The viability of the Compression Engine could only be determined by high event rate tests on the full FASER DAQ system. This was planned in the final days of the project. The Compression Engine would be subjected to a calibration LED Random Trigger, simulating conditions during proton-proton collisions in the LHC. The code was compiled on a spare production server and hooked to the FASER TDAQ system. The module published metrics indicating the compression ratio, the number of events received and sent out, and the internal queue size. The event rate was also monitored. The objective was to verify that there were no bottlenecks due to compression and that the module dropped no events.

| ![TriggerDashboard](https://sumalyo.github.io/benchmarkFASER/FASERImages/triggersetup.png) | 
|:--:| 
| *Fig 4 The FASER Trigger Dashboard during High Rate Tests* |

A __compression level 5__ was tested for the __ZSTD Compressor__

| ![TriggerDashboard](https://sumalyo.github.io/benchmarkFASER/FASERImages/finaltest4.png) | 
|:--:| 
| *Fig 5 The Compression Module Metrics Dashboard* |

It can be seen that the event rate was pushed up to 4kHz, and the average compression ratio reported was around 2. This means the __file sizes were halved__ during data acquisition. The internal queue, with a capacity of about 1000, only filled up to 200, which proved that there was no performance bottlenecks. No messages were dropped during compression. The Sender and the receiver queues were fairly freed up, indicating that the non-blocking multi-threaded approach was implemented successfully.


## Conclusion
Contributing to the project for the last four months was really exciting. This was a great learning experience for me as I got to work on everything from DevOps to python scripting and multi-threaded C++. The studies done to determine the best compression engine was quite insightful and, I got to know a lot about how the design of a compressor affects performance and how it adapts to physics event data. Implementing the compression engine module was quite interesting as it helped me understand how to optimize my code for high throughput systems. It was really exciting to test out my code on the actual FASER experiment (down at the LHC ! ) setup with a full readout. I would like to thank my mentors, Brian Petersen and Claire Antel, for their guidance and support. It was a great experience implementing the real-time lossless data compression engine for the FASER experiment.

<br>

![footer](https://sumalyo.github.io/benchmarkFASER/FASERImages/footerImage.png)
