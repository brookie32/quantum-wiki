---
title: "A Block Tensor Train Burer-Monteiro Framework for Low-Rank Quantum State Tomography"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.09457"
summary: "arXiv:2609.09457v1 Announce Type: new Abstract: Quantum state tomography is a fundamental technique for estimating the state of a quantum system from measured data and plays a crucial role in evaluati"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09457v1 Announce Type: new Abstract: Quantum state tomography is a fundamental technique for estimating the state of a quantum system from measured data and plays a crucial role in evaluating the performance of quantum devices. However, standard estimation methods become computationally prohibitive as the system size increases due to the exponential growth of the density matrix, describing a quantum state, with the number of qubits. We propose a low-rank tensor-network framework for mixed-state quantum state tomography based on a block tensor train (Block-TT) factorization. Specifically, the density matrix is represented as the contraction of a Block-TT with its Hermitian transpose, yielding a TT analogue of the Burer-Monteiro factorization. This parameterization guarantees Hermiticity and positive semidefiniteness by construction while compressing the number of optimization variables from exponential to linear in the number of qubits. Building on this representation, we develop single-site and two-site density matrix renormalization group (DMRG) algorithms for estimating quantum states from compressed measurements. The resulting methods operate directly on the compressed parameterization, support adaptive rank refinement, and exploit efficient tensor-network contractions for expectation-value evaluation. The framework is applicable to a broad class of low-rank quantum states, including pure states, nearly pure states, and ground states that admit accurate tensor-network approximations. Numerical experiments demonstrate accurate state reconstruction from limited measurements together with substantial reductions in memory requirements and computational cost compared with conventional low-rank tomography methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.09457) | 2026-09-10
