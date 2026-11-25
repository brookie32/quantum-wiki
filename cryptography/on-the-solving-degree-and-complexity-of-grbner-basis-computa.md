---
title: "On the solving degree and complexity of Gröbner Basis computation over finite fields"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3007"
summary: "Solving systems of multivariate polynomial equations over finite fields is a central problem in algebraic cryptanalysis, commonly approached using Gröbner basis algorithms. The complexity of Gröbner b"
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

Solving systems of multivariate polynomial equations over finite fields is a central problem in algebraic cryptanalysis, commonly approached using Gröbner basis algorithms. The complexity of Gröbner basis computation depends on the algorithm employed and is governed by the solving degree, defined as the maximum degree of the polynomials processed during the computation. Estimating this quantity is therefore crucial, and several bounds in terms of the degree of regularity have been established in the literature. In this work, we investigate the effect of Buchberger's criteria on the elimination of redundant pairs, and prove that the solving degree of a Gröbner basis algorithm combining linear algebra with Buchberger's original algorithm is bounded above by the degree of regularity defined by the leading forms of the involved polynomials. This result provides a rigorous justification for using the degree of regularity in complexity estimates for Gröbner basis algorithms, thereby supporting a common assumption in algebraic cryptanalysis. We refine the complexity analysis by establishing bounds on the number of pairs that must be processed. These bounds improve upon published complexity estimates, with particularly significant gains in certain parameter ranges.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3007) | 2026-11-23
