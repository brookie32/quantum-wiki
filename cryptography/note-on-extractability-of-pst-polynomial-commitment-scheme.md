---
title: "Note on Extractability of PST Polynomial Commitment Scheme"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2398"
summary: "A recent work by Belohorec et al. (Crypto, 2025) shows that the well-known PST multivariate polynomial commitment scheme is black-box extractable under falsifiable assumptions. They show that a minima"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

A recent work by Belohorec et al. (Crypto, 2025) shows that the well-known PST multivariate polynomial commitment scheme is black-box extractable under falsifiable assumptions. They show that a minimally modified (extended) PST is extractable under an assumption ARSDH(n), and that the canonical PST is extractable under an assumption GARSDH(n). Both of these assumptions are new and more specialized than the original ARSDH assumption proposed by Lipmaa et al. (Eurocrypt, 2024) to prove black-box extractability of the univariate KZG polynomial commitment. A natural question is whether these assumptions are actually stronger than the original ARSDH assumption. We answer this negatively: we show that both ARSDH(n) and GARSDH(n) are equivalent to the original ARSDH assumption. Secondly, we point out a gap in the proof that canonical PST is extractable under GARSDH(n) assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2398) | 2026-10-07
