---
title: "DTRU: A Versatile, Compact, Simple, and Robust NTRU KEM with Double E_8 Encoding"
date: "2026-08-16"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1701"
summary: "Responding to China's 2025 call for commercial cryptographic standards mandating 128-bit, 256-bit, and 512-bit security (optional 384-bit), we propose DTRU, a versatile, compact, simple, and robust NT"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

Responding to China's 2025 call for commercial cryptographic standards mandating 128-bit, 256-bit, and 512-bit security (optional 384-bit), we propose DTRU, a versatile, compact, simple, and robust NTRU-based key encapsulation mechanism (KEM). Our principal design contribution is double E_8 encoding, which constructs 16-dimensional lattice codes from E_8 with low decoding complexity. We further provide a detailed analysis of decryption-failure probability under this encoding mechanism. DTRU's design achieves a careful balance among versatility, compactness, simplicity, and robustness. To accommodate diverse application requirements, it supports multiple ring structures, including power-of-two cyclotomic rings, tricyclotomic rings, and large-Galois-group prime-degree prime-ideal number fields (LPPNF). The double E_8 encoding enables DTRU to achieve enhanced error correction with compact bandwidth. The design prioritizes simplicity to facilitate deployment on low-power devices, achieved by eschewing additional coefficient compression techniques and redundant invertibility checks during key generation, while enabling circuit/code reuse. Security robustness is guaranteed through parameter selections that offer adequate security redundancy, mitigating potential cyclotomic ring risks via LPPNF, and precluding sparse noise distributions in the recommended parameter sets. Complementing our theoretical advances, we present comprehensive implementations of all the parameter sets with dedicated support for C, AVX2, and ARM platforms, leveraging architecture-specific optimizations. For example, compared to NTRU-HRSS and Kyber at the same security levels, our KEM is 49%-52% more compact and 3.84–15.69imes faster than NTRU-HRSS in the round-trip time of ephemeral key exchange, and is 7%-27% more compact and 1.05–1.32imes faster than Kyber.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1701) | 2026-08-16
