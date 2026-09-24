---
title: "Quantum Reinforcement Learning for Cost and Delay Tradeoffs in Quantum Cloud Orchestration"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.27446"
summary: "arXiv:2609.27446v1 Announce Type: cross Abstract: Quantum cloud computing, delivered through the quantum-as-a-service (QaaS) model, provides access to quantum computing resources. However, applying un"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.27446v1 Announce Type: cross Abstract: Quantum cloud computing, delivered through the quantum-as-a-service (QaaS) model, provides access to quantum computing resources. However, applying uniform time-based pricing across fundamentally heterogeneous quantum resources significantly complicates task orchestration, particularly when addressing the tradeoff between execution costs and system performance. While heuristic methods rely on predefined scheduling rules, classical deep reinforcement learning (DRL) models may require more trainable parameters in this setting. Motivated by the potential of parameterised quantum circuits (PQCs) as compact function approximators, we propose QRLQ, a cost-delay-aware quantum cloud scheduling framework integrating PQCs with a dueling double deep Q-network (D3QN) to dynamically account for both cost and delay. Our simulation results show that QRLQ achieves lower mean cost and delay than the heuristic baselines, achieving a 5-11% lower mean cost relative to availability-based and rotation-based heuristics and reducing mean delay by 17% and 82% relative to the strongest and weakest heuristic baselines, respectively, while retaining execution fidelity within 2% of a fidelity-greedy policy. Compared with the classical DRL baseline, QRLQ achieves comparable scheduling performance while using 72% fewer trainable parameters. This work explores the feasibility of using QRL for task orchestration in quantum cloud environments and demonstrates its potential for cost-delay-aware quantum resource management.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.27446) | 2026-09-24
