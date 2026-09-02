---
title: "Discrete Gaussian Sampling Meets BDGL Decoding: Solving the Shortest Vector Problem in 2^{0.5596n+o(n)} Time"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1844"
summary: "Aggarwal, Dadush, Regev, and Stephens-Davidowitz (ADRS) gave a 2^{n+o(n)} time algorithm for the Shortest Vector Problem (SVP) based on discrete Gaussian sampling (DGS), together with an honest sample"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Aggarwal, Dadush, Regev, and Stephens-Davidowitz (ADRS) gave a 2^{n+o(n)} time algorithm for the Shortest Vector Problem (SVP) based on discrete Gaussian sampling (DGS), together with an honest sampler producing 2^{n/2} samples above the smoothing parameter in 2^{n/2+o(n)} time and space. Gao, Feng, and Hu (GFH) subsequently introduced DGS on random prime-index superlattices, making this sampler available at the shortest vector scale and obtaining a 2^{0.7314n+o(n)} time algorithm. In a different direction, the Becker--Ducas--Gama--Laarhoven (BDGL) sieve uses spherical product codes to find correlated pairs and runs in 2^{0.2925n+o(n)} time under the random list heuristic. We combine the random superlattice DGS framework with a single BDGL product code decoding layer. The algorithm splits the DGS output into two lists. For a fixed shortest vector v, the Gaussian midpoint identity turns the event X-Y=v into a birthday event, while equal quotient labels certify that the reported difference belongs to the input lattice. The product code decoder locates the corresponding pair without enumerating all pairwise differences. Our analysis makes no random list assumption. For a fixed shortest vector v, once the retained lists contain a pair x,y with x-y=v, the BDGL product code finds that pair with high probability. We extend the product code analysis so that this guarantee is compatible with the claimed time and space bounds. A centered quotient line gives a 2^{0.5822n+o(n)} time algorithm. We then replace the line through the zero residue with a random affine translate. This lets us target a rarer midpoint shell. As a result, we obtain a randomized classical algorithm for SVP that runs in 2^{0.5596n+o(n)} time and uses 2^{n/2+o(n)} space.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1844) | 2026-08-31
