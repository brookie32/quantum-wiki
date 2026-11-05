---
title: "Keyber: Recovering the Signal by Amplifying the Noise in ML-KEM"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2766"
summary: "ML-KEM (FIPS 203) is now being deployed in real-world applications to provide security against adversaries with quantum computers. Therefore, the resistance of ML-KEM’s implementations to physical att"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

ML-KEM (FIPS 203) is now being deployed in real-world applications to provide security against adversaries with quantum computers. Therefore, the resistance of ML-KEM’s implementations to physical attacks requires thorough evaluation. So far, fault attacks on ML-KEM have targeted the decapsulation operation. The key generation operation has received little attention from a fault-attack perspective. In this work, we present Keyber, the first statistical ineffective fault attack (SIFA) on the key generation of ML-KEM. Keyber is a key-recovery attack that needs only a single fault in key generation. The fault adds a known value to the error vector. Thus, the public key becomes faulty, while the seed of the public matrix remains intact. Every subsequent decapsulation, therefore, carries a known induced error. The adversary encapsulates locally and keeps only ciphertexts whose induced error peaks at exactly one coefficient. A decapsulation failure can then be attributed to that coefficient. Each query yields one linear inequality on the secret key, with no further faults. We observe that approximately 0.2-27% of encapsulations are usable for different parameter sets of ML-KEM. The full secret key is recovered using up to 30,000 inequalities across all security levels. We also realise the attack for ML-KEM-512 on an ARM Cortex-M4 device using a single over-clock fault. We then recover the entire secret key end-to-end. A single fault in this one-time operation thus compromises the key for its entire lifetime. Protecting ML-KEM, therefore, demands hardening not only decapsulation, but also key generation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2766) | 2026-11-04
