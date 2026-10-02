---
title: "Quantum Approximate Multi-Objective Optimization in Routing Problems"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00168"
summary: "arXiv:2610.00168v1 Announce Type: cross Abstract: Multi-objective optimization (MOO) problems are common in logistics, where routing decisions must balance conflicting objectives such as travel distan"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00168v1 Announce Type: cross Abstract: Multi-objective optimization (MOO) problems are common in logistics, where routing decisions must balance conflicting objectives such as travel distance, delivery time, and operational risk. A recently proposed Quantum Approximate Optimization Algorithm (QAOA) parameter-transfer strategy solves multi-objective MAX-CUT problems by reusing parameters trained on smaller instances, avoiding costly reoptimization for each scalarized problem. However, its effectiveness has only been demonstrated on proof-of-concept instances tailored to quantum hardware connectivity. In this work, we evaluate the applicability of this strategy to realistic routing problems. We formulate the Traveling Salesman Problem (TSP) and Vehicle Routing Problem (VRP) as Quadratic Unconstrained Binary Optimization (QUBO) models, reduce them to MAX-CUT, and assess the parameter-transfer framework under conditions matching the original study. Validation is performed through classical simulations and experiments on IBM quantum hardware. The resulting Pareto fronts are compared with those obtained using an adapted classical {epsilon}-constraint method, using hypervolume as the primary quality metric. Results indicate that parameter transfer remains effective, frequently achieving higher hypervolume and often finding competitive solutions earlier. However, performance depends on problem structure. The approach is consistently effective for TSP instances but less stable for the more constrained VRP, suggesting that QAOA parameter transferability decreases as the optimization landscape becomes more complex. These results provide the first comprehensive evaluation of QAOA parameter transfer on realistic multi-objective routing problems and demonstrate its potential beyond proof-of-concept MAX-CUT benchmarks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00168) | 2026-10-02
