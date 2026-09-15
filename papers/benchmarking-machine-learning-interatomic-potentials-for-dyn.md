---
title: "Benchmarking Machine-Learning Interatomic Potentials for Dynamical Stability in Inorganic Semiconductor Nanocrystals: A CdSe Case Study"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.15299"
summary: "arXiv:2609.15299v1 Announce Type: cross Abstract: Machine-learning interatomic potentials (MLIPs) enable nanosecond-scale atomistic simulations of inorganic semiconductor nanocrystals, but low errors "
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.15299v1 Announce Type: cross Abstract: Machine-learning interatomic potentials (MLIPs) enable nanosecond-scale atomistic simulations of inorganic semiconductor nanocrystals, but low errors on held-out configurations do not necessarily guarantee stable molecular dynamics. We benchmark five graph-neural-network MLIPs, SchNet, PaiNN, NequIP, Allegro and MACE, for dynamical stability in a chloride-passivated cadmium selenide nanocluster containing 149 atoms. The models were trained under harmonized conditions on 1,000 configurations and evaluated against 2,000 held-out configurations generated using density functional theory, considering force accuracy, computational efficiency, uncertainty and structural stability during 1 ns simulations at 300 K. Allegro produced the lowest validation force mean absolute errors, ranging from 12 to 14 meV per angstrom, whereas SchNet produced the largest, ranging from 84 to 110 meV per angstrom. This ranking did not predict dynamical robustness: NequIP remained stable for 1 ns without additional training data, whereas MACE became stable only after an ensemble-based active-learning procedure added 34 uncertainty-selected configurations. PaiNN and Allegro remained unstable after the addition of 100 and 95 configurations, respectively, and SchNet also failed to achieve stable dynamics within the tested augmentation budget. Under the benchmark hardware conditions, the machine-learning potentials required 6-66 ms per molecular-dynamics step, compared with approximately 20 s for density functional theory. These results show that held-out prediction errors alone are insufficient for selecting interatomic potentials for finite, surface-dominated nanostructures. Reliable deployment requires long-timescale dynamical testing combined with uncertainty-guided refinement, while the effectiveness and data efficiency of active learning remain strongly architecture dependent.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.15299) | 2026-09-15
