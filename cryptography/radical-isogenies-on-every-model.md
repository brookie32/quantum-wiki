---
title: "Radical isogenies on every model"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2661"
summary: "Radical isogeny formulae compute a cyclic chain of N-isogenies with one Nth root per step and without sampling torsion points, but for general N they were only known in Tate normal form. We give radic"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Radical isogeny formulae compute a cyclic chain of N-isogenies with one Nth root per step and without sampling torsion points, but for general N they were only known in Tate normal form. We give radical steps of every odd degree N directly on short Weierstrass, Montgomery, twisted Edwards, Huff, extended Jacobi quartic, twisted Hessian, Legendre and Jacobi intersection curves, on Kummer lines, and on all curves with a rational point of order~2. Our approach is model-independent. The Tate normal form data is obtained from the x-coordinate of the kernel generator by a shifted recursion, and the codomain is recovered in the original model by locating the image of a distinguished torsion point, without square roots. In Tate normal form we lower the cost of a step from 12.5N to 10N multiplications plus one exponentiation, and short Weierstrass curves come close at 10N+35. Montgomery and twisted Edwards curves cost 10.5N+O(1). However, pushing a point through their steps costs only 2N multiplications without precomputation, against 2N+16 plus a shared 2N-7 in Tate normal form, which makes them the cheapest models for chains that transport torsion points, e.g. for all Nge19 when two points are pushed. The other models cost between 11.5N+O(log N) and 15.5N+O(log N) per step. All algorithms are inversion-free, with exact operation counts.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2661) | 2026-10-27
