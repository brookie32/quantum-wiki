---
title: "Getting to the right root: radical isogenies of every degree"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2595"
summary: "Class group actions on supersingular elliptic curves over mathbb F_p as in CSIDH are typically evaluated as long chains of isogenies of small prime degree. Radical isogeny formulae compute such chains"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Class group actions on supersingular elliptic curves over mathbb F_p as in CSIDH are typically evaluated as long chains of isogenies of small prime degree. Radical isogeny formulae compute such chains using a single Nth root per step, without sampling torsion points. Compact formulae of linear size had been conjectured for all odd N. We prove a corrected version of these formulae for every Nge4, odd and even, over every field of characteristic coprime to 2N. In our formulation, every building block is a twisted sum of a discrete Kronecker function over mathbb Z/Nmathbb Z, and the formulae follow from a distribution relation for the Kronecker theta function. For even N, the Nth root is only determined up to sign over mathbb F_p, and the sign decides whether the walk stays on the surface of the 2-isogeny volcano. We show that the radical times a 2-torsion coordinate of the next curve is a square, which yields the horizontal choice for all even N; previously this was only known for Nle14. Algorithmically, one radical step costs about 12.5N multiplications and one exponentiation, without inversions. For horizontal 2-isogeny walks, radical 2^m-isogenies with min{5,6,7} are optimal for primes of 512 to 4096 bits. Finally, we show how to evaluate radical isogenies on points. As a consequence, a class group action can be computed from two given points, one on the curve and one on its quadratic twist, without ever sampling torsion points.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2595) | 2026-10-22
