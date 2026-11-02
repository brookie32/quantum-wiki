---
title: "The Quartic Gap Between Quantum and Dequantized Algorithms for Linear Algebra Is Tight"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.42069"
summary: "arXiv:2610.42069v1 Announce Type: new Abstract: Quantum algorithms for linear algebra that access a matrix A through quantum random access memory (QRAM) prepare quantum states proportional to the solu"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.42069v1 Announce Type: new Abstract: Quantum algorithms for linear algebra that access a matrix A through quantum random access memory (QRAM) prepare quantum states proportional to the solutions of linear systems and related problems. Dequantized classical algorithms, when given sampling and query access to A, return sampling and query access to an approximate solution. Both kinds of algorithms use a number of queries that is polynomial in the normalized Frobenius norm rho=|A|_F/|A| and does not directly depend on the dimension. For linear systems at fixed condition number and accuracy, quantum algorithms use widetilde O(rho) queries, whereas the best dequantized algorithms use widetilde O(rho^4). We prove that this quartic gap is tight in the worst case, up to a logarithmic factor. For every constant kappa_0>1, we construct dense linear systems with condition number at most kappa_0 for which sampling from the solution within a sufficiently small constant total variation distance requires Omega(rho^4/logrho) classical queries but only Theta(rho) quantum queries. The same separation holds, for errors below smaller thresholds, for positive-definite systems, least squares, ridge regression, matrix powers and square roots, imaginary-time and real-time Hamiltonian evolution, and sampling from the top principal component. Our results therefore show that many quantum algorithms for linear algebra, achieve a near-quartic speedup in the worst case, over classical algorithms with sampling and query access. All of these classical lower bounds follow from the same framework, which is based on a lower bound for sampling from distributions that depend on a fixed set of Fourier coefficients of an unknown Boolean function.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.42069) | 2026-11-02
