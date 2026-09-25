---
title: "On the Cryptographic Structure Required for Verifying Qubits"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.05527"
summary: "arXiv:2606.05527v2 Announce Type: replace Abstract: Classically testing for the presence of anti-commuting operators on a quantum device is a critical tool underpinning recent progress in classical ve"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2606.05527v2 Announce Type: replace Abstract: Classically testing for the presence of anti-commuting operators on a quantum device is a critical tool underpinning recent progress in classical verification of quantum computation. While such tests can be based on cryptographic assumptions, known constructions rely on highly structured assumptions, e.g. trapdoor claw-free functions. In this work, we seek to explain this state of affairs by constructing strong cryptography from (certain forms of) classical tests of anti-commutation. In particular, we formulate the notion of a test of non-commutation (ToNC), an interactive protocol between a quantum prover and classical verifier in which the prover's final-round response is obtained by measuring one of two binary observables P_0,P_1 depending on the verifier's challenge bit c. We prove that, for a broad range of parameters, ToNC implies classical-communication key agreement (KA), and ToNC combined with one-way functions implies oblivious transfer (OT). Along the way, we develop tools for and provide the first known results on hardness amplification for post-quantum KA and OT, where communication is classical but adversaries may be quantum. In particular, we prove the following results of independent interest. - Post-quantum hard-core measure theorem: For any efficiently sampleable high-min-entropy distribution D over pairs (x,b) such that quantum circuits have advantage at most elta in predicting b from x, there exists a sub-distribution Mpreceq D of density (1-elta) on which b is nearly optimally quantum-hard to predict. - Post-quantum interactive XOR lemma: Given any classically-interactive protocol, if quantum adversaries have advantage at most elta in guessing a private challenger bit b, then two sequential repetitions reduce the advantage for predicting the XOR of the challenger bits b_1oplus b_2 to at most elta^2+rm{negl}(lambda).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.05527) | 2026-09-25
