---
title: "Enabling Threshold Custody for the Lightning Network with Nested Threshold Multi-Signatures"
date: "2026-08-21"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1757"
summary: "The Bitcoin Lightning Network secures hundreds of millions of dollars, yet channel endpoints rely on vulnerable single online keys. Although threshold signatures are routinely used to protect on-chain"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

The Bitcoin Lightning Network secures hundreds of millions of dollars, yet channel endpoints rely on vulnerable single online keys. Although threshold signatures are routinely used to protect on-chain Bitcoin, no practical deployment has been possible for Lightning channels. This is because thresholdizing a Lightning party requires nesting a threshold signature scheme inside of an established two-party MuSig2 protocol without altering its nonce exchange or message flow. In this work, we resolve this limitation by formalizing nested threshold multi-signatures, a new cryptographic primitive for thresholdizing one participant inside a multi-signature protocol. As an instance of this primitive, we present Iceberg, the first construction for nested threshold MuSig2 signatures. Iceberg enables one side of a Lightning channel to operate as a t-of-n threshold group while appearing to the counterparty as a standard MuSig2 participant. As a result, threshold custody can be deployed unilaterally on today's Lightning Network without requiring any modifications to Bitcoin, the Lightning protocol, or channel counterparties. We prove the security of Iceberg, integrate a prototype into a production Lightning node, and benchmark its performance. Our measurements show that thresholdizing a Lightning channel incurs only modest overhead, since a threshold group tolerating one corrupted member sustains over 93% of the payment throughput of an unmodified endpoint.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1757) | 2026-08-21
