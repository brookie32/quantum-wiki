---
title: "A unified reduction from RLWE to MP-LWE"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2026"
summary: "The Middle-Product Learning With Errors (MP-LWE) problem, introduced by Roşca, Sakzad, Steinfeld, and Stehlé (Crypto 2017), is a structured variant of LWE defined independently of any specific number "
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The Middle-Product Learning With Errors (MP-LWE) problem, introduced by Roşca, Sakzad, Steinfeld, and Stehlé (Crypto 2017), is a structured variant of LWE defined independently of any specific number field K. Its hardness has been based on the hardness of Ring-LWE (RLWE) over families of number fields. Two main reductions exist, one from Roşca, Sakzad, Steinfeld, and Stehlé (Crypto’17) and Njah Nchiwo and Pellet-Mary (PKC’26), and another one due to Peikert and Pepin (Journal of Cryptology’24). Both reductions cover different families of number fields, and none of the two supersedes the other. In this work, we propose a unified reduction from RLWE to MP-LWE parameterized by a pair of field elements (y_a,y_s) in K^2, which recovers both prior reductions as concrete instantiations. Optimizing the choice of (y_a,y_s), we obtain the first reduction from RLWE to MP-LWE that holds for all number fields K = Q[X]/f(X) where f is a monic irreducible polynomial of a given degree and with polynomially bounded coefficients (and whose discriminant is coprime to the modulus q of the RLWE and MP-LWE problems, a constraint that also appeared in previous works). This new reduction supersedes the two previously known reductions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2026) | 2026-09-14
