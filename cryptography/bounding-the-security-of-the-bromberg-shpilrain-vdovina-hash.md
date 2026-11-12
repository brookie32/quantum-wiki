---
title: "Bounding the security of the Bromberg-Shpilrain-Vdovina hash function"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2851"
summary: "The Bromberg-Shpilrain-Vdovina hash functions are a family of Cayley hash functions indexed by an integer parameter kge 2. Hashes are matrices in SL_2(p) where p is a large prime. We present an attack"
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

The Bromberg-Shpilrain-Vdovina hash functions are a family of Cayley hash functions indexed by an integer parameter kge 2. Hashes are matrices in SL_2(p) where p is a large prime. We present an attack which finds collisions of length O(log p) whose average-case time complexity is O(p^{0.28}) when k=2 and O(p^{0.36}) when k=3 under an assumption in the spirit of Zaremba's Conjecture on continued fractions. This is an improvement on the more general attacks of Mullan-Tsaban and Slaughter which have average-case time complexity O(sqrt{p}). For any k, the average-case time complexity of our attack is O(p^{1-elta_k+o(1)}) where elta_k is the Hausdorff dimension of a certain Cantor set. This tends to O(sqrt{p}) as koinfty, so our attack has time complexity comparable to Mullan-Tsaban and Slaughter's attacks as k grows. We give examples of collisions for large primes found by our attack when k=2, 3.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2851) | 2026-11-10
