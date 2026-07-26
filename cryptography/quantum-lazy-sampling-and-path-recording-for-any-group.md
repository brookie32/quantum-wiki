---
title: "Quantum Lazy Sampling and Path Recording for Any Group"
date: "2026-07-23"
updated: "2026-07-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1510"
summary: "A central challenge in quantum algorithm analysis and cryptography is reasoning about algorithms with oracle access to a random group element (e.g. a random function, a random permutation, a random un"
last_verified: "2026-07-26"
review_by: "2026-10-24"
stale: false
---

A central challenge in quantum algorithm analysis and cryptography is reasoning about algorithms with oracle access to a random group element (e.g. a random function, a random permutation, a random unitary). Can we efficiently simulate such algorithms? Can we determine what they know after t queries? Classically, an important tool for this is lazy sampling, where the oracle does not commit to the full group element at the beginning, but rather samples partial information about it on the fly. We study a quantum analog of lazy sampling: compressed oracles (or recording oracles), which are quantum data structures that allow such on-the-fly simulation for quantum queries. Compressed oracles were originally introduced by Zhandry (CRYPTO '19) for random functions, were generalized to random unitaries by Ma-Huang (STOC '25) and to permutations by Carolan (STOC '26), and have been employed to great effect in security proofs and query complexity lower bounds due to their interpretability. In this work, we define and analyze a general-purpose and interpretable path-recording oracle, derived from first principles, that perfectly simulates random elements of any closed subgroup of U(N). Our path-recording oracle stores superpositions of t input-output pairs |(x_1, y_1), ots, (x_t, y_t)rangle, which encode a Feynman path explored by the algorithm and thus transparently records the information that the algorithm may have learned from its queries. Our compressed oracle builds on a recent work of Grinko and Yoshida (QIP '26), who proposed a different kind of general-purpose compressed oracle without clear interpretability. Crucially for applications, we derive an operationally useful mathematical description of our update procedure in terms of the commutant of the group's tensor power representation. One powerful feature of our path-recording oracle is that it enables direct comparisons between compressed oracles for different groups, which gives a new technique for proving pseudorandomness results. For our main application, we formally relate the S_N and U(N) compressed oracles, yielding what is arguably the simplest construction to date of pseudorandom unitaries: the product PC of a pseudorandom permutation and a random Clifford. This improves on the prior PFC construction of (Metger-Poremba-Sinha-Yuen, FOCS '24; Ma-Huang, STOC '25).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1510) | 2026-07-23
