---
title: "A General Approach to Adaptor Signatures"
date: "2026-09-04"
updated: "2026-09-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1889"
summary: "Adaptor signatures have emerged as a powerful contract-minimal mechanism for fair exchange on blockchains, enabling efficient and privacy-preserving atomic swaps and conditional payments. However, exi"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

Adaptor signatures have emerged as a powerful contract-minimal mechanism for fair exchange on blockchains, enabling efficient and privacy-preserving atomic swaps and conditional payments. However, existing adaptor schemes are limited to narrow classes of NP relations (e.g., discrete logarithm secrets) and specific signature schemes, limiting their scope both in terms of constructions and applications. This work addresses this gap by presenting a new framework that supports arbitrary NP relations and a broad range of signature schemes, significantly extending the reach of adaptor signatures beyond prior works and broadening the design space for adaptor signature constructions. Our framework also yields adaptor signatures that are compatible with today's blockchain systems. More specifically, we devise two general compilers for adaptor signatures. First, we show how to efficiently lift adaptor signatures from structured languages (such as discrete log relations) to general NP languages with the help of degree-2 homomorphic encryption, resulting in adaptors for standard signature schemes and general NP languages. Secondly, we develop a compiler that transforms any signature scheme with a subliminal channel into an adaptor signature scheme for general NP languages using circuit-private fully homomorphic encryption. Signatures with subliminal channels enable the encoding of witnesses in the signing randomness, and include randomness-recoverable schemes like Schnorr, ECDSA, CL, BBS, as well as salted versions of deterministic signatures schemes like BLS and RSA. Both constructions achieve a novel property called statement truth privacy, which guarantees that a buyer learns nothing about the underlying statement, not even its truth, unless the protocol successfully completes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1889) | 2026-09-04
