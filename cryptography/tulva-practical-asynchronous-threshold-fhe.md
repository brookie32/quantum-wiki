---
title: "Tulva: Practical Asynchronous Threshold FHE"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2485"
summary: "Fully homomorphic encryption (FHE) allows arbitrary computation over encrypted data, but its secret key presents a single point of failure which limits its applications. Threshold FHE patches this gap"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Fully homomorphic encryption (FHE) allows arbitrary computation over encrypted data, but its secret key presents a single point of failure which limits its applications. Threshold FHE patches this gap by distributing the secret key to K parties, requiring a threshold t leq K of them to cooperate for decryption. We focus on the asynchronous setting where a ciphertext can be decrypted by collecting decryption shares from any t parties who do not need to coordinate or even be online simultaneously. Asynchronous schemes are sought in applications such as privacy-preserving Ethereum Virtual Machines (EVM), processing of long-lived private data with quorum-based decryption and the thresholdisation of any cryptographic primitive in general. We present Tulva, a practical threshold FHE scheme which equips a base FHE scheme with an asynchronous threshold decryption mechanism in a modular way. Our scheme simultaneously (1) is compatible with virtually any base FHE scheme and leaves its ciphertexts unchanged apart from an appended random tag, (2) supports a wide range of threshold profiles (t,K) and ring degrees geq 256 with 6--25 bits partial decryption per plaintext bit, and (3) achieves security in the presence of partial decryption queries on challenge ciphertexts based on the standard LWE assumption. We provide an open-source implementation, benchmark its threshold decryption performance and evaluate the end-to-end costs for typical privacy-preserving EVM use cases. For 16-out-of-512 threshold and a publicly preprocessed ciphertext, computing secret-dependent partial decryption and public share combination requires only 3.7ms and 0.5ms, respectively, on commodity hardware. Compared with the state-of-the-art synchronous scheme [Zyskind et al., CCS'25], we replace their ciphertext-independent yet interactive preparation of secret-correlated randomness with a public, ciphertext-dependent 0.5s preprocessing step, eliminate interaction in the online phase while maintaining similar decryption time on the same machine, and support 32imes more total users.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2485) | 2026-10-14
