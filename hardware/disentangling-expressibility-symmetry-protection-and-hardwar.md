---
title: "Disentangling Expressibility, Symmetry Protection, and Hardware Noise in Variational Quantum Simulation of the Two-Flavor Schwinger Model"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30496"
summary: "arXiv:2609.30496v1 Announce Type: new Abstract: Existing quantum simulations of the two-flavor Schwinger model have run at a single lattice size, and it is not known how far the variational approach c"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.30496v1 Announce Type: new Abstract: Existing quantum simulations of the two-flavor Schwinger model have run at a single lattice size, and it is not known how far the variational approach can be pushed or which weakness stops it first. Following the model from N = 2 to 6 staggered lattice sites, we find that the binding constraint at reachable sizes is hardware noise rather than circuit expressibility or trainability, and identify N = 3 as the immediately viable extension of existing trapped-ion experiments. The energy error of a charge-conserving ansatz collapses onto one function of p/d, the ratio of variational parameters to physical-sector dimension, and falls by more than two orders of magnitude as p/d rises through order unity, giving the expressibility condition L(4N - 1) >= binom(2N,N) for L circuit layers. The condition is local in chemical potential: at N = 3 the layer count sufficient at zero chemical potential leaves a 74.38% error near the first-order boundary, while one further layer reaches 0.08%. Charge conservation also protects trainability and prevents charge-sector leakage: as the qubit count doubles from 4 to 8, the normalized gradient variance falls to 1/3.56 of its starting value for the constrained ansatz, versus 1/13.57 for an unconstrained circuit. Comparing a global contraction with per-gate local noise, a fixed-parameter control shows that the noise model, not whether the optimizer runs inside the noisy loop, sets how strongly noise degrades the first-order transition. At N = 4, a noiseless control reaches 0.12% mean error, whereas the same circuit at 1.00% depolarizing noise reaches 25.69 to 52.81%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30496) | 2026-09-28
