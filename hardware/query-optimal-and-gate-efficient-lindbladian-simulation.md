---
title: "Query-Optimal and Gate-Efficient Lindbladian Simulation"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.18757"
summary: "arXiv:2609.18757v1 Announce Type: new Abstract: We give a quantum algorithm for Lindbladian simulation given a block encoding of the Hamiltonian H and a projected unitary encoding of the stacked jump "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18757v1 Announce Type: new Abstract: We give a quantum algorithm for Lindbladian simulation given a block encoding of the Hamiltonian H and a projected unitary encoding of the stacked jump operator B=sum_{k=1}^m lvert krangleotimes L_k, with normalization factors alpha_H and alpha_B, respectively. For evolution time t, set au=(alpha_H+alpha_B^2)t. The algorithm approximates the evolution channel to diamond-norm error arepsilon using O!left(au+frac{log(1/arepsilon)}{log!left(e+log(1/arepsilon)/auright)}right) oracle queries, matching the query lower bound for Hamiltonian simulation. The number of additional one- and two-qubit gates is linear in the query complexity up to polylogarithmic factors. The query- and gate-complexity bounds extend to Lipschitz-continuous time-dependent Lindbladians under coherent time-indexed oracle access. Our construction uses a one-query transducer that implements a product of rational approximations to short-time evolution when supplied with a catalyst. We bound the error from omitting the catalyst by exploiting orthogonality between different sequences of Kraus labels. The gate implementation combines a compressed Kraus-label representation, which stores only the positions and values of the nonzero labels, with the rotation factorization of Chen et al.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.18757) | 2026-09-17
