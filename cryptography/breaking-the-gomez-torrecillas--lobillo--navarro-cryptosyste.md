---
title: "Breaking the Gomez-Torrecillas--Lobillo--Navarro Cryptosystem: LLL Recovers the Secret Key Within Seconds"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2225"
summary: "We present a key-recovery attack on the knapsack McEliece-based public key cryptosystem recently proposed by Gomez-Torrecillas, Lobillo, and Navarro in DCC 2026. Given the public key alone, the attack"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We present a key-recovery attack on the knapsack McEliece-based public key cryptosystem recently proposed by Gomez-Torrecillas, Lobillo, and Navarro in DCC 2026. Given the public key alone, the attack recovers the complete private key in time polynomial in the bit-length of the public key, and therefore constitutes a total break. The attack combines two observations based solely on the public key. An integer combination of the public entries whose coefficients sum to zero eliminates the secret mask. If such a combination is also orthogonal to the public key and sufficiently short, then its coordinates are divisible by the corresponding private key integers. The modulus required for correct decryption creates a large norm gap between these short vectors satisfying the hidden private key relations and the remaining vectors in the lattice. LLL reduction exploits this gap to recover the short vectors and hence the corresponding divisibility relations. The private key integers and the remaining secret parameters are then recovered by combining information from multiple overlapping lattices and using greatest common divisors. We implemented the attack in SageMath and recovered the complete private key for all twenty four parameter sets proposed by the authors within 3 seconds, despite claimed security levels ranging from 64 to 156 bits. Our analysis further shows that the weakness is structural rather than a consequence of the particular parameter choices.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2225) | 2026-09-26
