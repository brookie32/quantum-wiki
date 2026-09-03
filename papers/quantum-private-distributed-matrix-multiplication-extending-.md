---
title: "Quantum Private Distributed Matrix Multiplication: Extending the Classical Codes and Limitations"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.23406"
summary: "arXiv:2511.23406v2 Announce Type: replace-cross Abstract: In this paper, we explore how quantum resources can be used to increase the rate of private distributed matrix multiplication (PDMM). In PDMM,"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2511.23406v2 Announce Type: replace-cross Abstract: In this paper, we explore how quantum resources can be used to increase the rate of private distributed matrix multiplication (PDMM). In PDMM, a user who has two high-dimensional matrices, A and B, and lacks the computational capabilities to apply matrix multiplication locally, divides the matrices A and B into K and L sub-blocks, respectively. Then, the user sends them to N servers to apply the required multiplication privately, i.e., any T colluding servers cannot get any information about the user's matrices. The goal is to reduce the number of servers needed to perform the required matrix multiplication, thereby decreasing the communication cost. First, in the high-privacy regime, the state-of-the-art classical code is called the gap additive secure polynomial (GASP) code. We define a feasibility requirement in the quantum setting for the GASP code such that the highest performance is achieved when the requirement is satisfied. Thus, super-dense coding gain is achieved when the feasibility condition is satisfied. We show that when T geq KL-K+1, the feasibility condition is always satisfied and the GASP code can be extended to the quantum version. In the case of T < KL-K+1, the feasibility can still be satisfied. To further examine this behavior, we numerically study how the minimum privacy requirement depends on the matrix dimensions and provide a quadratic estimate for this relation. The results suggest that feasibility can be achieved when T sim 0.5 KL. Second, in the low-privacy regime, the recently developed cyclic-addition degree tables (CAT) and discretely optimized GASP (DOG) codes are among the most efficient known classical constructions for PDMM. We show that the feasibility condition developed for GASP can be adopted for both CAT and DOG codes as well, thus unifying the feasibility framework for multiple classical PDMM coding schemes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.23406) | 2026-09-03
