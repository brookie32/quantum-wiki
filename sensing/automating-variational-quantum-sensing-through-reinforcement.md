---
title: "Automating Variational Quantum Sensing through Reinforcement-Learned Circuit Structures"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17582"
summary: "arXiv:2608.17582v1 Announce Type: new Abstract: Variational quantum sensing offers a promising route to high-precision parameter estimation, but its performance depends strongly on the circuit archite"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17582v1 Announce Type: new Abstract: Variational quantum sensing offers a promising route to high-precision parameter estimation, but its performance depends strongly on the circuit architectures used for probe preparation and measurement. Existing approaches typically optimize continuous parameters within predefined ansatze, restricting the accessible design space and limiting adaptation to sensing tasks and hardware constraints. Here, we introduce extsc{AutoQSense}, a reinforcement-learning framework that searches circuit architectures using Fisher-information-based objectives. For few-qubit systems, a single agent sequentially constructs preparation and measurement circuits. For larger systems, a distributed formulation assigns local circuit design to subsystem agents and inter-block entanglement to a budgeted agent. Numerical results show that the learned architectures recover known benchmark strategies, adapt to dephasing noise, and outperform fixed hardware-efficient ansatze while using fewer entangling gates. These results establish extsc{AutoQSense} as a resource-aware approach to adaptive and hardware-compatible quantum sensing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17582) | 2026-08-19
