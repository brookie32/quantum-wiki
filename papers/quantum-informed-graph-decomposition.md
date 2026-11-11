---
title: "Quantum-Informed Graph Decomposition"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14180"
summary: "arXiv:2611.14180v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a near-term quantum algorithm for solving combinatorial optimization problems, but its accuracy"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14180v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a near-term quantum algorithm for solving combinatorial optimization problems, but its accuracy and resource requirements may scale poorly with problem size or structure, reducing its utility in practice. Approaches such as the Graph Decomposition for Optimization Algorithm (GDOA) seek to address this by iteratively reducing an input problem until it reaches a size where it can be solved using QAOA while maintaining the same optimal solution. This algorithm, however, requires solving integer programs that have exponentially many variables, and can result in suboptimal solutions, as the integer programs may contain slack terms. In this work, we propose a heuristic called the Quantum Enhanced Graph Decomposition (QEGD) algorithm. Its novelty lies in its use of QAOA as a subroutine for sparsifying a graph through local vertex-merging. The algorithm, when used to sparsify MaxCut problems that are then solved using QAOA, achieves higher approximation ratios across all tested graphs than GDOA for random 5-regular and 6-regular graphs. We then compare the time-to-solution and approximation ratio of QEGD to other QAOA variants a collection of Erdos-Renyi graphs. QEGD has higher approximation ratios on average than QAOA^2 and ParaQAOA on all tested graphs. It also results in higher average approximation ratios than DC-QAOA on sparse Erdos-Renyi graphs and comparable average approximation ratio on denser Erdos-Renyi graphs. However, its average wall-clock time is between 0.4% and 5% of the average DC-QAOA wall-clock time.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14180) | 2026-11-11
