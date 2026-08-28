---
title: "Dealing Haystack: Towards Trustless Haystack in the Optimistic Setting"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1804"
summary: "Hash-based constructions occupy a distinctive position among post-quantum signatures: their security reduces to well-tested properties of hash functions rather than to newer assumptions such as lattic"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Hash-based constructions occupy a distinctive position among post-quantum signatures: their security reduces to well-tested properties of hash functions rather than to newer assumptions such as lattices or isogenies. This work focuses on stateful schemes instead of stateless, because the former are considerably more efficient. However, they have the problem of state handling, since reusing a one-time key twice enables signature forgeries. Despite threshold signatures mitigate this problem by spreading trust among a set of disjoint parties, building them from hash-based schemes is difficult, since these lack the homomorphic structure needed to recombine partial signatures, and generic multiparty computation can be expensive for hash-based constructions. Kelsey, Lang and Lucks recently proposed Haystack, the first threshold scheme for hash-based signatures producing standard LMS or XMSS signatures, at the cost of a fully trusted setup and a large common reference value. We analyze Haystack along two dimensions: performance and security. First, as Haystack lacks an implementation and realistic benchmarking, we implement the protocol in Java and produce a network-aware evaluation of its viability in real deployments, concluding that it performs comparably to other post-quantum threshold schemes. Second, we relax the trust placed in the dealer. For that, we introduce a variant of the setup built on an optimistic, lightweight MPC-based partial-DKG. It does not remove the dealer's ability to forge, but it prevents it from impersonating trustees within the signing protocol, while preserving the standard signature format. Also, an optional succinct-argument layer provides public auditability. We further consider a full-DKG setting with no dealer and where the trustees run the entire setup under MPC. Both variants are implemented in MP-SPDZ and their costs have been analyzed.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1804) | 2026-08-26
