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

  /* WHY DOES THIS NOT WORK? */
  a .glyphicon {
    text-decoration: none;
  }
</style>



Training in software and computing are essential ingredients for the success of any HEP experiment. As most experiments have similar basic prerequisites (Unix shell, Python, C++, …) we want to join our efforts and create one introductory software training curriculum that serves HEP newcomers the software skills needed as they enter the field, and in parallel, instill best practices for writing software.

The curriculum is comprised of a set of standardized *modules*, so that students can focus on what is most relevant to them. More about the style of these modules is written in the [guidelines for training material](/training/module-guidelines.html). If you want to create your own HSF training module, see [here](/training/howto-new-module.html); if you already have one and want to update it with the HSF style, see [here](/training/howto-update-module-style.html).

This mission relies on active contributors: [This page](/training/educators.html) outlines the different roles that need to be filled.

## The modules

### Beginner level

| Module  | Description  | Status | Authors | Repo | Site/Material                           |
| -------- | -------- |-------- |-------- |-------- |-------- |
| The Unix Shell | Introduction to the [unix command line/shell](https://en.wikipedia.org/wiki/Unix_shell) | stable | SWC |  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/shell-novice"></a> |
| Advanced Shell | E.g. SSH |  |  | | |
| Version controlling with git | | stable | SWC |  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/git-novice"></a> |
| Advanced git  | | | | | |
| Programming with python | | stable | SWC |  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/python-novice-inflammation"> |
| Basic ``C++`` | | | | | |
| Build systems:  ``cmake`` | | | H. Schneider |  | <a class="glyphicon glyphicon-book" href="https://henryiii.github.io/cmake_workshop/"></a> |
| Distributed file systems and grid computing |||| | |
| ``ROOT`` | | | | | |
| ``uproot`` | Reading and writing ROOT files without having to install ROOT. | beta | M. Profitt | | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-uproot-webpage/"></a> |
| A simple analysis | A simple analysis using CMS open data| stable | S. Wunsch |  | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-cms-analysis-webpage/"></a>  &nbsp; <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=gplMywJAFDI&list=PLKZ9c4ONm-Vk0wnDKaaovoEkOk3PVdL0V"></a> |
| Unit testing                                | [Unit testing](https://en.wikipedia.org/wiki/Unit_testing) in python | beta | K. Huff |  | <a class="glyphicon glyphicon-book" href="http://carpentries-incubator.github.io/python-testing/"></a> |

### Intermediate

| Module  | Description  | Status | Authors | Repo | Site/Material |
| -------- | -------- |-------- |-------- |-------- |-------- |
| Parallel programming |  |  |  |  | |
| Docker | Introduction to the [docker](https://www.docker.com/) container image system | stable | M. Feickert |  | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-docker/index.html"></a> &nbsp;  <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=Qr42pEtio-Q&list=PLKZ9c4ONm-VnqD5oN2_8tXO0Yb1H_s0sj"></a> |
| Workflows & reproducability | E.g. ``yadage`` and ``reana`` |  |  |  | |
| Machine learning | | WIP | | |  |
| CI/CD | [Continous integration and deployment](https://docs.gitlab.com/ee/ci/) with [gitlab](https://about.gitlab.com/) | stable | G. Stark |  | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-cicd/"></a> &nbsp; <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=C9auGFgIHns&list=PLKZ9c4ONm-VmmTObyNWpz4hB3Hgx8ZWSb"></a> |

### Advanced


| Module  | Description  | Status | Authors | Repo | Site/Material |
| -------- | -------- |-------- |-------- |-------- |-------- |
| Documentation | ``sphinx``, ``doxygen``, etc. | | | | |
| Event generation and MC | ``pythia``, ``sherpa``, ``madgraph``, etc. | | | | |
| alpaka | [alpaka](https://alpaka.readthedocs.io/en/latest/index.html) is a header-only C++ abstraction library for accelerator development | WIP |  |  |  |

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
