---
title: "Superlattice methods for the shortest vector problem and discrete Gaussian sampling"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2761"
summary: "We give worst-case algorithms for the shortest vector problem (SVP) and discrete Gaussian sampling (DGS) at arbitrary widths. Both algorithms generate lists on a dense superlattice and combine vectors"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

We give worst-case algorithms for the shortest vector problem (SVP) and discrete Gaussian sampling (DGS) at arbitrary widths. Both algorithms generate lists on a dense superlattice and combine vectors along a chain down to the input lattice. Random shifts let us control the expected number of representations of a vector regardless of the lattice. For SVP we balance these counts with a novel midpoint-shell test to ensure output distributions are sufficiently uniform. For DGS we use Gaussian weights and correct the probabilities of selecting entries from the final list. For SVP, our optimized algorithm runs in time 2^{0.409 n+o(n)} and space 2^{0.259 n+o(n)}, improving the best 2^{n/2 + o(n)} worst-case SVP complexities of Hhan [ePrint, 2026]. For Haar-random lattices, or assuming a natural upper bound on the kissing constant, the costs of the algorithm match the 2^{0.292 n+o(n)} time and 2^{0.208 n+o(n)} space of Becker-Ducas-Gama-Laarhoven [SODA 2016]. For quantum SVP, through a series of refinements and generalizations we obtain worst-case time and space 2^{0.247n+o(n)}. This improves the best known heuristic quantum SVP time complexity of 2^{0.256n+o(n)} due to Bonnetain-Chailloux-Schrottenloher-Shen [Eurocrypt 2023], without requiring any heuristic assumptions. For discrete Gaussian sampling, we provide a sampling algorithm at any width with distribution error 2^{-kappa}, running in worst-case time 2^{0.292 n+o(n)} operatorname{poly}(kappa) and space 2^{0.208 n+o(n)} operatorname{poly}(kappa), improving upon the previous best 2^{n + o(n)} cost for sampling at arbitrary widths of Aggarwal-Dadush-Regev-Stephens-Davidowitz [STOC 2015]. As further applications, we obtain fast algorithms for approximate-SVP/CVP, bounded distance decoding, and estimating the Gaussian mass and smoothing parameter of any lattice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2761) | 2026-11-04
