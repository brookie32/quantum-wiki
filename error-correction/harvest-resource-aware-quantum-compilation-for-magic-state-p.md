---
title: "Harvest: Resource-Aware Quantum Compilation for Magic State Protocols"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03315"
summary: "arXiv:2608.03315v1 Announce Type: new Abstract: Fault-tolerant quantum processors based on topological codes execute programs through lattice surgery, where operations must be mapped, routed, and supp"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03315v1 Announce Type: new Abstract: Fault-tolerant quantum processors based on topological codes execute programs through lattice surgery, where operations must be mapped, routed, and supplied with magic states across a 2D grid of physical patches. Non-Clifford operations require these magic states, produced either by distillation factories or by cultivation, each trading footprint against preparation latency, and delivering a magic state to the data patches that consume it requires routing through the same shared layout as every other operation. Yet placement, routing, scheduling, and magic-state supply cannot be optimized in isolation: two operations with no circuit-level dependency can still contend for the same ports, routes, or magic-state terminals once placed, so a compiler that decouples instruction scheduling from magic-state generation, or hard-codes a single generation protocol, is forced to trade execution time against layout footprint instead of co-optimizing both across protocols. We present Harvest, a resource-aware compilation approach for lattice-surgery that co-optimizes magic-state consumption with circuit-aware placement and congestion-aware routing under a protocol-agnostic resource model, then reclaims unused layout footprint after scheduling. Across standard benchmark suites (QAOA, QFT, QASMBench), Harvest achieves an average speedup of 4.83imes (up to 17.8imes) over sequential execution, improves schedule length by up to 1.35imes through circuit-aware placement, and reclaims up to 72.0% of unused magic-state patches and 33.9% of unused routing patches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03315) | 2026-08-05
