---
title: "AES-Based Grinding for MPC-in-the-Head Signatures"
date: "2026-08-06"
updated: "2026-08-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1625"
summary: "Grinding is a technique which introduces a proof of work into the Fiat-Shamir transform: by constraining the challenge to satisfy a w-bit condition, forging a proof requires about 2^w/arepsilon evalua"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

Grinding is a technique which introduces a proof of work into the Fiat-Shamir transform: by constraining the challenge to satisfy a w-bit condition, forging a proof requires about 2^w/arepsilon evaluations of the hash function instead of 1/arepsilon, where arepsilon is the soundness error of the underlying protocol. This allows one to select reduced parameters, yielding shorter proofs and signatures. Grinding is used in FAEST, MQOM and SDitH, the three MPC-in-the-Head schemes selected for the third round of the NIST additional post-quantum signature standardization process, where it is instantiated with Keccak. In this short paper, we investigate grinding schemes in which the proof of work is expressed in terms of block cipher computations, specifically AES, which is significantly faster than Keccak on modern CPUs, is already a building block of these schemes, and underlies the very definition of the NIST security categories. We formalize the notion of grinding scheme together with a protocol-agnostic security notion, we propose a construction performing two cipher calls per iteration, and we prove, in the ideal cipher and random oracle models, that an adversary making Q_E cipher queries breaks it with probability at most frac{4}{3} dot arepsilon, Q_E / 2^w, up to negligible terms. We further generalize the scheme to use more cipher calls per iteration, which makes the constant frac43 tend to 1.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1625) | 2026-08-06
