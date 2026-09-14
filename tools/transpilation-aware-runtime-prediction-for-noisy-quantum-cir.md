---
title: "Transpilation-Aware Runtime Prediction for Noisy Quantum Circuit Simulation"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12980"
summary: "arXiv:2609.12980v1 Announce Type: new Abstract: Predicting the runtime of noisy quantum circuit simulations is important for scheduling, resource allocation, and performance optimization. However, acc"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12980v1 Announce Type: new Abstract: Predicting the runtime of noisy quantum circuit simulations is important for scheduling, resource allocation, and performance optimization. However, accurate prediction is challenging because backend-aware transpilation can substantially alter the original circuit structure, while the backend-derived noise model and simulator execution behavior can introduce additional runtime variation. We study the effectiveness of graph neural networks (GNNs) and conventional regression methods in predicting Qiskit Aer simulation runtime measured after transpilation. We construct a dataset from a benchmark pool of 1,402 unique circuits spanning 22 circuit families, two Qiskit fake-backend configurations, and four transpiler optimization levels. Specifically, we compare a source GNN using original circuit information, hybrid GNN combining source-level graph with post-transpilation features, and transpiled GNN using only transpiled circuit information, along with five regression models. In the overall-model setting, the transpiled GNN achieves the strongest performance among the graph-based representations at all four optimization levels, obtaining R^2 values of 0.974, 0.713, 0.745, and 0.605 for optimization levels 0 through 3, respectively. However, under backend-specific evaluation, the advantage of GNN decreases, with conventional regression models matching or outperforming the GNNs in several settings. These results indicate that post-transpilation information is useful, while the value of explicit graph modeling depends on the backend and optimization level.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12980) | 2026-09-14
