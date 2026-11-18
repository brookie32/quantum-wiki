---
title: "Randomness Certification from Statistically Hiding Commitments"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.25518"
summary: "arXiv:2610.25518v2 Announce Type: replace Abstract: Randomness certification aims to guarantee that the output of an untrusted quantum device contains genuine randomness that remains unpredictable eve"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2610.25518v2 Announce Type: replace Abstract: Randomness certification aims to guarantee that the output of an untrusted quantum device contains genuine randomness that remains unpredictable even given quantum side information held by an adversary. For a classical verifier interacting with a single quantum device, such a guarantee cannot rely on the physical separation underlying standard Bell tests and must instead follow from computational restrictions on the prover. Building on the framework of computational Bell inequalities, we distinguish classical and quantum virtual-input hiding, showing that the former suffices for proofs of quantumness, whereas the latter enables randomness certification against quantum side information. Our main technical contribution is to establish quantum virtual-input hiding for a commitment-based protocol derived from an earlier proof of quantumness (Morimae and Yamakawa, CRYPTO, 2024). We show that statistical hiding together with ordinary computational binding against quantum polynomial-time senders suffices, without requiring stronger quantum binding notions such as sum-binding or collapse-binding. This yields a randomness-certification protocol from post-quantum statistically hiding bit commitments. We give three instantiations. The NOVY commitment from any post-quantum one-way permutation yields randomness certification in the standard model with an inefficient classical verifier. Post-quantum trapdoor claw-free functions additionally provide trapdoor inversion, enabling an efficient classical verifier. In the quantum random-oracle model, a hash-based commitment yields randomness certification without additional computational assumptions, again with an inefficient verifier. These instantiations separate the cryptographic properties sufficient for randomness certification from the additional structure required for efficient verification within our commitment-based framework.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.25518) | 2026-11-18
