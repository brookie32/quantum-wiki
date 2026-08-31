---
title: "Vectorized Symmetric and Fermionic Tensor Network Implementations for GPU-Accelerated Variational Monte Carlo"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27861"
summary: "arXiv:2608.27861v1 Announce Type: cross Abstract: Variational Monte Carlo (VMC) calculations based on tensor networks (TN) have recently achieved competitive accuracy in ground-state calculations of s"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27861v1 Announce Type: cross Abstract: Variational Monte Carlo (VMC) calculations based on tensor networks (TN) have recently achieved competitive accuracy in ground-state calculations of strongly correlated spin and fermionic systems. However, existing tensor network VMC (TN-VMC) algorithms have not been formulated in a manner that can fully utilize GPU acceleration. We tackle the key missing ingredient, namely, the vectorized evaluation of tensor network amplitudes and tensor network operations. This ensures high GPU utilization by batching over computations with identical structure. In particular, we show how to achieve vectorization for the practically relevant case of abelian symmetric tensor networks (which includes fermionic tensor networks) by developing a ``flat'' tensor network formalism for block-sparse tensor representation and contraction. Using this, we construct a GPU-adapted symmetric TN-VMC workflow with batched tensor network computation. In the two-dimensional Fermi--Hubbard model, we demonstrate a GPU speedup of up to 300 imes over single core CPU implementations, for fermionic TN variational wavefunctions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27861) | 2026-08-31
