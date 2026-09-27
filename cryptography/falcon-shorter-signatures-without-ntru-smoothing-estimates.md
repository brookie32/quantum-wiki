---
title: "FALCON++: Shorter Signatures without NTRU Smoothing Estimates"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2226"
summary: "Falcon{} is a digital signature scheme based on NTRU lattices, known for its compact signatures. Its weak-smoothness variant, FalconWS{} (ASIACRYPT 2025), reduces signature sizes by allowing narrower "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Falcon{} is a digital signature scheme based on NTRU lattices, known for its compact signatures. Its weak-smoothness variant, FalconWS{} (ASIACRYPT 2025), reduces signature sizes by allowing narrower Gaussian sampling distributions. Further reductions require efficient sampling at narrower widths and a security analysis that accounts for the resulting distributions. We analyze the distribution of accepted preimages directly, without estimating the smoothing parameter of the NTRU lattice. We also modify the rejection-corrected Klein--GPV sampler to reduce sampling cost while controlling the resulting distributional error. We combine these results to construct FalconPP{}, a variant of Falcon{}, and give UF-CMA and SUF-CMA bounds in the classical random-oracle model. For ring degrees 512 and 1024, our estimates give signature sizes of 419 and 921 bytes, respectively. These are 37.09% and 28.05% smaller than Falcon{} signatures, and 11.60% and 5.92% smaller than the estimates for FalconWS{} at their respective parameter sets.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2226) | 2026-09-26
