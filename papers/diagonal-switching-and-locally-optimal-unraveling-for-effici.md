---
title: "Diagonal, Switching, and Locally Optimal Unraveling for efficient quantum trajectories in metastable open quantum systems"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.36067"
summary: "arXiv:2610.36067v1 Announce Type: new Abstract: Open quantum systems can display metastability, with multiple long-lived states coexisting. Examples include the bistability of bright and dim manifolds"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36067v1 Announce Type: new Abstract: Open quantum systems can display metastability, with multiple long-lived states coexisting. Examples include the bistability of bright and dim manifolds in nonlinear driven resonators, or the long-lived coherent states of opposite phases in parametrically-driven systems, the building block of cat-state-based quantum computers. Metastability often emerges at system sizes where density-matrix evolution is impractical. Quantum trajectories mitigate this issue by evolving wavefunctions rather than density matrices. Metastable states then emerge as attractors towards which the system rapidly relaxes until a rare switching event brings it to another attractor. Simulating them remains costly, as one must resolve fast intra-attractor dynamics over timescales long enough to gather switching statistics. To tackle this problem, we introduce the Diagonal, Switching, and Locally Optimal Unraveling (DiSLOU) method, which combines three optimization layers: (i) Switching among locally optimal unravelings that minimize the number of quantum jumps in each metastable region. (ii) Diagonal propagation: the no-jump evolution is accelerated by diagonalizing the non-Hermitian effective Hamiltonian once per attractor. (iii) Local reduced eigenspaces: the no-jump state can be faithfully propagated in a truncated subspace of only slowly decaying eigenmodes. We benchmark DiSLOU on the driven-dissipative Kerr resonator, finding no measurable loss of accuracy and the largest speedup in the bistable regime, where standard trajectories are most expensive. We then apply the method to the more challenging problem of accurately simulating rare bit-flip events in the cat manifold emerging in a two-mode dissipatively stabilized parametric oscillator, obtaining a performance improvement of over one order of magnitude. An implementation of DiSLOU in Julia is available as an open-source package.



## Related
- [[quantum-instanton-approach-to-metastable-collective-spin-sys|Quantum instanton approach to metastable collective spin systems: Numerical implementation and applications]]
- [[from-normal-lindbladians-to-non-normal-quantum-trajectories|From normal Lindbladians to non-normal quantum trajectories]]
- [[collective-dissipation-induced-dark-and-metastable-like-stat|Collective-dissipation-induced dark and metastable-like states for enhanced quantum battery performance]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.36067) | 2026-10-28
