---
title: "Sampled-Based Guided Quantum Walk: Non-variational quantum algorithm for combinatorial optimization"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.15138"
summary: "arXiv:2509.15138v2 Announce Type: replace Abstract: We introduce SamBa-GQW, a novel quantum algorithm for solving binary combinatorial optimization problems of arbitrary degree with no use of any clas"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2509.15138v2 Announce Type: replace Abstract: We introduce SamBa-GQW, a novel quantum algorithm for solving binary combinatorial optimization problems of arbitrary degree with no use of any classical optimizer. The algorithm is based on a continuous-time quantum walk on the solution space represented as a graph. The walker explores the solution space to find its way to vertices that minimize the cost function of the optimization problem. The key novelty of our algorithm is an offline classical sampling protocol that gives information about the spectrum of the problem Hamiltonian. Then, the extracted information is used to guide the walker to high quality solutions via a quantum walk with a time-dependent hopping rate. We investigate the performance of SamBa-GQW on several quadratic problems, namely MaxCut, maximum independent set, portfolio optimization, and higher-order polynomial problems such as LABS, MAX-k-SAT and a quartic reformulation of the travelling salesperson problem. We empirically demonstrate that SamBa-GQW finds high quality approximate solutions on problems up to a size of n=30 qubits by only sampling poly(n) states among 2^n possible decisions. Furthermore, SamBa-GQW compares in par with classically optimized variational approaches, such as the variational guided quantum walk and QAOA (the latter when run on deep circuits). This places Samba-GQW as a promising heuristic to tackle combinatorial problems beyond the NISQ regime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.15138) | 2026-10-02
