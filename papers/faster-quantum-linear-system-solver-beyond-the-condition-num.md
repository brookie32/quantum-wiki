---
title: "Faster quantum linear system solver beyond the condition number"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.07691"
summary: "arXiv:2607.07691v2 Announce Type: replace Abstract: The spectral condition number is a widely adopted measure of worst-case cost for quantum linear system solvers. Yet it can significantly overestimat"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2607.07691v2 Announce Type: replace Abstract: The spectral condition number is a widely adopted measure of worst-case cost for quantum linear system solvers. Yet it can significantly overestimate the actual runtime for a typical problem instance. We present two quantum algorithms that produce the normalized solution |xrangle of linear system Ax=| b rangle to accuracy epsilon with complexity independent of the condition number kappa=lVert A^{-1}rVert. We focus on the standard input model where A is accessed through a block encoding and | b rangle is prepared by a unitary. But we also introduce an affine dilation model that encodes A and | b rangle jointly, allowing further refinements of the query complexity. Our truncation-based solver makes an optimal number of queries to | b rangle and operatorname{mathbf{O}}left(kappa_{eff}operatorname{polylog}left(frac{kappa_{eff}}{epsilon}right)right) queries to A. We prove a family of upper bounds on the effective condition number, including kappa_{eff}leqfrac{lVert(A^agger A)^{-t/2}|xranglerVert^{1/t}}{epsilon^{1/t}} for positive even integer t and kappa_{eff}leqfrac{lVert A^{-1agger}(A^agger A)^{-(t-1)/2}|xranglerVert^{1/t}}{epsilon^{1/t}} for positive odd t, overcoming the kappa-barrier. Our filtering-based solver is extremely simple with a favorable runtime prefactor. In particular, the solver has query complexity 3frac{lVert A^{-1agger}|xranglerVert}{epsilon} to leading order when the solution norm is known. We then present a similarly simple solution norm estimator with the same asymptotic cost up to logarithmic factors. Our quantum linear system solvers thus substantially improve a recent algorithm of Li, enabling faster quantum linear system solving beyond the condition number.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.07691) | 2026-10-05
