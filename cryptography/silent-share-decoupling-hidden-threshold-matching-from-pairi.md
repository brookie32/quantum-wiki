---
title: "Silent-Share: Decoupling Hidden Threshold Matching from Pairing Operations via Group-Valued Oblivious Key-Value Stores"
date: "2026-08-29"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1831"
summary: "Matchmaking encryption (ME) enables bilateral access control with private policies, but existing pairing-based constructions tie receiver-side authorization cost to the policy size. This is especially"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

Matchmaking encryption (ME) enables bilateral access control with private policies, but existing pairing-based constructions tie receiver-side authorization cost to the policy size. This is especially problematic when one party holds a large hidden policy while the other holds only a small attribute set. We present Silent-Share, a bilateral hidden-policy threshold access-control protocol that decouples policy representation from pairing-based authorization. The construction combines a one-sided hidden-threshold policy-based key encapsulation mechanism (PB-KEM) with a sparse group-valued oblivious key-value store (GOKVS). The GOKVS compactly encodes policy-dependent group elements, so a receiver holding attribute set A performs exactly 2|A| pairings, independent of the policy size |P| and threshold d. Total decapsulation additionally incurs a hidden-threshold reconstruction cost, characterized separately. Two independent one-sided instances are composed and bound with AES-GCM to realize bilateral authorization. We prove one-sided KEM confidentiality and policy hiding in the random-oracle model under a hidden common exponent assumption, and extend these guarantees to the bilateral composition. Our implementation on BN254 shows that, when the correct d-subset is provided, one-sided decapsulation for |A|=10 takes about 394 ms, dominated by pairing operations. The pairing-based authorization layer remains flat as |P| grows from 50 to 800, confirming the policy-size independence. The hidden-threshold reconstruction cost is reported separately and can dominate when |A| is large. Encapsulation is approximately 2--3imes faster than fuzzy matchmaking encryption across the tested parameter range.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1831) | 2026-08-29
