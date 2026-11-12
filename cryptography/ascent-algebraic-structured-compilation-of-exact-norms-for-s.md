---
title: "ASCENT: Algebraic Structured Compilation of Exact Norms for Succinct Lattice Proofs"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2853"
summary: "Norm bounds are semantic constraints in lattice cryptography: satisfying the modular equations is not enough unless the witness also satisfies the prescribed shortness bound. Existing norm reductions "
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

Norm bounds are semantic constraints in lattice cryptography: satisfying the modular equations is not enough unless the witness also satisfies the prescribed shortness bound. Existing norm reductions either introduce slack, or rely on general sumcheck style machinery whose transcript cost grows with the witness length. We introduce a reduction-of-knowledge compiler for exact ell_2-norm constraints. It compiles the original norm language for a committed lattice witness into a narrow structured relation consisting only of commitment-opening constraints, tensor-structured witness-public inner-product claims, and relaxed admissible shortness bounds. Exact norm soundness is enforced inside the reduction, so the remaining proof obligation is structured and algebraic. The compiler adds only O(1) prover-to-verifier communication, measured in ring and field elements, independent of the witness length N, and requires only O(log N) verifier work. The same techniques can also extend to a folding mechanism for broader quadratic relations, including R1CS-type circuits. At 128-bit security, our concrete estimates give transcripts of about 27.69KB for exact norm reduction and 27.75KB for the R1CS folding application. This is about 3--4imes smaller than LatticeFold+, about 2--3imes smaller than SALSAA, and remains close to the compact estimates reported for Cyclo.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2853) | 2026-11-10
