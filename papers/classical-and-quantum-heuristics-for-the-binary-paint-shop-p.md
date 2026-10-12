---
title: "Classical and Quantum Heuristics for the Binary Paint Shop Problem"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.15294"
summary: "arXiv:2509.15294v3 Announce Type: replace Abstract: The Binary Paint Shop Problem (BPSP) is an mathsf{APX}-hard optimisation problem arising in automotive manufacturing: given a sequence of 2n cars, c"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2509.15294v3 Announce Type: replace Abstract: The Binary Paint Shop Problem (BPSP) is an mathsf{APX}-hard optimisation problem arising in automotive manufacturing: given a sequence of 2n cars, comprising n distinct models each appearing twice, the task is to decide which of two colours to paint each car so that the two occurrences of each model are painted differently, while minimising consecutive colour swaps. Performance is measured by the paint swap ratio -- the average number of colour changes per car -- which directly affects production efficiency and cost. Prior work showed that the Quantum Approximate Optimisation Algorithm (QAOA) at depth p=7 achieves a ratio of 0.393, outperforming the then-best-known classical heuristic, Recursive Greedy, with a proven asymptotic expected ratio of 0.4 [Phys. Rev. A 104, 012403 (2021)]. More recently, the Recursive Star Greedy (RSG) heuristic was proposed with a conjectured expected ratio of 0.361. Here, we formally reduce BPSP to weighted MaxCut, yielding an exact Ising formulation, and benchmark two state-of-the-art low-depth QAOA variants -- eXpressive QAOA and Recursive QAOA -- at p=1 (denoted XQAOA_1 and RQAOA_1) against four classical BPSP heuristics. Across instances ranging from 2^7 to 2^{12} cars, XQAOA_1 achieves an average paint-swap ratio of 0.357; in our instance-wise benchmarks, it outperforms RQAOA_1 on almost all instances and each of the four classical baselines, including RSG, on every instance. Surprisingly, RQAOA_1 deteriorates with problem size despite employing provably near-optimal QAOA_1 parameters at each recursive step, eventually falling behind RSG at the largest sizes. To our knowledge, this is the first report of size-dependent performance degradation of RQAOA_1 at scale. In contrast, XQAOA_1 remains stable across all tested sizes, with no evidence of size-dependent degradation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.15294) | 2026-10-12
