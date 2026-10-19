---
title: "Quantum-Assisted Unambiguous Discrimination of Pure States with Robustness Bounds"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.22954"
summary: "arXiv:2610.22954v1 Announce Type: new Abstract: We propose a hybrid quantum-classical framework for the unambiguous discrimination of pure states by combining the noisy intermediate-scale quantum semi"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.22954v1 Announce Type: new Abstract: We propose a hybrid quantum-classical framework for the unambiguous discrimination of pure states by combining the noisy intermediate-scale quantum semidefinite program solver (NSS) with the reciprocal-state representation. In NSS, a given semidefinite program (SDP) is represented within a subspace spanned by chosen ansatz states, with the required quantities estimated using quantum circuits, and the resulting optimization is performed classically. This makes NSS naturally applicable to discrimination problems involving circuit-prepared states, as finding a discrimination measurement can be formulated as an SDP. By choosing the discriminated states themselves as the ansatz and exploiting the reciprocal-state representation, the general matrix-variable NSS formulation is reduced to an optimization over N scalar variables, where N is the number of discriminated states. The resulting formulation reduces the number of optimization variables and positive-semidefinite constraints compared with the original NSS formulation. We further establish robustness guarantees against Gram matrix estimation errors, including a rescaling procedure that guarantees a valid positive operator-valued measure (POVM) under bounded perturbations. The resulting bounds quantify both the deviation in average success probability and violations of the no-error condition using only the estimated Gram matrix, its SDP solution, and a characterized perturbation bound, without access to the ideal Gram matrix. Numerical simulations validate the derived robustness bounds and characterize finite-shot scaling. We also perform experiments on IBM quantum hardware to estimate pairwise overlaps, and then evaluate the performance of the resulting POVMs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.22954) | 2026-10-19
