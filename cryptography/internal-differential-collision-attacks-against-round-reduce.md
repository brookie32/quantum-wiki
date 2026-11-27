---
title: "Internal Differential Collision Attacks against Round-Reduced SHA-3"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3041"
summary: "The sc{Keccak} hash function was selected by NIST as the winner of the exttt{SHA-3} competition in 2012 and was adopted as the exttt{SHA-3} hash standard of NIST in 2015. This paper focuses on interna"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The sc{Keccak} hash function was selected by NIST as the winner of the exttt{SHA-3} competition in 2012 and was adopted as the exttt{SHA-3} hash standard of NIST in 2015. This paper focuses on internal differential collision attacks on round-reduced exttt{SHA-3} and various sc{Keccak} variants. Inspired by the work of Dinur, Dunkelman and Shamir in 2013, we propose an improved variant of internal differential cryptanalysis as well as a new target internal difference algorithm by probabilistic linearization. More exactly, we improve the internal differential cryptanalysis by abstracting new concepts such as differential transition conditions and differential transition system, and propose conditional internal differentials to reduce the complexity of the first two rounds. In terms of Sbox linearization, we proposed full Sbox linearization and probabilistic Sbox linearization techniques for internal differentials. We also exploit new strategies for optimizing the internal differential characteristic. Furthermore, we determine the expected size of collision subsets in internal differentials, by analyzing the collision probability of the digests rather than the intermediate states input to the last nonlinear layer. These techniques enhance the analysis of internal differentials, leading to the best theoretical collision attacks on nine sc{Keccak} instances, including six round-reduced instances of exttt{SHA-3} and three instances of sc{Keccak} contest. Specifically, the number of attacked rounds is extended to 5 from 4 for exttt{SHA3-384}, and the attacks on 4-, 5- and 6-round exttt{SHAKE256} are the first collision attacks on reduced exttt{SHAKE256}. We also present the best collision attacks for 4-round exttt{SHA3-512} and 6-round exttt{SHAKE128}. For the sc{Keccak} contest, we propose theoretical collision attacks on up to 6 rounds, and successfully reduce the complexity of one previously unbroken instance to 2^{53}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3041) | 2026-11-25
