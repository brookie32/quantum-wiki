---
title: "Quantum Circuit Cutting: Complexity and Optimization"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23700"
summary: "arXiv:2604.23700v1 Announce Type: new Abstract: The current noisy intermediate-scale quantum (NISQ) era is characterized by substantial errors and noise, which limit the practical feasibility of deep,"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23700v1 Announce Type: new Abstract: The current noisy intermediate-scale quantum (NISQ) era is characterized by substantial errors and noise, which limit the practical feasibility of deep, many-qubit circuits. To address these constraints, quantum circuit cutting has emerged as a promising tool. Recently, there has been significant research on methods for performing such cutting effectively. In this work, the duality between quantum circuits and classical graphs - specifically, directed acyclic graphs (dags) - is leveraged to analyze the complexity of finding an optimal circuit-cutting configuration that minimizes the number of cuts. After developing a rigorous graph-theoretic framework, the complexity of identifying cut locations that partition a given quantum circuit into smaller fragments is characterized. The corresponding graph-combinatorial task is then defined, and the resulting partition problem is shown to be NP-complete. Furthermore, even a simplified version of the problem, restricted to circuits composed only of one- and two-qubit gates, is shown to be NP-complete. Finally, based on these constraints, an algorithm grounded in satisfiability modulo theories (SMT) is proposed to find optimal cuts when the number of qubits per partition is bounded. This work therefore provides a complexity-theoretic characterization of cut placement and a practical solver for bounded-size decompositions.



## Related
- [[few-shot-cross-device-transfer-for-quantum-noise-modeling-on|Few-Shot Cross-Device Transfer for Quantum Noise Modeling on Real Hardware]]
- [[beyond-monolithic-scaling-modularity-and-heterogeneity-as-an|Beyond Monolithic Scaling: Modularity and Heterogeneity as an Architectural Imperative for Utility-Scale Quantum Computing]]
- [[quantum-decoherence-of-the-surface-code-a-generalized-caldei|Quantum Decoherence of the Surface Code: A Generalized Caldeira-Leggett Approach]]
- [[fixed-reservoir-vs-variational-quantum-architectures-for-cha|Fixed-Reservoir vs Variational Quantum Architectures for Chaotic Dynamics: Benchmarking QRC and QPINN on the Lorenz System]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23700) | 2026-04-28
