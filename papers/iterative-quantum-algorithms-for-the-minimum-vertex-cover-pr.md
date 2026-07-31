---
title: "Iterative quantum algorithms for the minimum vertex cover problem based on continuous-time quantum walks"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.27915"
summary: "arXiv:2607.27915v1 Announce Type: new Abstract: We introduce a constraint-preserving hybrid quantum-classical greedy framework for the minimum vertex cover problem, which extends directly to maximum i"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.27915v1 Announce Type: new Abstract: We introduce a constraint-preserving hybrid quantum-classical greedy framework for the minimum vertex cover problem, which extends directly to maximum independent set by bitwise complementation. The framework uses projected Pauli-X terms whose sum preserves the feasible subspace and acts within it exactly as the adjacency matrix of a layered graph of feasible covers. This graph is connected, so every feasible cover is linked to the configuration containing all vertices by a sequence of allowed single-vertex flips. Starting from this configuration, the corresponding continuous-time quantum walk propagates amplitude into layers containing progressively smaller covers. We rank vertices using either their marginal cover probabilities or the expected cover size obtained after fixing each candidate vertex in the cover, and use these rankings to guide recursive greedy reductions. Across several random-graph families, with walk times fixed using independent calibration ensembles, the quantum-informed algorithms achieve lower mean approximation ratios and solve a larger fraction of instances optimally than their corresponding classical greedy baselines. The conditioned-energy strategy performs best on the tested instances and retains algorithmic performance close to the exact continuous-time limit under low-depth Trotterisation. For bounded-degree graphs, each Trotter layer has circuit depth independent of system size, and the framework requires neither penalty terms nor variational training.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.27915) | 2026-07-31
