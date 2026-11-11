---
title: "ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.14287"
summary: "arXiv:2611.14287v1 Announce Type: new Abstract: Structure-based virtual screening needs a receptor conformation that fits the ligand class, but for most targets no ligand-bound crystal is available --"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14287v1 Announce Type: new Abstract: Structure-based virtual screening needs a receptor conformation that fits the ligand class, but for most targets no ligand-bound crystal is available -- and a single predicted model or an apo structure often misses the binding-competent state. We present ANTIOCH-VS, an open-source framework that runs an entire in silico screening campaign, from a protein sequence to a ranked shortlist of candidate binders, as one plug-and-play workflow. It first builds a conformational ensemble by reduced-MSA subsampling with ColabFold, then uses AlphaFold2-RAVE (AF2RAVE) -- short molecular-dynamics simulations with State Predictive Information Bottleneck analysis -- to pick out docking-ready, Boltzmann-weighted metastable states. It then detects the binding pocket, prepares receptors and ligands, docks the library across the ensemble with DOCK6 or AutoDock Vina, builds a consensus ranking, and triages the top hits by physics-based metadynamics (CTMD). We benchmark it on two very different targets, JAK2 kinase and ADRB2 GPCR, using their DUD-E benchmark sets of known binders and property-matched decoys. Starting from sequence alone -- no ligand-bound crystal, no manual intervention -- the AF2RAVE ensembles gave top-20 shortlists strongly enriched for true binders: a 20% hit rate for JAK2 and 60% for ADRB2 (random ~1-2%), on par with ligand-bound crystals and, for the kinase, above single AF2 models and an apo crystal. The full pipeline runs end to end on a workstation or HPC from a single command, or each module can be run on its own with user-supplied inputs. ANTIOCH-VS is freely available at https://github.com/tiwarylab/antioch-vs

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.14287) | 2026-11-11
