---
title: "Secret Sharing from Non-Extractable Randomness"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2477"
summary: "Bosley and Dodis (TCC 2007) proved that a class of imperfect randomness sources that suffices for information-theoretic encryption of messages longer than the logarithm of the key length must admit de"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Bosley and Dodis (TCC 2007) proved that a class of imperfect randomness sources that suffices for information-theoretic encryption of messages longer than the logarithm of the key length must admit deterministic extraction of nearly uniform bits, and asked whether the same is true of two-out-of-two secret sharing. Aggarwal, Chung, Obremski, and Ribeiro (TCC 2022) gave a positive answer for schemes that are in addition leakage-resilient or non-malleable; the original question remained open. We answer it in the negative. For every bge2 we construct a class of flat sources on {0,1}^{b+2}, each of min-entropy at least b, together with a perfectly correct and perfectly private two-out-of-two scheme that shares a b-bit secret into two (b+1)-bit shares using any source in the class, and we show that every deterministic map from {0,1}^{b+2} to {0,1} is at statistical distance at least 1/6 from uniform on some source in the class. This implies that sharing a long enough secret does not require extractable randomness. The proof is a short parity argument. The idea of the construction extends to other thresholds: for two-out-of-n and r-out-of-r sharing we give perfect schemes with (b+1)-bit shares, private for classes of flat sources from which no single bit can be extracted with error below 1/(4n-2) and 1/(2(2^r-1)), respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2477) | 2026-10-14
