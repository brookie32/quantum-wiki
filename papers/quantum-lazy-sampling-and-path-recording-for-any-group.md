---
title: "Quantum Lazy Sampling and Path Recording for Any Group"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.30281"
summary: "arXiv:2606.30281v2 Announce Type: replace Abstract: A central challenge in quantum algorithms and cryptography is reasoning about algorithms with oracle access to a random group element (e.g. a random"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2606.30281v2 Announce Type: replace Abstract: A central challenge in quantum algorithms and cryptography is reasoning about algorithms with oracle access to a random group element (e.g. a random function, permutation, or unitary). Can we efficiently simulate such algorithms? Can we determine what they know after t queries? A classical tool for this is lazy sampling: the oracle does not commit to the full group element upfront, but rather samples partial information about it on the fly. We study a quantum analog of lazy sampling: compressed oracles (or recording oracles). These are quantum data structures that allow on-the-fly simulation for quantum queries, originally introduced by Zhandry (CRYPTO '19) for random functions, and generalized to unitaries by Ma-Huang (STOC '25) and permutations by Carolan (STOC '26), and used to great effect in security proofs and lower bounds due to their interpretability. We define and analyze a general-purpose and interpretable path-recording oracle, derived from first principles, that perfectly simulates random elements of any closed subgroup of U(N). Our oracle stores, in superposition, t input-output pairs, with updates described in terms of the commutant of the group's tensor power representation. This transparently records the information the algorithm has learned. Our oracle builds on recent work of Grinko-Yoshida (QIP '26), who gave a different general-purpose compressed oracle without clear interpretability. One interesting application of our path-recording is allowing direct comparisons between compressed oracles of different groups, giving a new technique for proving pseudorandomness results. For example, comparing S_N and U(N) yields what is arguably the simplest construction to date of pseudorandom unitaries: the product PC of a pseudorandom permutation and a random Clifford, improving on the prior PFC construction (Metger-Poremba-Sinha-Yuen, FOCS '24; Ma-Huang, STOC '25).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.30281) | 2026-10-01
