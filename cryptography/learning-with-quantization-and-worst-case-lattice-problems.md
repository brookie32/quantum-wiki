---
title: "Learning with Quantization and Worst Case Lattice Problems"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2613"
summary: "Motivated by the MAMBA proposals, we study the worst case hardness of learning with quantization (LWQ) with public dither. We allow any efficiently computable dither function and efficiently samplable"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Motivated by the MAMBA proposals, we study the worst case hardness of learning with quantization (LWQ) with public dither. We allow any efficiently computable dither function and efficiently samplable seed distribution; the matrix is uniform and independent of the secret and the seed. Using the randomized polar lattice quantizer of Lyu et al., we construct explicit families with polynomial power of two moduli. For the search family, polynomial time recovery of the uniformly chosen secret with inverse polynomial probability yields quantum polynomial time algorithms for the gap shortest vector problem (GapSVP) and the shortest independent vectors problem (SIVP) on arbitrary (n) dimensional lattices, with approximation factors (O(nlog n)) and (O(n(log n)^2)), respectively. Under stronger parameter conditions, a second family admits a decision reduction: a polynomial time algorithm with inverse polynomial distinguishing advantage yields quantum polynomial time algorithms for the same lattice problems with factors (O(n(log n)^3)) and (O(n(log n)^4)), respectively. Conditional on the public seed, the comparison output is uniform in the prescribed dither coset and independent of the matrix. We also examine extensions to learning with errors (LWE) with interval uniform errors, as arising in MAMBA Frost. We identify obstacles caused by deterministic quantization boundaries and give a local perturbation bound with explicit dependence on the number of observations. This analysis does not establish a complete worst case reduction for these errors or hardness at the concrete MAMBA parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2613) | 2026-10-23
