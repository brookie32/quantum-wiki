---
title: "Flow-Based Lattice Surgery Optimization with Runtime T Gate Scheduling"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23756"
summary: "arXiv:2609.23756v1 Announce Type: new Abstract: Lattice surgery on the surface code is a leading route to fault-tolerant quantum computation. Compiling logical circuits into lattice surgery operations"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23756v1 Announce Type: new Abstract: Lattice surgery on the surface code is a leading route to fault-tolerant quantum computation. Compiling logical circuits into lattice surgery operations is a pivotal step that determines the resource cost of a computation. Prior compilers build on idealized assumptions, and one that works in practical settings remains to be developed. Existing works are either unscalable or route one gate at a time within a layer, so the embedding depends on the order of gates and opportunities to route many gates at once are lost. In addition, they assume magic states are always available and cost-free, even though preparing one costs more than a Clifford operation. We present FlowRouter, the first topological lattice surgery compiler that places Clifford routing and stochastic magic state cultivation inside a single 3D embedding. At compile time, FlowRouter formulates the routing of an entire circuit layer as a maximum-flow problem, embedding many gates simultaneously. At runtime, it allows magic states to be cultivated at every idling patch, works with the realistic cultivation process with multiplexing and multi-stage post-selections, and absorbs the stochasticity by introducing delay mechanisms that add as little spacetime volume as possible. With magic states assumed free, FlowRouter reduces spacetime volume by 2.3x and compiles 10.8x faster than the state-of-the-art static topological lattice surgery compiler. With the cultivation-aware setting that includes both Clifford and magic state cost, FlowRouter reduces spacetime volume by 2.3x on a distance-13 surface code when compared with the state-of-the-art runtime compiler.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23756) | 2026-09-22
