---
title: "Logarithmic depth compression of Heisenberg Hamiltonian simulation by fan-out parallelization, with built-in error detection"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20250"
summary: "arXiv:2608.20250v1 Announce Type: new Abstract: Noisy intermediate-scale quantum computers are constrained by circuit depth, while product-formula simulation of spin systems leads to narrow and deep c"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.20250v1 Announce Type: new Abstract: Noisy intermediate-scale quantum computers are constrained by circuit depth, while product-formula simulation of spin systems leads to narrow and deep circuits. Here we introduce a fan-out-based gadget compiler that trades circuit depth for width in simulations of Heisenberg-type nuclear magnetic resonance (NMR) Hamiltonians. Each logical spin is encoded into a small repetition-code register sized by its interaction degree, so that all pairwise interactions of a given Pauli type execute in parallel after a logarithmic-depth CNOT fan-out, and the redundant registers provide error detection for post-selection at no additional algorithmic overhead. The central result is a fixed-protocol resource comparison of the two compilations, transpiled to heavy-hex superconducting and all-to-all trapped-ion targets across a set of NMR spin systems. For interaction graphs with a high-degree hub the volume-optimal schedule halves the two-qubit depth and reduces the volume 1.7-fold for the 13-spin demonstration, which on heavy-hex also lowers the two-qubit gate count, and the depth reduction rises to 2.5-fold on all-to-all for the highest-degree molecule studied. On all-to-all the two-qubit gate count rises for every system, so the volume reduction is a benefit on depth-limited hardware. The gain grows with the degree inhomogeneity of the interaction graph and vanishes for dense uniform graphs, where the optimum is the sequential circuit. We simulate the zero-field NMR spectrum of tetramethylsilane, a 13-spin star system. Under a noise model scaled from a published present-day processor calibration, the shallower gadget circuits match or surpass the sequential compilation only after post-selection on their built-in error detection, once error rates improve by one to one and a half orders of magnitude. We verify the spectra against an independent classical computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20250) | 2026-08-21
