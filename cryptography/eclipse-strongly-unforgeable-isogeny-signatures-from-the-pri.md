---
title: "ECLIPSE: Strongly Unforgeable Isogeny Signatures from the Prime-Degree Variant of PRISM"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2312"
summary: "ECLIPSE is the prime-degree signature construction that the PRISM authors describe next to their salted scheme, with that salt, implemented. It exists because a two-dimensional isogeny signature carri"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

ECLIPSE is the prime-degree signature construction that the PRISM authors describe next to their salted scheme, with that salt, implemented. It exists because a two-dimensional isogeny signature carries an auxiliary isogeny that the hash does not bind: the SQIsign round-3 specification states that SQIsign cannot achieve strong unforgeability for this reason, and PRISM's prime-degree variant was designed without the auxiliary isogeny but published without parameters, code or a verifier that runs. This paper gives the first implementation, on the SQIsign round-3 primes: a verifier that evaluates the paper's criterion through one isogeny chain and a pull-back, a canonical wire format with a strict decoder that recovers one coefficient from two Weil pairings with no residual bits, randomisable keys, and two independent implementations that accept each other's signatures. Signatures are 206 bytes at NIST level I, within 15 bytes of SQIsign at every matched compression and message-binding state. In one session against the SQIsign reference's assembly build, signing is 2.3 times faster than the reference's and verification costs twice as much, or 1.7 times as much with the public key prepared once. This work instantiates and measures ECLIPSE and leaves a formal argument for its strong unforgeability (SUF-CMA) to future work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2312) | 2026-10-02
