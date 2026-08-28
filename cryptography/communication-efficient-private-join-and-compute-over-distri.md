---
title: "Communication-Efficient Private Join and Compute over Distributed Input Sets"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1812"
summary: "Private Join and Compute (PJC) enables two parties to compute aggregates over matching records from their private datasets. In this work, we focus on the inner-product variant of PJC, which computes t"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Private Join and Compute (PJC) enables two parties to compute aggregates over matching records from their private datasets. In this work, we focus on the inner-product variant of PJC, which computes the inner product over matching records from their private datasets. It has important applications such as privacy-preserving ad conversion measurement. However, existing PJC protocols assume each party holds the entire dataset, which is often unrealistic in practice, where relevant datasets are distributed across multiple data owners. No existing PJC protocols directly support distributed input sets across multiple clients, while straightforward generic approaches introduce substantial overhead. We propose an efficient approximate PJC protocol for distributed input sets while keeping the communication sublinear in the input size. Our protocol works in the semi-honest setting and uses two non-colluding servers that learn nothing beyond the final approximation. The core technical contribution is a novel adaptation of the Godel Prize-winning AMS sketch redesigned for efficient evaluation under fully homomorphic encryption. Concretely, we show a new structured randomness that can be homomorphically generated from short seeds using just 3 levels of multiplication while maintaining the best plaintext accuracy bound. Based on our optimized implementation, clients can insert each input element into an encrypted sketch in 30 ms, which has a size of 250 KB, independent of input size. The servers can recover the final output within seconds, orders of magnitude faster than the generic method.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1812) | 2026-08-27
