---
title: "Faster Polynomial Factorization over Finite Fields via Batched Modular Composition"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2625"
summary: "In the algebraic model, where one counts operations in F_q uniformly in the characteristic, the best published algorithm for factoring a polynomial of degree n over F_q, due to Kaltofen and Shoup with"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

In the algebraic model, where one counts operations in F_q uniformly in the characteristic, the best published algorithm for factoring a polynomial of degree n over F_q, due to Kaltofen and Shoup with the rectangular products of Huang and Pan, uses n^{1.80535+o(1)}log q operations, and its bottleneck is the modular compositions of the giant steps. A new algorithm is presented for these compositions. Like the algorithm of Neiger, Salvy, Schost and Villard, the new method is based on the relation matrices of the argument. Since all compositions at one level of the giant steps share one argument, the relation matrices and a table of remainders are computed only once, and the remaining work consists of rectangular matrix products. For the two-matrix evaluation, we prove that a random change of basis puts every Frobenius image in good position. This reduces the cost of factorization in this model $ext{from}quad n^{1.80535+o(1)}log qquadext{to}quad n^{1.5532+o(1)}log q, and to n^{3/2+o(1)}log q if omega=2; with the compositions of Neiger, Salvy, Schost and Villard performed one at a time, the exponent would be 1.7147. In the bit model, and algebraically in small characteristic, Kedlaya and Umans obtained the exponent 3/2. For a single composition with an arbitrary argument modulo a separable polynomial, the content of one short relation separates large value fibers, which gives a Las Vegas algorithm for every input at the exponent (omega+3)/4<1.3429, previously known only for generic inputs, and a fourth evaluation level, with truncated powers obtained by transposition, lowers it to 1.3309. As applications, we obtain faster algorithms for normal bases, minimal polynomials and irreducibility testing, and, for large q, factorization in O(n^{1.5983})+n^{1+o(1)}log q$ operations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2625) | 2026-10-24
