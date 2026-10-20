---
title: "From if to Oops: Turning a conditional into a key-recovery oracle"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2542"
summary: "Deterministic variants of CSIDH remove randomness from the group action, either through implementation techniques or, as in Houben's deterministic CSIDH and OSIDH-LD, by design. Since earlier fault at"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Deterministic variants of CSIDH remove randomness from the group action, either through implementation techniques or, as in Houben's deterministic CSIDH and OSIDH-LD, by design. Since earlier fault attacks on CSIDH mostly target random point sampling, determinism seems to close that avenue. We show that it opens another: every secret-dependent step occurs at a fixed, public point of every execution, so an attacker can fault the same step repeatedly. Our attack forces the mask that selects which of two lanes computes the next isogeny to zero, for example by skipping one instruction. Whether the output changes reveals whether a secret exponent reaches a chosen threshold, and a binary search over these thresholds recovers the full key with one fault per execution: at most 297 oracle queries for OSIDH-LD and 222 for deterministic CSIDH with CSIDH-512-sized keys. We recover full OSIDH-LD keys in a software fault simulation of the reference implementation, and show on a ChipWhisperer-Lite that the targeted instruction is skipped with probability at least 0.94 at an isolated fault position. Finally, we argue that fault resistance requires giving up determinism, and propose countermeasures relying on randomization.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2542) | 2026-10-19
