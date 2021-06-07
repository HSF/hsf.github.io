---
title: "HSF Generator Meeting #14, 27 May 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #14, 27 May 2021

*Agenda: <https://indico.cern.ch/event/1032037>*

Present (remote): Andrea Valassi, Olivier Mattelaer, Efe Yazgan, Graeme Stewart, Gurpreet Singh Chahal, Josh McFayden, Lix Sexton-Kennedy, Michal Kreps, Paolo Torrielli, Rikkert Frederix, Simone Amoroso, Stefan Roiser, Walter Hopkins, Fabio Maltoni (partly), Alexander Grohsjean, Phil Ilten (partly)

Apologies: Phil Ilten (will be late)

## News

Our WG paper has finally been published by Springer's Computing and Software in Big Science: 
- https://doi.org/10.1007/s41781-021-00055-1

There were a few talks on generators at the vCHEP conference last week. Slides and recordings are on the web. In particular:
- Mohan Krishnamoorthy, "Apprentice for Event Generator Tuning". https://indico.cern.ch/event/948465/contributions/4324130/
- Andrea Valassi, "Design and engineering of a simpliﬁed GPU workﬂow execution for the Madgraph5_aMC@NLO event generator". https://indico.cern.ch/event/948465/contributions/4323568/
- Juan Cruz Martinez, "MadFlow: towards the automation of Monte Carlo simulation on GPU for particle physics processes". https://indico.cern.ch/event/948465/contributions/4324113/

## Madgraph5_aMC@NLO report for LHCC review 
Speaker: O. Mattelaer

Olivier presents the slides describing the answers from the MG5aMC team to the question received for the second phase of the LHCC review of HL-LHC computing.
- MG5aMC allows a lot of very different calculations. It does not do PS itself, delegating it to Pythia instead.
- A composite team of theorists with different expertise, mostly permanent.
- It would be nice to give recognition to the people doing the coding, not just the paper authors.
- Theorists are mostly interested in doing new things, while a performance improvement even by a factor 2-4 is not that recognized (ok a factor 10 might be more recognised).
- Slide 6. There is quite a bit of help available from experimentalists initially, but what happens later can be a problem, if the new features are not picked in production by the experiments (eg MPI, readonly gridpack, previous GPU port...).
    - Simone: why are these things only useful for experimentalists? I use MPI for NNLO, this is probably used by theorists too? Also you theorists would use the GPU implementation if it is available. Olivier: again, theorists are more interested in new stuff than in faster stuff. For instance readonly gridpack is something no theorist would ever use. Alexander: agree for MPI (a tool for pheno study), but readonly gridpack is definitely very useful.
    - Josh: what exactly is readonly gridpack? Olivier: you put the gridpack on cvmfs and then you let jobs run from there.
    - Josh about MPI, where did this come from originally? Olivier: from the ATLAS MC WG, there was Zach and Stefano Frixione. The main focus was to use HPCs. Alexander: do you actively use this in ATLAS? Josh: no probably we are not, hence the complains; maybe Taylor requested this and is using this. Olivier: yes Taylor definitely helped a lot with this. Josh: agree that it can be frustrating, but do not recall that there was a really pressing request about that. Andrea: sometimes it is complex for a software provider outside the experiment to know with whom you should be talking to. Josh: about uptake timescales, we are actually quite fast now in picking up new releases. Efe: also in CMS we were quite slow, but now we are much faster in picking up new releases. Efe: maybe we should also invite the computing team.
    - Liz: I was the software/computing coordinator in the past. We did a better job with Geant4 in testing/integrating the latest software, than with generators. We set up a branch using the latest Geant4, so that we could switch in production at the next window of opportunity. We probably need a bit more coordination, and the Geant4 model is good. Olivier: fully agree on this, we need a better coordination, and the Geant4 model may be interesting. Josh: now we (ATLAS) are actually already in that mode, where we test the latest version quite fast.
