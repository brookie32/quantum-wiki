---
title: "A Hybrid BP-SAT Attack on MILENAGE: Combining the Complementary Strengths of Algebraic and Soft-Analytical Side-Channel Attacks"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2487"
summary: "Profiled side-channel attacks combine noisy leakage predictions with the mathematical relations imposed by the target algorithm to recover secrets from a small number of observations. Two established "
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Profiled side-channel attacks combine noisy leakage predictions with the mathematical relations imposed by the target algorithm to recover secrets from a small number of observations. Two established approaches are algebraic side-channel analysis (ASCA), which encodes leakage predictions and algorithmic relations as a Boolean satisfiability (SAT) problem, and soft-analytical side-channel analysis (SASCA), which performs probabilistic inference over a factor graph using belief propagation (BP). We evaluate both on the AES-based MILENAGE authentication algorithm deployed on USIM cards, targeting the first AES-128 invocation on mathit{RAND}oplusmathit{OPc} under the subscriber key K, where mathit{OPc} is an operator-specific secret unknown to the attacker. Neural networks predict posterior probability distributions over the AES S-box output byte values across multiple rounds and these predictions are supplied to ASCA and SASCA to recover K and mathit{OPc} from a single trace. SASCA recovers both secrets in 87.7% of attacks, but converges to an incorrect mathit{OPc} in 6.1% of cases despite recovering K correctly. ASCA enforces global consistency and resolves this ambiguity, but it succeeds in only 34% of attacks under a 1-hour timeout and our constraint-selection strategy. Motivated by these complementary failure modes, we combine the two into a hybrid attack in which BP refines the neural network predictions before they are supplied to the SAT solver. The hybrid approach recovers both secrets in 93.8% of single-trace attacks, resolving all cases where SASCA recovers K correctly but mathit{OPc} incorrectly. It has a higher success rate and a lower average runtime than either method alone, despite performing more work per attack. Finally, we suggest a countermeasure, based on masking each AES round key with an independent, per-device secret, that reduces an attacker's advantage over guessing K and mathit{OPc} to zero bits, and confirm empirically that it defeats the hybrid attack in all evaluated cases.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2487) | 2026-10-14
