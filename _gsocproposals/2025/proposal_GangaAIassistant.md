---
project: Ganga
title: Incorporate a Large Language Model to assist users
layout: gsoc_proposal
year: 2025
difficulty: medium
duration: 350
mentor_avail: May-November
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The [Ganga](https://github.com/ganga-devs/ganga) user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

As a scripting and command line interface, there will naturally be users that have problems with getting the syntax correct. To solve this, they will often spend time searching through mailing lists, FAQs and discussion fora or indeed just wait for another more advanced coder to debug their problem. The idea of this project is to integrate a Large Language Model (LLM) into the command prompt in Ganga. This should allow the user to describe in words what they would like to do and get an example that they can incorporate. It should also intercept exceptions thrown by the Ganga interface, help the user to understand them and propose solutions.

We have an interface based on ollama that will build a RAG that contains extra information about Ganga that has not been available for the training of the underlying LLM.

## Task ideas
 * Explore different options for integrating the LLM into a command line prompt.
 * Integrate the interaction with the LLM and RAG into Ganga.
 * Setup a server such that the LLM can run on a remote server requiring minimal installation by the user.
 * Test which samples are most useful for adding to the RAG (mailing list discussions, manuals, instant messages)
 * Develop continuous integration tests that can ensures that LLM integration will keep working.

## Expected results
For the scientific users of Ganga, this will speed up their development cycle as they will get a faster response to the usage queries that they have.

As a student, you will gain experience with the challenges of large scale computing where some tasks of a large processing chain might take several days to process, have intermittent failures and have thousands of task processing in parallel. You will get experience with how LLMs can be integrated directly into projects to assist users in the use of the CLI and in understanding error messages.

## Evaluation Task
Interested students please contact Ulrik (see contact below) to ask questions and for an evaluation task.

## Requirements
Python programming (advanced), Linux command line experience (intermediate), use of git for code development and continuous integration testing (intermediate)

## Mentors 
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)
  * **[Ulrik Egede](mailto:ulrik.egede@monash.edu)**

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
