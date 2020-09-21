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

  .stable {
  	background: #28a745;
    width: 1.3em;
    height: 1.3em;
    border-radius: 0.65em;
    color: white;
    font-weight: bold;
    padding: 0em;
    display: inline-block;
    text-align: center;
    padding-bottom: 2.5ex !important;
  }

  .beta {
  	background: #ffc107;
    width: 1.3em;
    height: 1.3em;
    border-radius: 0.65em;
    color: white;
    font-weight: bold;
    padding: 0em;
    display: inline-block;
    text-align: center;
  }

  .alpha {
  	background: #6c757d;
    width: 1.3em;
    height: 1.3em;
    border-radius: 0.65em;
    color: white;
    font-weight: bold;
    padding: 0em;
    display: inline-block;
    text-align: center;
    padding-bottom: 2.5ex !important;
  }
</style>


## Idea

Training in software and computing are essential ingredients for the success of any HEP experiment. As most experiments have similar basic prerequisites (Unix shell, Python, C++, …) we want to join our efforts and create one introductory software training curriculum that serves HEP newcomers the software skills needed as they enter the field, and in parallel, instill best practices for writing software.

The curriculum is comprised of a set of standardized *modules*, so that students can focus on what is most relevant to them.

## The modules

* Want to **study**? Click on the book <span class="glyphicon glyphicon-book"></span> or video <span class="glyphicon glyphicon-film"></span> button
* Want to **contribute**? Click on the wrench <span class="glyphicon glyphicon-wrench"></span>

### Beginner level

| Module  | Description  | Status | Authors | Repo | Site/Material                           |
| -------- | -------- |-------- |-------- |-------- |-------- |
| The Unix Shell | Introduction to the [unix command line/shell](https://en.wikipedia.org/wiki/Unix_shell) | <span class="stable">✔</span> | [authors](https://github.com/swcarpentry/shell-novice/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/swcarpentry/shell-novice"></a>  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/shell-novice"></a> |
| Advanced Shell | E.g. SSH |  |  | | |
| Version controlling with git | | <span class="stable">✔</span> | [authors](https://github.com/swcarpentry/git-novice/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/swcarpentry/git-novice"></a>  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/git-novice"></a> |
| Advanced git  | | | | | |
| Programming with python | | <span class="stable">✔</span> | [authors](https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/swcarpentry/python-novice-inflammation"></a>  | <a class="glyphicon glyphicon-book" href="http://swcarpentry.github.io/python-novice-inflammation"> |
| Basic ``C++`` | | | | | |
| Build systems:  ``cmake`` | | <span class="stable">✔</span> | [authors](https://github.com/hsf-training/hsf-training-cmake-webpage/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-cmake-webpage"></a> | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-cmake-webpage/"></a> |
| Distributed file systems and grid computing |||| | |
| ``ROOT`` | | | | | |
| ``uproot`` | Reading and writing ROOT files without having to install ROOT. | <span class="beta">β</span> | [authors](https://github.com/hsf-training/hsf-training-uproot-webpage/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-uproot-webpage"></a>  | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-uproot-webpage/"></a> |
| A simple analysis | A simple analysis using CMS open data| <span class="stable">✔</span> | [authors](https://github.com/hsf-training/hsf-training-cms-analysis-webpage/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-cms-analysis-webpage"></a> | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-cms-analysis-webpage/"></a>  &nbsp; <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=gplMywJAFDI&list=PLKZ9c4ONm-Vk0wnDKaaovoEkOk3PVdL0V"></a> |
| Unit testing                                | [Unit testing](https://en.wikipedia.org/wiki/Unit_testing) in python | <span class="beta">β</span> | [authors](https://github.com/carpentries-incubator/python-testing/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/carpentries-incubator/python-testing"></a> | <a class="glyphicon glyphicon-book" href="http://carpentries-incubator.github.io/python-testing/"></a> |

### Intermediate

| Module  | Description  | Status | Authors | Repo | Site/Material |
| -------- | -------- |-------- |-------- |-------- |-------- |
| Parallel programming |  |  |  |  | |
| Docker | Introduction to the [docker](https://www.docker.com/) container image system | <span class="stable">✔</span> | [authors](https://github.com/hsf-training/hsf-training-docker/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-docker"></a> | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-docker/index.html"></a> &nbsp;  <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=Qr42pEtio-Q&list=PLKZ9c4ONm-VnqD5oN2_8tXO0Yb1H_s0sj"></a> |
| Workflows & reproducability | E.g. ``yadage`` and ``reana`` |  |  |  | |
| Machine learning | | <span class="beta">β</span> | [authors](https://github.com/hsf-training/hsf-training-ml-webpage/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-ml-webpage"></a> | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-ml-webpage"></a> |
| CI/CD | [Continous integration and deployment](https://docs.gitlab.com/ee/ci/) with [gitlab](https://about.gitlab.com/) | <span class="stable">✔</span> | [authors](https://github.com/hsf-training/hsf-training-cicd/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-cicd"></a> | <a class="glyphicon glyphicon-book" href="https://hsf-training.github.io/hsf-training-cicd/"></a> &nbsp; <a class="glyphicon glyphicon-film" href="https://www.youtube.com/watch?v=C9auGFgIHns&list=PLKZ9c4ONm-VmmTObyNWpz4hB3Hgx8ZWSb"></a> |

### Advanced


| Module  | Description  | Status | Authors | Repo | Site/Material |
| -------- | -------- |-------- |-------- |-------- |-------- |
| Documentation | ``sphinx``, ``doxygen``, etc. | | | | |
| Event generation and MC | ``pythia``, ``sherpa``, ``madgraph``, etc. | | | | |
| alpaka | [alpaka](https://alpaka.readthedocs.io/en/latest/index.html) is a header-only C++ abstraction library for accelerator development | <span class="alpha">α</span> | [authors](https://github.com/hsf-training/hsf-training-alpaka-webpage/blob/gh-pages/AUTHORS) | <a class="glyphicon glyphicon-wrench" href="https://github.com/hsf-training/hsf-training-alpaka-webpage"></a> |  |

## Further reads

* I want to **contribute** or **teach**:
Contributions of any kind are very welcome! There are various ways you can get involved:

    * Join our **meetings** to give feedback and discuss with us (details at our [main page](/workinggroups/training.html))
    * **Bugs reports or feature requests**: Directly open an issue on github or (even better) submit a pull request to fix things.
    * Want to **contribute your own module**? We compiled a small list of recommendations [here](/training/module-guidelines.html). Of course we always encourage you to talk to us early for a better coordination. There is also more technical information for [creating a new module](/training/howto-new-module.html) or using the [HSF style](/training/howto-update-module-style.html).
    * Want to **help out at a workshop?**: [More information on the different roles in our training events](/training/educators.html)
    * Want to **organize your own workshop**? [ We got you covered.](/training/howto-event.html)
