---
title: "Mixture of experts architectures for machine learning interatomic potentials"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2603.07977"
summary: "arXiv:2603.07977v3 Announce Type: replace Abstract: Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficient"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2603.07977v3 Announce Type: replace Abstract: Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically investigate Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures within the DPA3 framework for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model consistently outperforms all DPA3-based baselines across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2603.07977) | 2026-08-18
