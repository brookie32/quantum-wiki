---
title: "ARGON: A GNN-Empowered Compilation Framework for Scalable Neutral Atom Computing"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21216"
summary: "arXiv:2607.21216v1 Announce Type: cross Abstract: Neutral atom quantum systems offer a promising pathway to large-scale quantum computing due to high qubit uniformity and flexible connectivity. To exp"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21216v1 Announce Type: cross Abstract: Neutral atom quantum systems offer a promising pathway to large-scale quantum computing due to high qubit uniformity and flexible connectivity. To exploit this architecture, compilers must coordinate dynamic atom transport alongside highly parallel entangling gates. As circuits scale, the interplay between these operations becomes a system bottleneck, introducing denser logical interactions and longer temporal dependencies. Compilers must simultaneously satisfy rigid spatial constraints and complex movement schedules. Existing joint spatiotemporal compilation methods face an exponentially expanding search space, incurring substantial overheads or compromising fidelity as circuit size grows. In this work, we propose ARGON, a scalable compilation framework that introduces a spatiotemporal decoupling paradigm for neutral atom processors. Our key novelty is offloading static geometric conflict resolution to an offline phase, precomputing a library of hardware-certified, high-parallelism spatial layouts. To guide temporal routing, we deploy a Graph Neural Network (GNN) predictor to evaluate candidate layouts against deep temporal horizons, proactively evading downstream kinematic bottlenecks. Finally, a heuristic router translates the selected sequence into collision-free physical transport. Evaluations show ARGON completes compilation in under 10 seconds, delivering up to a >10^4x and 600x average speedup over state-of-the-art baselines. ARGON also minimizes routing decoherence and reduces Rydberg stages, improving execution fidelity by up to 10^2x on dense circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21216) | 2026-07-24