- Slide 7. Typically the experiments validate and start to use a rather old version, never the last one, and they do not discuss with the authors. Then they re-discover some bugs that are already fixed in newer versions. This is very inefficient because it leads to double work for support.
- Slide 8. To address this, now changed the model to have a "long term stable" version with only bug fixes. Hope that the experiments can pick that.
    - Andrea: what are the concrete versions now? Olivier: 2.9.x (2.9.3, soon 2.9.4) is current latest stable, latest feature is 3.1.0 (soon 3.1.1). Efe: CMS is in 2.6 something now (Alexander: 2.6.5). [corrected later in the discussion, CMS is at 2.7.x]
    - Efe: depends also on how long is a long term stable. Olivier: currently 2 years (but it is a new concept to be discussed, maybe 3 or 4?). Efe: definitely not less than 1.5 years. Liz: this proposal is definitely good! LIz: would also need some tests.
    - Alexander: [about what type of test is done] we start with a gridpack. When we switch to a new MG version, we create new gridpacks and there we make new tests. We need physics stability and an efficient framework (low fail rate),  so we do careful tests (validating the physics output!) before putting in production the latest version. Liz: really like the long term stable idea because this is a guarantee from the developers that the physics will not change. Alexander: also like this idea for the same idea.
    - Andrea: when you say "bug fix" do you mean that it is a bug that does not affect physics? Because otherwise people must be aware that you may get a different physics. Olivier: it depends, some times there are things that change the physics distributions but if they are completely wrong, then you want to fix them. For instance if the running of alphas is de-activated. Liz: agree, eg in the past we had energy non-conservation and that's clearly a bug. 
    - Phil: take into account also that you may need to retune after fixing these bugs. Liz: for Geant4, typically we tell the detector experts that Geant4 authors suggested a change that will affect physics distributions, but will make them better. Phil: alphas example for us would require tuning of everything again, and we would need a completely new release of the software stack.
    - Josh: our latest validated in ATLAS is 2.9.3, should be there as of Monday. We also fully automated nightly tests within the CI, where we check logs and LHE files, but then we also have some physics validation. So in principle the LTS idea is not really necessary for ATLAS.
    - Alexander to Josh, how is the workflow set up? Josh: many things in parallel, test many different MG modes. The test is always with respect to the previous version. Liz: CMS treats these as externals and does not rebuild them.
    - Phil: in LHCb we only recently started using MG. We are at 2.7.x, using the cvmfs builds from LCG. We also have some tricks to reduce the gridpack size by orders of magnitude, if people are interested. Alexander/Josh: yes definitely, please email us both in CMS/ATLAS!
- Funding goes through different chemes, we had MCnet but this is going to  expired in few months. Foresee physics improvements especially for EW. From HSF there is already a lot of good help in the GPU project, but would like help about coordination with experiments.
- Slide 10. Bottleneck is the ME calculation both at LO and NLO. We have many tricks for the NLO loops, so actually at NLO the real emission is the bottleneck, not the loop. After the improvements from helicity recycling, full color is now a bottleneck.
    - Andrea: is the helicity recycling speedup interesting for the experiments to jump on a new MG version? Simone: this is only at LO, while NLO is our botttleneck. If this was an NLO speedup, we would jump on it, ask Olivier for help, and give many citations. Josh: on the other hand, if we have just produced large NLO samples, we would not redo a big production immediately. Alexander: some of the speeups on slide 11 actually look quite interesting for us.
- Slide 11. In addition to helicity recycling, there were also huge improvements in the phase space integration. The speedups by 100x or more are mainly from phase space integration, not the ME helicity recycling. Some of these will also be possible at NLO.
    - Andrea: if these improvements are in the phase space sampling, can the experiments keep the unweighting efficiency? Just know for how many phase space points you had to compute the ME, and how many final events you get. Olivier: it's not really available actually but maybe in the crossx.html file and/or quite hidden in some log. Andrea: if it is not, it would be extremely interesting to have it in the logs.
- Slide 12: with vectorization you might get up to a factor 4 (work with Andrea/Stefan/Stephan). Should start preparing for this now.
    - Andrea: actually -O3 and also fast math are orthogonals improvement to vectorization, gives you maybe 25% better. Olivier: -O3 now gives a larger improvement because the color matrix now takes more time and that part can be vectorised by the compiler.
    - Simone: started to discuss this internally in ATLAS and we would be very interested in this. In the case of gridpacks, we can recompile on a specific machine. Olivier: this should work (except that CMS remove the source code from the gridpack).
    - Alexander about recompiling gridpacks. In CMS we now remove the source but we could keep it. For HL-LHC how stable the infrastructure will be so that this is not a problem? Is it a problem if we use different releases for gridpacks and the rest of CMSSW? Liz: it is a risk. Olivier: may also create a fat binary. Andrea: for vectorization we will probably do some tests within the dev team, trying to get the same results at different vectorization levels.
- Slide 13. A lot of work also on MC@NLO-Delta, with much better negative weights.
- Slide 14. Also collaborating with VegasFlow to improve Vegas with new ML (Vegas already is "ML"!).
- Slide 15. We also have a GPU proof of concept, developed together with the vectorization.

Additional comments/discussion:
- Simone on VegasFlow. What is the perspective? They are moving to TensorFlow everything that can be moved to TensorFlow. Potential bottleneck? Olivier: cannot comment, do not know enough of this. Simone: LO only or also NLO? Olivier: they are only NLO.
    - Andrea: would it be a problem for the experiments if it is a completely new generator? Simone: if it is just the backend it is easier, but if it is a new generator I cannot say yet.
- StefanR: completely unrelated point, we saw that single precision would be a factor 2 more improvement, what do people think of that?
    - Rikkert: tried at some point single precision, and this just does not work for complex preocesses, even at LO. We also need quad precision for some of the loops, so this would need to be fixed for GPUs. Andrea: agree that it would be very interesting to follow this up, if possible. Josh: is this obviously no fixable, or is it worth investing more effort into it? Rikkert: the determinants may become zero in some cases, you could use a different base to do the calculation, but it is very complicated, not clear if it is worth it. We have some internal tests to detect issues (eg recompute the same quantity twice after some permutations). 

## AOB

- The next two meetings will probably on June 17 and 24, discussing Herwig and POWHEG, resepectively. But it is still possible that we organize one (or two) more meeting(s) on June 10 (and/or June 3).
