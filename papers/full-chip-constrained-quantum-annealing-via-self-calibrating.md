---
title: "Full-chip constrained quantum annealing via self-calibrating spin-susceptibility control"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27702"
summary: "arXiv:2611.27702v1 Announce Type: new Abstract: Discrete optimization in finance, power grids, and logistics requires minimizing Ising Hamiltonians under coupled linear constraints. However, quadratic"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27702v1 Announce Type: new Abstract: Discrete optimization in finance, power grids, and logistics requires minimizing Ising Hamiltonians under coupled linear constraints. However, quadratic-penalty formulations generate dense cliques that exhaust the minor-embedding capacity of sparse superconducting processors at 128-176 spins, and first-order dual subgradient schemes diverge or stall under constraint coupling. Accordingly, this study proposes a closed-loop primal-dual scheme, designated as Self-Calibrating Quantum Susceptibility Quasi-Newton (SelfCal-QSQN), in which linear constraints are encoded in longitudinal fields and dual curvature is reconstructed from single-shot spin-fluctuation covariances. This scheme requires no penalty couplers, slack qubits, or perturbation queries. Evaluated over 891 runs on D-Wave Advantage (5,612 qubits) and Advantage2 (4,560 qubits), SelfCal-QSQN achieves 83.3% full-chip exact feasibility, reduces high-constraint error by 6.1-20.1-fold over K-scaled first-order updates (138.4-323.3-fold over fixed-gain curvature), outperforms time-matched mixed-integer programming at 256 spins, and attains 95.0%-96.7% feasibility on non-native and inequality benchmarks. Moreover, the scheme is robust toward shot noise and freeze-out drift.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27702) | 2026-11-23
