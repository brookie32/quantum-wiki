---
title: "A Security-Aware PQC Benchmarking Framework on Dual-Core Xtensa Silicon"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2384"
summary: "Deploying memory-heavy post-quantum cryptography (PQC) at the smart grid edge threatens real-time substation determinism, directly conflicting with the strict le 3 ms GOOSE tripping window of the IEC "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Deploying memory-heavy post-quantum cryptography (PQC) at the smart grid edge threatens real-time substation determinism, directly conflicting with the strict le 3 ms GOOSE tripping window of the IEC 61850 standard. To resolve this architectural tension, we propose a security-aware, hardware-in-the-loop benchmarking framework on the dual-core Xtensa LX7 (ESP32-S3) SoC running FreeRTOS. To prevent inter-core resource contention, the framework employs an asymmetric task-isolation design, pinning cryptographic operations to Core 1 while leaving Core 0 responsive to line-rate grid interrupts. Additionally, we define a programmatic heap-auditing methodology to model how heap_4.c maps key-state allocations across physical DRAM fragments while preserving the primary 128 KB contiguous system heap. Finally, we formulate an analytical latency model of the external Octal-SPI PSRAM interface, mathematically characterizing the CPU stall overhead (C_{ext{stall}}) induced when side-channel masking forces secret polynomial shares to spill over the external bus during non-sequential Cooley-Tukey NTT strides. This framework provides a rigorous methodology to characterize micro-architectural trade-offs, enabling utility engineers to plan post-quantum migration pathways without violating real-time grid constraints.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2384) | 2026-10-06
