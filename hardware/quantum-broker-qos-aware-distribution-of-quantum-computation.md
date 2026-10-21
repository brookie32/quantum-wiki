---
title: "Quantum Broker: QoS-Aware Distribution of Quantum Computations"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28342"
summary: "arXiv:2610.28342v1 Announce Type: new Abstract: Cloud-accessible quantum computing has made heterogeneous Quantum Processing Units (QPUs) available through provider platforms that differ in qubit tech"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.28342v1 Announce Type: new Abstract: Cloud-accessible quantum computing has made heterogeneous Quantum Processing Units (QPUs) available through provider platforms that differ in qubit technology, calibration state, queueing behavior, and pricing model. This heterogeneity makes execution management a quantum-engineering concern: a quantum circuit may be executable on several backends, but the resulting cost, latency, fidelity, and reproducibility depend on backend selection and on how measurement shots are allocated. This paper presents the Quantum Broker, an open-source and provider-agnostic framework for Quality-of-Service-aware quantum execution management. The framework operationalizes shot-wise distribution by exploiting the statistical independence of quantum measurement shots to dispatch a single circuit across multiple heterogeneous QPUs according to user-defined constraints and optimization objectives. It combines a modular execution architecture, interchangeable backend-profiling strategies, and the Quantum QoS Specification Language (QQSpec), a declarative language for expressing QoS requirements. Dispatch planning is supported by two solver backends: a mixed-integer linear-programming (MILP) solver, and a nonlinear dual-annealing solver. Experiments on benchmark quantum circuits and noisy simulator backends show that the Quantum Broker can produce feasible QoS-aware dispatch plans under heterogeneous backend conditions and can improve QoS satisfaction with respect to single-backend and naive multi-backend baselines. The results also expose a practical trade-off between planning time and dispatch quality, with the nonlinear solver producing higher-quality allocations at increased computational cost. Overall, the Quantum Broker provides an extensible execution-management layer for engineering portable, reproducible, and QoS-aware quantum software over fragmented quantum cloud infrastructures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28342) | 2026-10-21
