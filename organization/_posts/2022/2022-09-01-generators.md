---
title: "HSF Generator WG Meeting #24, 1 September 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1180220/>

Present: Aman Desai, Amartya Rej, Andrea Valassi, Gurpreet Chahal, Javier
Fernandez, Liz Sexton-Kennedy, Saptaparna Bhattacharya, Stefan Roiser, Stephen
Mrenna, Anja Butter, Markus Diefenthaler, Josh McFayden, Efe Yazgan, Taylor
Childers, Jie Xiao, Benjamin Rosser, Stephen Jiggins, Simone Amoroso, Michele
Faucci Giannelli, Kajari Mazumdar

Machine Learning and LHC Event Generation

- Intro by Markus D.
- Steve Mrenna:
  - slide 8: "for limited data there is no unique solution". Is not it a general
    problem?
  - A.B.: Yes.
  - S.M.: Is there anyway to estimate the volume of the possible solution space?
  - A.B.: Complicated but if you have a model beforehand you can make a fit but
    we do not have that. BNN is advantageous since you are training single
    network for ensemble of networks.
  - S.M.: Do you encode physics principles like gauge invariance?
  - A.B.: Yes, ...
- Andrea Valassi:
  - Slide 10, why do you say that there is no approximation?
  - A.B.: There is no additional uncertainty coming from the NNs. The point here
    is that the calculation of this loop amplitude is already an integration by
    numerical methods, which can be done only with a given precision. The use of
    ML here reduces the variance with respect to the variance without ML. In
    other words there is an error in both cases, but the error is smaller with
    ML.
- AV: Slide 18: One of the most crucial point of using ML: use cases where ML
  approximations just lead to poor computing efficiency (eg sampling) vs use
  cases where they lead to errors (eg replacing MEs/amplitudes by ones
  approximated through ML). Normalizing flows: IIUC sherpa team used that only
  for phase space sampling but you described cases where NF seems to be used
  also for replacing amplitudes?
  - AB: Sherpa uses as in slide 13 only for phase space calculations. But the
    techniques are the same and NFs can be used also in other ways, to replace
    amplitudes.
  - AV: To enhance adoption of these ML methods where they do not lead to
    errors, it would be useful to separate the things that could be used without
    errors and the others, this may push the experiments to adopt them. For
    instance using ML for improving unweighting efficiency should be non
    controversial: it would help to give numbers about how much the efficiency
    improves and how much computing power you save.
  - AB: Collaborating with sherpa, MG, other teams on many of these issues.
- Stephen Jiggins: From the Sherpa authors, is the work you referred to
  normalizing flows and there was the rejection sampling.
  - AB: Yes, there were 3 early papers by Sherpa from which were using the
    normalizing flows as samplers and as phase-space generator; and there was
    one for event generator, and more recently there was the one for regression
    which was this rejection network.
  - SJ: Yes, these are all good to increase the efficiency.
- SJ: May be due to lack of my understanding on my side, I have a question on
  slide 16: the issue here is the normalizing flow because of the gaussian that
  is assumed smears out into the whole in DeltaR
  - AB: Yes
  - SJ: When you do classification which minimizes the area of the density on
    the ratio on slide 17 there is a discontinuity between the spaces generated
    by the invertible NN and the training you want to reweight to. Does this
    trick suffer from conversion problem?
  - AB: The issue is that at that point there is no data there. So the true
    phase space density is zero. The INN generates something non-zero.
    Classifier needs to learn this ratio of something that is non-zero initially
    then it is going to learn the weight here will be very small. So, it will
    push D(x) --> 0.
  - SJ: If you flip this, then it will tend to a infinitely large number.
  - AB: Yes, if you take the data and reweight it to look like the INN generated
    data, then you will get very large numbers which will result in a highly
    unstable situation. So, it is important to choose your phase space not to
    have holes in the beginning. As long as you are covering your phase space
    with INN you are safe.
