---
title: "Exact Maximum Likelihood Decoding beyond Treewidth via Rank-Decomposition Dynamic Programming"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39556"
summary: "arXiv:2609.39556v1 Announce Type: new Abstract: Maximum-likelihood decoding provides an optimal decoding strategy for quantum error correction under stochastic Pauli noise. However, computing logical-"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39556v1 Announce Type: new Abstract: Maximum-likelihood decoding provides an optimal decoding strategy for quantum error correction under stochastic Pauli noise. However, computing logical-class probabilities is challenging, and the leading exact tensor-network contraction requires time exponential in treewidth. In this work, we introduce a new decoding algorithm based on rank-decomposition dynamic programming (Rank DP). We express decoding partition functions with independent local fault factors as quadratic sums of powers and apply Rank DP. The resulting exact evaluator has arithmetic complexity polynomial in the input size and exponential in the Tanner graph's rank-width with respect to the fault partition, including decomposition construction. After Gaussian elimination, it gives polynomial-time decoding for punctured quantum Reed-Muller codes and a Steane-concatenated family with growing distance under independent single-qubit Pauli noise. Standard contraction of the corresponding tensor networks requires superpolynomial time. A nonnegative realization gives relative floating-point error bounds under explicit arithmetic assumptions. Numerical experiments demonstrate runtime advantages over the tested tensor-network implementations on selected code-capacity and circuit-level instances, with full likelihood evaluation for Reed-Muller codes up to 1{,}023 qubits. We further use these likelihoods to learn circuit noise parameters from syndromes, evaluate rare postselection probabilities, and quantify decoder optimality gaps. Our work opens new avenues for exploiting algebraic structure in quantum decoding and noise characterization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39556) | 2026-10-01
