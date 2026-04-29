---
title: "Constrained Optimal Polynomials for Quantum Linear System Solvers"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.20513"
summary: "arXiv:2604.20513v2 Announce Type: replace-cross Abstract: Quantum linear system solvers typically realize the inverse map as a polynomial transformation of the spectrum, so their practical cost hinges"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.20513v2 Announce Type: replace-cross Abstract: Quantum linear system solvers typically realize the inverse map as a polynomial transformation of the spectrum, so their practical cost hinges on implementing this transformation at a low polynomial degree. We introduce constrained optimal polynomials as a framework for this task, drawing on classical Krylov subspace theory. Within this framework, we develop two classes of solvers. Constrained Uniform Polynomial (CUP) solvers optimize the tradeoff between approximation accuracy and block encoding normalization under a uniform spectral model consistent with the available bounds. Constrained Adaptive Polynomial (CAP) solvers retain this structure but replace the uniform model with a probability measure reconstructed from spectral moments via a maximum entropy ansatz, where the moments are extracted from QSVT measurements. Numerical experiments under hardware and stochastic noise show that these methods achieve lower error than standard QSVT-based and Chebyshev-iteration-type solvers, particularly in noise-limited regimes. CUP offers robust performance under generic spectra, while CAP provides further improvement when the spectral structure can be exploited.



## Related
- [[constant-factor-analysis-of-optimal-quantum-linear-solvers-i|Constant Factor Analysis of Optimal Quantum Linear Solvers in Practice]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.20513) | 2026-04-29
