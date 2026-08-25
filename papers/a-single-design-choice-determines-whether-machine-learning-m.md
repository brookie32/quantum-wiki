---
title: "A single design choice determines whether machine learning models of materials make physically impossible predictions"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18714"
summary: "arXiv:2608.18714v1 Announce Type: cross Abstract: Machine-learned models are replacing first-principles calculations across materials discovery, and physical symmetry is the central guarantee built in"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18714v1 Announce Type: cross Abstract: Machine-learned models are replacing first-principles calculations across materials discovery, and physical symmetry is the central guarantee built into them. The debate over how much symmetry to hard-wire rather than learn has run on rotations, where a symmetry error is an approximation error. Some constraints are exact: symmetry forces certain property tensors to exactly zero, so a nonzero prediction is physically impossible rather than inaccurate. Here we show that whether a model can make such predictions is decided before training by one rarely reported design bit, whether its features carry parity labels, and derive a criterion, the parity gap, that computes from group theory alone which properties and crystals are exposed. Across matched architecture pairs differing only in that bit, evaluated on two thousand centrosymmetric crystals whose piezoelectric tensor must vanish, parity-labelled arms sit at the floating-point floor while rotation-only arms predict forbidden responses on 90-96% of crystals, six orders of magnitude apart, at no accuracy cost. Training on explicit zeros does not recover exactness, and a head on a frozen universal potential inherits its backbone's symmetry group. One reflection at random initialization verifies the label in seconds.



## Related
- [[variational-quantum-circuit-parameterization-of-schnet-a-sim|Variational Quantum Circuit Parameterization of SchNet: A Simulator-Based Feasibility Study for Conservative Molecular Force Fields]]
- [[when-do-machine-learned-exchange-correlation-improvements-in|When do machine-learned exchange-correlation improvements inherit into density-functional tight binding?]]
- [[foundation-neural-effective-hamiltonian-for-strongly-correla|Foundation Neural Effective Hamiltonian for Strongly Correlated Quantum Materials]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18714) | 2026-08-20
