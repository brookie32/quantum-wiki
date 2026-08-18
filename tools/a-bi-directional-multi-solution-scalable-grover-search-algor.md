---
title: "A Bi-directional Multi-solution Scalable Grover Search Algorithm"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2404.15616"
summary: "arXiv:2404.15616v2 Announce Type: replace Abstract: Grover's search algorithms, including various Partial Grover Searches (PGS), suffer from scaling issues when multiple solutions are sought, as the n"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2404.15616v2 Announce Type: replace Abstract: Grover's search algorithms, including various Partial Grover Searches (PGS), suffer from scaling issues when multiple solutions are sought, as the number of iterations scales with the number of solutions or marked states, making implementation more computationally expensive. Inspired by recent PGS algorithms for multi-solution searchers, this article proposes a scalable Grover quantum search algorithm, referred to as Bi-directional Multi-solution scalable Grover Search (BMGS), to efficiently search for an arbitrary number of solutions from an unstructured database. We introduced a novel multi-segment bidirectional search tactic with PGS across multiple equal segments of each state, starting from an initial state and multiple marked states in parallel, obviating the need for merge operations. We have shown in this work that for each solution our novel approach requires at most sqrt{N}left (1- sqrt{frac{1}{b^{lfloorfrac{r}{dk}rfloor}}}right) iterations (here, N=2^r elements, k=log_2 b, d is the number of equal segments on r qubits, and b is the branching factor). Our proposed BMGS algorithm is benchmarked against state-of-the-art Depth First Grover Search (DFGS) and PGS implementations for an arbitrary number of solutions, ranging from 2 to 20 qubits, as a proof of concept. We also show that our BMGS requires fewer iterations for shallow quantum circuits and achieves an optimal O(sqrt{sN}) average complexity for s solutions, when dk < r. The Qiskit Python implementation of the proposed BMGS algorithm is available on GitHubfootnote{https://anonymous.4open.science/r/Multi-Solution-DFGS-BMGS-B507/}.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2404.15616) | 2026-08-18
