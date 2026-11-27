---
title: "Resource-Aware Deployment of NIST Additional PQC Signatures on Automotive ECUs"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3049"
summary: "The transition to Post-Quantum Cryptography (PQC) is vital for securing next-generation automotive architectures. However, deploying candidate algorithms from the NIST Round 3 Additional PQC Signature"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The transition to Post-Quantum Cryptography (PQC) is vital for securing next-generation automotive architectures. However, deploying candidate algorithms from the NIST Round 3 Additional PQC Signature track onto automotive ECUs, such as those based on the Infineon AURIX TC4 (TriCore v1.8 architecture), is severely obstructed by stringent hardware constraints. Standard reference implementations incur excessive stack and heap memory demands that exceed the limited capacity of the core's Data Scratchpad RAM (DSPR), triggering memory overflows and fundamentally jeopardizing real-time predictability and system dependability. To resolve this challenge, this paper presents a systematic software-level memory optimization approach framed as a resource-aware design-space exploration across the NIST Round 3 additional signature candidates. We strategically tailor memory layouts and buffer lifetimes to strictly satisfy the hard DSPR boundaries of the AURIX TC4 core, targeting a core RAM budget of at most 171.4,kB (with up to 139.4,kB stack and 32,kB heap) while offloading non-sensitive artifacts to global RAM, while preserving execution efficiency and worst-case timing behavior for time-critical automotive tasks. We evaluate our optimized implementations of MQOM, SDitH, MAYO, and QR-UOV on real automotive hardware, providing comprehensive empirical benchmarks of execution cycle counts and memory footprints against baseline implementations of ML-DSA and SLH-DSA. Our results identify MAYO-3 with our memory optimizations (MAYO-3-memopt) as the best-performing candidate overall, achieving keygen, sign, and verify times of 10.4,ms, 24.9,ms, and 11.5,ms, respectively, while candidates such as SLH-DSA and SDitH remain unsuitable for on-device signing due to prohibitive execution latency, despite fitting comfortably within the memory budget. Our findings show that not all NIST Round 3 additional signature candidates are equally suited to such constrained environments, but that with targeted memory optimization, at least some can be predictably integrated into memory-constrained automotive controllers without compromising real-time guarantees or system reliability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3049) | 2026-11-25
