---
title: "HSF Generator Meeting, 14 February 2019"
layout: meetings
---
# {{page.title}}

*Agenda:
[<span class="underline">https://indico.cern.ch/event/799280/</span>](https://indico.cern.ch/event/799280/)*

*Present/Contributors: Andrea Valassi, Josh Mcfayden, Steve Mrenna,
Taylor Childers, Stefan Hoeche*

## News, general matters
  - This is a meeting of the five convenors to organise the upcoming
    general WG meetings.
  - Andrea: created mailing lists and a page in the HSF website.
  - Andrea: following up with the madgraph team about GPUs. Did not
    get a reply with technical details yet, but Junichi will be giving
    a talk at the JLAB workshop about this.

## Workshop follow-up and proceedings
  - Workshop proceedings in Overleaf:
    [<span class="underline">https://www.overleaf.com/1326158343ftxgrxxcspxg</span>](https://www.overleaf.com/1326158343ftxgrxxcspxg)
      - Andrea: did not do any work on this
      - Josh: added a table to proceedings
  - Josh: rerunning some of the tests that had been presented at the
    workshop, so that it may be a bit more like apples to apples for
    sherpa to madgraph, in particular about unweighting.
      - Stefan: please include me in the loop on this.
      - Josh: quoting the fraction of negative weights is not enough,
        it would be nice to do some convolution of the statistical
        dilution with simulation and reco time.
  - Josh: also following up on ATLAS vs CMS comparison. There was some
    discussion between ATLAS and CMS. The CMS fraction seems too
    small. ATLAS contacted the CMS generator convenors, who are
    looking at this.
      - Steve: one thing that is not clear is how the time to generate
        the gridpacks is accounted for. Taylor: actually ATLAS too
        does not account for this.
      - Josh: suggest that we send a mail to both ATLAS and CMS
        convenors about the status of the comparison. Andrea: good
        idea, we can ask them to present the status
  - Josh: also following up about the sharing of productions between
    ATLAS and CMS. Turns out that for SUSY searches their groups are
    using the same processes but generated in slightly different ways,
    and they are now thinking of sharing the samples.
      - Andrea: would be nice to also discuss this in two weeks.
      - Taylor: would be nice if this can also be done for background.
      - Stefan: very good to hear that this is happening already, and
        if this happens for signal then we could also get to
        background eventually.
  - Stefan: added one plot with Haswell to KNL comparison. We manage
    to run sherpa on KNL even if there is very little memory. This is
    using MPI parallelization, it’s including some new work done over
    Christmas.
      - Taylor: GPUs are different anyway.
      - Andrea: would be useful to get this into the benchmarking
        suite. Stefan: can certainly send you a script for the tests
        that went into this plot.

## Regular meetings
  - First general meeting in two weeks on Thursday 28 at 4pm
  - Andrea: schedule ATLAS/CMS comparison and sample sharing, anything
    else specifically?
  - Taylor: should try to focus the WG on where we want to be in 5
    years, with new architectures (e.g. GPU) and technologies (e.g.
    ML). Josh: agree, but not clear how to do that. Josh: also,
    related to this, keep in mind how to fund this effort and get the
    relevant people. Stefan: could use the results in the proceedings
    to motivate this work and put priorities between physics and
    computation - it was not clear to me before the workshop that
    getting the physics results is of limited relevance if we have no
    computing for that. Taylor: important to point out that there is
    an organized effort to do this, e.g. for madgraph/GPU this avoids
    having many different people doing work independently - we should
    avoid wasting people’s time.

## AOB
  - Negative weights
      - Josh: would it be “easier” to remove automation when attacking
        this problem? Stefan: yes it may make sense to do this in a
        dedicated way for W and Z production. The problem of negative
        weights is certainly process-specific.
