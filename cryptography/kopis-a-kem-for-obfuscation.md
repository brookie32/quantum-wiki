---
title: "Kopis: A KEM for Obfuscation"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2268"
summary: "Password-authenticated key exchange (PAKE) and obfuscated key exchange (OKEX) are widely used protocols, appearing in passport access control, Tor's censorship evasion, and more. As quantum threats gr"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Password-authenticated key exchange (PAKE) and obfuscated key exchange (OKEX) are widely used protocols, appearing in passport access control, Tor's censorship evasion, and more. As quantum threats grow nearer, there have been an increasing number of proposals for post-quantum PAKE and OKEX. All such protocols are similar in that they build on a KEM, obfuscating public keys and/or ciphertexts sent over the wire, e.g., by adding a random mask or applying an ideal cipher. Many propose instantiation with ML-KEM, a NIST-standardized lattice-based KEM. Unfortunately, ML-KEM is a poor fit for these obfuscating protocols. The algebraic structure of ML-KEM public keys and ciphertexts means that obfuscating these values requires custom procedures for hash-to-vector, matrix expansion, serialization/deserialization, and randomized ciphertext decompression. In order to be broadly useful, these procedures also must be constant-time to prevent side channels and must be standardized to permit interoperability. No such set of procedures exists today. We observe that the barriers to instantiating PAKE and OKEX disappear if some of the KEM's algebraic structure is removed, i.e., if ML-KEM is replaced with a KEM whose public keys and ciphertexts appear to be uniform as bytestrings. In this work, we specify Kopis, a Module Learning-with-Rounding (MLWR) KEM with public keys and ciphertexts that are uniform as bytestrings. Kopis is intended to be a drop-in replacement for ML-KEM, in size, speed, and security. Kopis is nearly identical to Saber, a NIST PQC finalist, and thus inherits its years of cryptanalysis. We demonstrate that Kopis bears the security properties needed for use in various PAKE and OKEX schemes and provide a formally verified Rust implementation complete with portable, AVX2, and NEON backends, and a non-formally-verified C implementation for Cortex-M4. We perform benchmarks and find that Kopis is comparable to and often outperforms the fastest known ML-KEM implementations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2268) | 2026-09-29
