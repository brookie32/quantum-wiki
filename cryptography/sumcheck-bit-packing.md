---
title: "Sumcheck bit packing"
date: "2026-11-04"
updated: "2026-11-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2770"
summary: "Circuit-based zero-knowledge proofs over large fields waste most of a field element when they commit to a single bit. We study the problem of committing to packed witnesses, in which m bits are stored"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

Circuit-based zero-knowledge proofs over large fields waste most of a field element when they commit to a single bit. We study the problem of committing to packed witnesses, in which m bits are stored in one element of GF(2^m), while still allowing the proof system to verify linear claims about the individual bits. Prior approaches to this problem either (a) scale to packing only 4 bits[Fs24], (b) require tensor-structured claims and additional sumcheck rounds that incur larger soundness error [DP23,DP25], or (c) rely on Frobenius automorphisms [Koc26]. In contrast, we present a simpler reduction that exploits only the GF(2)-linearity of the field trace and achieves soundness error 2^{-m} for arbitrary bit-linear claims. We then use a characterization of trace-zero field elements to make the reduction zero-knowledge over any hiding linear commitment scheme: whereas previous constructions verify O(m^2) or O(m)quadratic constraints in the commitment scheme, our protocol requires only linear constraints.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2770) | 2026-11-04
