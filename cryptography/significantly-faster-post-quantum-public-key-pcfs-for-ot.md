---
title: "(Significantly) Faster Post-Quantum Public-Key PCFs for OT"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3065"
summary: "Public-Key Pseudorandom Correlation Functions (PK-PCFs) enable N users to locally generate and publish their public keys on a bulletin board, from which any pair of users can non-interactively compute"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Public-Key Pseudorandom Correlation Functions (PK-PCFs) enable N users to locally generate and publish their public keys on a bulletin board, from which any pair of users can non-interactively compute an unbounded number of correlated strings. These outputs can then be used to significantly speed up secure computation protocols. A line of work has focused on building efficient PK-PCFs for Oblivious Transfer (OT) in the post-quantum regime. To this end, the recent work of Agrawal, Bhushan, Couteau and Riahinia (CRYPTO 2026), henceforth ABCR, introduces a family of lattice-based PK-PCFs that can generate 500-1K OTs per second. However, a significant gap remains compared to quantum-insecure counterparts: the state-of-the-art classical (group-based) PK-PCFs for (standard) OTs reach a throughput of roughly 30K OTs per second making them nearly two orders of magnitude faster. In this work, we significantly improve the state-of-the-art of post-quantum PK-PCFs for OTs. We provide a new construction whose security is based on roughly the same lattice-based assumptions as used by ABCR. In contrast, we achieve a much higher throughput; we implement our construction and measure a rate of 208k OTs/sec for the sender, and 189k OTs/sec for the receiver on a single thread, and 746k/709k on six threads. Our key sizes, remain in the megabytes, similar to ABCR. Concretely, sender and receiver respectively store keys of size 188MB and 66MB. Our speedup is obtained via a new blueprint for constructing PK-PCFs from public-key algebraic homomorphic MACs (PK-aHMACs), that we introduce and instantiate. We are optimistic that our ideas will find independent applications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3065) | 2026-11-26
