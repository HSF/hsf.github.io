---
title: "Community White Paper - Publishing to arXiv"
author: "Graeme Stewart"
layout: default
---

## Publishing CWP Working Group Papers to arXiv

This is the currently **and strongly** recommended way to publish each of the CWP WG
papers to [arXiv](https://arxiv.org). This route ensures a high presentation standard 
for the finished paper and allows reuse of bibtex files and author affiliations.
It also archives the document sources in the HSF document repository.

1. Finalise paper text, ensuring a good standard of English 
  (select your preferred variant and use it for the whole document),
  scientific content and rigour (we have come a long way -
  let's not fall at the final hurdle!).
  - Try to do this as much as possible within your working
    group, but ask the [CWP Ghost Writers team](mailto:hsf-cwp-ghost-writers@googlegroups.com) 
    for help if needed.
1. If necessary, convert from Google Doc to LaTeX using pandoc
    - Download your Google Doc as docx, a.k.a. MS Word, format
    - Using [pandoc](https://pandoc.org/), which is easily [installed](https://pandoc.org/installing.html),
      convert your docx file to latex:
        ```bash
        pandoc -f docx -t latex -o wgpaper.tex wgpaper.docx
        ```
    - The conversion is generally very accurate, but within `itemize` environments you
      may find that text is inside a spurious `quote` environment and that some
      odd non-breaking spaces appear. Just delete these.
1. Adopt the [JHEP preprint](https://jhep.sissa.it/jhep/help/JHEP/TeXclass/DOCS/JHEP-author-manual.pdf)
   style, using the template in the
   [software development paper](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-13_soft-dev/latex/).
    - Copy the `jheppub.sty` file into your latex area as it is needed for arXiv side compilation.
1. Build the author list: the **strongly recommended** way is to create a text file 
   `authors.txt` and use the `a2tex.py` tool to generate the TeX-formatted author list, 
   following the steps below:
   * `authors.txt`: the easiest is to start from the global CWP 
     [author list](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-01_roadmap/authors/authors.txt)
     and remove unnecessary entries. The line format in this file is:
       ```
       Surname, Forename - Affiliation_ID (footnote_key)
       ```
   * In the previous line, `Affiliation_ID` refers to the first word in the
   [affiliation list](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-01_roadmap/authors/addresses.txt) 
   and `footnote_key` to the number at the start of the line in the
   [footnote list](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-01_roadmap/authors/footnotes.txt). 
   If there are several affiliations, use ` & ` as the separator. If there are several 
   footnotes, separate them with a comma without surrounding spaces.
   * Run `a2tex.py` to generate the `authors.tex` file (and `arxiv.txt` for arXiv submission). Assumming you used the recommended 
   directory structure, the command to use is (use `--help` for more details):
       ```bash
       ../../HSF-CWP-2017-01_roadmap/authors/a2tex.py \
                                               --jhep \
                                               --footnotes ../../HSF-CWP-2017-01_roadmap/authors/footnotes.txt \
                                               --affiliations ../../HSF-CWP-2017-01_roadmap/authors/address.txt

       ```

1. To create the title page use the `\maketitle` statement (without arguments). **Before** 
you need to define the title, the abstract and the author list (look at 
[DOMA papger](https://github.com/HSF/documents/blob/master/CWP/papers/HSF-CWP-2017-04_doma/latex/hsf-cwp-dm.tex) 
for an example):
  * The title must be `HEP Software Foundation Community White Paper Working Group -- My Working Group`. 
  To define it, use the following statement:
      ```latex
      \title{the title text}
      ```
  * To define the astract, use:
    ```latex
    \abstract{your abstract text}
    ```
  * To define the author list, use the `authors.tex` file created at the previous step, 
  using:
    ```latex
    \input{authors.tex}
    ```
1. Add a copyright and license statement as a LaTeX comment (first line of your `.tex` 
file) - we strongly recommend:
    ```latex
    % Copyright (C) 2018, The HSF Community White Paper authors, licence CC-BY-4.0.
    ```
1. When finalised/finalising add the document sources to the
  HSF documents github repo,
  [https://github.com/HSF/documents](https://github.com/HSF/documents), following the
  usual pull request workflow. You can ask `hegner`, `eduardo-rodrigues`, `graeme-a-stewart`
  or `jouvin` for a review (best to pick at least two).
    -  Your paper should go into 
       `CWP/papers/HSF-CWP-2017-XX_short-wg-name/latex` (the first part for correct ordering,
       the second for allowing people to know which paper is which at a glance).
1. You can take advantage of the [large bibtex](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp.bib) file that
  was used for the roadmap for your references.
  - There is also a common file for references to [WG papers](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp-chapters.bib) themselves.
1. Upload to arXiv, use "Computational Physics (physics.comp-ph)" as the primary 
   subject, with "High Energy Physics - Experiment (hep-ex)" as a secondary.
    - Note that when uploading files to arXiv, it is the `.bbl` file of resolved and formatted 
      references that is required, not the source `.bib` files.
1. You can now finalise your own paper's reference in
  [CWP/papers/HSF-CWP-2017-01\_roadmap/latex/cwp-chapters.bib](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp-chapters.bib).
  - Make a final commit to github with this last piece of information so that all regenerated 
    WG texts will include the new cross reference correctly.

