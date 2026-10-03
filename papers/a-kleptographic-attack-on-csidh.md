---
title: "A Kleptographic Attack on CSIDH"
date: "2026-09-30"
updated: "2026-10-03"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2283"
summary: "This note reports an attack scenario for CSIDH that does not appear to have been considered in the literature. A subverted device of Alice can leak a shared curve between Alice and Bob through Alice's"
last_verified: "2026-10-03"
review_by: "2027-01-01"
stale: false
---

This note reports an attack scenario for CSIDH that does not appear to have been considered in the literature. A subverted device of Alice can leak a shared curve between Alice and Bob through Alice's public curves in later CSIDH sessions. The attack adapts the Young--Yung kleptographic attack from classical Diffie--Hellman to CSIDH using the Goldreich--Levin theorem and rejection sampling. We prove that a CSIDH public curve [mathfrak a]star E_0 remains computationally indistinguishable from an honest public curve even when its secret class [mathfrak a] is rejection-sampled according to a hard-core bit of a hidden parallelization curve [mathfrak a][mathfrak c]star E_0 formed by the same class [mathfrak a] together with an independent curve [mathfrak c]star E_0. The proofs rely only on the computational assumptions underlying CSIDH itself. We hope that this note provides a useful starting point for the study of algorithm-substitution attacks in isogeny-based cryptography, complementing existing work on side-channel and fault attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2283) | 2026-09-30
