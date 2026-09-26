---
title: "Rethinking Zero-Knowledge TLS: Proof of Protocol Execution and the Reclaim Protocol"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2187"
summary: "In a zkTLS protocol, a user proves to a third party a property of data obtained from an online service over TLS, revealing nothing beyond the statement proven. Each existing scheme, however, comes wit"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

In a zkTLS protocol, a user proves to a third party a property of data obtained from an online service over TLS, revealing nothing beyond the statement proven. Each existing scheme, however, comes with its own security model, written for that scheme alone, so the schemes are not proven secure against a common definition. The root cause is a mismatch of levels: existing models are stated at the level of TLS and therefore reflect how each construction handles it. Yet TLS is only the transport, and a zkTLS proof is about the application-layer protocol executed over it. We therefore introduce the first transport-agnostic security model for zkTLS, stated at the application layer and mentioning neither TLS nor any particular construction. The resulting notion, Zero-Knowledge Proof of Protocol Execution (zkPoPE), defines what it means for a party that has executed an arbitrary two-party protocol with a counterparty to prove, in zero knowledge, that its private input and the reply it received satisfy a chosen property, and, crucially, that the reply comes from a real execution with that counterparty rather than being fabricated. This proof-of-execution requirement separates zkPoPE from a NIZK over the input--reply pair: knowing a satisfying pair does not by itself show that an execution occurred. We formalize zkPoPE as a UC ideal functionality F_{zkpope}. We then introduce the Reclaim Protocol, a zkTLS scheme that UC-realizes F_{zkpope} under a deployment-aligned trust model and underlies a production system. Reclaim builds on Distributed-AEAD, a new three-party authenticated-encryption primitive of independent interest. On a lower-mid-range phone, Reclaim attests to a 1200kB response in 7.28s, two orders of magnitude beyond any size previously benchmarked for zkTLS.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2187) | 2026-09-23
