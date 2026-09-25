---
title: "One-shot Routing in Quantum Networks"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29752"
summary: "arXiv:2609.29752v1 Announce Type: new Abstract: Distributed quantum computation requires many entangled pairs to be available simultaneously, so routing must optimize fidelity from a fixed, short-live"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29752v1 Announce Type: new Abstract: Distributed quantum computation requires many entangled pairs to be available simultaneously, so routing must optimize fidelity from a fixed, short-lived set of network resources rather than the rate of pairs accumulated over time. We formulate this one-shot routing problem for heterogeneous Werner-state links and jointly optimize path selection and the schedule of entanglement swapping and distillation. We show that the common purify-then-swap ordering is not optimal network-wide and that exact schedule enumeration requires m^{Theta(m)} time. We introduce Fidelity-Optimizing Local Detours (FOLD), a heuristic that starts from the highest-fidelity path and merges a detour only when distillation improves on both routes and raises end-to-end fidelity. FOLD runs in polynomial time, recovers almost all of the optimal fidelity on tractable instances, and is four orders of magnitude faster than exact optimization at circuit rank 5. On the Internet topologies where any strategy improves on shortest-path routing, FOLD achieves the highest mean end-to-end fidelity among the polynomial baselines. We further extend the formulation to links whose fidelities are known only as distributions, where uncertainty, rather than the effort spent routing, limits the fidelity delivered. Through an example of requests competing for the same links, we show that coordination becomes a condition for feasibility, and that a shared path budget controls the fidelity trade-off between them.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29752) | 2026-09-25
