---
title: "HSF Generator Meeting #6, 27 June 2019"
layout: meetings
---
# {{page.title}}

*Agenda:
[<span class="underline">https://indico.cern.ch/event/821205</span>](https://indico.cern.ch/event/821205)*

*Present/Contributors: Andrea Valassi, Stephen Jiggins, Josh McFayden,
Zach Marshall, Qiang Li, Kyle Cormier, Javi Fernandez Menendez, Simone
Amoroso, Alexander Grohsjean, Graeme Stewart, Steve Mrenna*

## General news / Josh
  - Low attendance initially due to clash with Parton Shower
    Uncertainties workshop
    ([<span class="underline">https://indico.cern.ch/event/827858/</span>](https://indico.cern.ch/event/827858/))
  - Propose to move from biweekly to monthly meetings
  - Ideas for longer term activities after the ATLAS/CMS accounting?
      - Andrea: preliminary to GPU/HPC port it would be nice to get a
        reproducible setup

## ATLAS and CMS event generator update / Qiang and Josh
  - Copied from the
    [<span class="underline">note</span>](https://indico.cern.ch/event/821205/contributions/3433135/note/)
    attached to the indico agenda:
      - <span class="underline">CMS numbers</span> in Table1 (Updates
        marked in red):
          - (1) [<span class="underline">Sample
            Statistics</span>](https://docs.google.com/spreadsheets/d/1vbNb4fWG5N5y9zqrpfGqFVH29DgkUzpR_jfVFH44Jxs/edit#gid=542361540):
            9.4-\>12.3B (we missed to count some samples)
          - (2) Reminder: Time/Evt numbers from Computing Experts
              - G+S = 50 sec /ev/core, D = 10 sec/ev/core, R = 25
                sec/ev/core : **<span class="underline">Tot:
                85sec/ev/core</span>**
          - (3) GEN fraction: updates from
            [<span class="underline">https://indico.cern.ch/event/804266/</span>](https://indico.cern.ch/event/804266/)
              - Old GEN fraction ~7.3%
                (1.41\*0.05+1.96\*0.17+0.43\*0.05+1.94\*0.04+0.712\*0.05+0.154\*0.05+0.876\*0.05+1.95\*0.05)/9.4
              - New GEN fraction ~9.3%
                (1.62\*0.05+4.58\*0.17+0.43\*0.05+1.94\*0.04+0.712\*0.05+0.154\*0.05+0.876\*0.05+1.95\*0.05)/12.2
              - Where 0.05, 0.17 and 0.04 ....are from numbers achieved from local tests.
              - Thus for GEN we have 85\*9.3%\~7.9 sec/ev/core.
              - And the total GEN CPUs is 7.9\*12.26B\~96.9B
          - (4) In Table 1, we also provided GEN CPUs for each sample category:
              - For example, DY MG MLM\~1.9s/event for GEN step based on local
                tests, thus the total CPUs is 1.9\*1618M=3.07B.
          - **Summing over the numbers we get in Table1 for each sample
            category, we get 95.5B, which is quite close to 96.9B**
      - <span class="underline">ATLAS numbers</span> (Josh)
          - (1) Changes to numbers since last time came from two places:
              - Double counting of a small number of samples
              - Accidental removal of samples that should be included
              - \--\> Relatively small effect
          - (2) HS06s vs s
              - All the ATLAS numbers are raw seconds. Would be preferable
                to have in HS06 seconds instead. Technically this is
                possible but will require relatively major update to the
                code, in the end it's just a matter of finding the time to
                do it.
      - For reference: current tables in 
        [<span class="underline">https://www.overleaf.com/1326158343ftxgrxxcspxg</span>](https://www.overleaf.com/1326158343ftxgrxxcspxg):
          - Table 1
![Table 1 of proceedings]({{ site.baseurl }}/images/2019-06-27-generators1.png)
         - Table 2
![Table 2 of proceedings]({{ site.baseurl }}/images/2019-06-27-generators2.png)
  - Qiang/CMS
      - After update of statistics and reconstruction/digitisation/sim
        times, fraction of time for generation is now 9.3% for CMS
        compared to full MC production chain
      - One relatively large sample is missing, will add this and make
        few other updates later
      - Note that 9.3% for CMS and 17% for ATLAS is relative to full
        MC production chain only, not relative to the full Grid time.
        Andrea: should multiply both by around 50%? Josh: MC
        production is more like 70% for ATLAS.
      - CMS has only one s/evt column in table 2 while ATLAS has two,
        because CMS does not have the B/C filters that ATLAS uses,
        which need an extra efficiency factor.
  - Josh/ATLAS
      - ATLAS numbers are in raw seconds, will try to get HS06 seconds
        but it will take time. For CMS these are probably also in real
        seconds, not HS06 seconds now. Andrea: it only makes sense to
        ask ATLAS to move to HS06 if also CMS can do it, we should
        have the same units at least. Qiang: will follow up with CMS
        computing.
  - Andrea: why ttbar+jets LO missing for ATLAS even if so big for
    CMS? Josh: ATLAS chose not to generate these so far as they are
    largely covered by the Powheg production, but might generate these
    in the future using sherpa, which may also take quite some CPU
    time. Javi: for CMS this is used for SUSY analyses only for
    consistency, but for all other top analysis the ttbar inclusive is
    used.

## Les Houches / Josh
  - A lot of discussion on negative event weights in Les Houches
    (details in Josh’s slides)
  - Also discussed standard test configurations (using docker), output
    formats and GPU.
      - There was not a huge amount of positivity about porting
        generators to GPUs...

## ATLAS/CMS ttbar sample sharing / Kyle and Javi
  - Slide 9: differences between ATLAS/CMS come mainly from showering
    (different Pythia settings), rather than from ME (different Powheg
    settings)
  - Josh: would it be difficult to set up an EOS area for this?
    Andrea: probably not, should investigate. Zach: there is also a
    public EOS area that I have already used to share data with
    theorists.
      - Andrea: will follow up in CERN IT
  - Andrea: are LHE files actually produced already? Josh: in ATLAS we
    do separate the two steps, first we produce LHE files and then we
    shower to full HepMC, but CMS probably does it differently (with
    LHE an internal format in memory). The timeshare is probably 50-50
    % for a simple process like this.

## Proposal for PDGID extension / Zach
  - Zach: forwarded request to the CMS exotica conveners. Qiang: will
    do the same again.

## AOB
  - Next meeting in four weeks, to be confirmed (or even earlier if we
    have things to discuss)
