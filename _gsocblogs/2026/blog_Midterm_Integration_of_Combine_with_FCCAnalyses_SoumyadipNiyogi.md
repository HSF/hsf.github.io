|  |  |
| --- | --- |
| Name | [Soumyadip Niyogi](https://github.com/captainvogon) |
| Organisation | [IISER Thiruvananthapuram](https://www.iisertvm.ac.in/), [CERN](https://home.cern/), [HSF](https://hepsoftwarefoundation.org/) |
| Mentor | [Juraj Smiesko](https://kjvbrt.org/) (CERN), [Jan Eysermans](https://github.com/jeyserma) (MIT) |
| Project | [Integration of CMS Combine with FCCAnalyses](https://summerofcode.withgoogle.com/programs/2026/projects/FyDjzZ3Y) |

## Introduction
Hi again! We are at the midpoint of GSoC 2026, and I am excited to share the progress on my project bridging `FCCAnalyses` and `CMS Combine`. Since my introductory post, I have spent my time deep in the Python architecture of `FCCAnalyses`, transforming ROOT histograms from simulated e⁺e⁻ → ZH events into automated statistical models.

The primary goal of this first half was to build the core datacard generation engine. I am happy to report that the automated pipeline is now up and running. You can check out the finalized skeleton framework in [my latest Pull Request here](https://github.com/HEP-FCC/FCCAnalyses/pull/520).

## Progress So Far: The Core Engine
Over the past month, I have successfully implemented the `fit.py` interface within the `FCCAnalyses` framework. Here is what the tool can currently do:

*   **Automated Datacard Generation:** The framework reads a user-defined, object-oriented Python configuration and automatically maps the requested signal and background processes to their respective ROOT shape histograms. It then spits out a perfectly formatted text-based `datacard.txt`.
*   **The Execution Flag (`-e`):** To make the workflow completely seamless, I added a backend hook. By simply appending `-e` to the CLI command, the framework passes the newly generated datacard directly into a `subprocess` to execute `Combine` natively, eliminating the need for physicists to manually string together terminal commands.

## The Technical Challenge: ROOT
In the beginning I ran into a curious technical roadblock. When testing the `-e` direct execution flag on our generated datacards using Combine's `AsymptoticLimits` method, the framework kept throwing a fatal C++ exception: `Caught exception Value 2.2 is outside the default range [0, 1.76]`. 

Initially, I thought our physics statistics were too low, or that the datacard was structurally broken. After some debugging with my mentors, we discovered the real culprit was ROOT 6.30.
The newest version of ROOT bundled in the Key4hep nightly builds has deprecated the old "silent boundary clipping" behavior. When running `AsymptoticLimits` on our perfectly smooth Asimov dataset, Combine's internal minimizer (Minuit) would aggressively guess a parameter boundary, step slightly out of bounds to test a value, and instantly trigger this new, strict ROOT exception, crashing the entire job!

**The Validation:** To bypass Combine's range-guessing and prove that my Python code was generating valid datacards, we switched the backend to run a `-M FitDiagnostics` test instead. The fit converged perfectly on our fake dataset, yielding `Best fit r: 1.0` with roughly a ~1.25% uncertainty. This proof that the datacards are structurally sound was a massive relief.

## Next Steps
With the core generation and execution engine validated, the second half of the summer will focus on the physics and usability.

**Full Statistics Validation:** Moving past the Asimov testing phase to run the framework on full-statistics ZH → μμ background and signal shapes.

**Documentation:** Writing the user tutorials and `pytest` suite so the FCC community can actually learn to use the interface.

## Acknowledgements
A huge thank you to my mentors, Jan and Juraj, for their responsive feedback on Mattermost and for helping me decipher cryptic ROOT exceptions. I am looking forward to bringing this tool to the finish line over the next couple of months.