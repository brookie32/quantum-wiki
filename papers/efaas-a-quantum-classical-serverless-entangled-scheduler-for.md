---
title: "EFaaS: A Quantum-Classical Serverless Entangled Scheduler for Hybrid Variational Algorithms"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.27540"
summary: "arXiv:2605.27540v2 Announce Type: replace Abstract: As quantum computing enters the Utility Era, realizing near-term advantage relies heavily on Hybrid Variational Quantum Algorithms (VQAs). These alg"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2605.27540v2 Announce Type: replace Abstract: As quantum computing enters the Utility Era, realizing near-term advantage relies heavily on Hybrid Variational Quantum Algorithms (VQAs). These algorithms require a tightly coupled, iterative loop between a classical CPU optimizer and a Quantum Processing Unit (QPU). However, current quantum cloud access models are bottlenecked by decoupled batch-queues that sever this loop, introducing massive Time-to-Next-Shot (TTNS) latency. This delay inflates convergence time from minutes to hours and exposes the computation to quantum hardware drift, degrading algorithmic fidelity. Unlike prior work that relies on resource-wasting static hardware reservations or state-oblivious, stateless functions, we propose EFaaS, a novel serverless middleware designed specifically for hybrid quantum workflows. EFaaS fundamentally departs from existing architectures by treating classical parameter optimization and quantum circuit execution as entangled, session-aware events. Our main technical innovations are threefold: (1) a Calibration-Aware placement strategy that dynamically routes circuits to QPUs with warm calibration caches, circumventing cold-start penalties, (2) a Dual-Resource Fair Queuing scheduler that maximizes quantum utilization by strictly prioritizing active iterative loops, and (3) the "EF-QuantumFuture" programming abstraction, a novel primitive enabling classical speculative execution to mask compute latency. Across the evaluated baselines, EFaaS achieves TTNS reductions of 11.4%-94.3%, QDC gains of 2.02%-15.78% points, and convergence speedups of 83.2%-98.3%, while eliminating drift penalties.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.27540) | 2026-08-11
