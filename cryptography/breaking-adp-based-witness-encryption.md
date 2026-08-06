---
title: "Breaking ADP-Based Witness Encryption"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1594"
summary: "Witness encryption (WE) allows one party to encrypt a message under an arbitrary satisfiable circuit, so that anyone holding a satisfying input can decrypt. Efficient WE enables numerous modern applic"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Witness encryption (WE) allows one party to encrypt a message under an arbitrary satisfiable circuit, so that anyone holding a satisfying input can decrypt. Efficient WE enables numerous modern applications, such as identity-based and attribute-based encryption. Recent candidates for efficient WE base their security on rank properties of structured ciphertext matrices, which encode the validity of a given witness. This shrinks ciphertext sizes considerably compared to previous constructions, but rests on heuristic arguments rather than security reductions. We describe two attacks against two such constructions, namely the affine determinant program (ADP) construction from 2020 and its arithmetic extension, the AADP, from 2026. The first attack observes that for sparse circuits, the natural regime for both schemes, commutators formed from the public ciphertext matrices have unexpectedly low rank. Elementary linear algebra on these matrices then recovers the encrypted message directly from the public ciphertext, without knowledge of any witness, and hence breaks the security of both schemes. The second attack linearizes the nearly-skew-symmetric (NSS) variant of the ADP construction, recovering the encryption randomness and the message. To our knowledge, ours are the first attacks against these WE candidates, and we verify both in practice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1594) | 2026-08-03
