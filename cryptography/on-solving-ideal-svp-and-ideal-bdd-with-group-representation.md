---
title: "On Solving Ideal-SVP and Ideal-BDD with Group Representations"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2042"
summary: "Ideal lattices over number fields play a central role in post-quantum cryptography, as evidenced by the NIST-standardized schemes Kyber and Dilithium. Understanding the hardness of ideal-lattice probl"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Ideal lattices over number fields play a central role in post-quantum cryptography, as evidenced by the NIST-standardized schemes Kyber and Dilithium. Understanding the hardness of ideal-lattice problems such as the Unique Shortest Vector Problem (Id-uSVP) and Bounded Distance Decoding (Id-BDD) is therefore essential. Recent works have shown that certain algebraic symmetries can significantly reduce the dimension of the Ideal-SVP problem. In particular, subfield attacks exploit the decomposition group to solve SVP in a smaller subfield. However, existing reductions are limited to SVP and rely on multiplicatively closed substructures. In this work, we introduce a representation-theoretic framework for solving Id-uSVP and Id-BDD. Let K/Q be an abelian extension whose Galois group G is known, and let I be an integral ideal of K stabilized by a nontrivial subgroup Hsubseteq G. We use the irreducible rational representations of H to construct scaled projection operators q_i that decompose K into a direct sum of linear subspaces V_i. Applying these operators to I yields low-dimensional lattices I_i = q_i(I). We show that an Id-BDD instance (t,I) can be solved by solving independent BDD instances on the I_i's and recombining the solutions, provided the target is within a distance bounded by lambda_1(I)/(2|H|^2). For Id-uSVP, we prove that under mild uniqueness conditions a shortest vector of I lies in at least one of the nonzero I_i. In cyclotomic fields, the rotation property gives two stronger results: (i) every nonzero I_i contains a shortest vector of I, so solving SVP on the lowest-rank nonzero I_i suffices; and (ii) BDD is further accelerated by reducing a single instance to n low-rank instances on the same lowest-rank nonzero I_i. To the best of our knowledge, our approach is the first to employ group representation theory directly in lattice cryptanalysis. It addresses the limitation of previous subfield methods that they cannot solve BDD, removes the need for multiplicative closedness, and remains at least as efficient as prior SVP reductions. These results refine the understanding of the hardness of structured lattice problems and have implications for the security analysis of cryptosystems with additional algebraic structure.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2042) | 2026-09-15
