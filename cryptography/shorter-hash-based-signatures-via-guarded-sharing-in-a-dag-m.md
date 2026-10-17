---
title: "Shorter Hash-Based Signatures via Guarded Sharing in a DAG Model"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2502"
summary: "Stateless hash-based signatures are among the most important post-quantum signature schemes. Although they have been standardized by NIST, they still have large signatures. Within these constructions,"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Stateless hash-based signatures are among the most important post-quantum signature schemes. Although they have been standardized by NIST, they still have large signatures. Within these constructions, the few-time signature component is receiving increasing attention. Recent work has introduced new techniques, including rejection sampling, forced pruning, bucket thinning, and hash chains. In this work, we continue to improve few-time signatures with a new technique, guarded sharing. Our construction moves beyond the previous tree-based model to a DAG-based signature. By combining guarded sharing with bucket thinning, hash chains, and rejection sampling, we obtain a new signature scheme called BGS-CC. Our construction further improves on the state-of-the-art few-time signature BPORS-C+BFP. Most notably, for 128-bit security and a small use quota of Q=2^{24}, it yields complete signatures of 2,228 bytes. To our knowledge, this is the first SPHINCS-based stateless signature to be shorter than the 2,420-byte signatures of the standardized module-lattice scheme ML-DSA-44.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2502) | 2026-10-16
