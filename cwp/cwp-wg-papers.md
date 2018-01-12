---
title: "Community White Paper - Publishing to arXiv"
author: "Graeme Stewart"
layout: default
---

## Publishing CWP Working Group Papers to arXiv

This is the currently recommended way to publish each of the CWP WG
papers to [arXiv](https://arxiv.org). This route ensures a high presentation standard 
for the finished paper, allows reuse of bibtex files and archives
the document sources in the HSF document repository, so it it strongly
recommended.

1. Finalise paper text, ensuring a good standard of English,
  scientific content and rigour (we have come a long way -
  let's not fall at the final hurdle!).
  - Try to do this as much as possible within your working
    group, but ask the [CWP Ghost Writers team](mailto:hsf-cwp-ghost-writers@googlegroups.com) 
    for help if needed.
1. If necessary, convert from Google Doc to LaTeX using pandoc
    - Download your Google Doc as docx, a.k.a. MS Word, format
    - Using [pandoc](https://pandoc.org/), which is easily [installed](https://pandoc.org/installing.html),
      convert your docx file to latex:
        - `pandoc -f docx -t latex -o wgpaper.tex wgpaper.docx`
    - The conversion is generally very accurate, but within `itemize` environments you
      may find that text is inside a spurious `quote` environment and that some
      odd non-breaking spaces appear. Just delete these.
1. Adopt the JHEP preprint style, using the template in the
   [software development paper](https://github.com/HEP-SF/documents/tree/master/CWP/papers/HSF-CWP-2017-13_soft-dev/latex/).
    - Copy the `jheppub.sty` file into your latex area as it is needed for arXiv side compilation.
1. The paper title should be `HEP Software Foundation Community White Paper Working Group \-- *My Working Group*`.
1. You will need to add an abstract for arXiv.
1. Add a copyright and license statement as a comment - we strongly recommend <br>`% Copyright (C) 2018, The HSF Community White Paper authors, licence CC-BY-4.0.`
1. When finalised/finalising add the document sources to the
  HSF documents github repo,
  [https://github.com/HEP-SF/documents](https://github.com/HEP-SF/documents), following the
  usual pull request workflow. You can ask `hegner`, `eduardo-rodrigues`, `graeme-a-stewart`
  or `jouvin` for a review (best to pick at least two).
    -  You paper should go into 
       `CWP/papers/HSF-CWP-2017-XX_short-wg-name/latex` (the first part for correct ordering,
       the second for allowing people to know which paper is which at a glance).
1. You can now take advantage of the [large bibtex](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp.bib) file that
  was used for the roadmap for your references.
  - There is also a common file for references to [WG papers](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp-chapters.bib) themselves.
1. Upload to arXiv, use "Computational Physics (physics.comp-ph)" as the primary 
  subject, with "High Energy Physics - Experiment (hep-ex)" as a secondary.
1. You can now finalise your own paper's reference in
  [CWP/papers/HSF-CWP-2017-01\_roadmap/latex/cwp-chapters.bib](https://github.com/graeme-a-stewart/documents/blob/master/CWP/papers/HSF-CWP-2017-01_roadmap/latex/cwp-chapters.bib).
  - Make a final commit to github with this last piece of information so that all regenerated 
    WG texts will include the new cross reference correctly.

