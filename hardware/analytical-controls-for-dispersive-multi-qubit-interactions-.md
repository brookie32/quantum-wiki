---
title: "Analytical controls for dispersive multi-qubit interactions in mediator-coupled quantum registers"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03064"
summary: "arXiv:2610.03064v1 Announce Type: new Abstract: Fast control of long-lived quantum registers often relies on an auxiliary degree of freedom, a mediator, but real mediator excitation can introduce deco"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03064v1 Announce Type: new Abstract: Fast control of long-lived quantum registers often relies on an auxiliary degree of freedom, a mediator, but real mediator excitation can introduce decoherence, leakage, or loss when the mediator is not the coherence-optimized component. We introduce dispersive interaction via analytical linear inversion (DIAL), an analytical control construction for excitation-suppressed interaction engineering in mediator-coupled quantum registers. In the dispersive regime, we show that off-resonant driving of an effective two-level mediator transition yields a diagonal Hamiltonian whose Pauli-(Z) interaction rates depend linearly on the drive intensities through a transfer matrix determined by the register-resolved transition spectrum. This establishes a direct linear map from experimentally accessible controls to induced multi-qubit interactions, enabling control design without iterative propagation of the full driven dynamics. We turn this structure into the target-aware DIAL algorithm, which selects favorable off-resonant tones and determines their drive intensities for a prescribed target interaction. We benchmark the resulting controls across 100 register realizations for each register size (n=2,3,4,5), targeting the highest-order interaction (Z_1dots Z_n) with an interaction phase of magnitude (pi/4), which generates an (n)-qubit GHZ state up to local equivalence. Propagation under the full driven mediator-register dynamics yields typical gate fidelities above (0.997), while the maximum transient mediator excitation remains near (1%) on average, far below what is typically possible with resonant Rabi drives. The manuscript is accompanied by an open-source Python package implementing the target-aware DIAL algorithm and the associated numerical validation workflow.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03064) | 2026-10-05
