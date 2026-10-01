---
title: "A Fourier-Label Information-Loss Barrier for Dihedral Coset Algorithms"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40062"
summary: "arXiv:2609.40062v1 Announce Type: new Abstract: We establish a no-go theorem for a broad class of quantum algorithms for the dihedral coset problem (DCP). We consider the Fourier-sampling and subset-s"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40062v1 Announce Type: new Abstract: We establish a no-go theorem for a broad class of quantum algorithms for the dihedral coset problem (DCP). We consider the Fourier-sampling and subset-sum-measurement template proposed by Regev (SIAM Journal on Computing, 2004), which is one of the main approaches to solving DCP. Suppose that, after measuring the lower n-1 bits of the subset sum, the algorithm discards any omega(log n) bits from each of the Fourier labels. Then we prove that the algorithm cannot succeed in solving DCP. This shows that any algorithm following this template must make extensive use of the Fourier labels, and thus serves as a useful guide for developing algorithms for DCP. As a main application, we show that the recent algorithm by Simon (IACR ePrint:2026/1591, August 11 2026) does not solve DCP. We show that after the subset-sum measurement, this algorithm can be implemented (up to exponentially-small error) using only the most-significant third of the Fourier labels, and is therefore subject to our general no-go theorem. To help with verifiability, we release Lean 4 code for our results.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40062) | 2026-10-01
