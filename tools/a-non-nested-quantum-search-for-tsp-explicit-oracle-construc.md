---
title: "A Non-Nested Quantum Search for TSP: Explicit Oracle Construction Beyond the 2^n Barrier"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.07322"
summary: "arXiv:2606.07322v3 Announce Type: replace Abstract: The traveling salesman problem (TSP) is a classic NP-hard problem. Held--Karp dynamic programming~ite{held1962dynamic, bellman1962dynamic} solves it"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2606.07322v3 Announce Type: replace Abstract: The traveling salesman problem (TSP) is a classic NP-hard problem. Held--Karp dynamic programming~ite{held1962dynamic, bellman1962dynamic} solves it exactly in O(n^2 2^n) time. Ambainis et al.~ite{ambainis2019quantum} (SODA~2019) proposed a hybrid classical-quantum dynamic programming that improved the query complexity to O^*(1.727^n). However, their algorithm uses nested quantum minimum finding, which complicates coherent circuit implementation, particularly the handling of threshold updates within nested subroutines. To address this difficulty, we design a quantum divide-and-conquer framework without any recursive process. We overcome the oracle-construction bottleneck by preparing a set partition state, requiring O(n^2) gates and O(n) depth. Under assumed QRAM model, the structured state preparation enables polynomial-depth oracle evaluation, yielding an overall running time of O^*(1.866^n) for TSP. Qiskit simulations for n=6 and 7, using QFT-based data loading in place of QRAM, yield empirical optimal-solution probabilities of 98.9% and 100%, respectively, in fixed-threshold amplitude-amplification tests.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.07322) | 2026-11-20
