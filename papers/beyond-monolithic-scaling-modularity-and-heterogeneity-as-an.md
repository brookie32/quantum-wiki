---
title: "Beyond Monolithic Scaling: Modularity and Heterogeneity as an Architectural Imperative for Utility-Scale Quantum Computing"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24059"
summary: "arXiv:2604.24059v1 Announce Type: new Abstract: Scalable quantum computing is fundamentally bottlenecked not by qubit count or fabrication yield, but by a rigid temporal mismatch: macroscopic classica"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24059v1 Announce Type: new Abstract: Scalable quantum computing is fundamentally bottlenecked not by qubit count or fabrication yield, but by a rigid temporal mismatch: macroscopic classical coordination latency (au_c) inevitably grows with system diameter, while microscopic quantum coherence (au_q) remains strictly bounded. Beyond a critical scale, this mismatch breaches the classical control light cone, triggering a superlinear geometric penalty (epsilon > 0) that renders monolithic synchronization physically impossible. We formalize the resulting structural phase transition through a governing scaling law, 1+epsilon > gamma, which mandates modular decomposition and a shift from global unitaries to Local Operations and Classical Communication (LOCC). To manage the resulting resource contention under strict coherence budgets, we introduce a layered semantic architecture and a time-aware Reserve--Commit protocol. By embedding predictive temporal pre-validation, the protocol acts as an architectural semantic classifier: it preemptively aborts transactions that exceed the causal horizon and explicitly converts scheduling-induced failures into location-known erasure metadata, directly relaxing hardware fidelity thresholds for downstream QEC decoders. Under near-term transduction targets (eta_{trans} sim 0.1), we project a crossover scale at N_c sim 10^5--10^6 physical qubits. This threshold marks a profound architectural convergence: the footprint required for modularity aligns precisely with early fault-tolerant utility, establishing time-aware distributed orchestration, rather than monolithic expansion or centralized classical control, as the physical imperative for utility-scale quantum computing.



## Related
- [[few-shot-cross-device-transfer-for-quantum-noise-modeling-on|Few-Shot Cross-Device Transfer for Quantum Noise Modeling on Real Hardware]]
- [[diffqec-a-versatile-diffusion-model-for-quantum-error-correc|DiffQEC: A versatile diffusion model for quantum error correction]]
- [[fair-decoder-baselines-and-rigorous-finite-size-scaling-for-|Fair Decoder Baselines and Rigorous Finite-Size Scaling for Bivariate Bicycle Codes on the Quantum Erasure Channel]]
- [[quantum-circuit-cutting-complexity-and-optimization|Quantum Circuit Cutting: Complexity and Optimization]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24059) | 2026-04-28
