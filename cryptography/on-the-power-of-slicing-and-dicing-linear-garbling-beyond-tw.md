---
title: "On the Power of Slicing and Dicing: Linear Garbling Beyond Two-Input Gates"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2200"
summary: "Communication is a central efficiency bottleneck in garbled circuits. Rosulek and Roy (CRYPTO 2021) introduced slicing and dicing, obtaining a garbling scheme in which XOR gates require no communicati"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Communication is a central efficiency bottleneck in garbled circuits. Rosulek and Roy (CRYPTO 2021) introduced slicing and dicing, obtaining a garbling scheme in which XOR gates require no communication and each two-input AND gate costs (1.5lambda + 5) bits, where (lambda) is the security parameter. In this work, we investigate the power of these techniques for garbling gates of larger fan-in. We develop a linear-algebraic framework that yields concrete constructions and asymptotic bounds. For three- and four-input gates, we obtain constructions with communication costs 7lambda/3 + 35 and 15lambda/4 + O(1) bits, respectively. For arbitrary fan-in (n), we give a construction for any single-output gate with communication cost bounded by (22 dot 2^nlambda/n + 2^n) bits. Our constructions are compatible with free-XOR, and all hash queries within each gate are nonadaptive. We prove security of the framework in the random-oracle model and under a circular correlation robustness (CCR) condition for any number of slices. We also evaluate simple uses of the three-input construction against the best two-input circuits collected in our experiments, finding evidence of communication savings on control circuits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2200) | 2026-09-24
