---
title: "AcepK_{rm a}: Thermodynamics-Informed pK_{rm a} Prediction and Protonation-State Generation in PlayMolecule AI"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.00841"
summary: "arXiv:2604.00841v2 Announce Type: replace Abstract: The acid dissociation constants (pK_{rm a}) and the protonation states that they determine govern solubility, permeability, and protein--ligand bind"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2604.00841v2 Announce Type: replace Abstract: The acid dissociation constants (pK_{rm a}) and the protonation states that they determine govern solubility, permeability, and protein--ligand binding, making their accurate prediction essential in drug discovery. We present AcepK_{rm a}, an application in the PlayMolecule AI platform that implements the Uni-pK_{rm a} framework, which couples statistical mechanics with representation learning. Rather than treating pK_{rm a} as a scalar regression target, AcepK_{rm a} models the complete protonation ensemble, enforcing thermodynamic consistency across coupled ionization sites. The application is built on an independently retrained Uni-Mol backbone that matches state-of-the-art accuracy on standard public benchmarks. We further describe three engineering contributions: AceConfgen, a GPU-accelerated conformer generator approximately 7 times faster than other GPU implementations and more than an order of magnitude faster than multithreaded RDKit; a streamlined inference engine that protonates molecules directly; and a 3D-aware mode that applies predicted protonation states to bound ligand poses. AcepK_{rm a} supports library-scale prediction and provides a validated, ready-to-use implementation of this methodology, available at open.playmolecule.org.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.00841) | 2026-09-01
