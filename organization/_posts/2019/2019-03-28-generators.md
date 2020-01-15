---
title: "HSF Generator Meeting, 28 March 2019"
layout: meetings
---
# {{page.title}}

*Agenda:
[<span class="underline">https://indico.cern.ch/event/804266</span>](https://indico.cern.ch/event/804266)*

*Present/Contributors: Andrea Valassi, Josh McFayden, Servesh
Muralidharan, Qiang Li, Frank Siegert, Graeme Stewart, Stephen Jiggins,
Efe Yazgan*

## ATLAS and CMS event generator accounting update 
  - Latest numbers in
    [<span class="underline">https://www.overleaf.com/1326158343ftxgrxxcspxg</span>](https://www.overleaf.com/1326158343ftxgrxxcspxg)

![Table 1 of proceedings](/images/2019-03-28-generators1.jpg)
  - Qiang: update on CMS accounting numbers (attached to the agenda):
      - Official Numbers from CMS Computing:
          - Gen+Sim = 50 sec/ev/core
          - Digi: 10 sec/ev/ecore
          - Reco: 25 sec/ev/core
          - Assume 1 core = 10 HS06, note this introduces a 20% error
            at least.
      - Table 1, CMS:
          - Total Events:
            1.41+1.96+0.43+1.94+0.712+0.154+0.876+1.95=9.4B
          - GEN fraction \~7.3% (1.41\*0.05 + 1.96\*0.17 + 0.43\*0.05 + 
            1.94\*0.04 + 0.712\*0.05 + 0.154\*0.05 + 0.876\*0.05 +
            1.95\*0.05)/9.4, where 0.05, 0.17 and 0.04 are from
            numbers achieved from local tests, presented in last
            meetings (DY LO MLM 5%, DY NLO 17%, TT powheg 4%, QCD
            50to80 Pythia8 \<1%)
          - Thus GEN -\> 85\*7.3%=6.2 sec/ev/core (6.2\*9.4B=58.3B)
  - Qiang: this 7% is GEN as a fraction of MC production, but MC prod
    is only \~50% of worldwide CMS computing, so this translates to
    GEN being approximately 4%.
      - Josh: note that 4% is still lower than the ATLAS number
        previously presented, but it is larger than the 1% previously
        presented by CMS at the CSRG. On the other hand, there are
        also some other small samples missing.
      - Josh: will also change the ATLAS numbers to have a closer
        apples-to-apples comparison
  - Josh on ATLAS numbers in the other tables.
      - Andrea: would be nice now to concentrate on one biggest
        consumer, ie sherpa for ATLAS and MG for CMS in V+jets. Josh:
        this is exactly what I am trying to do in the next tables in
        the document. Table 2 is one V+jets (W→eν+jets@NLO).

![Table 2 of proceedings](/images/2019-03-28-generators2.jpg)
  - Josh: two columns for sec/evts, to take into account the
    generation time with and without filtering. Average 400 sec/event
    because many events are thrown away by filtering, while
    60sec/event is intrinsic generator speed. Andrea: interesting,
    maybe CMS generation is faster also because of a different
    filtering.
  - Josh: CPU% adds up to 100% for all rows. It is based on the first
    column, not the second.
  - Would it be possible to get similar numbers as in Table 2 and 3
    for CMS (from local tests?). Qiang: will try to get some numbers
    for the next meeting in two weeks.
  - Josh on the next section on benchmarking (eg figure 2).
      - Josh: we should think of a more meaningful way to present
        weight effect than just negative weight distribution. Andrea:
        could this be a multiplicative factor, “you have to generate
        and simulate 10 times as many events”? Frank: yes a
        multiplicative factor is probably what we need, but we need to
        convolute all sorts of effects, not just negative weights but
        also non-unity weights, so we definitely need to include
        weight distributions.

![Figure 2 of proceedings](/images/2019-03-28-generators3.jpg)
  - Josh: in figure 4 the difference between blue and yellow is in the
    choice of the scale. Efe: please write down the scale choice, so
    we can try the same in CMS too. Frank: we should make sure that
    green MG and yellow sherpa are comparable.

![Figure 4 of proceedings](/images/2019-03-28-generators4.jpg)

## AOB
  - Josh to Andrea: any progress in investigating the use of some
    machines for benchmarking? Andrea: would help to get a five-line
    plan, do we need this one day per week, or one week every few
    months, is it bare metal, and so on.
  - Graeme: there was a presentation by Junichi about Madgraph on
    GPUs. Should invite him along to one of these meetings. Graeme:
    will email him and cc the WG convenors.
