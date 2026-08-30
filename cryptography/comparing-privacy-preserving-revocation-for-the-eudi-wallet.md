---
title: "Comparing Privacy-Preserving Revocation for the EUDI Wallet"
date: "2026-08-28"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1824"
summary: "The European Digital Identity Wallet has integrated anonymous credentials into its technical specifications, and singles out four constructions for privacy-preserving revocation, drawn from two famili"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

The European Digital Identity Wallet has integrated anonymous credentials into its technical specifications, and singles out four constructions for privacy-preserving revocation, drawn from two families: positive dynamic accumulators and signed-pairs. The two families are described in the literature in substantially different terms, and no common basis for comparing them exists, which currently prevents informed and quantitative decision making. In this work, we give a unified treatment of both families, showing that signed-pairs, despite their very different presentation, can be expressed in the standard accumulator syntax. We use this to define a single revocation mechanism that any of the four constructions instantiates, which in turn allows us to compare the resulting mechanisms both at the protocol level and empirically. We measure the performance of all four across the full credential lifecycle, on server-class hardware for the Status Manager and on a smartphone for the Holder and Verifier, with parameters taken from a live national eID scheme. No construction dominates in every aspect, and we make the resulting trade-offs explicit, showing which construction suits which deployment, and identify promising avenues for further improvement at the protocol level.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1824) | 2026-08-28
