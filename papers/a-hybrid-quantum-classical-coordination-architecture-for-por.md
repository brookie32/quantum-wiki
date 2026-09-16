---
title: "A Hybrid Quantum-Classical Coordination Architecture for Portfolio Optimization via Global Context Injection"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.15708"
summary: "arXiv:2609.15708v1 Announce Type: cross Abstract: Near-term quantum and quantum-inspired solvers for portfolio optimization rely on local subproblem execution under severe size constraints, but this l"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.15708v1 Announce Type: cross Abstract: Near-term quantum and quantum-inspired solvers for portfolio optimization rely on local subproblem execution under severe size constraints, but this locality can omit cross-cluster covariance essential for global risk coordination. We propose Context-Aware Folding (CAF), a lightweight hybrid quantum-classical coordination layer between one-shot static decomposition and full-matrix optimization. CAF injects a compressed global risk state into each local subproblem via a state-dependent linear bias, decouples local candidate generation from global commitment, and retains a sequential acceptance rule with a monotonic non-divergence guarantee. On a 2016 Russell 3000 subset (N=484) with Simulated Annealing (SA), CAF improves the scalarized mean-variance objective by 6.59% over a static baseline (20/20 wins), and by 0.2579% on an additional 2018 panel (N=1397, 17/20 wins). We further report matched folded N=40 compatibility studies with the Quantum Approximate Optimization Algorithm (QAOA) and simulated quantum annealing (SQA) as local solvers, together with a frozen hardware-in-the-loop run on Origin Quantum's Wukong 180 (exttt{WK_C180}) for one warm-started QAOA subproblem at n=5. These results support CAF as a coordination architecture with strong classical large-scale evidence, cross-backend compatibility, and local executability on real quantum hardware in the noisy intermediate-scale quantum (NISQ) era.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.15708) | 2026-09-16
