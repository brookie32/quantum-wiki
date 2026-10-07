---
title: "Deploying Native-Rust KpqC: Pluggable Post-Quantum KEMs and Signatures across TLS, Space Links, and the OQS Ecosystem"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2342"
summary: "Post-quantum migration is no longer only an algorithm problem but a deployment problem: standardized schemes must be dropped into real protocol stacks, on real (often resource-constrained) targets, wi"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Post-quantum migration is no longer only an algorithm problem but a deployment problem: standardized schemes must be dropped into real protocol stacks, on real (often resource-constrained) targets, without giving up memory safety. The Korean Post-Quantum Cryptography (KpqC) competition standardized two KEMs (NTRU+, SMAUG-T) and two signature schemes (HAETAE, AIMer), distributed as memory-unsafe C. Building on our native-Rust KpqC implementation, we expose the schemes through a single pluggable provider and evaluate them across three deployment front-ends: (i) a rustls TLS 1.3 key-exchange group, (ii) an Open Quantum Safe (OQS) compatible C ABI that lets the native-Rust code stand in for the C reference behind the liboqs API, and (iii) an analytical CCSDS/SDLS satellite constrained-link model. All three are demonstrated end-to-end: a complete TLS 1.3 handshake using only a KpqC KEM for key establishment, a C program that drives the Rust KEMs and signatures through the OQS-shaped ABI, and a fragmentation/latency analysis over illustrative LEO/GEO link profiles. This work extends our earlier C/OQS-OpenSSL TLS benchmark of KpqC (Sim et al.) with a memory-safe Rust implementation, an explicit memory-footprint axis, and deployment breadth beyond localhost/LAN. On a constrained space link, the compact SMAUG-T key exchanges (SMAUG-TiMER 1280 B, SMAUG-T1 1344 B) are smaller and faster than ML-KEM-768 (2272 B). All seven KpqC KEM parameter sets and four signatures (AIMer and HAETAE modes 2/3/5) are demonstrated across the three front-ends. We further give NTRU+ a full memory-optimized build for all three sets, byte-identical and KAT-verified, that cuts peak stack by up to 25% at no measurable time cost (≈ 0.99× handshake latency).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2342) | 2026-10-05
