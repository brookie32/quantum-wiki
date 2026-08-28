---
title: "Adaptive Multi-Algorithm Key Exchange for Quantum-Resilient Secure Communication: Dynamic Switching among QKD, Post-Quantum, and Classical Key Establishment with Entropy Fusion"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1803"
summary: "With the arrival of scalable quantum computers, classical key exchange protocols like RSA, elliptic-curve and finite-field Diffie-Hellman are vulnerable to harvest-now-decrypt-later attacks. Quantum k"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

With the arrival of scalable quantum computers, classical key exchange protocols like RSA, elliptic-curve and finite-field Diffie-Hellman are vulnerable to harvest-now-decrypt-later attacks. Quantum key distribution offers information-theoretic security but is sensitive to channel noise, loss, and distance, while post-quantum cryptography provides quantum resistance on conventional hardware at the cost of larger keys and a dependence on hardware computational strength. Existing hybrid defenses generally rely on static configurations that require manual intervention when channel conditions degrade, and no prior software-defined system performs real-time three-way switching among these approaches while preserving uninterrupted key availability. This paper presents an adaptive multi-algorithm key generation and exchange framework that dynamically selects among quantum key distribution (BB84), post-quantum cryptography (Kyber512, standardized as ML-KEM-512), and classical Diffie-Hellman according to real-time monitoring of the quantum bit error rate and network latency, fusing key material from all active sources through an HMAC-based key derivation stage. The framework was implemented and evaluated in a controlled simulation environment built on Qiskit, liboqs, and the Python cryptography library. Across all five operating modes it attained a 100% key-generation success rate, with the quantum-resistant modes sustaining a secret-key throughput of approximately 3 kbps at a 256-bit key size and mode transitions completing without loss of key availability. A Kruskal-Wallis test confirmed that the timing differences among modes were statistically significant (H = 133.32, p < 0.001), and the security model was placed on a formal footing using the robust key-combiner framework. The results indicate that adaptive multi-algorithm key exchange can substantially improve the quantum resilience of secure communication systems in terms of security, availability, and performance.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1803) | 2026-08-26
