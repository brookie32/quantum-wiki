---
title: "Robustness of quantum spectrum estimation: weak Schur sampling under noisy inputs"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03582"
summary: "arXiv:2610.03582v1 Announce Type: new Abstract: We initiate the study of weak Schur sampling (WSS) under noisy input. Many optimal quantum learning algorithms rely on this measurement, for instance in"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03582v1 Announce Type: new Abstract: We initiate the study of weak Schur sampling (WSS) under noisy input. Many optimal quantum learning algorithms rely on this measurement, for instance in such fundamental tasks as quantum spectrum estimation (QSE) and quantum state tomography (QST). The standard analysis of WSS, QSE and QST assumes that the n input copies of the target state rho are identical. We study what happens when they are not, a more realistic noisy scenario that breaks the very permutation symmetry on which WSS is built. In the simplest noise model, the copies are independent but not necessarily identical, i.e. they form a product state, and each is epsilon-close in trace distance to the d-dimensional target state rho. A naive data-processing argument lets the per-copy errors accumulate to nepsilon on measurement output, growing with the input size. We prove that they do not accumulate: the expected output error in total variation is at most epsilon+eta(n,d), where eta(n,d)=O(d/sqrt n) is the noiseless error, and the additive noise term epsilon is optimal. Beyond noisy product states, for arbitrary inputs omega we show that the outcome observables of WSS are 1/n-Lipschitz with respect to the quantum Wasserstein distance W_1 of De Palma et al., so the error is at most eta(n,d)+frac{1}{n}|omega-rho^{otimes n}|_{W_1}. In particular, our results imply, for the first time, noise-robustness of Keyl and Werner's seminal algorithm for QSE, more than two decades after its introduction. Within our model of robustness, the promise cannot be weakened to closeness of single-copy marginals or to a global trace-distance budget alone, since in both cases some noisy inputs defeat every measurement and estimator. Our results are a necessary step towards optimal quantum learning in practice, and help make progress towards robustness of many other problems in quantum information theory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03582) | 2026-10-05
