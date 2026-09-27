---
title: "Hidden-Bits Generators with Succinct CRS and Openings"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2212"
summary: "Feige, Lapidot, and Shamir [FOCS'90] presented a generic approach for building non-interactive zero-knowledge proofs via the notion of hidden-bits generators (HBGs). At a high level, an HBG allows a p"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Feige, Lapidot, and Shamir [FOCS'90] presented a generic approach for building non-interactive zero-knowledge proofs via the notion of hidden-bits generators (HBGs). At a high level, an HBG allows a prover to statistically commit to a k-bit pseudorandom string in the CRS model with a succinct commitment. Later, the prover can open this pseudorandom string at an arbitrary subset S subseteq [k] of positions by providing a proof pi_S. The hiding property requires that unopened positions remain pseudorandom. In this work, we study the efficiency of HBGs, focusing on direct constructions that make black-box use of cryptography. We obtain the following results: Succinct CRS: Assuming learning with errors (LWE), we construct an HBG with {em succinct} CRS of size mathsf{poly}(lambda,log k) for generating k hidden bits. This achieves an exponential improvement over a recent sequence of works by Waters [STOC'24], Branco et al.~[EUROCRYPT'25], and Waters, Wee, Wu~[EUROCRYPT'25] that required a CRS of size at least k dot mathsf{poly}(lambda). Batch opening: Using pairings, we construct an HBG with batch opening, where the proof size for any subset is mathsf{poly}(lambda). Previously, this was only known from the Naccache-Stern public-key cryptosystem [Groth, ASIACRYPT'10]. Succinct CRS and Batch opening: Assuming the hardness of RSA, we construct an HBG where both the CRS and the opening proof for any subset are of size mathsf{poly}(lambda,log k). No black-box constructions achieving this efficiency were previously known.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2212) | 2026-09-25
