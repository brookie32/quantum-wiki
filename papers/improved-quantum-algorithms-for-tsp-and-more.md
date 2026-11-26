---
title: "Improved Quantum Algorithms for TSP and More"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33730"
summary: "arXiv:2611.33730v1 Announce Type: new Abstract: The traveling salesman problem (TSP) is a canonical NP-hard optimization problem. For general edge weights, the classical dynamic programs of Bellman an"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33730v1 Announce Type: new Abstract: The traveling salesman problem (TSP) is a canonical NP-hard optimization problem. For general edge weights, the classical dynamic programs of Bellman and of Held and Karp solve TSP on n cities in O^*(2^n) time. To date, no Oh(c^n)-time classical algorithm is known for any c<2. Combining Grover search with the dynamic programming technique, Ambainis et al. (SODA 2019) introduced a quantum algorithm with running time O^*(1.7274^n), which is still the best known quantum time bound. In this work, we improve the running time to O^*(1.70961^n). The core idea of our algorithm is to combine the framework of Ambainis et al. with the extremal set-system framework, which was recently used for classical space-time tradeoffs of TSP by Jabal Ameli, Nederlof and Wang (FOCS 2026) and Dallant and Kozma (FOCS 2026). To obtain our upper bound, we decompose the optimal tour into four consecutive subpaths of different sizes, for which, based on the idea of set-systems, the optimal values are computed using dynamic programming with small success probability and use amplitude amplification. Using the same idea, we also give a new quantum space-time tradeoff for TSP, improving the previous results of Caroppo et al. (ESA 2026) and Dallant (arXiv:2607.12374). Finally, we obtain the same quantum upper bounds for several other related problems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33730) | 2026-11-26
