---
title: "Truffle: Maliciously Secure Three-Party Shuffles with Applications to Parsing"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2376"
summary: "Deploying Secure Multiparty Computation (MPC) to operate on data from real world sources requires many connective elements that have not received much attention in the literature. One prominent exampl"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Deploying Secure Multiparty Computation (MPC) to operate on data from real world sources requires many connective elements that have not received much attention in the literature. One prominent example is that MPC protocols typically assume conveniently structured data, whereas data in the real world comes in formats that are meant to be handled by string parsing engines. In this work, we give a new constant round protocol for securely parsing secret shared strings into an MPC-friendly format, built upon secure shuffle as a key primitive. Secure shuffle applies a permutation to a list while keeping both the permutation and the underlying data secret-shared at all times. While highly efficient protocols exist in the semi-honest setting, achieving malicious security has incurred significant overhead in both rounds and communication. We present Truffle, a new three-party shuffle protocol that is secure against one active corruption to bridge this gap. Truffle achieves an amortised round complexity that for the first time matches the state-of-the-art semi-honest protocol, while incurring only sublinear communication overhead. The core technique that underlies Truffle is a novel distributed verifier zero-knowledge proof that checks the correctness of a putative shuffle. We implement Truffle and show via benchmarks that it is performant enough to handle real application data. Beyond parsing secret shared data, secure shuffle finds applications in graph analytics, anonymous communication, Distributed Oblivious RAM, aggregate statistics, and secure sorting, each of which stand to benefit from the improvement that Truffle provides.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2376) | 2026-10-06
