---
title: "Quantum algorithms for path and cycle containment problems"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.09017"
summary: "arXiv:2605.09017v2 Announce Type: replace Abstract: The quantum query complexity of subgraph-containment problems, which ask whether a given subgraph H is present in an input graph G, has been the sub"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2605.09017v2 Announce Type: replace Abstract: The quantum query complexity of subgraph-containment problems, which ask whether a given subgraph H is present in an input graph G, has been the subject of considerable study. However, even for relatively simple subgraphs, such as paths and cycles, a complete understanding of their query complexities remains elusive. In this work, we consider several variants of path- and cycle-containment problems in the adjacency matrix model, where we search for paths or cycles of constant length k. We compare the settings where the graphs are directed or undirected, where the goal is to detect or find the existence of a path/cycle, and where the path/cycle we are looking for has length exactly k, or at most k. We also consider several promise versions of these problems, where we suppose that the input graph has a certain structure. We characterize the relative difficulty of these variants of the path/cycle-containment problems, by relating them to one another using randomized reductions, and grouping them into equivalence classes. When we restrict our attention to path-containment problems, we get a dichotomy result. Some of the path-containment problems can be solved using a linear number of queries, and all the others are equivalent to one another (and additionally to several cycle-containment problems) under randomized reductions, up to constant overhead. For the latter equivalence class, we prove a novel quantum-walk-based algorithm that achieves query complexity widetilde{O}(n^{3/2-alpha_k}), where alpha_k in Theta(c^{-k}) and c = sqrt{3+sqrt{17}}/2 approx 1.33, beating the previous best upper bound O(n^{3/2}) on its query complexity. We also provide a conditional lower bound based on the graph-collision problem, which implies that this equivalence class does not admit linear-query quantum algorithms unless graph collision admits an O(sqrt{n}) query algorithm.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.09017) | 2026-08-06
