---
project: ROOT
title: RNTuple climate data tutorial and Reference Specifications
author: John Yoon
date: 11.03.2021
year: 2020
layout: blog_post
logo: ROOT-logo.png
intro: |
  Google's Season of Docs offers an opportunity for technical writers and open source organizations to collaborate on projects that would improve through documentation. Following the program's application process, I was fortunate enough to match up with CERN, specifically with its software framework team, ROOT. Per ROOT's own [website](https://root.cern.ch/root/htmldoc/guides/primer/ROOTPrimer.html#motivation-and-introduction), "ROOT is a software framework for data analysis and I/O: a powerful tool to cope with the demanding tasks typical of state of the art scientific data analysis." 
---

# GSoD 2020: ROOT's RNTuple

# Introduction
Google's Season of Docs offers an opportunity for technical writers and open source organizations to collaborate on projects that would improve through documentation. 

Following the program's application process, I was fortunate enough to match up with CERN, specifically with its software framework team, ROOT. Per ROOT's own [website](https://root.cern.ch/root/htmldoc/guides/primer/ROOTPrimer.html#motivation-and-introduction), "ROOT is a software framework for data analysis and I/O: a powerful tool to cope with the demanding tasks typical of state of the art scientific data analysis."

Due to the nature of CERN, ROOT's primary use cases revolve around particle physics analysis. This fact catalyzed the inspiration for my proposal, which heavily focused on creating a tutorial that would use datasets beyond the physics realm, in order to introduce ROOT's incredible capabilities to a wider audience. Specifically, the scope for this endeavor highlighted on ROOT's RNTuple feature.

# Preparations
My main team within ROOT was the Input & Output group. In particular, I interacted frequently with my mentor, Jakob Blomer. Logistically, we structured our communications so that once per week, I would join the broader Input & Output team's RNTuple meetings. Similarly (and just as valuably), I would have a weekly one-on-one with Jakob in order to review the project's progress. For all other conversations, we primarily used CERN's in-house communication tools.

During the start of the program, I bounced ideas off of Jakob, as we considered possibilities for datasets to use. After creating an extensive list of possible non-physics related datasets (from Kaggle), we narrowed it down to three candidates from the fields of: climate data, sports data, and movie data. We decided that from these three, the climate data would serve as our primary dataset for the tutorial. We also decided that the other two datasets would later be revisted if appropriate within the timeframe and usefulness (we ultimately did not use the other two, because the pedagogical purpose of the tutorial had marginal returns from using the other datasets after already creating the climate data-related tutorial).

In addition to the tutorial, we decided that RNTuple required a reference specification document. This document would allow users to create their own implementations.

# Goals
In summary, I would create:
* a tutorial using climate data that would highlight several ROOT features, and
* a reference specification document for RNTuple

# Development
After establishing the success criteria for the project, I began to deep dive into the source code and review any existing documentation. Then I began to create the tutorial using the language, C++. The first major milestone was getting RNTuple to properly work with the climate data. The next stage consisted of taking the inputted data and filtering it to a more granular level so that the tutorial could use the data in combination with another ROOT feature, RDataFrame. Once this part was completed, we focused on outputting the results as visualizations. Afterwards, there were several iterations of adding and improving the comments within the code.

Once the tutorial was complete, I shifted gears towards creating the eference specification document for RNTuple. This comprised of establishing and defining the key terms that is used in the understanding RNTuple, as well as translating the C-based implementation of RNTuple into a universally accessible guide that would allow developers to implement their own take on RNTuple, i.e. into other programming languages like Python.

# Challenges
Most of the challenges relating to the completion of either goals derived from the fact that the parts of ROOT that I was contributing towards consisted mainly of its experimental version, ROOT 7. Consequently, it was difficult at times, such as during troubleshooting, to determine if the code was crashing due to a bug implemented on my part, or if it was due to the inherently experimental nature of the feature. Similarly, there were compatibility issues that arose between the experimental ROOT 7 version, and the currently accepted version. Fortunately, in both situations, my mentor, the I/O team, and the broader ROOT community was always there to offer insights and suggestions.

# Summary
The final two results can be found:
* [as "global_temperatures.cxx"](https://github.com/root-project/root/tree/master/tutorials/v7), or [alternatively](https://root.cern/doc/master/global__temperatures_8cxx.html)
* [RNTuple reference specification](https://github.com/root-project/root/blob/master/tree/ntuple/v7/doc/specifications.md)

As mentioned before, due to the inherently experimental nature of the version ROOT 7, it is highly likely that both of my products will be living and dynamic documents that frequently experience updates.

My GSoD experience with CERN's ROOT was a rewarding and enjoyable one. I was able to learn a lot more about the technical writing field and open source organizations, thanks to my mentor, Jakob Blomer, as well as the entire I/O team!
