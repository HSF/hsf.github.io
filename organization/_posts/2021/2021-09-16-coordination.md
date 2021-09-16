---
title: "HSF Coordination Meeting #214, 16 September 2021"
layout: plain_toc
---

Present/Contributing:
Alexander Moreno,
Allie Hall,
Andi Salzburger,
Attila Krasznahorkay,
Benedikt Hegner,
Caterina Doglioni,
Davide Constanzo,
Dorothea vom Bruch,
Eduardo Rodrigues,
Graeme Stewart,
Kevin Pedro,
Kilian Lieret,
Krzysztof Genser,
Kyle Knoepfel,
Luke Kreczko,
Marc Paterno,
Mason Proffitt,
Meirin Oan Evans,
Michael Villanueva,
Paul Laycock,
Pere Mato,
Philippe Canal,
Serhan Mete

Apologies: Andrea Valassi, Josh McFayden, Efe Yazgan

## Presentation about PyHEP workshop by E. Rodrigues

Slides are [attached to the agenda](https://indico.cern.ch/event/1043627/).

Graeme - gender balance was better at PyHEP cf. vCHEP, but we also noticed that the younger the demographic the better the balance.

Eduardo - indeed, this is a common trend.

Is PyHEP actually better as an online event, due to the very high turnout?

- There is a lot to be gained from f2f meetings, so we don't want to abandon that entirely; perhaps a hybrid approach would be a future solution, when travel is easier.

## News, general matters, announcements

### Julia Mini-Workshop

The *Julia for HEP* mini-workshop will take place on Monday 27 September: <https://indico.cern.ch/event/1074269/>.

### HL-LHC Review Phase 2

Reminder that we have the first (evolving) drafts of most documents:

- [Generators](https://drive.google.com/file/d/18_ID_XLw4K1AjaYXuQC2pdNjZEWWbhk4/view?usp=sharing) (PDF copy)
- [Simulation](https://docs.google.com/document/d/1Rl9PH43gEWSzYtELT12-77zi-uW1avz8uClL44wcDvE/edit?usp=sharing) (Google Doc)
- [Foundation](https://docs.google.com/document/d/160o1LtpjL0Zgb4Suey1vyD_l03Ggh4frrADXMlOUcC4/edit?usp=sharing) (Google Doc)
- Analysis
  - [Data Science Tools](https://docs.google.com/document/d/13b1icyAsr99gPqgTQo5-Lso5x6aotdvVXe8lXjD5YvY/edit?usp=sharing) (Google Doc)
  - [ROOT](https://docs.google.com/document/d/15dlmSbOUCXXC35tOX5axNlK96MqnOqw_93RnSgCpDjI/edit?usp=sharing)
- [DOMA](https://www.overleaf.com/read/gkbppxdvcvvf)

These are now being prepared for submission to the LHCC reviewers.

### WLCG Report

The software and projects [report for WLCG](https://docs.google.com/document/d/1-2VXmhEu2KXsx6DlJJrj1DO4FyPsHPsK/edit?usp=sharing&ouid=108095447452240056352&rtpof=true&sd=true) for 2021H2 has been written and was submitted 15 September.

Thanks to all for implicit (gathered from LHCC talks) and explicit inputs!

### NorCC Meeting

Presentation at NorCC meeting: [slides](https://docs.google.com/presentation/d/1w0Kk8OPNEdQe7G5PNbgRO6G9bOEfYq0nH7j9TgwO_Kc/edit?usp=sharing) was well received (slides are a good reference of funded projects). Main point that came up in the discussion was the need to rethink algorithms from a parallel standpoint to use modern hardware.

### HSF Support Letter, ExaTEPP

UK colleagues are applying for the second phase of funding in the ExCALIBUR programme. Because of some changes in the programme (reducing the number of bids that will succeed) they have a joint bit with the Lattice community, dubbed ExaTEPP, but this carries on work that was done in the [programme’s first phase](https://excalibur.ac.uk/projects/excalibur-hep/).

- The [ExaTEPP overview](https://drive.google.com/file/d/1D6WeS4p0yq60yFdd8lWCoIP9-Mikes7H/view?usp=sharing)
- [Support letter draft](https://docs.google.com/document/d/1RAVFsVsM4AEbT4lhDpFoatxyqe9JSB4I-DP7Amegj_g/edit?usp=sharing)

Meeting endorsed the proposal and the HSF supports the bid.

## Working Group Updates

### Data Analysis

Meeting tentatively scheduled for 29 Sep to wrap up the metadata document and preview plans for next topical meeting. Specifically, we plan to discuss ways to expand the analysis benchmarks in collaboration with IRIS-HEP.

[Analysis metadata document](https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY/edit) mostly finished except the last section.

We note a tension between representative analyses of what the experiments are doing and open data analysis - to be explored!

### Detector Simulation

Considering possible topics for an ML-oriented meeting later in the fall

### Reconstruction and Software Triggers

Still planning second 4D reconstruction topical meeting and gathering feedback on a possible mini-workshop on heterogeneous computing (this would also involve the frameworks group).

### PyHEP

Nothing else to report atop the PyHEP 2021 report, see the slides in Indico.

### Software Tools and Packaging

Starting to plan next topical meetings; more details to follow. We've been in touch w/ potential speakers/topics but the progress has been slow due to vacation schedule. As always, if you wish to see specific topics covered feel free to get in touch w/ us.

### Software Training

- Successful C++ training end of August.
- Plan to have C++ and Training hackathon/brainstorming - Date to TBD. Please join!
- CSBS paper: reviewer comments being implemented
- ACAT 2021: abstract submitted

- Upcoming training - Helpers welcome!
  - Matplotlib training: November 22nd-26th
  - Basic curriculum (Software Carpentry): December 13th-15th

### Event Generators

We are working on the comments received from the community about the document for the LHCC review. We will circulate a new draft in the next few days.

### Frameworks

After last week's meeting (discussing about developments in CMSSW), we are in the process of organising the next meeting. Which may likely be (only) on 6th October, about ATLAS's multi-threaded (physics performance) monitoring code.

## Other Interest and Activity Areas

### Licensing

Started a discussion with the HepMC authors about changing the license away from GPL. This seems to be going well, but needs still to conclude.

HepMC is the bridge from the theory/generator world and experiment code, so it's a key package to have non-viral.

---

## AOB

### Linux Future Committee

Considering the future linux distributions to be used in HEP there has been a number of meetings outlining plans ([GDB](https://indico.cern.ch/event/876793/), [Linux Future Committee](https://indico.cern.ch/event/1070475/)). There seems to be convergence on proposing CentOS Stream 8 (to be followed by 9) for the experiments:

> ...we propose to target CentOS Stream 8 as the standard distribution for experiments.  We feel that deploying CentOS Stream 8 is low risk, and we now have months of experience running production workloads on CentOS Stream 8 without any significant issues.

(CERN/Fermilab Joint Statement)

Some concern expressed that updates might still break *existing* releases. This could indeed happen (not clear how high the risk is). Would we need to build containers for releases to mitigate this?

Such concerns should be expressed to the LFC.

### SIDIS COST Proposal

We are currently working on a funding proposal (EU COST) in the context of the "Software Institute for Data Intensive Sciences", aiming to bridge the gap between computer scientists and natural science software engineers. The "grand theme" of the proposal will be around the topic of "software sustainability".

For a success proposal it is useful to include participants also from "inclusive target" countries (mostly eastern European countries). In case you have contacts in this direction please get in contact with Graeme or Stefan.

### Website

#### Absolute URLs

- So far we had a lot of links to subpages linked like this: `[text](/link/to/page.html)`.
- However this breaks deploys via github pages from forks of our repository (so it's an obstacle to testing the page)
- Proper procedure is `[text]({{site.baseurl}}/link/to/page.html)`
- Same for links/images in HTML
- More technical background in [this PR](https://github.com/HSF/hsf.github.io/pull/976)
- There's a new check in place that will complain if you create links without `site.baseurl`

#### pre-commit hooks

- We have added several checks via [pre-commit](https://pre-commit.ci/)
- This includes a spell checker with very few false positives (12 for the whole page as of now). False positives can be added to `codespell.txt`

To use the checks locally, run

```sh
pip3 install pre-commit
pre-commit install  # in hsf.github.io 
```

this will run checks every time you run `git commit`.

### Next Meeting

Next meeting 30 September.
