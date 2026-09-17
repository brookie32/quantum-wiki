---
title: "Silk: Computation-Efficient and Post-Quantum-Friendly Randomness Beacon"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2021"
summary: "Distributed randomness beacons enable mutually distrustful parties to jointly generate public randomness. Several existing beacons built from secret sharing use costly pairings or group operations to "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Distributed randomness beacons enable mutually distrustful parties to jointly generate public randomness. Several existing beacons built from secret sharing use costly pairings or group operations to verify shares. Their underlying discrete-logarithm assumptions are also vulnerable to quantum attacks. Moreover, running a separate Byzantine fault-tolerant (BFT) consensus instance for each output incurs repeated computation and communication costs, even when secrets are shared in batches. We present Silk, a computation-efficient, post-quantum-friendly and deterministic randomness beacon under partial synchrony. Silk's sharing protocol, Mulberry, realizes batched asynchronous verifiable secret sharing with partial output (bAVSS-PO), using hash-based share verification to reduce computation cost. Silk further amortizes BFT consensus across a batch of outputs, requiring only one BFT instance per batch. We establish Mulberry's bAVSS-PO properties and Silk's beacon properties under static corruption and the stated security assumptions. We implement Silk and Mulberry in Rust and evaluate their computation and communication costs. In WAN experiments with 121 replicas across eight AWS regions, Silk achieves a throughput of 5.414 outputs/s, 1.53× that of Rondo [NDSS'25] and 4.18× that of Spurt [IEEE S&P'22].

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2021) | 2026-09-14
