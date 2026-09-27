---
title: "Fully Anonymous Perfect Threshold Secret Sharing: Explicit One-Bit Construction and Rate Amplification"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2202"
summary: "Fully anonymous perfect threshold secret sharing combines exactly uniform unauthorized shares with reconstruction from unlabeled share values. Con, Li, and Mazor proved that short-share schemes exist "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Fully anonymous perfect threshold secret sharing combines exactly uniform unauthorized shares with reconstruction from unlabeled share values. Con, Li, and Mazor proved that short-share schemes exist for every threshold, leaving efficient general constructions and constant rate open. We address both questions. First, we give an explicit one-bit scheme with (2t-3)lceillog_2nrceil-bit shares, expected-polynomial-time sharing, and deterministic polynomial-time reconstruction. The key is an exact sampler for localized affine relations, including collision patterns. Second, an affine-hull compiler turns any one-bit primitive with alphabet {0,1}^b into a long-secret scheme with additive share overhead b(t-1)lceillog_2(n+1)rceil, up to field-alignment padding. Authorized payloads determine an affine space; a short anonymously shared certificate identifies the secret within it. Instantiation gives L+O(t^2log^2n)-bit shares and rate 1/2 at L=Theta(t^2log^2n). For fixed 2le t<n, the rate approaches one, which the classical bound of Kishimoto et al. shows is unattainable at any finite nontrivial secret alphabet. Finally, we prove the universal bound |Omega|ge(n-t+1)(n-t+2) for 3le tle n-2. Together with Con--Li--Mazor's specialized threshold-three construction, this establishes the exact fixed-length optimum of 2m share bits for (t,n)=(3,2^m), mge3. All guarantees are information-theoretic and exact. The technical work is done by GPT 6 Astra.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2202) | 2026-09-24
