---
title: "LLM-Guided Evolutionary Search for Algebraic T-Count Optimization"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.29894"
summary: "arXiv:2603.29894v2 Announce Type: replace Abstract: T-count minimization is an NP-hard problem that arises in fault-tolerant quantum compilation. In the parity-matrix representation, which captures th"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2603.29894v2 Announce Type: replace Abstract: T-count minimization is an NP-hard problem that arises in fault-tolerant quantum compilation. In the parity-matrix representation, which captures the non-Clifford part of a quantum circuit, algebraic optimizers such as TODD can achieve state-of-the-art results. However, heuristics fixed in advance determine which transformation is applied, limiting the exploration of alternative trajectories that may lead to better solutions. We show how LLM-guided evolutionary search can help explore these degrees of freedom, which VarTODD exposes through a policy that determines how to allocate the available evaluation budget and how to guide the search. Execution diagnostics guide LLM-generated revisions to both numerical search parameters and program logic, with the possibility of exploiting earlier results by starting from intermediate matrices saved during previous runs. This formulation turns heuristic design into an automated search problem and, across all evaluated instances, matches or improves on the lowest listed reference T-count for every evaluated instance; for example, on the GF(2^n) multiplier benchmarks, it yields a mean relative reduction of 7.0%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.29894) | 2026-08-19
