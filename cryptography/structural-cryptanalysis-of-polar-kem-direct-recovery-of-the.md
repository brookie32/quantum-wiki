---
title: "Structural Cryptanalysis of Polar-KEM: Direct Recovery of the Secret Isometry"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2211"
summary: "Polar-KEM is a lattice-based key encapsulation mechanism submitted to the Next-generation Commercial Cryptographic Algorithms Program. Its security is claimed to rely on a lattice isomorphism problem "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Polar-KEM is a lattice-based key encapsulation mechanism submitted to the Next-generation Commercial Cryptographic Algorithms Program. Its security is claimed to rely on a lattice isomorphism problem over polar-code-defined Construction-D lattices. In its core key-generation algorithm, a polar lattice basis is constructed from a polar-code chain, reduced using LLL, and left-multiplied by a secret orthogonal matrix. The resulting matrix is published as the public key. We show that the key-generation procedure does not instantiate a general lattice isomorphism problem. The reduced reference basis is generated through a public chain of computations: public parameters determine frozen sets, the frozen sets determine a polar-code chain, the code chain determines a Construction-D basis, and the basis is then reduced by the public LLL procedure. Under the natural executable interpretation of the specification, an adversary can reproduce the same reduced basis. If the public key is ensuremath{B_{mathsf{pk}}=O B_{mathsf{red}}}, the secret orthogonal matrix is recovered by the single linear-algebra operation $ O=B_{mathsf{pk}}B_{mathsf{red}}^{-1}. $ The attack is polynomial time and recovers the exact secret isometry, or its numerical representation, without solving a shortest-vector problem or a general lattice isomorphism problem. We also examine the erasure parameter used by the frozen-set selection algorithm. The specification neither assigns it a concrete value nor defines it as a sampled secret with a distribution, encoding, entropy requirement, or storage mechanism. Treating this unspecified value or unspecified LLL tie-breaking as secret entropy would define a different scheme and would not repair the published construction. The present paper focuses on this direct basis-alignment weakness. Additional structural and correctness analyses are left to an extended version.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2211) | 2026-09-25
