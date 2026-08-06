---
title: "LFSRs and Boolean Masking: An In-depth Security Analysis"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1614"
summary: "Masking is a widely adopted countermeasure to protect cryptographic implementations from side-channel attacks. Subsequent research has focused on designing masking schemes and formally proving their s"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Masking is a widely adopted countermeasure to protect cryptographic implementations from side-channel attacks. Subsequent research has focused on designing masking schemes and formally proving their security, notably through the development of automated tools, within models abstracting the reality of a sidechannel analysis. These designs rely on an external source of randomness; however, there is currently no consensus on the choice of (pseudo-)random number generators for masking. To the best of our knowledge, existing formal proofs for masking security do not consider particular choices of random number generators, but rather assume that they yield uniformly distributed and independent random variables. In that context, we introduce the first verification framework that jointly analyzes a pseudorandom number generator— specifically, but not limited to, a linear feedback shift register—and a masking scheme, in the d-probing model. Our framework relies on the Walsh-Hadamard transform by drawing on techniques from linear cryptanalysis, which we extend to the robust probing model. We demonstrate our method on 4-bit and 8-bit S-boxes, provide a detailed analysis of the formal verification outcomes, and corroborate the findings with practical evaluations on an FPGA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1614) | 2026-08-05
