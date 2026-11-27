---
title: "EpochPIR: Low Amortized Communication PIR at Near-Optimal Throughput"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3025"
summary: "Existing single-server private information retrieval (PIR) schemes face a sharp trade-off between server throughput and communication. Schemes built on SimplePIR scan the database at nearly memory ban"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Existing single-server private information retrieval (PIR) schemes face a sharp trade-off between server throughput and communication. Schemes built on SimplePIR scan the database at nearly memory bandwidth using native integer arithmetic, but require either a large client-side hint or hundreds of kilobytes of communication per query. Conversely, schemes based on fully homomorphic encryption (FHE), such as Spiral, require only a few to tens of kilobytes per query, but process the database several times more slowly. We present EpochPIR, a single-server PIR scheme that achieves amortized communication comparable to Spiral’s while maintaining server throughput close to SimplePIR’s. Our starting point is the observation that SimplePIR queries do not require independent secrets: under a fixed public matrix, the d negacyclic rotations of a single ring-LWE (RLWE) secret can safely serve as the secrets for d consecutive queries under the standard RLWE assumption. Uploading a single encrypted secret once every d queries allows the server to precompute the homomorphic hint-products for the entire batch of d queries, eliminating the per-query homomorphic hint evaluation of prior hintless schemes. Because the rotated secrets form a negacyclic Toeplitz matrix, the server can evaluate all d encrypted hint-products simultaneously in quasilinear time using two-dimensional number-theoretic transforms, producing the results directly in packed RLWE ciphertexts. This yields a modular two-stage framework: a SimplePIR-based column selector reduces PIR over the entire database to homomorphic selection over a single encrypted column, and any FHE row selector using long-lived client evaluation keys can then compress that column into a compact response with minimal impact on overall throughput. Instantiated with a Spiral-style CMUX row selector, EpochPIR retrieves a 256-byte entry from an 8 GB database with 74 KB of communication per query at a sustained single-core throughput of 10.7 GB/s, 77% of SimplePIR’s, without a clientside hint. A communication-optimized variant communicates only 26 KB per query, 41× less than the hintless ReinsPIRe at 97% of its throughput and 25% less than Spiral at 14× its throughput.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3025) | 2026-11-24
