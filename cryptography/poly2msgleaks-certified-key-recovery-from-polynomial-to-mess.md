---
title: "Poly2MsgLeaks: Certified Key Recovery from Polynomial-to-Message Leakage"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2657"
summary: "We present Poly2MsgLeaks, a profiled chosen-ciphertext power-analysis attack that recovers the complete 512-coefficient public-key encryption (PKE) secret of SMAUG-T in its TiMER parameter set. Each p"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

We present Poly2MsgLeaks, a profiled chosen-ciphertext power-analysis attack that recovers the complete 512-coefficient public-key encryption (PKE) secret of SMAUG-T in its TiMER parameter set. Each polynomial-to-message (P2M) decision depends on four ternary secret coefficients and therefore on one of 81 local states. We characterize all admissible P2M predicates and show that our six-query schedule maps the 81 states to 57 binary transcripts; even with both exact polynomial weights, noiseless transcripts leave a mean residual ambiguity of 27.2 bits. Poly2MsgLeaks retains waveform scores for all 81 states, couples the 128 local blocks through the exact weights, and enumerates a calibrated cost region against the public-key relation. Under a uniform-matrix model, we prove that an incorrect key is released with probability at most 2^{-2095.6}; for exchangeable calibration and evaluation keys, the probability that the true key lies outside the searched region is bounded without a channel model. Using six physical P2M traces recorded on an STM32F415, Poly2MsgLeaks recovers 999 of 1,000 previously unseen secrets, and a verifier-driven policy recovers all 1,000 secrets of a second cohort at a mean cost of 7.021 traces, without false acceptances. With the same decoder and limits, equalizing the scores within each transcript class reduces recovery from 998 to 112 keys. Against single-write message assembly and a two-share masked P2M, the evaluated six-execution attack recovers no complete secret.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2657) | 2026-10-27
