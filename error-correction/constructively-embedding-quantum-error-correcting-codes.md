---
title: "Constructively Embedding Quantum Error-Correcting Codes"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33389"
summary: "arXiv:2611.33389v1 Announce Type: new Abstract: Implementing quantum error-correcting codes (QECCs) requires more than favorable algebraic parameters: the interactions among data qubits and ancillas m"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33389v1 Announce Type: new Abstract: Implementing quantum error-correcting codes (QECCs) requires more than favorable algebraic parameters: the interactions among data qubits and ancillas must also fit physical hardware. Surface codes map naturally onto two-dimensional arrays, but many quantum LDPC codes have Tanner graphs with nonlocal connections. We develop a constructive pipeline that maps a QECC's Tanner graph to the targeted hardware lattice in three stages (continuous embedding, grid assignment, and path routing). Continuous embeddings reveal the geometric structure of the code, including differences between stabilizer generator sets of the same code. The discrete stages produce explicit routed layouts that we can characterize and compare using proxy metrics for footprint, communication overhead, and congestion for syndrome extraction. We examine three continuous embedding methods: multidimensional scaling (distance-based), spectral embedding (Laplacian-based), and spring layout (force-based) for the first stage. Experiments across tested codes show how routing geometry, dimension, and scale selection affect the resulting costs. In ablation studies on the radius-2 (R2) HaPPY code, graph-aware methods for continuous embedding and the choice of path-routing algorithm matter more than the grid assignment under our chosen weights in the cost function. Changing the continuous embedding reveals a trade-off: MDS incurs greater communication overhead than spectral embedding over most tested scales, while spring layout can reduce communication overhead at intermediate scales but increases congestion and is less stable across scales.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33389) | 2026-11-26
