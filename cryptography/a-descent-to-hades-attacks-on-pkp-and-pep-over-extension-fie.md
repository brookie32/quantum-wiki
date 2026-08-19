---
title: "A Descent to Hades: Attacks on PKP and PEP over Extension Fields"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1711"
summary: "The Permutation Code Equivalence Problem (PEP) and Permuted Kernel Problem (PKP) are two notorious computational problems over linear codes used for building post-quantum digital signature schemes. Al"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

The Permutation Code Equivalence Problem (PEP) and Permuted Kernel Problem (PKP) are two notorious computational problems over linear codes used for building post-quantum digital signature schemes. Although traditionally analyzed over prime fields, recent proposals, such as the signature schemes PERK and SETH, have considered extension fields to improve efficiency and compactness. In this work, we analyze the hardness of solving PKP and PEP when instantiated over field extensions. For binary field extensions, by exploiting a reduction to a structured variant of the Regular Syndrome Decoding Problem (RSD), we uncover new polynomial-time parameter regimes for both PKP and PEP, including families of self-orthogonal PEP instances and all self-dual instances over extensions of degree nu>4. We also adapt the permutation-based Regular-ISD algorithm of Esser and Santini for RSD (CRYPTO '24) to PKP-derived instances, and uncover regimes of parameters for which it improves upon the state-of-the-art. Moreover, we present a reduction from a broad family of PEP instances over extension fields with odd characteristic to the Graph Isomorphism Problem, yielding a polynomial-time algorithm to solve those instances. Overall, our results invalidate the use of PEP over extension fields for most of the scenarios, and provide novel insights into the security of PKP over extension fields.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1711) | 2026-08-17
