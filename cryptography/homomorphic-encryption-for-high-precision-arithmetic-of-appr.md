---
title: "Homomorphic Encryption for High-precision Arithmetic of Approximate Numbers"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2524"
summary: "The CKKS fully homomorphic encryption scheme enables efficient arithmetic over complex numbers, but each homomorphic multiplication consumes a large modulus to ensure enough precision, limiting both t"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

The CKKS fully homomorphic encryption scheme enables efficient arithmetic over complex numbers, but each homomorphic multiplication consumes a large modulus to ensure enough precision, limiting both the circuit depth and precision supported by CKKS. This work addresses this problem by proposing Generalized CKKS (GCKKS), a CKKS analogue of the GBFV scheme (EUROCRYPT 2025) that trades the number of slots for reduced modulus consumption. Despite its high-level similarity to GBFV, GCKKS faces new challenges caused by the different encoding and encryption structures of CKKS. We address these challenges with novel techniques not present in GBFV. Our plaintext encoding starts with an improved and SIMD version of Costache, Smart, and Vivek's encoding in 2017. Namely, it rounds complex values to cyclotomic integers instead of Gaussian integers, and reduces the rounding problem to solving CVP instances. This encoding allows storing high-precision complex values in polynomials with small canonical norms. As an important observation, the encoding can be simplified to a sparse CKKS encoding followed by multiplication with a polynomial constructed from a short vector in the encoding lattice. We show that by integrating this encoding format into GCKKS decryption, most GCKKS homomorphic operations and the corresponding noise analyses reduce to their CKKS counterparts. This relieves GCKKS from any heavy computational or noise overhead. In experiments, GCKKS provides 7 levels with 1000-bit precision at ring dimension 2^{14}, where each multiplication takes less than 30 ms. To our knowledge, this precision has never been achieved before. It can be used to preserve enough precision after noise flooding, a necessary ingredient for CKKS circuit privacy and a common approach to secure threshold CKKS and to provide IND-CPA^ext{D} security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2524) | 2026-10-18
