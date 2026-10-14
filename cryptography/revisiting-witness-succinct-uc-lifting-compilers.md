---
title: "Revisiting Witness-Succinct UC-lifting Compilers"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2453"
summary: "Zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) are increasingly used within larger cryptographic protocols, making security under composition essential. Generic compilation "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) are increasingly used within larger cryptographic protocols, making security under composition essential. Generic compilation to Universal Composability (UC) requires straight-line, black-box extraction while preserving succinctness and controlling prover cost. We introduce verifiable reconstructible straightline codes (VRSCs), a primitive that separates public hiding, transcript-based reconstruction, binding, and proof non-rerandomizability. This abstraction exposes a missing security requirement in the witness-succinct UC compiler of Ganesh et al. (EUROCRYPT 2023). Permuting previously revealed evaluation openings produces a fresh accepting proof with non-negligible probability without violating non-extrapolation, invalidating the claimed simulation argument. Proof non-rerandomizability captures this attack at the certificate level. Our construction prevents transfers between repetitions through verifier-enforced disjoint evaluation domains. We formulate a generic UC lifting theorem in terms of VRSCs and give a pairing-based instantiation using a Fischlin-style search over authenticated codeword symbols. Structured Reed--Solomon encoding and jointly computed KZG openings reduce certificate-generation work from quadratic to (O_{lambda}(nlog n)), where (n) is the witness size. Only a linear-time encoding check enters the underlying SNARK circuit. To our knowledge, this is the first generic UC lifting compiler that simultaneously achieves quasi-linear prover overhead and constant additional proof size and verification work with respect to the witness size.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2453) | 2026-10-12
