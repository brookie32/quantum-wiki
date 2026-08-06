---
title: "Power side-channel leakage distinguishers on LESSv2.0 - Exploiting sparse columns in Gaussian Elimination"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1601"
summary: "We present the first passive side-channel distinguisher on LESSv2.0, a second-round candidate in NIST’s call for additional post-quantum digital signature schemes. We target the Gaussian elimination a"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

We present the first passive side-channel distinguisher on LESSv2.0, a second-round candidate in NIST’s call for additional post-quantum digital signature schemes. We target the Gaussian elimination at the core of LESS and and present a method to exploit algorithmic leakage arising from the manipulation of sparse versus dense columns. We show that this leakage, while trivially available in non-constant-time implementations, also persists in constant-time implementations and can be exploited using a distinguisher. Concretely, the proposed attack relies only on distinguishing zero-valued computations from random ones that are repeatedly evaluated during the computation, leading to a large attack surface and making the attack robust to noise. Through simulation, we experimentally show that the required number of observed signatures lies between 300 and 2357 depending on the parameter set. This relatively large number is due to the targeted information being inherently noisy, leading to a correlation-based key recovery attack, even with noiseless leakage. Furthermore, we discuss three common countermeasures: first-order masking, shuffling and blinding. Finally, we validate our approach on implementations with and without masking by showing the presence of leakage on a physical target.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1601) | 2026-08-04
