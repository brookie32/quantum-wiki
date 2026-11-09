---
title: "An improved algorithm to solve the isogeny problem in dimension 2 with precomputation"
date: "2026-11-06"
updated: "2026-11-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2808"
summary: "We give a new algorithm for the superspecial isogeny problem in dimension 2. After a one-time precomputation depending only on p (which succeeds with overwhelming probability), each instance is solved"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

We give a new algorithm for the superspecial isogeny problem in dimension 2. After a one-time precomputation depending only on p (which succeeds with overwhelming probability), each instance is solved in expected time and memory p^{3/4+o(1)}. This result is unconditional, relying on no heuristics. Including the precomputation, a single instance is solved in time p^{19/23+o(1)}, improving on the p^{1+o(1)} of the Costello-Smith algorithm. The improvement holds even with the same memory as (the rigorous version of) their algorithm. The key ingredient is an algorithm that computes the equations of the Humbert surfaces H_{N^2} modulo p for all N up to a bound D growing with p. These equations give a membership test for optimally (N,N)-split surfaces, which we evaluate in batches using fast multipoint evaluation. This speeds up the bottleneck of the Costello-Smith algorithm: finding an isogeny from a superspecial principally polarised abelian surface to a product of supersingular elliptic curves.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2808) | 2026-11-06
