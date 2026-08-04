---
title: "Fault-tolerant quantum computing with a microwave Cat Bus"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.01111"
summary: "arXiv:2608.01111v1 Announce Type: new Abstract: The scalability of fault-tolerant neutral-atom quantum computers is constrained by the latency of shuttling with optical tweezers, imposing a stringent "
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.01111v1 Announce Type: new Abstract: The scalability of fault-tolerant neutral-atom quantum computers is constrained by the latency of shuttling with optical tweezers, imposing a stringent trade-off between qubit overhead and circuit depth in quantum algorithm compilation. Here we propose a hardware-efficient, shuttling-free architecture that achieves all-to-all connectivity. Remote Rydberg atoms are resonantly entangled through a microwave ``Cat Bus''---a cavity mode autonomously stabilized in a bosonic cat state. The Cat Bus natively supports the highly parallelized execution of one-to-many CZ^n gates with exponentially suppressed crosstalk. We derive the resulting cat--atom error channel from the underlying interactions and physical constraints. For fault-tolerant operation, we develop a hardware-aware scheduling scheme that exploits the native cat--atom CZ^{n} gate to construct a syndrome-extraction circuit with minimum depth. We benchmark the architecture using hypergraph-product (HGP) codes and estimate a 180-fold reduction in syndrome-extraction cycle time at N=10^5 data qubits compared with an atom-rearrangement-based architecture. Under matched two-qubit depolarizing noise, the corresponding error threshold increases from 0.55% to 0.72%. Under the hardware-derived error model, we obtain a threshold of 0.80%, corresponding to a threshold cooperativity of C_{th}=7.8 imes 10^4, compatible with experimentally accessible parameters for Rydberg-coupled microwave-cavity systems. By avoiding atom transport, the Cat Bus provides a route towards high-speed, fault-tolerant neutral-atom quantum computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.01111) | 2026-08-04
