---
title: "Stay in Your Lane: Fast Arithmetic over Large Finite Rings with CKKS"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2190"
summary: "Recent CKKS-based constructions support homomorphic arithmetic modulo powers of two and more general moduli. We explore a complementary tradeoff: using polynomial rings native to CKKS simplifies arith"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Recent CKKS-based constructions support homomorphic arithmetic modulo powers of two and more general moduli. We explore a complementary tradeoff: using polynomial rings native to CKKS simplifies arithmetic and refreshing but restricts the message spaces. Building on Kim's interpretation of GBFV ciphertexts as CKKS ciphertexts, we use the decomposition R[X]/langle X^N+1rangle ong(R[X]/langle X^n+1rangle)^{N/n} into N/n polynomial lanes, where 2leq nleq N is a power of two dividing the RLWE dimension N. Following GBFV, each lane represents a message in Z[X]/langle X^n+1,trangle, where t is coprime to X^n+1 over Q. These message spaces include Z_{eta^n+1} for t=X-eta, products of modular integer rings, specific 128-, 256-, 512-, and 1024-bit prime fields, and extension fields such as F_{5^{16}}, F_{17^4}, and F_{37^{32}}. Unlike the triangle encoding of Gao and Zheng's construction (GZ), our lanes occur at intermediate stages of conventional CoeffToSlot and SlotToCoeff transformations, avoiding additional encoding-specific linear maps. We thus "stay in our lane" by performing arithmetic and refreshing within CKKS-native polynomial rings. Our arithmetic bootstrapping restores ciphertext levels, bounds polynomial representatives, and reduces approximation error. At N=2^{16}, it takes less than 4.5 seconds in every tested configuration, with little variation across t and n. Comparing our arithmetic modulo 2^n+1 with GZ's arithmetic modulo 2^n, same-machine, same-library experiments show a 2.2imes–3.8imes speedup for 2^3leq nleq 2^6. Our bootstrapping time remains nearly constant as n grows, whereas GZ's dense encoding-specific transformations increase its cost and, at larger n, exceed available memory, preventing direct comparisons. At n=2^{14}, extrapolating GZ's published timings suggests a 26imes speedup.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2190) | 2026-09-23
