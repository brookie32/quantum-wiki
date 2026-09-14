---
title: "Beyond DCR: HSS and PCFs from Subgroup Indistinguishability"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2006"
summary: "We construct homomorphic secret sharing (HSS) and pseudorandom correlation functions (PCFs) in a general group-theoretic framework, with security based on the subgroup indistinguishability (SgI) assum"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We construct homomorphic secret sharing (HSS) and pseudorandom correlation functions (PCFs) in a general group-theoretic framework, with security based on the subgroup indistinguishability (SgI) assumption introduced by Brakerski and Goldwasser (Crypto 2010). Under certain instantiations of this framework, SgI corresponds to decisional composite residuosity (DCR), but other instantiations are possible as well. Hence, our work expands the set of assumptions that imply HSS and PCFs. Our constructions crucially rely on the existence of an efficient distributed discrete logarithm (DDLog) algorithm for the utilized group. We construct a new DDLog algorithm that works in general groups as long as the order t of the base is smooth. In particular, our DDLog supports the prime-power case, which was previously an open problem. Moreover, we apply a divide-and-conquer optimization that significantly improves the performance from mathcal O(log^2 t / log log t) group operations (Abram et al., Crypto 2022) to mathcal O(log t log log t). Toward constructing PCFs, we introduce a new notion of public-coin subgroup indistinguishability (PC-SgI). We show that, in certain instantiations, SgI implies PC-SgI, so no new assumption is required. We then obtain PCFs for VOLE, OT, OLE, and degree-two correlations, all generically under PC-SgI. Our PCFs for OLE and degree-two correlations additionally rely on the sparse LPN assumption. Along the way, we discover and patch two security issues in prior work: first, an attack on decisional Diffie–Hellman (DDH) in the Joye–Libert instantiation by Abram et al. (Crypto 2022), and second, a flaw in the security proofs of optimized variants of the IKNP OT extension protocol and of many silent OT extension protocols.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2006) | 2026-09-13
