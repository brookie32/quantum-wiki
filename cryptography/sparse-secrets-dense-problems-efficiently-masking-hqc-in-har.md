---
title: "Sparse Secrets, Dense Problems: Efficiently Masking HQC in Hardware"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2509"
summary: "HQC has recently been selected by NIST as a code-based alternative to ML-KEM and is currently undergoing standardization. While multiple timing and power side-channel attacks against HQC have been pre"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

HQC has recently been selected by NIST as a code-based alternative to ML-KEM and is currently undergoing standardization. While multiple timing and power side-channel attacks against HQC have been presented, application of masking has so far only been studied for software implementations. As part of this work, we close this gap by first proposing a novel masking technique for the sparse-dense vector multiplication, one of the core components in all HQC operations. We manage to securely exploit the sparsity of the secret operand using a mixed Boolean and arithmetic masking technique and prove its first-order security in the transition- and glitch-robust probing model as well as its PINI-composability. With the same memory width, our configurable and highly parallelizable masked design takes only 3% more clock cycles than a previous unprotected HQC multiplier. Furthermore, our technique requires only 81 bits of randomness per cycle, irrespective of its parallelism. However, like previous Rotate-and-Add constructions, it is vulnerable to profiled horizontal side-channel attacks, which recover all support indices within ±8 positions from 200 traces of our FPGA implementation despite TVLA showing no signs of leakage after 10 million traces. To prevent such attacks, we integrate efficient hiding countermeasures natively into the architecture of the multiplier, resulting in only 1.7% additional latency and moderate area overhead. Together with efficiently masked fixed-weight samplers and a masked decoder, we present the, to our knowledge, first fully masked hardware implementation of HQC, supporting first-order masked key generation, encapsulation, and decapsulation. Notably, our masked key generation is faster than a previous unprotected design from literature on an Artix-7 FPGA. Lastly, all modules of our complete designs show no signs of first-order leakage after 1 million traces.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2509) | 2026-10-16
