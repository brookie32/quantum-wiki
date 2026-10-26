---
title: "Maximum-Likelihood Decoding of Gabidulin Codes Is NP-Hard Even in Dimension One"
date: "2026-10-25"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2637"
summary: "Fix a prime power q . We prove that deciding whether a received word y ∈ F^n_qm lies at rank distance at most n − 2 from the one-dimensional Gabidulin code {λg : λ in Fqm } is NP-complete. Thus maximu"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Fix a prime power q . We prove that deciding whether a received word y ∈ F^n_qm lies at rank distance at most n − 2 from the one-dimensional Gabidulin code {λg : λ in Fqm } is NP-complete. Thus maximum-likelihood decoding of Gabidulin codes is NP-hard even for k = 1, an analogue of the Guruswami-Vardy theorem for Reed-Solomon codes. In the Hamming metric, by contrast, hardness at this radius requires the dimension to grow with the length, as in the Guruswami Vardy theorem. The reduction is deterministic; consequently Rank Syndrome Decoding (RSD) and Rank Minimum Distance (RMD) for Fqm -linear codes are NP-complete under deterministic polynomial reductions, whereas the previously known reduction was randomized. The proof goes through a pivot problem that we introduce, Twisted Square Membership (TSM): given Fq -subspaces U, W in FqN , decide whether some non-zero a ∈ U satisfies a^(q+1) in W . Quadratic systems in d unknowns are encoded into TSM, then TSM into Gabidulin decoding. The last step views the received word as an Fq -linear map and decoding at radius n − 2 as the search for an Fq -plane on which it acts as a scalar. With support U + τ W in a cubic extension and map a + τ b → a^(q^2) + τ b^q , two Frobenius twists force solution planes to encode the relation a^(q+1) ∈ W . All constructions are explicit and polynomial, with N = O(qd^2 ), n ≤ N + d, and m = 3N .

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2637) | 2026-10-25
