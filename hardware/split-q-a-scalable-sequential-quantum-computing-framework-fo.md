---
title: "SPLIT-Q: A Scalable Sequential Quantum Computing Framework for Coherent Controlled Islanding"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12711"
summary: "arXiv:2608.12711v1 Announce Type: new Abstract: Growing integration of distributed energy resources increases power-system variability and uncertainty. During disturbances, these effects can intensify"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12711v1 Announce Type: new Abstract: Growing integration of distributed energy resources increases power-system variability and uncertainty. During disturbances, these effects can intensify generation-load imbalances and cascading failures. Controlled islanding limits their propagation by partitioning a compromised grid into connected, electrically sustainable islands. However, classical methods face rapidly growing computational costs as network size and island count increase. Quantum optimization offers an alternative for exploring this combinatorial partition space. Yet monolithic quantum formulations encode all assignment decisions in one circuit, causing qubit demand and circuit complexity to scale with network size. In this study, a qubit-bounded sequential distributed quantum approximate optimization algorithm (QAOA) framework is proposed to tackle coherent controlled islanding under limited quantum resources. It formulates the optimization as boundary-conditioned regional quadratic unconstrained binary optimization (QUBO) subproblems that are solved sequentially within a fixed qubit budget. Thus, circuit width remains independent of network size, with aggregate quantum workload scaling linearly on bounded-degree networks. Evaluation covers eleven IEEE systems from 9 to 300 buses using IBM quantum computing resources, with Gurobi and monolithic QAOA as references. Across all systems, the framework recovers feasible Gurobi-optimal partitions under noise, confirming the resilience of its solution quality. The results further show that the proposed method substantially reduces quantum-resource demand and circuit complexity relative to monolithic QAOA, allowing large islanding problems to be addressed within current hardware limits. The proposed framework provides a feasible and scalable pathway for quantum optimization in large-scale power systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12711) | 2026-08-14
