---
title: "FN-DSA on Arm Cortex-M55: Revisiting a Floating-Point Lattice Signature with Native FP64 and Helium"
date: "2026-10-20"
updated: "2026-10-21"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2559"
summary: "FN-DSA has the shortest signatures among NIST's post-quantum signature standards, but on microcontrollers its signing is slow because the binary64 arithmetic it specifies is emulated with integer inst"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

FN-DSA has the shortest signatures among NIST's post-quantum signature standards, but on microcontrollers its signing is slow because the binary64 arithmetic it specifies is emulated with integer instructions. Previous speedups either change the arithmetic or the order of random sampling, so their signatures no longer match the known-answer tests (KATs) of the reference implementation, or rely on double-precision SIMD instructions that microcontrollers lack. The Arm Cortex-M55 has both a double-precision FPU and the M-Profile Vector Extension (MVE). On this core, we present the first FN-DSA implementation that, unlike these approaches, reproduces the KATs of the reference and runs in constant time, yet is faster than the reference. On MVE, we vectorize the NTTs with layer merging and the fixed-point FFT of key generation with split-word Q32 arithmetic on 32-bit lanes. On the FPU, bit-exact FP64 computes the FFT, LDL decomposition, split, merge and sampler of signing without changing any result, and exponent-normalized division turns the bit-by-bit divisions of key generation into a single VDIV.F64 with operand-independent latency. For Keccak, vectorized bit interleaving speeds up every permutation, and request-level batching processes four independent verification requests at once; SLOTHY then reschedules our MVE and Keccak assembly. Key generation, signing and verification become up to 1.23x, 1.93x and 1.30x faster than the reference on the same core, and batch verification of four signatures up to 1.75x faster. Overall, the FPU pays off where the reference emulates an operation with many integer instructions, and MVE where it already computes with integers or fixed point.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2559) | 2026-10-20
