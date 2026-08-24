---
title: "To Scale Up or To Scale Out: Evaluating Space-Time Costs of Compiled Logical Circuits on Modular Superconducting Quantum Processors"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20462"
summary: "arXiv:2608.20462v1 Announce Type: new Abstract: Modular integration has emerged as the main pathway for scaling superconducting quantum processing units (QPUs) beyond the constraints of fabrication yi"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.20462v1 Announce Type: new Abstract: Modular integration has emerged as the main pathway for scaling superconducting quantum processing units (QPUs) beyond the constraints of fabrication yield and physical footprint. Currently, two primary strategies lead this effort. Mirroring the "Scaling Up" and "Scaling Out" approaches in GPU architectures and AI infrastructures, these are: chiplet-based scaling, which preserves dense connectivity and high gate fidelity at the expense of engineering complexity, and distributed architectures, which decouple system scaling from monolithic QPU advancements at the expense of sparser connectivity and lower interconnect quality. To evaluate these approaches, we introduce a quantitative stress test measuring the execution cost of a dense workload of random logical entangling operations using a surface code scheme. Using a dedicated compiler, we compute the space-time cost as the number of network nodes increases, analysing this scaling behaviour across various surface code distances, Bell-state fidelities, and Bell-pair generation times. We find that distributed architectures incur an up to exponential space-time performance penalty compared to an effectively monolithic architecture across all simulations. Our results also show that as the network grows, this penalty manifests in two distinct scaling regimes: a noise-dominated regime constrained by insufficient Bell-state fidelity and generation rates, and a connectivity-dominated regime bottlenecked by lattice-surgery routing congestion.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20462) | 2026-08-24
