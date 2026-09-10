---
title: "A Better Bivariate Resultant Attack on Round-Reduced Poseidon"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1905"
summary: "Poseidon is one of the most popular arithmetization-oriented (AO) hash function, due to its good performances both in evaluation and in Zero-knowledge proof protocols. It is for instance used in the P"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Poseidon is one of the most popular arithmetization-oriented (AO) hash function, due to its good performances both in evaluation and in Zero-knowledge proof protocols. It is for instance used in the Plonky3 library, and has been considered for use in the Ethereum protocol. The security of Arithmetization-oriented hash functions is commonly evaluated through the CICO-k problem, which consists in controlling simultaneously k coordinates in the input and output of the permutation. This problem is in particular relevant to finding preimages in sponge or compression mode and solving zero-test problems. Depending on the size of the underlying field, different values of k may be relevant. In this paper, we focus on the case of k=2, that was the subject of the recent bounty program by the Ethereum foundation. In this setting, one can model the CICO-2 problem as a bivariate system P(X, Y) = Q(X, Y) = 0 where the polynomials have total degree delta = d^(RF +RP). The best known methods for solving bivariate systems are algorithms for computing bivariate resultants. Over a generic system with coefficients over a finite field, the best algorithms achieve an asymptotic bit complexity that is linear in delta^(2+eps) log(q)^(1+eps), which is close to optimal, given that the input and output of the algorithm have bit size delta^2 log (q). However, the polynomial systems that stem from Poseidon are more structured, leading to a resultant that has degree DI = d^(2RF + RP), which is much less than what one would expect from a random bivariate system of degree d^(RF + RP). This fact has already been exploited in a previous work that used an evaluation-interpolation approach to compute the bivariate resultant in time that is quasi-linear in d^(3 RF + 2 RP). In this work, we exploit this fact by adapting another bivariate resultant algorithm to the special setting where the degree of the resultant of the equations is much lower than delta^2. By doing a careful analysis of the algorithm for systems with such property, we show that under some heuristics, the CICO-2 problem on Poseidon can be solved in time that is quasi-linear in DI delta^(1-1/w), where 2 <= w < 2.38 is the exponent of matrix multiplication. We validate our approach by implementing our attack on reduced versions of the Poseidon permutation, and show a practical speedup compared to the previous approaches.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1905) | 2026-09-07
