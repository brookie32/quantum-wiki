---
title: "Importance-Sampling Estimation of Gaussian Molecular Shape Overlap: Exact Union Volumes and Confidence-Bounded Virtual Screening"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.20766"
summary: "arXiv:2607.20766v1 Announce Type: new Abstract: Gaussian descriptions of molecular shape underpin 3D shape-based virtual screening, but existing methods evaluate Gaussian overlap analytically. The wid"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20766v1 Announce Type: new Abstract: Gaussian descriptions of molecular shape underpin 3D shape-based virtual screening, but existing methods evaluate Gaussian overlap analytically. The widely used first-order approximation is fast but systematically overestimates overlap, whereas the exact molecular volume requires a combinatorial inclusion-exclusion expansion. We introduce the first stochastic estimator of Gaussian shape overlap: an unbiased Monte Carlo method that importance-samples directly from a molecule's Gaussian mixture. The estimator reproduces analytic overlap without bias and extends to the exact union volume of all inclusion-exclusion orders with O(N) cost per sample. On drug-like molecules, the union estimator matches high-resolution grid quadrature with a mean relative error of 0.07 percent, while the first-order approximation overestimates the true union volume by 3.4x on average. The estimator provides analytic standard errors, enabling confidence-bounded screening that reduces sampling by 94 percent while preserving ranking. Implemented in JAX, it is fully differentiable and supports gradient-based rigid alignment on CPU, GPU, and TPU. On the DUD-E and LIT-PCBA benchmarks, the method achieves shape-only enrichment comparable to existing single-conformer approaches while additionally providing unbiased absolute volumes and uncertainty estimates.



## Related
- [[from-populations-to-absolute-binding-affinities-in-molecular|From populations to absolute binding affinities in molecular simulations: exact volumetric terms and practical estimators]]
- [[uncertainty-quantification-for-free-energy-calculations-by-g|Uncertainty Quantification for Free Energy Calculations by Generalized Hierarchical Bayesian Inference]]
- [[adaptive-inference-and-convergence-of-free-energy-landscapes|Adaptive Inference and Convergence of Free Energy Landscapes Using Non-parametric Bayesian Enhanced Sampling]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.20766) | 2026-07-24
