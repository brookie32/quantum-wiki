---
title: "Energy Consumption of Post-Quantum Cryptography on Constrained and General-Purpose Architectures"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2557"
summary: "With Q-day approaching, the transition to post-quantum cryptography (PQC) has begun, with governments across the US, UK and EU mandating migration to quantum-resistant standards. This paper benchmarks"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

With Q-day approaching, the transition to post-quantum cryptography (PQC) has begun, with governments across the US, UK and EU mandating migration to quantum-resistant standards. This paper benchmarks the three NIST-standardised PQC algorithms—FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA)—across key generation, signing and verification operations, measuring both computational performance and energy consumption on a range of constrained IoT-class devices, from the 32-bit Raspberry Pi 1 and Zero to the 64-bit Raspberry Pi 4, as well as commodity laptop hardware. Using the FNIRSI FNB58 USB power meter and OpenSSL 3.5, results show that ML-KEM and ML-DSA achieve energy and speed efficiency comparable to classical elliptic-curve cryptography across all tested architectures. However, SLH-DSA signing is inadvisable on constrained hardware: energy costs for SLH-DSA signing on 32-bit devices were up to 243% higher than on equivalent 64-bit hardware, making it impractical for resource-limited IoT deployments. These findings have direct implications for IoT security practitioners planning PQC migration.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2557) | 2026-10-19
