---
title: "Fully Homomorphic Encryption for Small Batches of Complex Numbers"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2513"
summary: "We propose a new approximate homomorphic encryption scheme to process small batches of complex numbers. Leveled operations are based on a new shaped rounding, whose error is a multiple of a fixed publ"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

We propose a new approximate homomorphic encryption scheme to process small batches of complex numbers. Leveled operations are based on a new shaped rounding, whose error is a multiple of a fixed public ring element g, small on the data slots and larger on the others. The unused slots form a guard band that is computed on but never decoded, and the polynomial scaling factor g^{-1}Delta generalizes the CKKS scaling factor, with g=1 recovering CKKS. Guard-domain bounds determine the scaling factor needed for stability, while a norm bound limits the precision gain for a given guard amplification. A replicated layout uses a unit from a small cyclotomic subring to preserve shaping under admissible rotations and traces. We give a native bootstrapping algorithm whose forward transform reads only data slots, and conversions to and from CKKS with shared keys. Security reduces to Ring-LWE with the same parameters as CKKS. In poulpy, at ring degree 2^{15} and parameters targeting 128-bit security, bootstrapping a ciphertext holding 16 or 64 values restores 21 levels and retains about 22.8 bits of minimum precision after 21 sequential products by fresh operands, while sparse CKKS supports only four levels at that degree and comparable precision. For these batch sizes, bootstrapping to restore 16 levels is about 3.6 times faster on one thread than sparse CKKS, which requires ring degree 2^{16}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2513) | 2026-10-16
