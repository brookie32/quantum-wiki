---
title: "Solving larger Travelling Salesman Problem networks with a penalty-free Variational Quantum Algorithm"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.06523"
summary: "arXiv:2512.06523v3 Announce Type: replace Abstract: The Travelling Salesman Problem (TSP) is a well-known NP-hard combinatorial optimisation problem with important industrial applications. Although ex"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2512.06523v3 Announce Type: replace Abstract: The Travelling Salesman Problem (TSP) is a well-known NP-hard combinatorial optimisation problem with important industrial applications. Although extensively studied, quantum solutions for instances beyond a dozen locations remain uncommon. We present a hybrid penalty-free Variational Quantum Algorithm (VQA) that significantly reduces both the qubit count and the runtime through a compact penalty-free formulation scaling as O(nlog_2 n) qubits compared to conventional formulations with O(n^2) scaling. The VQA achieves solution qualities exceeding 90% on Rigetti quantum hardware for instances of up to 17 locations. To the best of our knowledge, this represents the largest TSP instance solved on gate-based hardware. We systematically evaluate multiple encoding and optimisation strategies, and show that warm-start initialisation improves solution quality, while runtime is reduced by nearly two orders of magnitude through the use of gradient-free optimisation methods and cost-function caching. We additionally introduce a novel VQA inspired classical machine learning model (VQAi-CML) and benchmark the VQA against VQAi-CML, a greedy heuristic, a Monte Carlo baseline, and a strong classical optimisation baseline. Across the networks evaluated, the VQA consistently achieves superior solution quality relative to VQAi-CML, greedy heuristic, and Monte Carlo baselines, but not the classical solver

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.06523) | 2026-10-07
