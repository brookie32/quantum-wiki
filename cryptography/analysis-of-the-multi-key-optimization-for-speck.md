---
title: "Analysis of the Multi-Key Optimization for SPECK"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2514"
summary: "SPECK has recently been introduced as a code-based digital signature scheme exploiting the similarities between the Permuted Kernel Problem (PKP) and the Permutation Code Equivalence Problem (PEP). By"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

SPECK has recently been introduced as a code-based digital signature scheme exploiting the similarities between the Permuted Kernel Problem (PKP) and the Permutation Code Equivalence Problem (PEP). By utilizing PEP as a trapdoor for PKP, SPECK achieves a significant speedup compared to LESS, replacing expensive Gaussian elimination with vector-matrix multiplications. This comes at the cost of larger signatures, since each round of the Zero Knowledge (ZK) protocol used in SPECK has soundness error 1/2. A well known technique to reduce the soundness errors (and thus the number of parallel repetitions and, ultimately, the signature size) in ZK proofs based on group actions consists in giving multiple elements in the public keys. Despite being constructed around an instance of PEP, which admits a natural description as a code-based group action, the protocol employed in SPECK deviates from the traditional proof of knowledge used for group actions. As shown by the authors of SPECK, a naive use of the multi-key optimization may lead to concrete security concerns. Therefore, the question on whether such a technique can be applied successfully to SPECK remains open. In this paper, we give a positive answer to such a question. We revisit the multi-key optimization for SPECK and investigate the underlying security concerns in detail, identifying conditions and parameter constraints under which multiple keys can be securely integrated into the protocol. Even though, when instantiated with conservative parameters, the multi-key optimization leads to unappealing performance, we show there is wide room for improvements. Furthermore, we design a ring signature scheme based on the same underlying construction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2514) | 2026-10-16
