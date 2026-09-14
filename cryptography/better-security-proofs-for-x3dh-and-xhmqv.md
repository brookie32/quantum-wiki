---
title: "Better Security Proofs for X3DH and XHMQV"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1980"
summary: "The Signal protocol is used by billions of users daily and recognized as the gold standard for end-to-end encrypted messaging. Its initial handshake protocol X3DH uses XEdDSA to sign its semi-static k"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The Signal protocol is used by billions of users daily and recognized as the gold standard for end-to-end encrypted messaging. Its initial handshake protocol X3DH uses XEdDSA to sign its semi-static key and allows parties to derive a session key asynchronously. The protocol is implemented over Curve25519, relying on the assumed 128-bit hardness for solving Discrete Logarithms (DL). Previous non-tight reductions incur a large loss in the number of sessions, and the resulting concrete security guarantees fall far below the intended 128-bit security level. This motivates the development of tight security bounds for these protocols. In this paper, we improve the security analysis of X3DH and its recent enhancement XHMQV (Fiedler et al., CRYPTO'25) by providing tight security reductions under multi-user Diffie–Hellman (DH) assumptions (Kiltz et al., CT-RSA'23) in the Random Oracle Model. Unlike prior work, our proofs are in the more realistic multi-Test setting. The variant of X3DH that we analyze hashes additional context into the session key. Although this modification is minor, it yields tight security bounds and provides a stronger justification for the use of Curve25519. In light of our results, the Signal developers plan to adopt the same modification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1980) | 2026-09-11
