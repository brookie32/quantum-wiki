---
title: "PyuQuMuQu: Attacks on MQ-Based Linkable Ring Signatures and a New 5-Pass Construction"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2051"
summary: "Linkable ring signatures (LRS) let a member sign on behalf of a group anonymously while ensuring that any two signatures by the same signer are publicly linkable, a major component in e-voting and cry"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Linkable ring signatures (LRS) let a member sign on behalf of a group anonymously while ensuring that any two signatures by the same signer are publicly linkable, a major component in e-voting and cryptocurrencies. Random systems of multivariate quadratic (MQ) equations are one of the most conservative post-quantum assumptions, yet there are only two MQ-based LRS's in the literature: the first is due to Omar, Padhye, and Dey, and the second by Namdeo, Mishra, and Srivastava. Both of these schemes are built from Sakumoto-style identification protocols whose soundness for signatures is well-established, but in the ring setting was never re-examined. We present a sumset attack that lets a signer with no knowledge of an MQ solution universally forge accepting signatures in both protocols. In the same vein, we show that the four-challenge MQ protocol of Monteiro, Goya, and Terada (as transcribed in Namdeo, Mishra, and Srivastava) has soundness error 3/4 instead of the claimed 1/2, and this bound is tight. Its natural repair does achieve 1/2, but is only 3-special sound, so the two-transcript extraction argument upon which their LRS relies upon does not hold regardless. We then build PyuQuMuQu, a plausibly post-quantum MQ-based LRS from a 5-pass proof with a d-dimensional vector first challenge and an additively split second challenge, whose soundness error is frac{1}{2} + frac{N}{2(q^d-1)} for a ring with N leq q^d-1 members. We demonstrate anonymity, linkability, and non-slanderability in the random-oracle model under explicitly stated assumptions involving random MQ maps. PyuQuMuQu attains 355 kB signature sizes for a ring with 4 members 128 bits of security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2051) | 2026-09-15
