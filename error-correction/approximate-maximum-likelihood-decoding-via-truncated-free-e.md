---
title: "Approximate maximum-likelihood decoding via truncated free energies"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03928"
summary: "arXiv:2609.03928v1 Announce Type: new Abstract: Maximum-likelihood decoding (MLD) achieves the minimum logical error rate of stabilizer codes under known i.i.d. Pauli noise, but its exact evaluation i"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03928v1 Announce Type: new Abstract: Maximum-likelihood decoding (MLD) achieves the minimum logical error rate of stabilizer codes under known i.i.d. Pauli noise, but its exact evaluation is #P-hard. Practical pipelines therefore approximate MLD by minimum-weight decoding (MWD), retaining only the lowest-weight recovery per syndrome and discarding the coset degeneracy. The minimum-weight search is in turn implemented by stochastic solvers. We introduce approximate maximum-likelihood decoding (AMLD), a black-box framework that recycles the candidate samples discarded by stochastic inner decoders into a per-class truncated free-energy estimator. For every logical class represented in the candidate pool, the estimator is provably bounded below by the exact free energy and above by the empirical minimum weight. AMLD returns the logical class minimizing the estimated free energy with linear classical overhead. In SA-based Ising-decoder benchmarks, AMLD closes up to 83% of the MWD--MLD threshold gap across the toric and color codes under bit-flip and depolarizing noise. The largest threshold improvement, from 17.28% to 18.62%, occurs on the 6.6.6 color code under depolarizing noise. We further demonstrate AMLD on the [[144,12,12]] bivariate-bicycle code, whose bit-flip decoding problem has a hypergraph structure. This application requires neither matching-based enumeration nor code-specific tensor-network contraction. At p=0.05, AMLD reduces the logical error rate by 13% relative to MWD evaluated on the same BP-OSD candidate pool.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03928) | 2026-09-04
