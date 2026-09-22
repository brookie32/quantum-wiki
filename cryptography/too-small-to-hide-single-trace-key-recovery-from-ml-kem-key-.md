---
title: "Too Small to Hide: Single-Trace Key Recovery from  ML-KEM Key Generation"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2137"
summary: "Key generation in ML-KEM (CRYSTALS-Kyber) samples a short secret from a centered binomial distribution (CBD) and immediately transforms it with the number-theoretic transform (NTT). Each execution dra"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Key generation in ML-KEM (CRYSTALS-Kyber) samples a short secret from a centered binomial distribution (CBD) and immediately transforms it with the number-theoretic transform (NTT). Each execution draws fresh randomness, so an attacker obtains a single trace and cannot average. We show that one power trace of the optimized pqm4 implementation on an Arm Cortex-M4 suffices, and that the two operations leak complementary information. The CBD sampler stores each coefficient as a signed 16-bit two's-complement word, which reveals its sign almost without error but too little about its magnitude to yield long error-free hint sets. The missing magnitude leaks in the subsequent NTT, where coefficients are multiplied by public twiddle factors. Used as hints in a primal lattice attack, the combined leakage reduces the estimated BKZ block size for ML-KEM-768 from 624 to 129, corresponding to 2^{182.2} and 2^{37.7} in the core-SVP model. A control experiment shows that the same NTT code leaks the Hamming weight of a near-uniform operand as strongly as that of the secret, yet reveals almost nothing about its value. What makes a coefficient vulnerable is how few values it can take, not how small it is. That points to a countermeasure inside the CBD sampler. Each sample v is stored as a random representative widetilde v = v + rq of its residue class, with r nonzero, so the NTT and all later code run unchanged. This q-randomization drives the sign leakage to the noise floor, reduces the NTT magnitude leakage by 4.5imes, and raises the block size from 129 back to 611, about four bits of estimated security lost instead of more than 140. The sampler grows by 937 bytes of firmware.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2137) | 2026-09-21
