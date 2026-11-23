---
title: "How to Hash and Commit Real Values with Dynamic Precision"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2962"
summary: "When hashing or committing real values (represented by floating-point numbers), traditional cryptographic hash functions and commitment schemes have to first convert the real values to integers or fin"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

When hashing or committing real values (represented by floating-point numbers), traditional cryptographic hash functions and commitment schemes have to first convert the real values to integers or finite ring elements. Such solutions suffer from several drawbacks. The schemes do not support dynamic choices of precisions. More generally, hashing or committing algorithms lose the efficiency and flexibility of directly working on real numbers. In this paper, we define and construct cryptographic hash functions and commitment schemes with dynamic precision choices and native real number arithmetic. Our main contributions are: 1. Providing the definitions of the real value collision resistant hash function (RVCRH) and commitment for real numbers, formalizing the notions of dynamic precision choices in the hashing, committing, and opening algorithms. 2. Defining the continuous analogs of the Short Integer Solution Problem (CSIS) and proving their hardness based on the worst-case hardness of lattice problems. We then construct RVCRHs and compressing commitment schemes with dynamic precision and native real arithmetic from CSIS problems. 3. Constructing a statistically binding additively homomorphic commitment scheme that supports real number arithmetic from the Continuous Learning With Errors Problem (CLWE). As an application, we provide a Sigma protocol for proving the knowledge of real numbers from CLWE. We also show that additively homomorphic commitment schemes for real values are unlikely to be compressing by showing a partial impossibility result for achieving such schemes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2962) | 2026-11-20
