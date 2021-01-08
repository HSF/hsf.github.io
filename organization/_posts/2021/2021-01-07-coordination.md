---
title: "HSF Weekly Meeting #199, 7 January 2021"
layout: plain
---

Present: Graeme Stewart, Teng Jian Khoo, Eduardo Rodrigues, Pere Mato Vila, Agnieszka Dziurda, Serhan Mete, Allison Hall, Andreas Salzburger, Chris Jones, David Lange, Dorothea vom Bruch, Efe Yazgan, Gloria Corti, James Catmore, Caterina Doglioni, Jim Pivarski, Kevin Pedro, Krzysztof Genser, Marc Paterno, Meirin Oan Evans, Paul Laycock, Philippe Canal, Sudhir Malik, Torre Wenaus, Daniel Elvira, Vincent Pascuzzi, Witold Pokorski, Andrea Valassi. Agnieszka Dziurda, Andreas Morsch, Eduardo Rodrigues, Jyant, Marc Paterno, markusw, Meirin Oan Evans

Apologies: Liz Sexton-Kennedy, Josh McFayden

## Review of 2020 and Planning for 2021

See slides attached to the [agenda](https://indico.cern.ch/event/981562/), presented by Graeme Stewart.

### Feedback on the presentation / Discussion Points

#### Working groups

- Caterina Doglioni: Should we build better bridges between HSF and experiments, taking the opportunity of the new batch of conveners?
- Eduardo Rodrigues: in LHCb, we had a number of links / presentations. We keep the experimental committees aware of what we're doing and it's been working well.
- Caterina Doglioni: LHCb seems covered, I was suggesting a formal/informal "introduction to the new HSF WG conveners" e.g. in weekly meetings of ATLAS / CMS.
- Graeme: also worth looking back at mandates to check whether they are clear enough - we should make clear that we're here to be helpful. **ACTION**
- Marc Paterno: we could write a letter to other experiments as well to let them know they're welcome to join.
    - Graeme: we have good contacts with LHC and Belle-II, DUNE. We could write an email to the various experiments, pointing out the new conveners in 2021, and we can come and talk about HSF in the New Year. **ACTION**

#### Workshops

- Kevin Pedro: Zoom-fatigue problem -> make the workshops more focused on particular topics so that people pick and choose what to attend.
- Graeme: the 4-day workshop could probably have been spread out in 4 different meetings... even if it was focused and had improved based on the May workshop feedback.

---

- Andi Salzburger: on workshop, "complaints" about length of workshops especially late in the year. More topical workshop: should the WGs be doing their individual "workshops"?
- CD: agree with Andi. If no workshop, will we miss joint workshops with WLCG?
    - Liz and Graeme are in the management board - need to also discuss there.
- Andrea Valassi: are we actually managing to get people to talk together even when they go to the same workshop? There is the risk that people only attend their session.
- Andi: if this is "out of the box" of the WGs, we could have joint sessions between WG A and WG B. This could be a working mode. 
- Graeme: in particular we could also talk about I/O matters, which links analysis, frameworks and WLCG.
- Conclusion from this part: explore more restricted but cross-cutting topics. No appetite for a spring workshop, but keep open option for autumn (TBD with WLCG). **ACTION**

#### Training

- Sudhir Malik - Training WG: 
    - We (training) come from different experiments, so it would be good to understand what we are providing / what are our contributions in terms of simulation etc. Highlighting our success in terms of practical things. Some answer to "What have we achieved". **ACTION**
    - Question to all other WGs: training is connected to all other WGs. Physics / physics object groups help with newcomers training, so we could do the same with HSF.

#### Organisational Engagement

- David Lange: it would be useful from the coordination / WG groups to have more understanding of what the different projects that are "connected" to HSF. 
- Graeme: this list is not complete. We could identify other projects to have some engagement with. 
- Marc Paterno: maybe update the slides with links of what the organizations are?
- Open point: make sure everybody knows which organizations we have engaged with in the past, and how to engage in the future. **ACTION**

#### Software Projects

- Pere Mato: in terms of "hosted projects" we can't necessarily do like Apache, but we could aim for doing more. Where we can facilitate common work on software, we / conveners should jump on that.
- Andrea Valassi: within e.g. the Generators WG there is more preparatory work that has helped out being involved in porting Madgraph to GPUs.
- Graeme: in the coordination group we could do more, and see if there are other projects that want to be under the umbrella of HSF. E.g. the Phoenix event display was happy in being an HSF project, even the banner home could be a useful thing.

#### Post-Community White Paper

- Eduardo: have you looked back at the community whitepaper? 
- Graeme: It takes a lot of work to do full reviews, but we should take a look at that and see how things are going (we did some of it for the LHCC document). 
- Eduardo: not at all suggesting to prepare a formal document. The (informal) exercise will be useful for us in any case.
  
## News, general matters, announcements

### HDR Institute - Letter of Collaboration

We have been contacted by Mark Neubauer and Shih-Chieh Hsu asking for a letter of intention to collborate if their NSF proposal for *HDR Institute: Accelerated AI Algorithms for Data-Driven Discovery* is funded. Proposal:

> Graeme Stewart has agreed to coordinate the collaboration between the HEP Software Foundation (HSF) and A3D3. This collaboration will include AI efforts in event reconstruction and software triggering, and cohosting training and community events of mutual interest.

A summary of the proposal and draft letter (it's the NSF standard text) are attached to Indico.

The coordination group are favourable. Please give any feedback or comment by 11 January.

### Working Group Convenors for 2021

The search for new working group convenors for 2021 has completed. Our new convenors are:

**Reconstruction and Software Triggers**

- Dorothea vom Bruch (LPHNE/CNRS, LHCb, new)
- Andreas Salzburger (CERN, ATLAS, new)

Caterina Doglioni and Agnieszka Dziurda step down.

**Detector Simulation**

- Ben Morgan (Warwick, ATLAS+Geant4, new)
- Krzysztof Genser (Fermilab, Mu2e+Geant4, new)
- Kevin Pedro (Fermilab, CMS, new)

Witek Pokorski, Gloria Corti and Philippe Canal step down.

**Training**

- Michel Hernandez Villanueva (Mississippi, Belle II, new)
- Meirin Oan Evans (Sussex, ATLAS, new)

Sam Meehan and Kilian Lieret step down.

**Tools and Packaging**

- Marc Paterno (Fermilab, DUNE, new)
- Mircho Rozodov (CERN, CMS, new)

Ben Morgan and Martin Ritter step down.

We’d like to give huge thanks to Caterina, Agnieszka, Witek, Gloria, Philippe, Sam, Kilian, Ben and Martin for their work last year (and often before).

A warm welcome to Dorothea, Andi, Krzysztof, Kevin, Michel, Meirin, Marc, Mircho to the team, as well as to Ben for bravely swapping groups!

### Compute Accelerator Forum

The next [Compute Accelerator Forum](https://indico.cern.ch/event/975003/) is next week, Wednesday 13 January, 16h30 CERN time. Two topics, SYCL and HLS4ML:

* Heterogeneous Modern C++ using Khronos SYCL ad one API (Michael Wong, Codeplay)
* Fast Deep Learning Inference for Particle Physics and Beyond ( Vladimir Loncar, CERN)

### Software and Computing Roundtable

The [January edition](https://indico.jlab.org/event/420/) of the Software and Computing Roundtable is Tuesday 12 January, 17h CERN time.

As the new partner organising these events we have an HSF focused meeting: Graeme on HSF overview, Eduardo on PyHEP and Sudhur on Training. *All welcome to help discuss stronger links and common activities with our Nuclear Physics colleagues.*

---

## AOB

### IRIS-HEP Feedback

We have been asked to give another round of feedback to IRIS-HEP at their next steering board meeting on 16 February. Can you think about feedback (the good, the bad, the ugly) to send via Graeme?

For reference, the feedback given last year is here: <https://indico.cern.ch/event/809181/>.

### Next Meeting(s)

- Please check the HSF Calendar to make sure that events for 2021 are listed correctly
    - Mostly this was done - thank you!
    - Only DUNE was missing - Liz was following up
- Next meeting will be 21 January
    - In this meeting we will focus on a looking forward to *working group plans* for 2021
