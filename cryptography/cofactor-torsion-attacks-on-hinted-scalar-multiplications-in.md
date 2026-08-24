---
title: "Cofactor-torsion attacks on hinted scalar multiplications in SNARK circuits"
date: "2026-08-22"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1776"
summary: "Proving an elliptic curve scalar multiplication [k]P= Q ∈ E(Fp) inside a SNARK is much cheaper when the output Q is hinted by the prover and only verified in-circuit, rather than recomputed. The recen"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Proving an elliptic curve scalar multiplication [k]P= Q ∈ E(Fp) inside a SNARK is much cheaper when the output Q is hinted by the prover and only verified in-circuit, rather than recomputed. The recent scalar multiplication techniques of Eagen, El Housni, Masson and Piellard (Latincrypt 2025) certify a hinted Q with a short lattice reduction (fraction) decomposition of the scalar and a single group identity, and yield the fastest known in-circuit scalar multiplications. We observe that the soundness of this whole family rests on an implicit prime-order hypothesis: the certifying identity is checked over the full group E(Fp), and only when E(Fp) has trivial cofactor does it force Q into the prime-order subgroup. On cofactor curves the certification is unsound. We give two concrete forgery classes against these hinted gadgets: an any-scalar attack that, for a target scalar fixed by the statement, adapts the decomposition so a small rational torsion point cancels from the identity; and a chosen-scalar attack that vanishes the output-side coefficients modulo a small cofactor prime and solves for the scalar afterwards. Both make the gadget accept Q′ = [k]P + T for a non-zero torsion point T as if it were [k]P. We quantify the reachable torsion in terms of the sub-scalar range bound and validate the attacks on widely deployed curves such as BLS12-381, BN254 and BW6-761. The straightforward fix is to check that Q lies in the subgroup but is expensive. We propose a cheaper one that binds the hinted output through a hinted preimage, with the minimal such constant that suffices against each attack model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1776) | 2026-08-22
