---
title: "Classical Simulation and Design Frontiers for IBM's Doped Clifford Sampling Experiment"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.13110"
summary: "arXiv:2608.13110v1 Announce Type: new Abstract: We classically simulate the IBM doped Clifford random circuit sampling experiment, comprising 70 qubits, 70 entangling layers, and 468 inserted T gates."
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.13110v1 Announce Type: new Abstract: We classically simulate the IBM doped Clifford random circuit sampling experiment, comprising 70 qubits, 70 entangling layers, and 468 inserted T gates. A deterministic temporal-boundary tensor network contraction approach is specifically designed to tackle such open-boundary one-dimensional brickwork circuits with operator-Schmidt-rank-2 entangling gates. For an n-qubit circuit of depth d, the resulting unsliced path evaluates an exact amplitude with contraction width lceil d/2rceil; Ratcatcher calculations certify that no smaller width is possible for the tested instances. Because one-qubit gates are absorbed without changing the network topology, the width and dense scheduled contraction cost are independent of their values and of the number and placement of T gates. For the IBM instance, its largest intermediate tensor contains 2^{35} complex64 entries (256 times smaller than IBM's estimation), corresponding to a tensor payload of 256 GiB, and is distributed across eight GPUs within a node. Using 32 nodes, with eight NVIDIA H100 GPUs per node, we completed all 2051 amplitude batches corresponding to IBM's published output bitstrings in 37.3 minutes. The resulting probabilities yield a log-XEB estimate of 0.35034 with a 95% interval of [0.29763,0.40305]. Under the Porter--Thomas and scrambled-noise assumptions, this is numerically compatible with IBM's fidelity lower bound; separately, fidelity-weighted resource accounting projects a 583-contraction workload with a 10.6-minute makespan on the same 32 nodes. More broadly, the approach provides a practical diagnostic for experimental outputs and a quantitative tool for designing future doped Clifford sampling experiments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.13110) | 2026-08-14
