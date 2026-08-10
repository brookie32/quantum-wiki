---
title: "From Circuits to Hardware: Benchmarking Standard and Qubit-Efficient Quantum Optimization on Real Hardware"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.11637"
summary: "arXiv:2607.11637v2 Announce Type: replace Abstract: Despite rapid progress in quantum optimization, broad real-hardware benchmarks comparing multiple algorithmic families across diverse combinatorial "
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2607.11637v2 Announce Type: replace Abstract: Despite rapid progress in quantum optimization, broad real-hardware benchmarks comparing multiple algorithmic families across diverse combinatorial problems under a common protocol remain limited. We benchmark gate-based quantum optimization on four NP-hard problems: multi-dimensional knapsack (MDKP), maximum independent set (MIS), quadratic assignment (QAP), and market-share (MSP). We study VQE, CVaR-VQE, standard, multi-angle, and warm-start QAOA, together with qubit-efficient PCE and QRAO, on IBM Heron r1/r2 processors using resilience-level-2 mitigation. To our knowledge, this includes the first real-hardware QRAO results and the first multi-problem PCE hardware benchmark. Across 247 method-instance combinations, we report transpiled circuit size, hardware outcomes, and an independent-error gate-count fidelity proxy, F_{est}. For MDKP and MIS, an empirical operating point near F_{est}approx 0.1, corresponding to about 770 two-qubit gates at the median Heron-r2 CZ error rate, marks the onset of noise-dominated execution. QAP exposes a separate bottleneck: dense one-hot encodings and an exponentially sparse feasible manifold, with feasible fraction 10!/2^{100} at n=10; no tested hardware method produces a feasible assignment. Compiled QAOA-family circuits are generally noise dominated, and a matched uniform-random control shows that most feasible low-fidelity outcomes fall within the random range, apart from one finite-sample MIS warm-start exception. A SWAP-aware, fractional-gate, Nighthawk-topology compilation counterfactual reduces two-qubit counts but leaves all circuits below F_{est}=10^{-3}. These conclusions apply to the tested implementations rather than QAOA in general. Qubit-efficient methods extend runnable instance sizes, but only within the empirical fidelity budget.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.11637) | 2026-08-10
