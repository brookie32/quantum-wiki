---
title: "A Unified Analysis of Refresh Gadgets in the Random Probing Model"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2015"
summary: "Masking is a standard countermeasure against side-channel attacks on embedded cryptographic implementations. Its security is commonly analyzed in the random probing model, which offers a useful trade-"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Masking is a standard countermeasure against side-channel attacks on embedded cryptographic implementations. Its security is commonly analyzed in the random probing model, which offers a useful trade-off between realistic leakage assumptions and tractable security proofs. Recent years have seen the emergence of several masking compilers based on compositional security frameworks such as general/cardinal random probing composability (RPC). Most of these approaches rely on dedicated refresh gadgets whose structure is often tightly coupled to the targeted security analysis. In this work, we investigate the impact of refresh gadgets on the random probing security of masking compilers within the recent general/cardinal RPC frameworks. We formalize two broad families of refresh gadgets, namely direct and zero encoding-based refreshes, define ideal constructions for both families under explicit randomness and uniformity conditions, and extend the compositional analysis of zero encoding-based refreshes. We then introduce an atomic refresh function capturing the core operation underlying most refresh gadgets from the literature. This abstraction allows us to express and analyze existing constructions within a unified framework, derive their cardinal/general RPC envelopes, and obtain analytical formulas for several of them. Finally, we compare ideal and concrete refresh gadgets on masked implementations of AES and Raccoon. Our results provide a systematic comparison of the security-complexity trade-offs achieved by current refresh strategies.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2015) | 2026-09-14
