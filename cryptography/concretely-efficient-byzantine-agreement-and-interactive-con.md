---
title: "Concretely Efficient  Byzantine Agreement and Interactive Consistency for Honest Majority"
date: "2026-11-19"
updated: "2026-11-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2954"
summary: "We consider two of the main notions of round-efficient Byzantine agreement (BA): expected constant rounds and early stopping. Randomized protocols can terminate in an expected constant number of round"
last_verified: "2026-11-22"
review_by: "2027-02-20"
stale: false
---

We consider two of the main notions of round-efficient Byzantine agreement (BA): expected constant rounds and early stopping. Randomized protocols can terminate in an expected constant number of rounds, while early-stopping protocols terminate in a number of rounds that depends only on the actual number fle t of corrupted parties. Recent works achieve both guarantees at once, but at a high concrete cost: assuming PKI, for the optimal threshold t<n/2, the previous protocol with the smallest expected round complexity needs 37 rounds in expectation and 15f+29 in the worst case. In this work, we present a BA protocol for t<n/2, secure against an adaptive adversary assuming a PKI, that terminates in 18 rounds in expectation and in at most 8f+18 rounds in the worst case. Moreover, our protocol has the following optimistic feature: if no party is corrupted and all inputs agree, every party outputs after a single round. Our protocol is natively multi-valued and does not rely on random oracles. At the core of our result is a new randomized BA protocol in which a successful leader election leads to agreement within the same phase. We extend our results to Byzantine broadcast, obtaining a protocol that has 19 rounds in expectation and 8f+19 in the worst case, and to interactive consistency (IC), retaining the same round complexity while providing an optimistic fast path in which all parties output after only 2 rounds when everyone is honest. We do so by directly parallelizing our BB protocol, instead of using a generic IC compiler, for which, at t<n/2, the best known bounds are more than 4000 rounds in expectation and 184f+730 in the worst case.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2954) | 2026-11-19
