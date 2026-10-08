---
title: "Faster Provable Lattice Sieving with Spherical Codes"
date: "2026-10-07"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2388"
summary: "We study the computational problem mu-SVP, in which the goal is to find a mu-approximate shortest non-zero vector in a lattice L, for constant approximation factors mu > 1. Prior to this work, there w"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

We study the computational problem mu-SVP, in which the goal is to find a mu-approximate shortest non-zero vector in a lattice L, for constant approximation factors mu > 1. Prior to this work, there was a large gap between the fastest algorithms for this problem whose correctness had been proven and the fastest heuristic algorithms, whose correctness has not been proven (but which seem to work well in practice). We construct a novel sieving algorithm that combines the key tool used in the fastest heuristic sieving algorithms (faster nearest neighbor subroutines) together with the perturbation argument used in sieving algorithms with proven correctness. The result is an algorithm whose correctness we prove and whose running time depends on a simple geometric quantity: the maximal size of certain spherical codes. Under a reasonable assumption about the maximal size of spherical codes, our algorithm's running time is roughly 2^{0.3066n} for large constants mu, which is quite close to the best heuristic running time of roughly (3/2)^{n/2} approx 2^{0.2925n} and much faster than both the previous best known algorithm with proven correctness, which runs in time roughly 2^{0.802n} [Liu, Wang, Xu, and Zheng, 2011] and the very recent concurrent and independent work showing a 2^{n/2}-time algorithm [Hhan, 2026]. (However, the algorithm of Hhan also solves mu-SVP for mu =1, while our algorithm only works for large constant mu.) Using the best proven upper bound on the size of such spherical codes (which is almost certainly quite loose), we obtain a running time of roughly 2^{0.6078n}, which is much better than the previous best work but notably slower than the concurrent work of Hhan.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2388) | 2026-10-07
