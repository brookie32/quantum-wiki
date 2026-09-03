---
title: "QArray+: A physics-informed GPU-accelerated simulator for quantum dot arrays"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02736"
summary: "arXiv:2609.02736v1 Announce Type: cross Abstract: Semiconductor quantum-dot arrays are a compelling platform for scalable quantum technologies, yet their practical operation is hindered by the complex"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02736v1 Announce Type: cross Abstract: Semiconductor quantum-dot arrays are a compelling platform for scalable quantum technologies, yet their practical operation is hindered by the complexity of tuning large-scale devices. Existing automation tools rely on simplified physical models---such as constant-capacitance approximations and equilibrium Hubbard models---which assume instantaneous relaxation to a steady state. These frameworks fail in experimentally critical regimes where measurement rates exceed tunneling dynamics, necessitating more sophisticated non-equilibrium control strategies. To bridge this gap, we introduce QArray+, an extension of the QArray framework that incorporates gate-dependent tunnel coupling and a quantum open-system description of dissipative processes. This approach enables the unified simulation of coherent interdot charge-state hybridization and the non-equilibrium latching dynamics essential for training robust machine-learning models for automated device operation. Implemented in JAX with GPU acceleration, QArray+ scales across GPUs and multi-node systems. For example, a charge stability diagram for a 100X100 grid of gate voltages over 64 dots can be computed in sim0.17,s on multiple GPUs. Since interdot interactions are short-ranged and the corresponding tuning corrections are local, simulations at these scales capture the physics relevant to even larger devices. These capabilities support high-throughput dataset generation for automated device tuning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02736) | 2026-09-03
