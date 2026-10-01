---
title: "Conditioning-Free Non-Uniform Quantum Fourier and Chebyshev Transforms"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40277"
summary: "arXiv:2609.40277v1 Announce Type: new Abstract: We present an efficient quantum algorithm for the non-uniform Chebyshev transform. It is defined as the projection of a function onto Chebyshev polynomi"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40277v1 Announce Type: new Abstract: We present an efficient quantum algorithm for the non-uniform Chebyshev transform. It is defined as the projection of a function onto Chebyshev polynomials sampled at given nodes that are uniform in xin[-1,1], and hence non-uniform in the angle heta=arccos x, a setting that QFT-based quantum Chebyshev transforms cannot handle. Our construction is based on an improvement of an existing Non-uniform Quantum Fourier Transform (NUQFT) whereby we remove the conditioning from non-uniform node sampling. Hence, error bounds are independent of the geometry-dependent parameter kappa of prior work. We use the fact that Chebyshev transform matrix is the average of two Type-II non-uniform DFTs, which we implement with a single controlled NUQFT circuit. We provide explicit oracle constructions, including the row-access oracle previously left as an assumption. The resulting arepsilon-accurate block encoding has O(1) normalization and uses O(L) qubits and widetilde O(L^2) gates, where L=log N+log(1/arepsilon). We give an end-to-end implementation with complexity analysis, including the success probability and output-state error.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40277) | 2026-10-01
