---
title: "FixSampZ: A Fixed-Point Hardware-Efficient Discrete Gaussian Sampler for Falcon Signatures"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2731"
summary: "Falcon, a NIST-standardized post-quantum signature algorithm, offers compact signatures but relies on hardware-intensive floating-point arithmetic. Building on recent theoretical fixed-point formulati"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Falcon, a NIST-standardized post-quantum signature algorithm, offers compact signatures but relies on hardware-intensive floating-point arithmetic. Building on recent theoretical fixed-point formulations, we present a completely floating-point-free hardware architecture for SamplerZ, Falcon’s primary signing bottleneck. By utilizing zero-cost hardware bit-sliced retagging of fixed-point data, which software avoids due to instruction overheads, we enforce tighter data formats at every stage boundary without area or latency penalties. Furthermore, executing floor functions as trivial two's-complement arithmetic right shifts eliminates the complex floor-prediction and redundant data-paths required by floating-point designs. Implemented on UltraScale+ FPGA, our fixed-point sampler exactly matches all 1,024 official test vectors and requires 38% fewer LUTs, 21% less FFs and 36% less DSPs compared to the floating-point baseline, with 21% fewer cycles at a higher clock frequency. We also demonstrate that substituting the baseline ChaCha20 PRNG with lightweight NIST-standardized Ascon-XOF128 achieves further 2-3 × hardware resource savings with zero sampling latency overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2731) | 2026-11-03
