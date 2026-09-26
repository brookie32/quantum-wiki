---
title: "Square-Root Log-Rank Standard Deviations for the Higher-Rank Kadison–Singer Problem: Polynomial-Time Algorithms via Schatten-Norm Potentials"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2193"
summary: "We study the matrix signing problem for positive semidefinite matrices, assigning one sign to each original matrix regardless of its rank. This includes the higher-rank Kadison--Singer partition probl"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

We study the matrix signing problem for positive semidefinite matrices, assigning one sign to each original matrix regardless of its rank. This includes the higher-rank Kadison--Singer partition problem [KS59] when the matrices sum to the identity. For arbitrary positive semidefinite matrices A_1,ldots,A_minmathbb C^{nimes n}, we prove that there are signs sigma_iin{-1,1} such that |sum_i sigma_i A_i|le 3.34963|sum_i operatorname{tr}[A_i]A_i|^{1/2}. We give a deterministic algorithm achieving this bound in widetilde O(mn^2+n^{4.75}) real arithmetic operations. Inspired by the Lee--Sidford barrier, we use a potential function built from Schatten norms to obtain a square-root logarithmic dependence on the rank. Under the additional assumptions sum_iA_i=I, |A_i|lealpha, and operatorname{rank}(A_i)le r, we obtain a discrepancy of at most min{1,3.48745sqrt{alphalog(2r)}}. We also give a deterministic algorithm achieving a discrepancy of at most min{1,4.171sqrt{alphalog(2r)}} in widetilde O(mn^2+n^{6.38}) real arithmetic operations. This dependence on alpha and r is optimal up to an absolute constant when 0<alphale1/256 and rge256alpha^{-6}: even diagonal matrices can force every signing to have a discrepancy of at least min{1,sqrt{alphalog(2r)}}. For a zero-one incidence matrix with at most d ones in each row and each column, our deterministic algorithm achieves a discrepancy of O(sqrt{dlog(d)}), recovering Harvey's bound [Har15] by a different method. We give a deterministic construction of a single spanning tree that is simultaneously spectrally thin with respect to any given collection of kge1 positive edge weightings of the same graph, assuming small edge leverage in every weighting. The tree retains the original edge weights, and its thinness bound grows only logarithmically with k.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2193) | 2026-09-23
