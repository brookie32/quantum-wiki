---
title: "Cayley access models for matrix functions: reachable class and cost"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23429"
summary: "arXiv:2610.23429v1 Announce Type: new Abstract: We study how to compute f(A)b on a quantum computer, where A is Hermitian. When f is nonsmooth or has localized difficulty in the spectrum, classical nu"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23429v1 Announce Type: new Abstract: We study how to compute f(A)b on a quantum computer, where A is Hermitian. When f is nonsmooth or has localized difficulty in the spectrum, classical numerical linear algebra approximates it with rational functions rather than polynomials. We propose the Cayley transform, parameterized by sigma in R and gamma > 0, as an alternative to the standard quantum access model. The two parameters let one concentrate accuracy where f is difficult, which standard models can achieve only by raising the polynomial degree globally. This transformation converts Hermitian matrices to unitaries, allowing generalized quantum signal processing to apply Laurent polynomials bounded on the unit circle. We compare three access models (block encoding, matrix exponential, and Cayley encoding) in terms of query complexity and of the cost of their circuit realization. When the difficulty of f is localized in the spectrum, the Cayley encoding reduces the required degree by a factor of three to four, and it represents the shifted resolvent exactly at degree one. For spectral projectors, the standard models cannot reach the target accuracy at fixed degree, because their approximants cannot concentrate resolution near the discontinuity. Realizing the Cayley encoding from a block encoding requires solving a shifted linear system, whose cost offsets its query-complexity gain over the standard models. For structured matrices arising in practice, however, low-depth circuits for the encoding can be constructed directly, and the gain is preserved at the circuit level.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23429) | 2026-10-19
