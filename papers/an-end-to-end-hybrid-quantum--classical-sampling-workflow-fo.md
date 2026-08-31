---
title: "An End-to-End Hybrid Quantum--Classical Sampling Workflow for Discrete Markov Random Fields: A Reproducible Case Study"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09893"
summary: "arXiv:2607.09893v2 Announce Type: replace Abstract: Sampling from discrete Markov random fields (MRFs) is a hard problem. We study amplitude-encoded i.i.d. sampling for small MRFs where 2^n target pro"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2607.09893v2 Announce Type: replace Abstract: Sampling from discrete Markov random fields (MRFs) is a hard problem. We study amplitude-encoded i.i.d. sampling for small MRFs where 2^n target probabilities are precomputed classically. This removes quantum exponential speedup but allows a clean comparison against classical MCMC based on independent circuit samples (au approx 1). Across 60 instances spanning five graph families (1k-step burn-in, 3k retained samples), the mean ESS ratios of Quantum to Single-Site Gibbs, Block Gibbs, Tuned-Block, and Parallel Tempering are 16.35, 7.29, 1.82, and 1.79, showing modern classical samplers substantially close this gap. Amortizing O(2^n) preprocessing into wall-clock time, exact inverse-CDF sampling yields 17.7ext{M} ESS/s versus 488ext{K} ESS/s for the quantum sampler (36imes mean rate, 153imes per-instance), confirming no wall-clock advantage. We characterize MCMC autocorrelation costs and benchmark amplitude-encoded state preparation at n in {8,10,12}. An MPS scaling study (n le 40) shows bond dimension hi=32 achieves F=0.721pm0.059 at n=40. Finally, a matched-budget VQC vs. MPS comparison at n in {8,10,12} shows VQC fidelities fall far below MPS: (F_{VQC}, F_{MPS}) = (0.31, 0.99), (0.21, 0.96), (0.17, 0.88) at compressions 10.7imes, 34.1imes, and 113.8imes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09893) | 2026-08-31
