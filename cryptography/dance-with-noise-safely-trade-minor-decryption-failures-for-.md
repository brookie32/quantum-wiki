---
title: "Dance with Noise: Safely Trade Minor Decryption Failures for More Compact KEMs with Applications to IKEv2"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2201"
summary: "The standardization of post-quantum cryptography, notably ML-KEM, introduces a severe network bottleneck: large public keys and ciphertexts often exceed the Maximum Transmission Unit (MTU) limits of U"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

The standardization of post-quantum cryptography, notably ML-KEM, introduces a severe network bottleneck: large public keys and ciphertexts often exceed the Maximum Transmission Unit (MTU) limits of UDP-based protocols. This size explosion inevitably leads to unreliable IP-layer fragmentation or forces complex protocol workarounds. To overcome this, we propose a novel design philosophy for post-quantum Authenticated Key Exchange (AKE). We challenge the rigid cryptographic paradigm that mandates negligible decryption failure rates (DFR). By safely trading minor, manageable decryption failures for aggressive size compression, we drastically reduce the bandwidth footprint of lattice KEMs in ephemeral exchanges. We demonstrate this approach via a compact AKE for the Internet Key Exchange protocol (IKEv2). Integrating standard ML-KEM into IKEv2 currently necessitates the high-latency IKE_INTERMEDIATE exchange (RFC 9242) to distribute large payloads. By employing our compressed KEM design (800-byte public key, 928-byte ciphertext), the entire key exchange fits within the initial IKE_SA_INIT packet, completely eliminating the need for RFC 9242. To ensure that protocol aborts caused by decryption failures do not introduce security vulnerabilities, we formalize IND-CPAF (Indistinguishability under Chosen Plaintext Attack with Failures) to rigorously bound failure-dependent leakage. More importantly, we prove our IKEv2 instantiation still secure in the classical Canetti-Krawczyk model. Finally, our implementation in the strongSwan IPsec library confirms a fragmentation-free handshake: over 10,000 real-world connections, it achieves a 48.8 ms average setup time---matching classical ECDH---and keeps initial packets strictly under the 1280-byte IPv6 MTU, with merely a 0.002% retry rate.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2201) | 2026-09-24
