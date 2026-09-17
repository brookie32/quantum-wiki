---
title: "The Residue Is the Resource: Exact Fresh-State Complexity, Reconstruction Limits, and Optimal Challenge Design in Folding"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2019"
summary: "Folding protocols must preserve enough input-dependent information before a public challenge is known to support every required postchallenge output. We identify the representation-independent amount "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Folding protocols must preserve enough input-dependent information before a public challenge is known to support every required postchallenge output. We identify the representation-independent amount of fresh scalar information required at such a boundary, after crediting declared-free functions and information already supplied by the incoming state. Over a field, this exact retained width is the dimension of the residual target: the supported scalar-output directions that survive those credits. The invariant depends on the admissible semantic domain and actual challenge support. With a nonzero supported challenge and (k^2) distinct evaluation points, coordinatewise multiplication has direct width (k^2) on the full product domain but only (2k-1) on the corresponding Reed–Solomon domain. For bilinear maps over finite fields with independent uniform inputs, we characterize optimal reconstruction below the exact width through the ranks of missing scalar forms. Bilinear side information introduces a compatibility constraint on their representatives, so equal exact widths can yield different reconstruction profiles; for polynomial multiplication, this geometry determines the first three deficits exactly. Finally, for a direct homogeneous quadratic fold with one accumulator and (k) fresh sources on the full product domain, the fixed-family width is (r d_a), where (r) is the mixed-output span dimension and (d_a) is the dimension of the span, on the actual challenge support, of the weights (a_i) and pairwise products (a_i a_j) for (i<j). Diagonal separation forces (d_a ge k) and support size at least (2k+1); scaled-Cauchy challenges attain (d_a=k) and yield a degree-(<k), mixed-output-valued carrier occupying (rk) field coordinates.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2019) | 2026-09-14
