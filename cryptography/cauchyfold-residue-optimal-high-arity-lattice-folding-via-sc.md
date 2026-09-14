---
title: "CauchyFold: Residue-Optimal High-Arity Lattice Folding via Scaled Cauchy Challenges"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2011"
summary: "A direct k-ary quadratic fold with one accumulator and k fresh inputs exposes k + inom{k}{2} mixed interactions. These terms need not be retained independently across the folding challenge. A companio"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

A direct k-ary quadratic fold with one accumulator and k fresh inputs exposes k + inom{k}{2} mixed interactions. These terms need not be retained independently across the folding challenge. A companion boundary analysis shows that, under the separation condition used here, at least rk mixed-state coordinates are required, where r is the dimension of the bilinear mixed-output space of the quadratic relation. Scaled Cauchy challenges attain this width: every pairwise product of challenge coefficients lies in the span of the k single-source coefficients. After clearing the common denominator, the entire mixed contribution becomes a degree-< k polynomial with k output-valued coefficients. CauchyFold turns this representation into a lattice-based folding protocol. The polynomial carrier is committed before the Cauchy challenge and determines the mixed part of the folded quadratic relation afterward. Field-level checks then reduce the folded relation to committed linear relations over lattice rings, with explicit norm bounds for the openings used in extraction. Rewinding follows the same transcript order. Compatible recoveries lead back to source openings, while incompatible recoveries yield a nonzero short kernel for the corresponding commitment matrix by comparing the original short responses before lifting modular inverses. Under the associated Module-SIS assumptions, this gives node-level knowledge soundness. We implement a complete k = 16 CauchyFold node under two parameter profiles, including commitment generation, folding, the finite reduction chain, serialization, parsing, and verifier replay. The resulting prover-to-verifier folding transcripts are 127,887 and 129,002 bytes, respectively, with the 16 fresh-input commitments accounted for separately.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2011) | 2026-09-14
