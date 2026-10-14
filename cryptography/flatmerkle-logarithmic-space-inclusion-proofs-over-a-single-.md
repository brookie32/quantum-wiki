---
title: "FlatMerkle: Logarithmic-Space Inclusion Proofs over a Single Linear Hash Stream"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2468"
summary: "Merkle trees are the standard way to obtain logarithmic-size, logarithmic-time inclusion proofs over a large dataset, but they require a tree-shaped hash structure distinct from the ordinary, linear ("
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Merkle trees are the standard way to obtain logarithmic-size, logarithmic-time inclusion proofs over a large dataset, but they require a tree-shaped hash structure distinct from the ordinary, linear (Merkle--Damgaa rd) hashing that most deployed systems -- including Bitcoin's own transaction and witness hashing -- actually perform. We present FlatMerkle, a construction that achieves the same asymptotic guarantees, O(log N) proof size and O(log N) verification time, over a single ordinary linear hash stream, by periodically re-injecting the hash function's own past internal states (``checkpoints'') back into the stream as ordinary message content. The result is a flat byte sequence whose digest is a single, unmodified invocation of the underlying hash function -- syntactically an ordinary digest of an ordinary byte string, not a distinguishable commitment format -- while still supporting compact inclusion proofs for any element, and compact proofs that a published file is malformed, so that an honest party can always answer a malicious committer in logarithmic space. We give the recursive construction, a closed-form formula locating any element in the structured stream, worked examples with illustrations, a security reduction to free-start collision resistance of the hash function's compression step, an optimal element-size analysis for both a flexible toy primitive and real SHA-256, a batched multi-element proof construction, a measured construction-speed comparison against Merkle trees, a concrete application to committing data inside a Bitcoin transaction annex (BIP-341), a design sketch using that application as a data-availability layer for an optimistic Bitcoin rollup, a from-scratch gas-cost comparison, on Ethereum, Rootstock, and Arbitrum, of an in-contract FlatMerkle commitment against an in-contract Merkle tree, tracing the three chains' differing verdicts to specific protocol design choices rather than to anything intrinsic to either construction, and a comparison against the closest prior art we are aware of, authenticated append-only skip lists.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2468) | 2026-10-14
