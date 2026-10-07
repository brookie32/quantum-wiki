---
title: "Low-Latency Parallel Digit Decomposition and Sign Evaluation for CKKS"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2368"
summary: "Nonlinear functions such as sign, comparison, and ReLU are commonly evaluated in CKKS by approximating them with polynomials. The sign jumps at zero, so inputs on the two sides of zero, however close,"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Nonlinear functions such as sign, comparison, and ReLU are commonly evaluated in CKKS by approximating them with polynomials. The sign jumps at zero, so inputs on the two sides of zero, however close, must be mapped to outputs that differ by a constant. Comparison is the sign of a difference, and ReLU and max inherit this requirement when computed through the sign at high output precision. To distinguish inputs separated by about 2^{-p}, polynomial approximation needs Theta(p) multiplicative depth, and we show that, in a standard model where every level must keep the values of these inputs apart above the noise, its modulus consumption grows to Theta(p^2) bits. Evaluating the functions from radix-B digits avoids this cost, but existing methods extract the u digits of a real-valued input one at a time, with u sequential bootstrappings. We obtain all u digits in parallel with a single bootstrapping: each digit is produced with an error of at most one carry from the digit below, and carry look-ahead corrects all carries in O(log u) depth. For the sign, the same carry look-ahead combines the digits directly, without recovering them. As a result, close inputs separated by about 2^{-p} are distinguished with Theta(p) modulus bits instead of Theta(p^2), using O(log B) depth for table lookups and O(log u) depth for carry look-ahead, at the cost of Theta(u) slots per input. Benchmarks show a 2.04imes speedup for coefficient-integer digit decomposition at ten radix-64 digits and a 7.83imes speedup for sign evaluation on 1,024 real input pairs at 2^{-60} separation. The gain comes from where the precision is spent: a polynomial must keep the values of close inputs apart at every level, whereas the digits take only finitely many values, so our circuit, including its bootstrapping, runs at low precision, and the output precision is raised only at the end.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2368) | 2026-10-05
