---
title: "Solving the Shortest Vector Problem in 2^{0.7314n+o(n)} Time via Discrete Gaussian Sampling on Superlattices"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1587"
summary: "We give a classical randomized algorithm for the exact Euclidean Shortest Vector Problem (SVP) on arbitrary full-rank lattices. It runs in 2^{0.7314n+o(n)} time and2^{n/2+o(n)} space. More precisely, "
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

We give a classical randomized algorithm for the exact Euclidean Shortest Vector Problem (SVP) on arbitrary full-rank lattices. It runs in 2^{0.7314n+o(n)} time and2^{n/2+o(n)} space. More precisely, it returns a shortest vector with high probability and runs in $ 2^{E_0n+o(n)} quadext{time and}quad 2^{n/2+o(n)} quadext{space}, qquad E_0=0.73133754ldots . This improves the 2^{n+o(n)} classical bound of Aggarwal, Dadush, Regev, and Stephens-Davidowitz (ADRS, STOC 2015). It also beats the previous best known worst-case quantum bounds of Aggarwal, Chen, Kumar, and Shen (ACKS, SIAM J.Comp. 2025), namely 2^{0.9497n+o(n)} without QRAM and 2^{0.8345n+o(n)} with QRAM. The algorithm constructs a random prime-index superlattice Gammasupset L and applies the above-smoothing honest discrete Gaussian sampler of ADRS to Gamma. Then it simply scans the resulting samples and retains the shortest nonzero one that lies in L. The analysis passes to the dual lattice M=Gamma^*. The random codimension-one constraint reduces the expected contribution of vectors outside pL^* by a factor smaller than 1/p, while the forced Gaussian mass on pL^* is controlled geometrically using the Kabatiansky--Levenshtein sphere-packing bound. Consequently, Gamma is smooth at the sampling scale and a fixed shortest vector of L is hit with probability at least 2^{-E_0n-o(n)}$ per ideal sample.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1587) | 2026-08-03
