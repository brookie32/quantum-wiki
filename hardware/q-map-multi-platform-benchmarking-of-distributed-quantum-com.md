---
title: "Q-MAP: Multi-Platform Benchmarking of Distributed Quantum Computing for Coherent Controlled Islanding"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.27829"
summary: "arXiv:2609.27829v1 Announce Type: new Abstract: The integration of distributed energy resources into power networks is accelerating. The resulting variability narrows operating margins, so a disturban"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.27829v1 Announce Type: new Abstract: The integration of distributed energy resources into power networks is accelerating. The resulting variability narrows operating margins, so a disturbance can cascade into a wide-area blackout. Controlled islanding arrests that propagation by splitting a compromised grid into self-sustaining islands that keep coherent generators together. Exact classical solutions become intractable as the bus count and island number grow. Gate-based quantum optimization provides a different route through this combinatorial space, although its reach is limited when one circuit carries every bus assignment, since qubit count and depth then follow grid size. In this study, a round-synchronous distributed quantum computing framework is developed for coherent controlled islanding under a fixed per-circuit qubit budget. Every round derives all regional subproblems from one frozen grid-wide snapshot, dispatches them to independent quantum backends at the same time, and merges the returned candidates classically into one globally evaluated update. Circuits executed in parallel therefore keep a constant size as the grid grows, and a round costs the slowest region rather than the sum of all of them. Benchmarking spans IEEE systems from 9 to 300 buses on simulation and on quantum processors of different architectures. The framework attains optimal and operationally feasible partitions on every platform under noise, even where compilation cost differs by nearly an order of magnitude. Bounding width in this way places grids beyond the reach of monolithic circuits within range of present devices and establishes a multi-backend baseline for quantum computing in large-scale power-system optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.27829) | 2026-09-24
