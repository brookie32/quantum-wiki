---
title: "SpiderLS: Leveraging Full ZX Reduction for Lattice Surgery Compilation"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.30228"
summary: "arXiv:2608.30228v1 Announce Type: new Abstract: Lattice surgery compilation plays a central role in translating fault-tolerant quantum programs into efficient surface code realizations, where both spa"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30228v1 Announce Type: new Abstract: Lattice surgery compilation plays a central role in translating fault-tolerant quantum programs into efficient surface code realizations, where both spatial and temporal resources directly determine the cost of execution. Recent work has demonstrated the benefits of using ZX-diagrams as an intermediate representation for lattice surgery compilation, enabling semantics-preserving transformations that reduce spacetime cost. However, existing compilation restricts ZX reduction to preserve diagram structures that can be directly embedded as lattice surgery junctions. We present SpiderLS, which extends prior approach by leveraging full ZX reduction. To translate the resulting diagram into executable lattice surgery operations, SpiderLS applies a sequence of compiler passes that derives an execution order, generates target code by grouping compatible interactions into multi-target operations, and lowers the target code to Pauli-product measurements. The resulting explicit patch and Pauli-boundary requirements guide logical scheduling and structure-aware spacetime routing. Across representative algorithmic and random workloads, SpiderLS achieves average reductions of 49.2% in spacetime volume and 99.8% in compilation time compared with the prior ZX-based compiler.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.30228) | 2026-09-01
