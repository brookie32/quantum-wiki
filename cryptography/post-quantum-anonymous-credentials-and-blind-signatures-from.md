---
title: "Post-Quantum Anonymous Credentials and Blind Signatures from ML-DSA"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2961"
summary: "Anonymous credentials allow users to prove properties of their identity, such as their age or nationality, without revealing any other personal information. For institutional deployment, it is particu"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Anonymous credentials allow users to prove properties of their identity, such as their age or nationality, without revealing any other personal information. For institutional deployment, it is particularly desirable to build such systems from standardized post-quantum signature schemes, allowing issuers to retain their existing signing procedures. However, proving knowledge of a valid ML-DSA signature in zero knowledge is costly: ML-DSA verification mixes binary operations, notably SHAKE/Keccak, with arithmetic over F_q, together with sampling and decomposition procedures that are hard to arithmetize efficiently. As a result, recent concurrent works produce large proofs, ranging from several hundred kilobytes to approximately 1 MB. In this paper, we present an efficient zero-knowledge proof of knowledge (ZK-PoK) of an ML-DSA signature. Our approach separates the binary and prime-field computations and relies on SmallWood+, a hash-based zero-knowledge argument system built on the sum-check and GKR protocols. We use it to build blind signatures and anonymous credentials from ML-DSA. For ML-DSA-44, our ZK-PoK of a valid signature on a 32-byte private message has a proof size of about 87 KB. Our blind signature, which essentially consists of such a ZK-PoK, achieves a similar size of about 88 KB. We apply our construction to ISO/IEC 18013-5 mdoc credentials instantiated with ML-DSA, including device binding: the holder proves knowledge of an issuer-signed credential and of a device signature on the verifier's challenge under the certified, hidden device key. The resulting presentation proofs have a size of about 200 KB, compared with about 458 KB in a recent concurrent work. Our proof-of-concept implementation, partly written in Python and not yet optimized, generates the ZK-PoK and the blind signature in about 2 seconds and a credential presentation in about 15 seconds; we expect an optimized implementation to be significantly faster.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2961) | 2026-11-20
