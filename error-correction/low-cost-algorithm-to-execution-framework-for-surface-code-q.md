---
title: "Low-cost algorithm-to-execution framework for surface-code quantum computing"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10965"
summary: "arXiv:2609.10965v1 Announce Type: new Abstract: The execution of useful quantum algorithms on fault-tolerant processors requires more than a mapping from logical gates to encoded operations: the spati"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.10965v1 Announce Type: new Abstract: The execution of useful quantum algorithms on fault-tolerant processors requires more than a mapping from logical gates to encoded operations: the spatial organization, non-Clifford resource supply, and execution schedule must also be determined while keeping physical overhead within practical limits. Although the theoretical hierarchy from logical circuits to fault-tolerant operations is well established, these implementation choices are often specified and optimized separately. Here we develop a low-cost algorithm-to-execution framework for surface-code quantum computing. From hierarchical algorithm descriptions, it constructs dependency-preserving logical schedules and an executable workload capturing logical interactions, operation parallelism, and time-resolved non-Clifford demand, thereby linking logical computation to surface-code organization, resource-state preparation, and fault-tolerant execution in a traceable workflow. We apply the framework to twenty benchmark circuits across seven algorithm families and a hierarchically composed application-scale elliptic-curve discrete-logarithm workload. Physical costs vary substantially even for circuits with similar logical resource counts. Under our direct-rotation calibration, non-Clifford implementation selection reduces space-time volume by up to 241.5 times versus an all-synthesis baseline for the QAOA amplitude-amplification workload. Circuit-specific surface-code layouts reduce routed-latency estimates for all twenty benchmarks; thirteen also reduce space-time volume because communication savings outweigh added spatial overhead. These results show that low-cost fault-tolerant execution depends on computation scheduling and organization, not aggregate logical resource counts alone.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10965) | 2026-09-11
