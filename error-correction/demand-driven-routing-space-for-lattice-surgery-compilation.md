---
title: "Demand-Driven Routing Space for Lattice-Surgery Compilation"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.30747"
summary: "arXiv:2610.30747v1 Announce Type: new Abstract: Lattice-surgery compilation places logical qubits on a grid of surface-code tiles and routes their interactions. Sparse static layouts limit routing con"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30747v1 Announce Type: new Abstract: Lattice-surgery compilation places logical qubits on a grid of surface-code tiles and routes their interactions. Sparse static layouts limit routing contention but reserve space that often remains idle. Reducing this reservation requires balancing area savings against additional gate serialization and qubit movement. In this paper, we present a co-designed dynamic architecture and compiler that allocates routing space according to circuit demand. The architecture preserves a fixed virtual qubit floorplan while allowing its physical spacing to change between execution stages. The compiler coordinates placement, scheduling, and routing to implement lattice surgeries using fewer physical qubits. Across our application benchmarks, our method reduces space-time volume by 55.6% in geometric mean and compiles 75.5 times faster than the evaluated DasCot configuration. A circuit-synthesis case study shows how our compiler exposes optimization tradeoffs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.30747) | 2026-10-23
