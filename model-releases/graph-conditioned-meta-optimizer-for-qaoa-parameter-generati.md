---
title: "Graph-Conditioned Meta-Optimizer for QAOA Parameter Generation on Multiple Problem Classes"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25275"
summary: "arXiv:2604.25275v1 Announce Type: new Abstract: We study parameter transferability for the Quantum Approximate Optimization Algorithm (QAOA) across multiple combinatorial optimization problem classes "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25275v1 Announce Type: new Abstract: We study parameter transferability for the Quantum Approximate Optimization Algorithm (QAOA) across multiple combinatorial optimization problem classes from a parameter generation perspective. Specifically, a meta-optimizer is trained on one problem class and deployed on another during test time. Prior work employs a Long Short-Term Memory network to emulate QAOA optimization trajectories, but the learned dynamics usually collapse to near-identical paths, limiting cross-problem transfer efficiency. In this paper, we present a problem-aware graph-conditioned meta-optimizer for QAOA that learns to generate parameter trajectories over a fixed horizon, providing strong initializations with only a few steps. The optimizer is conditioned on compact graph embeddings and trained end-to-end using differentiable feedback from the QAOA objective, avoiding the need for ground-truth angles. We evaluate across multiple graph problem classes, including MaxCut, Maximum Independent Set, Maximum Clique, and Minimum Vertex Cover. We report both solution quality and feasibility-aware metrics where constraints apply. Results across a comprehensive empirical study consisting of 64 settings show that the learned optimizer can reduce optimization effort and improve performance over standard initialization, while exhibiting transferable behavior across graph families and problem types.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25275) | 2026-04-29
