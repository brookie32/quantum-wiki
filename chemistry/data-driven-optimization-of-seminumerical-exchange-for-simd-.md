---
title: "Data-Driven Optimization of Seminumerical Exchange for SIMD CPUs"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21075"
summary: "arXiv:2610.21075v1 Announce Type: cross Abstract: We present a seminumerical exchange algorithm (SNK) based on the sn-LinK method [Laqua et al., J. Chem. Theory Comput. 16, 1456 (2020)], optimized for"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21075v1 Announce Type: cross Abstract: We present a seminumerical exchange algorithm (SNK) based on the sn-LinK method [Laqua et al., J. Chem. Theory Comput. 16, 1456 (2020)], optimized for modern multi-core central processing units with single instruction multiple data vector instructions and report its implementation into the Q-Chem quantum chemistry program. Vectorization and memory management strategies for the Boys function and 3-center-1-electron (3c1e) integral kernels are given. Several new considerations are made in the computation of the 3c1e integrals: the Head-Gordon Pople horizontal recurrence relations, same-center optimizations, and multishell optimizations, all implemented symbolically employing the SymPy symbolic algebra library and exported as optimized C++ code leveraging common-sub-expression elimination (CSE) optimization techniques. A general scheme for choosing optimal integral kernels is developed through rigorous timing benchmarks. The resulting implementation is tested against traditional 4c2e exchange for several systems and basis sets, showing 1-2 orders of magnitude speedups for systems of practically relevant sizes (100-500 atoms, 2000-10000 basis functions). For smaller molecules, comparisons are also made against the more efficient occ-RI-K method showing a break-even point around 50-100 atoms beyond which SNK dramatically outperforms due to its superior sub-quadratic (between linear and quadratic) time complexity as well as its effectively negligible memory demand.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21075) | 2026-10-16
