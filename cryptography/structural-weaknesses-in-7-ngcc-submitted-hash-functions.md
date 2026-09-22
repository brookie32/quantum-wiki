---
title: "Structural Weaknesses in 7 NGCC Submitted Hash Functions"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2152"
summary: "The Institute of Commercial Cryptography Standards (ICCS) launched the Next-generation Commercial Cryptographic Algorithms Program (NGCC) and invited worldwide comments on draft submission requirement"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The Institute of Commercial Cryptography Standards (ICCS) launched the Next-generation Commercial Cryptographic Algorithms Program (NGCC) and invited worldwide comments on draft submission requirements and evaluation criteria for cryptographic hash algorithms. Our analysis of seven submitted hash functions gives the following results: - Message differences that cancel in every key injection give explicit collisions for all four fixed-output variants of extbf{MoFang} and both XOF variants at every finite output length. - Two distinct states of extbf{Neulaser} become equal after one update, giving collisions for all three variants with the initialization used by the v2 reference and optimized implementations. - An invariant subspace of extbf{CHIME-512} permits collision search using at most (2^{64}) hash evaluations when shifts act separately on 64-bit words, as in both submitted implementations. - extbf{CHAMP}'s determinant constraint gives collision searches using at most (2^{192}) and (2^{384}) hash evaluations for its 512- and 1024-bit variants, respectively. - The core permutation of extbf{QSH} acts on (64w) bits and preserves a binary subspace of dimension (16w) through all rounds, where (w) is the word size. - Both version of extbf{WChain} message expansions preserve invariant sets and admit schedules with periods one, three, and six through all prescribed rounds and final whitening. - A cyclic shift of eight binary coordinates describes extbf{Cuishen}'s message expansion on 256 register values throughout all 64 rounds. For fixed initial chaining and counter registers, the XOR differences between round keys have periods dividing eight. The stated evaluation budgets for extbf{CHIME-512} and extbf{CHAMP} give success probabilities greater than (0.39). keywords{Hash functions and Cryptanalysis and Collision attacks and Invariant subspaces and Message expansion}

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2152) | 2026-09-22
