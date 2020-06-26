---
title: "Towards a HEP Software Training curriculum"
layout: plain
---

<style type="text/css">
  table {
    padding: 0; 
    width: 100%;
  }
  table tr {
    border: 1px solid #cccccc;
    background-color: white;
    margin: 0;
    padding: 0; 
  }
  table tr:nth-child(2n) {
    background-color: #f8f8f8; 
  }
  table tr th {
    font-weight: bold;
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px; 
  }
  table tr td {
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px; 
  }
  table tr th :first-child, table tr td :first-child {
    margin-top: 0; 
  }
  table tr th :last-child, table tr td :last-child {
    margin-bottom: 0; 
  }
</style>

Training in software and computing are essential ingredients for the success of any HEP experiment. As most experiments have similar basic prerequisites (Unix shell, Python, C++, …) we want to join our efforts and create one introductory software training curriculum that serves HEP newcomers the software skills needed as they enter the field, and in parallel, instill best practices for writing software.

The curriculum is comprised of a set of standardized *modules*, so that students can focus on what is most relevant to them. More about the style of these modules is written in the [guidelines for training material](/training/module-guidelines.html).

This mission relies on active contributors: [This page](/training/educators) outlines the different roles that need to be filled.  

## The modules

### Beginner level

| Module  | Description  | Status |
| -------- | -------- |-------- |
| The Unix Shell | Introduction to the [unix command line/shell](https://en.wikipedia.org/wiki/Unix_shell) | [Created & Maintained by software carpentries](http://swcarpentry.github.io/shell-novice)|
| Advanced Shell | E.g. SSH | |
| Version controlling with git | | [Created & Maintained by software carpentries](http://swcarpentry.github.io/git-novice) |
| Advanced git  | | |
| Programming with python | | [Created & Maintained by software carpentries ](http://swcarpentry.github.io/python-novice-inflammation) |
| Build systems: From ``gcc`` to ``cmake`` | | |
| Basic ``C++`` | | |
| Distributed file systems and grid computing || |
| ``ROOT`` | | |
| A simple analysis | A simple analysis using CMS open data| [Created by S. Wunsch; maintained by HSF](https://hsf-training.github.io/hsf-training-cms-analysis-webpage/) |
| Unit testing                                | [Unit testing](https://en.wikipedia.org/wiki/Unit_testing) in python | [Created by K. Huff](http://katyhuff.github.io/python-testing/) |

### Intermediate

| Module  | Description  | Status |
| -------- | -------- |-------- |
| Parallel programming |  | |
| Docker | Introduction to the [docker](https://www.docker.com/) container image system | [Created by M. Feickert](https://matthewfeickert.github.io/intro-to-docker/) |
| Workflows & reproducability | E.g. ``yadage`` and ``reana`` | |
| Machine learning | | |
| CI/CD | [Continous integration and deployment](https://docs.gitlab.com/ee/ci/) with [gitlab](https://about.gitlab.com/) | [Created by G. Stark; maintained by HSF](https://hsf-training.github.io/hsf-training-cicd/) |

### Advanced


| Module  | Description  | Status |
| -------- | -------- |-------- |
| Documentation | ``sphinx``, ``doxygen``, etc. | |
| Event generation and MC | ``pythia``, ``sherpa``, ``madgraph``, etc. | |

## Contributing

Contributions of any kind are very welcome! There are various ways you can get involved:

* Join our meetings to give feedback and discuss with us (details at our [main page](/workinggroups/training.html))
* Bugs reports or features requests: Directly open an issue on github or (even better) submit a pull request to fix things.
* Want to contribute your own module? We compiled a small list of recommendations [here](/training/module-guidelines.html). Of course we always encourage you to talk to us early for a better coordination.
* [More information on the different roles in our training events](/training/educators.html)
* [Want to organize your own workshop? We got you covered.](/training/howto-event.html)

## FAQ

>  Where can I find the source (github repository) of the web pages linked above? 

Scroll down the page and click on "Source" or "Edit on GitHub".
