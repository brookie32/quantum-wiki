---
title: "Tightly and Adaptively Secure Two-Round Threshold Signatures from DDH"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1909"
summary: "Threshold signatures enable a set of n parties to jointly generate signatures under a single public key such that any subset of at least t+1 parties can produce a valid signature, whereas any coalitio"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Threshold signatures enable a set of n parties to jointly generate signatures under a single public key such that any subset of at least t+1 parties can produce a valid signature, whereas any coalition of at most t parties cannot. They constitute a fundamental primitive for distributed trust and are widely deployed in systems such as certification authorities, blockchains, and multiparty wallets. Modern applications require strong security guarantees under realistic adversarial models, including resistance to adaptive corruptions, tight security reductions, and low interaction complexity—most notably, a minimal number of communication rounds. Recent progress has produced threshold signature schemes in pairing-free groups that achieve tight and adaptive security with three rounds of interaction. This leaves open the central question of whether one can simultaneously achieve tight security, adaptive security, and two-round signing under a standard, non-interactive hardness assumption. In this work, we resolve this question by presenting TZAR, the first two-round threshold signature scheme that is tightly and adaptively secure under the standard decisional Diffie-Hellman (DDH) assumption in pairing-free cyclic groups. Our construction achieves full adaptive security against up to t < n corruptions and admits a tight security reduction with only constant-factor loss. Consequently, TZAR provides strong provable security guarantees and minimizes interaction by requiring only two signing rounds, an important advantage for latency-sensitive distributed environments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1909) | 2026-09-07
