---
title: "Revisiting the Security of OleF, t-OleF, and OlÆF"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2823"
summary: "We revisit the security of OleF, t-OleF, and olaef and identify two independent security flaws. First, we establish a mask-compensation relation between continuation and termination processing in OleF"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

We revisit the security of OleF, t-OleF, and olaef and identify two independent security flaws. First, we establish a mask-compensation relation between continuation and termination processing in OleF and t-OleF. Exploiting this relation, we construct a two-encryption-query distinguisher against OleF with advantage 1-2^{-2n}. We further give two concrete AXU hash families for which the same attack applies to t-OleF, revealing flaws in the original DOSPRP and SPRTOP security proofs. We extend these attacks to olaef through valid encodings, breaking its privacy and integrity. In particular, the integrity forgery succeeds with probability 1 under full-domain verification when the target expansion length is 1 and extends to larger expansion lengths under suffix-only verification. Second, we refute the claimed ideal RUP integrity bound for variable-expansion online authenticated encryption. Even with an ideal tweakable online permutation, prior unverified decryption queries at smaller expansion lengths can reveal part of the target authentication suffix. We construct counterexamples showing that two such decryption queries and one forgery attempt achieve a success probability of 3/8, exceeding the claimed bound of 1/4. We also derive a general expression for the forgery success probability. Finally, we discuss the corresponding repairing

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2823) | 2026-11-08
