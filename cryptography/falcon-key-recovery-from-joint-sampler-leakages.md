---
title: "Falcon Key Recovery from Joint Sampler Leakages"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2656"
summary: "Falcon and the forthcoming FN-DSA standard based on it generate signatures via discrete Gaussian sampling, during which power consumption leaks information about secret-dependent intermediate values. "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Falcon and the forthcoming FN-DSA standard based on it generate signatures via discrete Gaussian sampling, during which power consumption leaks information about secret-dependent intermediate values. While prior attacks exploit sampler leakages individually or in pairs, we present a unified key-recovery framework that fuses three observations from each SamplerZ call: the signed-exponent class e(k) of the integer center, the random-sign bit b, and a multi-class proposal magnitude z0. These fused observations define magnitude-preserving intervals or rays for accepted sampler outputs. Leveraging an exact public linear relation that holds in the absence of modular wraparound, we map these candidate sets directly into slab and halfspace constraints on the secret key. The resulting system is solved via smooth softplus interval regression and bounded integer reconstruction with public-key validation, entirely bypassing computationally intensive lattice reductions such as LLL or BKZ. For PQClean Falcon-512 running at-O3 on an ARM Cortex-M4, our 17-class center classifier achieves 99.34% call-level accuracy on held-out test signatures from the profiling keys. The resulting attack recovers all 50 disjoint evaluation keys using at most 34 signatures (median 11), with a median post-classification key-recovery runtime of 17.54s per key. Furthermore, on c-fn-dsa, where center conversion relies on a single constant-time CLZ instruction, a reduced-resolution 7-class classifier combined with proposal leakage still recovers 38 of 50 keys within 200 signatures. These findings demonstrate that instruction-level normalization alone cannot prevent key recovery, underscoring that side-channel countermeasures for FN-DSA must protect all sampler leakage channels jointly.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2656) | 2026-10-27
