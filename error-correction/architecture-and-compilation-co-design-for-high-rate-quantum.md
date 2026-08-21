---
title: "Architecture and Compilation Co-Design for High-Rate Quantum Product Codes on Neutral Atom Arrays"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20164"
summary: "arXiv:2608.20164v1 Announce Type: new Abstract: Achieving fault-tolerant quantum computing at a practical scale demands quantum error correction (QEC) codes with high encoding rates. Quantum low-densi"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.20164v1 Announce Type: new Abstract: Achieving fault-tolerant quantum computing at a practical scale demands quantum error correction (QEC) codes with high encoding rates. Quantum low-density parity-check (qLDPC) codes emerge as a promising candidate, especially given the rise of neutral atom arrays that provide dynamic long-range connectivity via atom movements. In general, synthesizing valid and efficient physical execution plans for QEC is a provably hard combinatorial problem, forming a critical compilation bottleneck that worsens as code sizes grow. To overcome this complexity, we focus on an important product family of qLDPC codes with dimension-reduction properties, and propose ONEX. This framework decomposes complex 2D physical execution planning into independent 1D subproblems, each solved to optimal execution depth within practical compilation time. First, we formulate the 1D execution plan with an explicit satisfiability modulo theories (SMT) encoding. This protocol produces provably depth-optimal solutions with substantial duration reduction. Second, we develop a multi-stage compilation pipeline featuring anytime optimization, movement compaction, and iterative feedback. This pipeline maintains practical wall-clock times while providing progressive refinement and on-demand retrieval of quality solutions. Third, we evaluate ONEX in the application of hypergraph product (HGP) code memory mapped onto neutral atom arrays, achieving 3.7x to 6.1x and 29.8x to 42.1x higher clock rates than the constructive 1D algorithm and the general 2D compiler, respectively, while scaling efficiently to codes with 2,500 data qubits. Finally, we extend ONEX to zoned layouts, revealing architectural insights into the associated trade-offs, and demonstrate its applicability to the broader lifted-product (LP) code family through a representative example.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20164) | 2026-08-21
