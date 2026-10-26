---
title: "A Kelsey–Kohno Attack Variant against SHA-2 Message Digests in HSS/LMS and XMSS"
date: "2026-10-25"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2635"
summary: "We present a multi-target second-preimage attack on the message hashing of the stateful hash-based signature schemes HSS/LMS and XMSS with SHA-256 and with the truncated SHA-256/192. The attack builds"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

We present a multi-target second-preimage attack on the message hashing of the stateful hash-based signature schemes HSS/LMS and XMSS with SHA-256 and with the truncated SHA-256/192. The attack builds on the herding technique of Kelsey and Kohno: the attacker takes the chaining states that follow the per-signature prefixes of many collected signatures and merges them, level by level through state collisions, into a single chaining state. From that state one search serves all collected signatures at once, which defeats the commitment to the key and to the one-time-signature leaf index at the start of the hash input that is meant to rule out multi-target attacks. The search can match the final digests, which is the better choice against SHA-256/192, or, after appending a Kelsey-Schneier expandable message, the internal chaining states of long signed messages, which is effective for full SHA-256. For SHA-256 with NIST's bound of 2^{64} signatures, which may be spread over any number of keys, the cost in compression-function calls falls from the nominal 2^{256} to about 2^{166} for messages of up to 4 GiB and to about 2^{156} in the formal limit of maximal message length, a loss of 100 bits. For SHA-256/192, digest matching costs about 2^{153} for 2^{64} signatures of any length, a loss of 39 bits. Because the attack pools signatures across keys, even the first signature of an individual key contributes to a potential overall exposure of an ecosystem. The attacks exploit the chaining state of SHA-256, which is narrower than twice the targeted security level; the SHAKE256 parameter sets are not affected.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2635) | 2026-10-25
