---
title: "Fast Linear Codes over Large Fields: Addition-Only and Small-Coefficient Encoders"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2316"
summary: "We construct fast linear codes over large fields using addition-only encoders and variants with small integer coefficients. A local precode is followed by rounds of a random permutation and a scan, a "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We construct fast linear codes over large fields using addition-only encoders and variants with small integer coefficients. A local precode is followed by rounds of a random permutation and a scan, a linear recurrence with a short feedback window. At dimension 2^{20}, rate 1/2, and p=2^{128}-159, two plain accumulators (unweighted prefix sums) give relative distance above 11.7%, except with probability below 2^{-49.64} over the sampling of the encoder. A binary subset-sum precode instead gives distance above 12.56%, except with probability below 2^{-22.05}. These addition-only encoders use fewer than 6.8125n and 3.3125n field additions, respectively, for output length n. Both exceed the binary rate-1/2 Gilbert--Varshamov benchmark. The proof counts the supports and ranks of the zero equations a codeword must satisfy, retaining the dependence between cancellations. Coefficient size and scan width extend the tradeoff. On one core, with a common implementation and setup failure below 2^{-40}, encoding time ranges from 12.171 ms at proved distance above 11.7% to 32.342 ms above 42.987%. A coefficient-independent upper bound limits every encoder with two width-one scans after the Newton precode to 39.6855%. The distance and setup-failure bounds hold over mathbb F_p and every finite extension, covering all nonzero messages after setup. Timings are for mathbb F_p. Extension preserves distance exactly because the encoder coefficients lie in the prime subfield. Changing characteristic requires a separate argument; we give field-transfer results in both directions, including counterexamples.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2316) | 2026-10-02
