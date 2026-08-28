---
title: "Towards Reproducible Evaluation of Distributed Quantum Circuit Partitioning Algorithms"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27099"
summary: "arXiv:2608.27099v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) addresses the physical scaling limitations of monolithic quantum processors by networking modular Quantum Processing"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.27099v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) addresses the physical scaling limitations of monolithic quantum processors by networking modular Quantum Processing Units (QPUs). Efficient execution of quantum algorithms on DQC architectures requires compiling them across QPUs while minimizing inter-QPU communication bottlenecks, primarily through circuit partitioning. However, current evaluations of state-of-the-art partitioning heuristics focus primarily on the total entanglement cost of the partitions, failing to capture the broader structural and temporal overheads introduced by distributed network constraints. This paper addresses this evaluation gap by applying established monolithic benchmarking metrics to partitioned distributed circuits to quantify the performance impact of network constraints. Using an open-source, automated evaluation pipeline, we systematically assess diverse partitioning algorithms across standardized workloads and quantum network topologies. Our empirical results reveal that partitioning algorithms with comparable entanglement costs can still introduce drastically different physical execution penalties. By exposing these hidden trade-offs, such as severe increases in circuit depth and substantial reductions in gate density, this study demonstrates that comprehensive circuit-level metrics are essential for guiding the future design of DQC compilers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27099) | 2026-08-28
