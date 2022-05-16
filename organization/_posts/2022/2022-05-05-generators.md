---
title: "HSF Generator WG Meeting #20, 5 May 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1145152/>

Participants: Steve Gardiner, Andrea Valassi, Celeste, Henry Israel, Jordan M. Mcelwee, Liz Sexton-Kennedy, Qiang Li, Saptaparna Bhattacharya, Josh McFayden, Markus Diefenthaler, Efe Yazgan

Theoretical tools for neutrino scattering: interplay between lattice QCD, EFTs, nuclear physics, phenomenology, and neutrino event generators
Speaker: Steven Gardiner 
* Talk is partially based on arXiv:2203.09030
* Neutrino generators
    * Experiment-focused generators: Genie, Neut
    * Theory-focused generators:GIBUU, NuWro
    * Marley for DUNE for supernova neutrino studies. 
    * ACHILLES
    * LeptonInjector used by ICECUBE. 
* CEvNS, Lattice QCD, Many-body ab initio quantum MC
* Sociological issues mentioned - challenges in common with LHC efforts. 
* Some problems already have known solutions in LHC (n-body phase space generation, HepMC3, Professor, ...)
* Many connections to nuclear physics theory and modeling (upcoming meeting on June 23), also to nuclear physics measurement. 



Discussion:
* Josh
    * Difficult to change model (or parameters). What makes it difficult? 
        * SG: Computationally expensive to re-simulate; if the model isn't in Genie it's often hard to compare since generators are more experiment-specific (because of event formats etc); depends on how the analysis are done - not only relying on simulation but depends on the measurement from the near detector - experiments have different recipes for that - no tools to transfer models between experiments. 
    * Are there any obvious problems using HEPMC3/RIVET in the neutrino generators? 
        * SG: Just started looking at it. Looks promising. Good direction to go. 
    * "No clear community leadership structure" what does it mean?
        * SG: Community meetings, useful plans but no community structure to coordinate the wortk although there are some developments. No collective organization that speaks for generator community.  
        * Josh: No clear organization at the LHC either except may be LHC WGs. 
* Efe: Is it possible to include predictions from new physics (like neutrino magnetic moment) in CEvNS?
    * SG: There is an internal code. It would be good to be able to test different models...
* Josh: Technically how do things like the neutrino cross section calculations interface with the rest of the simulation infrastructure?
    * SG: Upstream beam simulation to predict incident neutrino spectrum and geometry etc. Interface of beam and Genie. Genie interprets the input from the beam simulation and uses cross section information to calculate the scattering location, process and outgoing particle energies. Then final states goes to Geant4 then to custom detector simulation. There is a common framework for Ar-based detectors at Fermilab. In these respects it is simular to LHC simulations. 


