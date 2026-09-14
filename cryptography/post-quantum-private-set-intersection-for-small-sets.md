---
title: "Post-Quantum Private Set Intersection for Small Sets"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1985"
summary: "Are private set intersection (PSI) protocols ready for the post-quantum future? We focus on the PSI protocol of Rosulek & Trieu (``RT21'', ACM CCS 2021), which is the current state-of-the-art for PSI "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Are private set intersection (PSI) protocols ready for the post-quantum future? We focus on the PSI protocol of Rosulek & Trieu (``RT21'', ACM CCS 2021), which is the current state-of-the-art for PSI on small sets (less than a thousand items). The RT21 protocol presents some fundamental barriers to post-quantum security. First, although it is written in terms of an arbitrary KEM, it requires certain properties of Diffie-Hellman KEM that simply are not satisfied by any post-quantum candidates. Second, even if adapted to post-quantum KEMs, it would require an ideal permutation with blocklength larger than any known viable candidate. We show how to modify the RT21 to make it compatible with post-quantum KEM candidates like ML-KEM. We also describe a direct domain-extension construction for ideal permutations, showing how to construct a huge-block ideal permutation directly from one with smaller blocklength, such as the Keccak permutation family. Along the way, we also introduce new abstractions for oblivious key-value stores (Garimella et al., Crypto 2021) that make the analysis of these kinds of PSI protocols more modular. We implemented our protocol and evaluated its performance across different network settings and instantiations. We achieve PSI from standardized post-quantum primitives with latency as low as 0.25 ms/item and communication as low as 1.67 KiB/item. We find that the performance penalty for post-quantum security ranges from 1.25imes to 5.92imes in latency and is 16.7imes in communication, depending on the instantiation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1985) | 2026-09-11
