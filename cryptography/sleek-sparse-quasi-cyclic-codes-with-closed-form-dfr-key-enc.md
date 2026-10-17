---
title: "SLEEK: Sparse Quasi-Cyclic Codes with Closed-Form DFR Key Encapsulation"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2512"
summary: "Performance in terms of bandwidth and execution time, as well as decoding failures remain important challenges for code-based KEMs. This paper introduces SLEEK: Sparse quasi-cycLic codEs with closEd-f"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Performance in terms of bandwidth and execution time, as well as decoding failures remain important challenges for code-based KEMs. This paper introduces SLEEK: Sparse quasi-cycLic codEs with closEd-form DFR Key encapsulation, a Key Encapsulation Mechanism (KEM) based on Quasi-Cyclic Moderate-Density Parity-Check (QC-MDPC) codes. The scheme employs a parallel bit-flipping decoder with three iterations and a closed-form estimate of the decoding-failure rate (DFR). The latter allows parameter selection with analytically bounded failure probability and supports the use of standard IND-CCA transformations. We designed two variants of SLEEK. The first, SLEEK-LT, targets IND-CCA security for long-term keys, and supports QC-MDPC codes with different rates, allowing a tradeoff between public-key and ciphertext size. The second, SLEEK-E, targets IND-CPA security for ephemeral keys in settings requiring forward secrecy. While SLEEK-LT makes conservative choices and aims at security against active attackers, SLEEK-E relies on a novel QC key structure, for which we establish security equivalent to that of the original QC-MDPC construction under the same assumptions, while reducing key-generation cost. We explore a broad design space and provide parameter sets targeting 128-, 192-, and 256-bit security, together with an 80-bit configuration for constrained embedded platforms. We also optimize polynomial inversion and parallel bit-flipping decoding, the two dominant components of the implementation. We provide quantitative benchmarks of our optimized AVX2 implementation of SLEEK. For SLEEK-LT, ciphertexts are 4.9imes smaller than those of the NIST standard choice, HQC, at the cost of a 47% increase in the runtime, and is 1.3imes to 2.7imes faster than BIKE. For SLEEK-E, execution time improves by 1.6imes over HQC with a bandwidth usage reduced by 2.1imes. Compared with Lean-BIKE, SLEEK-E is 5.3imes faster and substantially reduces the impact of decoding failures on system reliability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2512) | 2026-10-16
