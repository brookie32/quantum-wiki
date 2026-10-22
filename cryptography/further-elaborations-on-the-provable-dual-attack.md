---
title: "Further Elaborations on the Provable Dual Attack"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2565"
summary: "The dual attack is one of the main strategies for attacking the learning-with-errors (LWE) problem. A recent line of work aims at provable analyses of dual attacks that rely on as few heuristic assump"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

The dual attack is one of the main strategies for attacking the learning-with-errors (LWE) problem. A recent line of work aims at provable analyses of dual attacks that rely on as few heuristic assumptions as possible. We present a provable dual attack that recovers a subvector oldsymbol{s}_{guess} of the LWE secret, and we derive an explicit lower bound on its success probability without any heuristic assumption. Our analysis unifies the provable approaches of Pouly and Shen (EUROCRYPT 2024) and Bashiri and Wiemers (J. Math. Cryptol. 2025), and removes the very few informal assumptions left in the previous works. Inspired by Qu, Tian, Wang, and Xu (ePrint 2026/2117), the dual vectors are sampled from the sublattice spanned by the first vectors of a reduced basis. Our key ingredient is a first-moment estimate for the wrong candidates, which is based on the exact uniform distribution of some appearing cosets. This leads us to discard certain typical assumptions on shortest vectors from previous works. We apply our results to ML-KEM, under one heuristic on its structured matrix, and improve on the first provable dual attack by 22 to 52 bits without any assumption on the rank of the sublattice, and by 47 to 100 bits (21 to 56 bits compared with Qu, Tian, Wang, and Xu (ePrint 2026/2117)) if this rank is bounded as in Qu, Tian, Wang, and Xu (ePrint 2026/2117). We also apply our results to ML-DSA, and demonstrate the attack experimentally on small instances. Our results do not threaten the security of ML-KEM or ML-DSA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2565) | 2026-10-20
