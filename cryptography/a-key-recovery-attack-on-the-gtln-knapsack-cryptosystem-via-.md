---
title: "A Key-Recovery Attack on the GTLN Knapsack Cryptosystem via Continued Fractions"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2543"
summary: "We present a continued-fraction key-recovery attack on the knapsack-based public-key cryptosystem proposed by Gómez-Torrecillas, Lobillo, and Navarro (GTLN). The key observation is that ratios of publ"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We present a continued-fraction key-recovery attack on the knapsack-based public-key cryptosystem proposed by Gómez-Torrecillas, Lobillo, and Navarro (GTLN). The key observation is that ratios of public-key differences closely approximate rational numbers with small denominators, enabling their exact recovery by continued fractions. Divisibility relations in the recovered fractions yield multiples of two private-key integers through greatest common divisor computations. Once these two integers are identified by a bounded cofactor search, all remaining private-key integers except the modulus and the shift are uniquely determined. Further greatest common divisor computations, cofactor enumeration, and modular inversion then recover the secret modulus and shift. The above process of key recovery uses only public keys. For fixed cofactor bounds, the algorithm runs in polynomial time in the public-key bit length, while a heuristic analysis predicts a high probability of recovering the original key. In experiments with prime-based key generation, our Python implementation recovered the complete private key in all 2,400 trials across the 24 recommended parameter sets, with each attack taking less than 0.05 seconds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2543) | 2026-10-19
