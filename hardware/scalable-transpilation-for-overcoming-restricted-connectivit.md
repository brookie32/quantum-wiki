---
title: "Scalable Transpilation for Overcoming Restricted Connectivity in Distributed Superconducting Quantum Architectures"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.07175"
summary: "arXiv:2611.07175v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) offers a promising pathway to scale superconducting quantum hardware, but restricted inter- and intra-module connect"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.07175v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) offers a promising pathway to scale superconducting quantum hardware, but restricted inter- and intra-module connectivity creates a major transpilation bottleneck. Current DQC transpilation methods often assume idealized hardware connectivity, ignore subsequent intra-module routing, or suffer from substantial computational overheads that limit their applicability at scale. To address this, we introduce a scalable transpilation method tailored for the restricted connectivity of distributed superconducting quantum architectures. Specifically, our quantum interaction graph (QIG) approach couples a graph-partitioning mapping step with a fast SABRE-inspired routing heuristic. On a 48-qubit (3 QPUs imes 16 qubits) architecture with all-to-all inter-core connectivity, our method reduces average aggregated costs by up to 24.72% (unstructured) and 24.01% (structured), while delivering >250imes speed-ups for structured workloads compared to the state-of-the-art DMapS algorithm. On the 399-qubit (3imes133) IBM Flamingo, where DMapS times out on dense circuits, our approach maintains practical runtimes. Against a DQC-adapted SABRE baseline, it reduces structured circuit routing costs by up to 51.94% (all-to-all inter-core topology) and 51.96% (restricted line topology). Ultimately, this work delivers a practical transpilation method for DQC at scale.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.07175) | 2026-11-06
