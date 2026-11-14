---
title: "Triads below the ISA: Optimizing Cryptographic Software in CPU Microcode"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2874"
summary: "Cryptographic software is typically optimized for the instruction set architecture exposed by the processor. Modern processors, however, contain deeper execution layers with computational capabilities"
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

Cryptographic software is typically optimized for the instruction set architecture exposed by the processor. Modern processors, however, contain deeper execution layers with computational capabilities and constraints that differ from those of the instruction set architecture (ISA). This work explores the programmable microcode layer in x86 as an implementation target. We characterize the microcode domain as a distinct target architecture for cryptographic computation and adapt implementations to the state, operations, invocation interface, capacity, and scheduling resources it exposes. We instantiate this methodology on Intel Goldmont with Keccak f [1600] and X25519, two case studies with substantially different computational structures. Our Keccak implementation reduces permutation latency by 7.36% relative to the fastest native implementation in our comparison, with the improvement remaining visible in incomplete SHA3-256 computations. For X25519, our microcode multiplication and squaring kernels free the multiplier from fixed operand registers and restrictive carry-flag semantics, outperforming the native implementations we evaluate. The resulting complete X25519 implementation requires 7.3% fewer cycles than s2n-bignum and 9.8% fewer cycles than OpenSSL. Together, these results demonstrate that looking below the ISA exposes a distinct design space for cryptographic implementation and provide a systematic methodology for exploring it.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2874) | 2026-11-12
