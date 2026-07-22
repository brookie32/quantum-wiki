---
title: "Robust Belief-State Policy Learning for Quantum Network Routing Under Decoherence and Time-Varying Conditions"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.08654"
summary: "arXiv:2509.08654v2 Announce Type: replace Abstract: Quantum network routing requires online decisions under probabilistic entanglement generation, finite quantum memories, decoherence, imperfect opera"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2509.08654v2 Announce Type: replace Abstract: Quantum network routing requires online decisions under probabilistic entanglement generation, finite quantum memories, decoherence, imperfect operations, and classical feedback, while the controller has incomplete knowledge of the physical state. This paper develops a robust belief-state routing framework based on a quantum partially observable Markov decision process (q-POMDP) and a feasibility-masked graph neural network (GNN). The model uses atomic micro-epochs in which each selected operation completes before the next decision boundary. This enables explicit accounting of memory reservations, pair-instance inventories, purification consumption, swapping outcomes, release decisions, queue service, and completion-time delivery fidelity. The controller maintains a classical belief over hidden physical states, including latent environmental conditions, and uses this belief to evaluate feasible actions and update posterior pair states. To make planning scalable, we introduce feasibility-stratified prototypes, identifier-free signatures, and role-aware action matching, which preserve hard resource constraints while enabling value transfer across structurally similar information states. A cached q-POMDP planner is then fused with a role-aware GNN policy through an adaptive trust rule, with a safe fallback for previously unseen feasibility signatures. We provide theoretical guarantees on feasibility, value approximation, policy performance, robustness, regret, and learning variance. Simulations over finite-memory quantum-network topologies show that the proposed hybrid controller improves high-fidelity goodput, reduces below-threshold deliveries, and maintains lower online decision cost than planner-only control, while outperforming heuristic, purification-aware, and learning-based baselines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.08654) | 2026-07-22
