---
title: "Estimating the generator of matrix exponential time-series"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.04521"
summary: "arXiv:2611.04521v1 Announce Type: cross Abstract: The achievable precision in estimating the spectrum of a time-series signal that is promised to be sparse in Fourier space deteriorates rapidly as the"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.04521v1 Announce Type: cross Abstract: The achievable precision in estimating the spectrum of a time-series signal that is promised to be sparse in Fourier space deteriorates rapidly as the spectral peaks get closer together, as soon as we introduce noise. Here, we study the related task of generator estimation: estimating the generator of a matrix exponential time-series and its eigenvalues. We obtain rigorous non-asymptotic precision guarantees on genESPRIT, a practical algorithm solving generator estimation, and show that this task can be solved with precision independent of the spectral spacing. The guarantees are complemented by a Cramer--Rao analysis of a relaxation of the problem. In particular, in the case of unitary data with bounded additive noise with effective entrywise variance sigma^2, we show that genESPRIT estimates the associated propagator matrix in Frobenius norm with precision scaling as ilde{O}(sigma NL^{-frac12}) in the length of the time-series L and matrix dimension N, matching the corresponding spectrum-independent Cramer--Rao standard deviation scaling up to logarithmic factors. We prove that the matching distance error in the spectrum estimated by genESPRIT scales as ilde{O} (sigma^2 N^3 L^{-1} + sigma N^{frac32} L^{-frac32} ), which we compare to the lower bound on the corresponding Cramer--Rao bound with the asymptotic standard deviation scaling O(sigma L^{-frac32}). These guarantees provide the first rigorous bounds on solving the generator estimation problem. As the matrix exponential time-series can be obtained from linearly independent vector time-series by concatenation, this work opens up a new direction in spectral estimation, which circumvents the problem of crowded spectra, under the additional assumption of linear independence.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.04521) | 2026-11-05
