---
title: "Towards the Impossibility of Imperfectly Complete Key Agreement in the QROM"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17610"
summary: "arXiv:2608.17610v1 Announce Type: new Abstract: We make progress towards the impossibility of imperfectly complete quantum-computation, classical-communication (QCCC) key agreement by constructing the"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17610v1 Announce Type: new Abstract: We make progress towards the impossibility of imperfectly complete quantum-computation, classical-communication (QCCC) key agreement by constructing the first unconditional attacks on quantum key agreement in the following restricted settings. In the two-message setting, we assume that Alice makes only classical queries to the oracle in the first round and that her message to Bob is classical, but otherwise both parties may perform arbitrary quantum computation, make quantum queries, and send a quantum state in the second round. Our attack and analysis are based on the heavy-query learning techniques from Austrin et al. (CRYPTO 2022) and the reprogramming techniques of Katz and Sela (arXiv 2401.14319). In the round-independent setting, we show that the attack of Barak and Mahmoody (CRYPTO 2009; J. Cryptology 2017) can be extended to multiple rounds when Alice and Bob share classical communication and make only classical queries in all but the final round. In both settings, the attacker is computationally unbounded and makes poly(lambda) queries to recover the key whenever each honest query bound is at most poly(lambda) and the valid agreement probability is inverse-polynomial. As a consequence, we rule out imperfectly correct quantum public-key encryption for classical messages whose length is bounded by a polynomial in lambda in the QROM when key generation has classical oracle access, even if encryption, decryption, and the ciphertext are quantum. In particular, the one-bit case applies to the imperfectly correct PKE obtained from two-round OSP by Bartusek and Khurana (CRYPTO 2025) whenever the classical OSP sender makes only classical random-oracle queries.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17610) | 2026-08-19
