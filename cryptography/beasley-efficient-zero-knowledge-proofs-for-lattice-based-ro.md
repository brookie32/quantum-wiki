---
title: "Beasley: Efficient Zero-Knowledge Proofs for Lattice-based Round-Optimal Oblivious Pseudorandom Functions"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2010"
summary: "Verifiable oblivious pseudorandom functions (VOPRFs) enable a client to evaluate a pseudorandom function on a private input under a server-held key while verifying that the server evaluated the functi"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Verifiable oblivious pseudorandom functions (VOPRFs) enable a client to evaluate a pseudorandom function on a private input under a server-held key while verifying that the server evaluated the function honestly using its committed key. Existing practical VOPRFs rely mainly on assumptions that are vulnerable to quantum attacks. Prior lattice-based constructions achieving both round optimality and malicious security have remained theoretical proposals without concrete implementations, largely because proving the correct evaluation of the underlying lattice-based PRF in zero-knowledge is prohibitively expensive. We present Beasley, the first concrete prototype implementation of a round-optimal, maliciously secure, lattice-based VOPRF from standard lattice assumptions. Beasley builds upon the framework of Albrecht et al. (PKC 2021) and LeOPaRd (CRYPTO 2026), introducing two core optimizations: First, we generalize the Boneh-Lewi-Montgomery-Raghunathan (BLMR13) pseudorandom function where each step processes w input bits simultaneously; instantiated with w=4 in our implementation, this reduces evaluation depth and running time by a factor of 4 without impact on security; Second, we replace LaBRADOR-style proofs with a ring-switching sumcheck protocol and develop an efficient arithmetization of the OPRF computation. This design allows us to use a relatively large ring dimension of 512, simultaneously delivering fast ring arithmetic and compact keys with efficient exact range proofs without security-degrading slack. Benchmarked on a commodity consumer laptop using a single core with AVX2, Beasley generates the full client request and NIZK proof in 520 ms, with a server verification time of 15.3 ms, a peak RAM footprint of 113.7 MB, and a client communication size of 109 KB. The NIZK proof itself is 75.4 KB. Our results demonstrate that maliciously secure, lattice-based VOPRFs can achieve practical performance for real-world applications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2010) | 2026-09-13
