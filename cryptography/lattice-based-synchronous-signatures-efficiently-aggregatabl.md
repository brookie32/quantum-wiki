---
title: "Lattice-Based Synchronous Signatures: Efficiently Aggregatable and Thresholdizable"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2121"
summary: "Aggregate signatures play an important role in proof-of-stake systems, where many validators sign a block. There is a strong desire to aggregate all these signatures into one short signature that is f"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Aggregate signatures play an important role in proof-of-stake systems, where many validators sign a block. There is a strong desire to aggregate all these signatures into one short signature that is fast to verify. Since all validators know the block number they are signing, this setting is well suited for synchronous (a.k.a stateful) signatures. Boneh and Kim (2019) showed that lattice-based one-time signatures (OTS) can be aggregated very efficiently. The Chipmunk and Lemur signature schemes extend this to an ell-time synchronous scheme using a (homomorphic) Merkle tree of ell one-time public keys. Each leaf of the tree is used to sign one message, and these one-time signatures can be aggregated across many signers. Due to the Merkle tree, every aggregate signature includes a Merkle authentication path of length O_lambda(log ell). We present a different lattice-based approach to constructing a synchronous aggregate signature scheme. The length of an aggregate signature in our scheme is independent of ell. The resulting signatures are asymptotically shorter than existing schemes, and concretely shorter for some parameter choices. The resulting signature verification algorithm is algebraic, which makes it amendable to efficient threshold signing. Moreover, we are able to prove security in an adaptive corruption model. We thus obtain an efficient lattice-based synchronous threshold signature scheme, where signatures from many signers can be aggregated into a single short signature. The scheme relies on a one time trusted setup to generate the public parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2121) | 2026-09-20
