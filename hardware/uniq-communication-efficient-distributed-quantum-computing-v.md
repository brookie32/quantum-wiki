---
title: "UNIQ: Communication-Efficient Distributed Quantum Computing via Unified Nonlinear Integer Programming"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.00401"
summary: "arXiv:2512.00401v2 Announce Type: replace Abstract: Distributed quantum computing (DQC) is widely regarded as a promising approach to overcome quantum hardware limitations. A major challenge in DQC li"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2512.00401v2 Announce Type: replace Abstract: Distributed quantum computing (DQC) is widely regarded as a promising approach to overcome quantum hardware limitations. A major challenge in DQC lies in reducing the communication cost introduced by remote CNOT gates, which are significantly slower and more resource-consuming than local operations. Existing DQC approaches treat the three essential components (qubit allocation, entanglement management, and network scheduling) as independent stages, optimizing each in isolation. However, we observe that these components are inherently interdependent, and therefore adopting a unified optimization strategy can be more efficient to achieve the global optimal solutions. Consequently, we propose UNIQ, a novel DQC optimization framework that integrates all three components into a non-linear integer programming (NIP) model. UNIQ aims to reduce the circuit runtime by maximizing parallel Einstein-Podolsky-Rosen (EPR) pair generation through the use of idle communication qubits, while simultaneously minimizing the communication cost of remote gates. To solve this NP-hard formulated problem, we adopt two key strategies: a greedy algorithm for efficiently mapping logical qubits to different QPUs, and a JIT (Just-In-Time) approach that builds EPR pairs in parallel within each time slot. Extensive simulation results demonstrate that our approach is widely applicable to diverse quantum circuits and QPU topologies, while substantially reducing communication cost and runtime over existing methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.00401) | 2026-10-02
