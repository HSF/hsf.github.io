---
project: CERNBox
title: Smashbox in Python 3
author: Anand Krishna
date: 28.07.2022
year: 2022
layout: blog_post
logo: cernbox-logo.png
intro: Porting the Smashbox test suite to Python 3
---

The first half of the GSoC coding period is almost over, and this first entry to the developer journal has been long overdue. I'll get right to the point:

## Schedule
I have fallen behind on the schedule I had proposed. Partly due to bad judgement, but mostly as my university academic schedule got super hectic because of COVID.

## Progress
Over the last month, I have
- Read through a large part of the codebase to understand the general lay of the land
- [**Made a new YAML based configuration system:**](https://github.com/cernbox/smashbox/pull/141)
  Configuration was earlier stored in a file, as valid Python code, which was then basically passed to [`exec`](https://docs.python.org/3/library/functions.html#exec)[^1]
 to read all the settings in.
Now, configuration is stored in a YAML file, that is read and parsed.
- [**Migrated away from pycurl:**](https://github.com/cernbox/smashbox/pull/140)
  Pycurl code is tough to read and maintain; we now use `httpx` (which comes with the added advantage of asyncio support)

## Plans
Next, I'll move on to
- Updating the CLI code (maybe use something like the `click` library instead of stdlib argparse)
- **Update the multiprocessing engine [^2]**
- **Migrate to loguru:**
  loguru is an alternate logging library that is simpler to use than the stdlib `logging`, and gives prettier outputs. The codebase has a mix of `logger.log` and plain old `print` statements, so I'll also standardize them (and only use the logger)

## Roadblocks
- Getting smashbox itself running was quite difficult, I probably wouldn't have been able to do it without the mentor's explaining how to do it first. The existing README instructions have some out-of-date instructions. This could potentially be improved in my project; maybe also releasing a Docker image would make it easier to get started?
- Working with a Python 2 codebase has been more difficult than I anticipated. I find myself constantly reaching for the documentation to find what some old deprecated function did so that I can find modern equivalents.

Hoping for an even more productive month of coding ahead! 🤞

 
[^1]: Well, [`execfile`](https://docs.python.org/2.7/library/functions.html#execfile) to be precise; a relic from Python 2 I hadn't previously heard of

[^2]: This is the part of the code that spins up multiple workers for test cases where we simulate multiple users interacting simultaneously.

