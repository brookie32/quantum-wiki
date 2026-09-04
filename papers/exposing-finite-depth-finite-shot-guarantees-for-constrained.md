---
title: "Exposing Finite-Depth, Finite-Shot Guarantees for Constrained Quantum Optimization via Fejer Filtering"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.01809"
summary: "arXiv:2603.01809v3 Announce Type: replace Abstract: Constrained quantum optimization algorithms need quantitative guarantees that connect circuit resources to the probability of actually sampling feas"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2603.01809v3 Announce Type: replace Abstract: Constrained quantum optimization algorithms need quantitative guarantees that connect circuit resources to the probability of actually sampling feasible or optimal solutions in finitely many shots. We establish such a connection by exposing a positive sampling law in which mixer-driven exploration and spectral selection can be controlled separately. We show that after removing interference between distinct cost eigenspaces as an analytic device, the measurement distribution becomes the normalized product of a mixer-induced exploration envelope and a Fejer spectral weight, with the former describing how the mixer spreads probability over the encoded manifold and the latter enhancing the target cost phase while suppressing spectrally separated nontarget phases. In this model, finite-shot success becomes a tractable competition between target weight and off-target leakage, yielding an explicit lower bound on the probability of sampling an optimum. For the primary bound, we rescale the cost Hamiltonian to an integer-valued spectrum, placing the wrapped cost phases on a controlled lattice for Fejer filtering. We then define elta as the minimum circular separation between the optimal phase and every nontarget phase. The single-shot success probability q_0 satisfies [ q_0 ge frac{x}{1+x}, qquad x = (p+1)^2 sin^2!left(frac{elta}{2}right) C_{eta}, ] where p is the filter order and C_{eta} is the mixer-envelope mass on the optimal set, exposing a finite-resource compensation law in which weaker phase separation or smaller envelope mass can be compensated by increased filter order and additional shots. The same filtering principle exposes a feasibility guarantee when applied to penalty phases. We further prove analogous bounds for nonlattice spectra through off-target suppression, extending our results beyond exact lattice normalization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.01809) | 2026-09-04
