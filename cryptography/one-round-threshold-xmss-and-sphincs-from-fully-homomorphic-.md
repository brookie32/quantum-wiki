---
title: "One-Round Threshold XMSS and SPHINCS+ from Fully Homomorphic Encryption"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2360"
summary: "While hash-based signatures such as XMSS and SPHINCS^+ are well-established and play a key role in post-quantum cryptography, thresholdizing them to enable use in distributed systems remains a challen"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

While hash-based signatures such as XMSS and SPHINCS^+ are well-established and play a key role in post-quantum cryptography, thresholdizing them to enable use in distributed systems remains a challenge. In particular, their lack of exploitable structure prevents any algebraic attempts that are otherwise possible in the context of classical signatures such as ECDSA, Schnorr, RSA, or BLS, whereas general-purpose MPC techniques are costly in round complexity. In this work, we construct and implement the first one-round threshold protocol for XMSS and SPHINCS^+, with concrete parameters yielding full backward compatibility. At a high level, the secret key is shared among the signing parties while the signing algorithm is evaluated homomorphically using a threshold fully homomorphic encryption scheme. Any t-of-n parties, via threshold decryption, can collaboratively derive the signature, which is accepted by the unmodified RFC 8391 or FIPS 205 verifier. At a technical level, we develop efficient homomorphic SHAKE evaluation over discrete CKKS for varying batch sizes. Analyzing XMSS and SPHINCS^+ signing reveals parallel hash computations and data-dependent selections, which we handle through batching and homomorphic lookup to obtain end-to-end circuits. Our implementation amortizes SHAKE256/256 evaluation to 3.4,ext{ms} per hash and completes online threshold XMSS signing in 0.69,ext{s}. Threshold SPHINCS^+ has roughly two orders of magnitude higher signing latency but over an order of magnitude lower setup latency than XMSS.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2360) | 2026-10-05
