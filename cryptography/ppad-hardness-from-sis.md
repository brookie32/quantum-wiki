---
title: "PPAD Hardness from SIS"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2603"
summary: "Understanding the hardness of the complexity class PPAD is an important question in complexity theory given that it contains problems such as computing a Nash equilibrium. Evidence of hardness, howeve"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Understanding the hardness of the complexity class PPAD is an important question in complexity theory given that it contains problems such as computing a Nash equilibrium. Evidence of hardness, however, has come primarily from cryptography, through a long line of work. Most recently, Chen, Freitag, Jin and Wichs (STOC 2025) based the hardness of PPAD on the polynomial hardness of the Learning with Errors (LWE) problem, together with a fine-grained average-case hardness assumption. In this work, we base the hardness of PPAD on a different lattice problem, the Short Integer Solution (SIS) problem, which, unlike the assumptions underlying prior work, is not known to imply public-key encryption. Specifically, we show that PPAD is hard on average assuming either: (i) polynomially hard SIS with a quasi-polynomial norm bound and a fine-grained average-case hardness assumption; or (ii) subexponentially hard SIS alone. Our main technical contribution is a succinct, incrementally updatable proof system for a class of exponentially large circuits with short descriptions. Building on the work of Wee (CRYPTO 2025) for succinct proof systems for circuits from SIS, we show how to make such proof systems satisfy these properties while preserving the unambiguity guarantee of the underlying scheme: it is hard to find two distinct accepted states for the same computation and time. Together, these are crucial for our PPAD hardness reductions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2603) | 2026-10-22
