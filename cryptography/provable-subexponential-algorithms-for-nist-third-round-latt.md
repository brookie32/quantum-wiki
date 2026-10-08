---
title: "Provable Subexponential Algorithms for NIST Third-Round Lattice Families"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2386"
summary: "We give provable classical subexponential algorithms for secret recovery in growing parameter families associated with NIST third-round lattice candidates. For the Kyber/ML-KEM, FrodoKEM, SABER, NTRU "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

We give provable classical subexponential algorithms for secret recovery in growing parameter families associated with NIST third-round lattice candidates. For the Kyber/ML-KEM, FrodoKEM, SABER, NTRU LPRime, and Dilithium/ML-DSA families studied here, polynomial moduli and polylogarithmic coefficient scales yield recovery of the short secret component in expected time and space 2^{(1/2+o(1))n/lnln n}. For noisy or rounded linear relations, we exploit an exact gap in the squared Euclidean norm of a comparison vector defined by each coordinate guess. One Gaussian list suffices to identify every secret coordinate by binary search, without enumerating the others. We establish the required sampling guarantees through new geometric bounds for structured public operators over prime and power of two moduli. The construction builds on the Wagner-style Gaussian sampling framework of Ducas, Engelberts, and Loyer (CRYPTO 2025) and the low-error decision-LWE algorithm of Han, Gao, and Hu (2026). For quotient relations of NTRU type, we develop an affine slice search: fixing coordinates restricts candidate pairs to slices of the public lattice, and their estimated Gaussian masses guide the choice of each next coordinate. In the stated modulus window, Falcon's key generation quality condition supplies the required mass bound. The algorithm then recovers an equivalent signing key with high probability in time and space 2^{O(n/lnln n)}. The same search recovers the short key core for cyclic NTRU-HPS/HRSS. Together, these results give subexponential algorithms for problem families associated with all seven NIST third-round lattice candidates. Despite the subexponential complexity, our results do not establish a reduction in the concrete security of the currently specified parameter sets.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2386) | 2026-10-06