- Markus D.: In your summary slide you also said that there would be
  opportunities for ML for parton showers and for the
  hadronization/fragmentation. Can you summarize this?
  - AB: I am going to try to give a short summary. For the parton shower it is
    tricky. Here we only cover parton splitting functions. There is few
    variability and the issue is that you reuse the same function a lot of times
    to generate something. We know that this is a good description. There are
    two strategies: one is to learn the splitting function (NNs or recurrent NNs
    but training is difficult) and there are other approaches trying to directly
    learn the full shower but this is inefficient because one has to learn a
    very large phase-spacewhen only there is a few variables; essentially
    splitting functions g->gg, g->qqbar, q->qg, and not more than that. There
    are different approaches but in general this is a difficult problem. For
    fragmentation/hadronization, people are looking into this in particular lund
    string vs clustering. There is some work on trying to use these approaches
    and to translate into ML.
- Efe Yazgan: On slide 24, you mentioned the matrix element method. So, are
  there studies for ML that can potentially replace that.
  - AB: Hopefully soon. What we are working on conceptually is that you have a
    detector level event and you are sampling it from a gaussian and you get the
    corresponding probability distribution there. This is something you can do
    to unfold detector level events to invert to parton level. For MEM, given an
    event at parton level you look at the probabilities at the ME level where
    you have full control but you need a transfer function that gets you from
    parton to detector level (in the forward direction). You can train a network
    to learn this but since you start from events at the detector level first
    you have to sample over every potential parton level event and then
    calculate the probability. This is numerically extremely difficult that is
    why people start with a delta function which is not so correct approximation
    even for leptons but for jets it is much worse. People also use gaussians
    which is a better approximation but with NNs one has much more flexibility
    and more power to capture more compelx features.
  - EY: So, at this point, using MEM in a straightforward way is still faster
    than using ML?
  - AB: Yes but many people have not worked on this so far. One has to give more
    time to include it and come out with standard packages.
- SJ: Just a follow up point on this. There is madminer and omnifold that kind
  of tries to do this.
  - AB: They are very different. Omnifold learns, with the classifier, the
    weights between parton level, and detector level using full distributions
    just like the reweighting. And it applies them to parton level events to get
    the distribution. So, there is no unfolding of individual events. It
    massages the MC such that it looks like the data and then finds out what
    would my generation look like. Madminer uses again classifiers to learn
    these ratios but it does it in a different way. It directly uses the MEs as
    well to learn the ratios.
- MD: Follow up. I do not understand what you mean by direct event to event
  correlation. Unfolding only works for samples not on individual events with
  particles. How you do that on an event-by-event basis?
  - AB: slide 25; you have the events at the detector level and at the particle
    level. If I go through the usual chain of simulation from particle level to
    reco level standard MC run may times, for individual events on the RHS, I
    will get a distribution on the LHS. So, I can have P(SIM\|GEN) or
    P(detector\|particle) distribution. Using Bayes, theorem, I can express
    P(particle\|detector) via
    P(detector\|particle)xprior(particle)xprior(detector). Then, assume
    prior(particle), I have the other. The limitation is numerical for learning
    these high dimensional distributions - this is where we use the generative
    model. Second limitation is bias from the prior(particle) and one can use
    iterative approaches (which is work in progress).
  - MD: So, you also still work on the sample. You replace the histogram by a
    probability distribution or inverted weights for each of the event you can
    classify for the origin of the particle.
  - AB: Right. In a way it is like classical unfolding goes to the matrix and
    you can interpret this matrix like if you have an event in one bin the
    matrix will tell the expected distributions of the bins (push this to the
    limit where bin-widths goes to zero). Also please take a look at the
    community report paper arguing also for event level unfolding instead of bin
    level.
  - MD: I am full advocate of event based analysis. We have started the complete
    opposite - unfold theory with experimental events and then do the inverse.
- AV: Slide 24: a comment from some work I did a couple of years ago
  (https://doi.org/10.1051/epjconf/202024506038). For parameter inference, an
  alternative to methods where you take the "inverse" path, like MEM and
  unfolding, may be to take immediately the event-by-event derivative of the ME
  with respect to the parameter that you want to infer, and then carry this
  forward through hadronization and detector simulation. Then you only need to
  go in the forward direction. This may have some similarity with MadMiner or
  Sallyno, but I am not sure.
  - AB: this is interesting, it reminds me a lot of what Lukas Heinrich et al
    are working on on MadJax. Note that there will be a workshop on
    differentiable programming next year in Munich where we will discuss also
    these approaches.
- MD: This is not the last time that we discuss AI and machine learning. We will
  use your talk as overview and go more into details. We will invite you for
  follow up discussions. It was great to have you here. Thanks.
- AB: Very nice discussion. Thanks.
