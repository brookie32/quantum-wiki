---
title: "Dimension Reduction for Theta Series of Ideal Lattices"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2028"
summary: "Theta series are fundamental functions that record lattice-vector lengths and connect lattice geometry with Gaussian quantities such as Gaussian mass and the smoothing parameter. For ideal lattices un"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Theta series are fundamental functions that record lattice-vector lengths and connect lattice geometry with Gaussian quantities such as Gaussian mass and the smoothing parameter. For ideal lattices under the canonical embedding, arithmetic coordinates are generally coupled, making fixed-coset theta-series evaluation and related Gaussian computations difficult in high dimensions. We show that an explicit, verifiable relative-basis condition yields an exact factorization of each fixed-coset theta series into lower-dimensional factors. For each fixed coset, when n = ℓ n₀, its n-dimensional theta-series computation is replaced by ℓ independent computations in dimension n₀. Equivalently, the canonical Gram matrix is block diagonal in the relative coordinates, and the factorization holds for every Gaussian parameter without approximation or a smoothing assumption. We verify the condition for several cyclotomic and non-cyclotomic extensions and derive explicit formulas for representative cyclotomic families. The same factorization gives lower-dimensional identities for Gaussian masses, independent Gaussian sampling within a fixed coset, and smoothing-parameter equations. It reduces the dimension of each coset calculation, while the outer sum over the residue classes in I_q remains unchanged. Our implementation achieves speedups of up to 335×, 215.45×, and 7.9× for fixed-coset theta-series evaluation, numerical smoothing-parameter evaluation, and sequential Gaussian sampling, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2028) | 2026-09-14
