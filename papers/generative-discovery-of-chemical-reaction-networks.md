---
title: "Generative discovery of chemical reaction networks"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.38236"
summary: "arXiv:2610.38236v2 Announce Type: replace-cross Abstract: Understanding chemical reactivity requires uncovering which pathways are accessible from a given set of reactants, how they compete, and how s"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2610.38236v2 Announce Type: replace-cross Abstract: Understanding chemical reactivity requires uncovering which pathways are accessible from a given set of reactants, how they compete, and how successive reactions reshape the mixture. Automated saddle-point searches can explore from reactants alone, but their computational cost rises sharply as competing pathways accumulate across successive steps. Machine-learning approaches to transition state generation typically require predefined products, yet identifying those products is a central goal of exploration. Here we introduce ReactNexus, a generative framework that generates transition-state candidates directly from reactant graphs without specifying products, predicts the species they connect, and refines pathways with a reactive machine-learned potential to guide network exploration. Its models were trained on a quantum-chemical database of 130 million structures from 1.1 million reaction records, spanning 11 elements and multiple charge and spin states. On held-out reactions, 93.6% of generated candidates refined to valid transition states at the density functional theory level, and 83.3% connected the supplied reactants to distinct products. Across decomposition, complex rearrangements, and organocatalysis, ReactNexus reveals how competing mechanisms shape product formation, uncovering pathways missed in previous studies. In a multisite nucleophilic aromatic substitution, ReactNexus identified diarylation products that explained initially unassigned LC-MS signals, with structural assignments supported by NMR after isolation. ReactNexus also predicted an additional product family not detected under the initial conditions; subsequent higher-temperature experiments provided LC-MS evidence supporting its formation. This work highlights the potential of generative models to extend mechanistic analysis to increasingly complex reaction mixtures.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.38236) | 2026-11-19
