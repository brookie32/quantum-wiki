---
title: "Natural Barriers to Quantum Extraction: On the Post-Quantum (In)security of (O)EKE and Masny-Rindal OT"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39844"
summary: "arXiv:2609.39844v1 Announce Type: new Abstract: Encrypted key exchange (EKE), introduced by Bellovin and Merritt (IEEE S&P 1992), and Masny-Rindal OT, introduced by Masny and Rindal (ACM CCS 2019), ar"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39844v1 Announce Type: new Abstract: Encrypted key exchange (EKE), introduced by Bellovin and Merritt (IEEE S&P 1992), and Masny-Rindal OT, introduced by Masny and Rindal (ACM CCS 2019), are highly-efficient methods for compiling essentially any KEM into advanced cryptographic protocols, namely password-authenticated key exchange (PAKE) and oblivious transfer (OT), by relying only on idealized symmetric-key primitives. They have become leading candidates for practically-implementable PAKE and OT due to (1) their simplicity, (2) their plug-and-play nature, allowing for flexibility in the choice of KEM, and (3) existing proofs of UC-security (in the classical adversarial model). Due to point (2) above, these compilers yield attractive candidates for efficient post-quantum PAKE and OT, especially given the recent post-quantum KEM standardization efforts. This motivates the question of whether the (UC-)security of these compilers translates to the quantum adversarial model. In this work, we show that it does not. In particular, we prove that a general family of (O)EKE protocols, as well as Masny-Rindal OT, are not UC-secure against quantum polynomial-time adversaries, even when instantiated with a post-quantum KEM. To establish UC-insecurity, we devise an adversarial strategy that provably thwarts any attempt by the simulator to extract its input (the password in the case of PAKE, and the receiver's choice bit in the case of OT). To complement these negative results, we establish that both compilers yield certain notions of game-based security. Along the way, we establish a novel ``advantage-tight'' one-way to hiding lemma that may be of independent interest.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39844) | 2026-10-01
