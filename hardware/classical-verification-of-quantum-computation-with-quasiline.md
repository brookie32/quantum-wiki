---
title: "Classical Verification of Quantum Computation with Quasilinear Resources, from Compiled Nonlocal Games"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38060"
summary: "arXiv:2609.38060v1 Announce Type: new Abstract: Computational self-testing gives a classical verifier command over the quantum register of a single computationally bounded prover. We use this framewor"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.38060v1 Announce Type: new Abstract: Computational self-testing gives a classical verifier command over the quantum register of a single computationally bounded prover. We use this framework to construct the first argument system for BQP with quasilinear total resource requirements in the circuit model. Our argument system is based on the learning with errors (LWE) assumption and requires total resources of O(poly(lambda, log g)dot g) for delegating a circuit with g gates, where lambda is the LWE security parameter. This is achieved by constructing a new computational self-test for certifying the prover's quantum state and using it to dequantize the efficient verification protocol of Broadbent (ToC 2018). Specifically, this self-test enables the verifiable, random remote state preparation of tensor product states of the single-qubit Clifford observables sigma_X, sigma_Y, sigma_Z, (sigma_Y-sigma_X)/sqrt{2} and (sigma_Y+sigma_X)/sqrt{2}, with constant robustness: the verification error is independent of the number of prepared qubits. This approach was first proposed by Coladangelo et al. (ToC 2024) in the multi-prover setting. We replicate their result in the single-prover setting by applying the compiler proposed by Kalai et al. (STOC 2023)---which turns any nonlocal game into a single-prover argument system---to a modified version of their self-test.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38060) | 2026-09-30
