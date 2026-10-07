---
title: "Optimized NEON Implementation of MAYO on Apple M1"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2350"
summary: "MAYO is one of nine third-round candidates in NIST’s process for additional post-quantum signatures. Its third-round specification of August 2026 changed the level-1 parameters and added a hash-derive"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

MAYO is one of nine third-round candidates in NIST’s process for additional post-quantum signatures. Its third-round specification of August 2026 changed the level-1 parameters and added a hash-derived linear term Λ to the verification equation, so earlier optimised implementations no longer match it. We present an optimised NEON implementation of MAYO Round 3 for the Apple M1 and compare it with the upstream NEON code on the same machine. A generator emits the sixteen GF(16) kernels of each parameter set as assembly whose output is byte-identical to that of the upstream intrinsics. Apart from the Λ kernel, the large kernels reach 86–96% of the speed an operation-count model predicts. A transposed constant-time echelon form needs 55–70% fewer cycles than the upstream one. An eight-way interleaved AES expands the public matrices at 0.18 instead of 0.43 cycles per byte. The linear term is expanded with NEON; with our changes off, its portable-C AES derivation takes 10–22% of signing and 18–37% of verification. As medians over seven function alignments, compact-key signing is 1.99–2.12 times faster than upstream on all four sets, and verification 2.11–2.62 times. A constant-time campaign with matched null runs finds the linear-algebra tests indistinguishable from their nulls, at 25% power for a twofold dispersion. The MAYO₂ signature test differs. Verification, which holds no secret, shows a key-fixed timing effect on public data, upstream as well; the signature test does not separate it from a secret one. All measurements are on one M1 Pro.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2350) | 2026-10-05
