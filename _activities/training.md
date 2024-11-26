---
title: HSF Training
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/training.html
  - /activities/training.html
  - /training/
  - /training/index.html
excerpt: none
---

<img src="{{site.baseurl}}/images/training/analysis_preservation_bootcamp_participants.jpg" style="float: right; width: 90vw; max-width:320px; margin-left: 20px;margin-bottom: 20px;">

The HSF Training Activity Area aims to help the research community to provide training in the computing skills needed for researchers to produce high quality and sustainable software. The group works with experiment training groups, HEP initiatives (such as [IRIS-HEP](https://iris-hep.org/) and [FIRST-HEP](https://first-hep.org/)) and organisations like [Software Carpentry](https://software-carpentry.org/) to coordinate training activities.

The group aims to develop a training program that can be pursued by researchers to achieve the level of required knowledge. This ranges from basic core software skills needed by everyone to the advanced training required by specialists in software and computing.

<div class="big-link-container">
  <a href="{{site.baseurl}}/Schools/events.html">
    Join an event!<br/>
    Discover new topics together with mentors and peers!
  </a>
  <a href="{{site.baseurl}}/training/curriculum.html">
    Self study!<br/>
    Learn at your own pace. No matter if you want to get a quick overview
    or dive in the details, this is for you!
  </a>
</div>


## Our mission

<img src="{{site.baseurl}}/images/training/instructor_mentor_small.jpg" style="float: right; width: 90vw; max-width:320px; margin-left: 20px;margin-bottom: 20px;">

The long term sustainability of the research software ecosystem is important for HEP as [HL-LHC](https://home.cern/science/accelerators/high-luminosity-lhc) and other facilities of the 2020s will be relevant through at least the 2030s. Meeting this challenge requires a workforce with a combination of HEP domain knowledge and advanced software skills.

The software skills required fall into two groups. Nearly all researchers need basic programming skills (Python, C++), basic software engineering skills (Unix, git/GitHub/GitLab, continuous integration, performance evaluation), and skills in the core data tools in HEP (e.g., the [ROOT data format and analysis framework](https://root.cern.ch/)).

More advanced training is then needed (with domain examples!) in parallel programming, efficient software implementations, performance optimization, and machine learning and data science tools. A workforce trained in this range of software skills is the critical ingredient from which the solutions to the computing challenges can grow.

Today's graduate students will be the young faculty members driving HEP research in the 2020s. Investing in their software skills is not only important to actually build the requisite software infrastructure, but will also change community norms, create role models and promote career paths for computational scientists within the HEP research community. Computation is a central element of 21st century science, and clearer career paths will provide a virtuous cycle of feedback to enhance the vibrancy of the training and workforce development activities.

<div class="big-link-container">
  <a href="https://arxiv.org/abs/2103.00659">
    Our most recent paper<br/>
    Several years of experiences and plans for the future (2021)
  </a>
  <a href="https://arxiv.org/abs/1807.02875">
    Whitepaper<br/>
    Our vision of software training as of 2018
  </a>
  <a href="{{site.baseurl}}/training/resources">
    More about us<br/>
    A collection of talks, papers and other material about our group
  </a>
</div>

## Learn with us

<div class="big-link-container">
  <a href="{{site.baseurl}}/Schools/events.html">
    Join an event!<br/>
    Discover new topics together with mentors and peers!
  </a>
  <a href="{{site.baseurl}}/training/curriculum.html">
    HSF Training center<br/>
    Learn at your own pace. No matter if you want to get a quick overview
    or dive in the details, this is for you!
  </a>
  <a href="https://hsf-training.github.io/analysis-essentials/">
    Analysis essentials<br/>
    A course on basic computing required for HEP
  </a>
  <a href="https://github.com/hsf-training/PyHEP-resources">
    PyHEP resources<br/>
    A curated list of python modules for HEP
  </a>
</div>

## Participate & Contribute!

The easiest way to get in touch are our weekly meetings, usually held at 16h00 CERN time on Mondays. Everyone is welcomed to discuss! Check [Indico](https://indico.cern.ch/category/10294/) for details. The live notes and the zoom connection is linked in the right sidebar in the category view.

Everybody is welcome to join the [forum](https://groups.google.com/forum/#!forum/hsf-training-wg) dedicated to HSF training activities. This is the place where ideas and proposals are discussed and actions decided!

<div class="big-link-container" style="margin-bottom: 1em">
  <a href="https://indico.cern.ch/category/10294/">
    Talk to us!<br/>
    We meet weekly, usually on Monday at 16h00 CERN time.
  </a>
  <a href="https://join.slack.com/t/hsftraining/shared_invite/zt-18sa7y3s6-5QuNY0sSnlP6HSNvoFREkg">
    Chat with us on Slack!<br/>
    Brainstorm your ideas with us. 
  </a>   
  <a href="{{site.baseurl}}/training/community.html">
    Join the community!<br/>
    Join more than {{ site.profiles | size | divided_by: 10 | times: 10 }} people working on our mission.
  </a>
  <a href="https://github.com/hsf-training/PyHEP-resources">
    Browse our GitHub Organization!<br/>
    Browse all of our training material. Issues & pull requests are always welcome!
  </a>
  <a href="https://groups.google.com/forum/#!forum/hsf-training-wg">
    Write us!<br/>
    Use our public mailing list and reach a wide range of training enthusiasts.
  </a>
</div>

<figure class="centered-figure" style="margin-bottom: 1em">
  <img src="{{ '/images/training/training_statistics.png' | relative_url }}" alt="Facilitator" style="max-width: 550px">
  <figcaption>
    The number of commits in our repository and the number of registered learners closely follows the number of our educators.
    You, too, can  make a difference!
  </figcaption>
</figure>
## Training events

We are always looking for volunteers from the community to help us with our training events.

<div class="big-link-container">
  <a href="{{site.baseurl}}/Schools/events.html">
    Training events<br/>
    A list of training events both with and without HSF participation
  </a>
  <a href="{{site.baseurl}}/training/educators.html">
    Training roles<br/>
    We have standardized the different roles your can fulfill at our events
  </a>
  <a href="{{site.baseurl}}/training/howto-event.html">
    How to organize a workshop<br/>
    Whether you work with us or not, these guidelines might help your organizing an awesome workshop!
  </a>
</div>

{% capture list_of_upcoming_schools %}{% include list_of_upcoming_schools.md %}{% endcapture %}
{% capture test %}{{ list_of_upcoming_schools | strip }}{% endcapture %}
{% if test  != "" %}
<div style="margin-top: 2ex; margin-bottom: 1ex">Upcoming schools:</div>

{{ list_of_upcoming_schools }}
{% endif %}
## Conveners

{% assign persons = "Alexander Moreno Briceño, Lera Lukashenko, Jim Pivarski, Holly Szumila-Vance" | split: ", " %}
{% include list_of_selected_profiles.html %}

The conveners can be [reached by email](mailto:alexander.moreno@uan.edu.co,valeriia.lukashenko@cern.ch,pivarski@princeton.edu,hszumila@jlab.org). <!-- markdown-link-check-disable-line -->

### Former Conveners:

- Sudhir Malik (CMS, University of Puerto Rico), 2018-2022
- Michel Hernandez Villanueva (Belle II, DESY), 2021-2022
- Dario Menasce (INFN Milano), 2016-2019
- Sam Meehan (CERN, ATLAS and FASER), 2020
- Meirin Oan Evans (ATLAS), 2021
- Wouter Deconinck
- Kilian Lieret
- Jason Veatch
