---
title: "Succinct Arguments with (almost) Minimal Time and Space Overheads from Symmetric-Key Primitives"
date: "2026-10-09"
updated: "2026-10-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2433"
summary: "We construct public-coin, succinct, zero-knowledge interactive arguments for NP relations decided by time-T, space-S random-access machines. Assuming the existence of collision-resistant hash function"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

We construct public-coin, succinct, zero-knowledge interactive arguments for NP relations decided by time-T, space-S random-access machines. Assuming the existence of collision-resistant hash functions, our arguments give a frontier of tradeoffs between prover time and space, and proof size. We follow the streaming PIOP+PCS framework of Block et al. (TCC 2020, CRYPTO 2021), reducing the problem of constructing time- and space-efficient arguments to time- and space-efficient streaming multilinear polynomial commitment schemes (MLPCS). We develop two code-based streaming MLPCS inspired by Brakedown (CRYPTO 2023) and BaseFold (CRYPTO 2024), implementing each scheme when additionally given succinct access to the underlying encoding matrices. We instantiate this framework assuming row-sparse, column-sparse, and Reed-Solomon encoders, then apply a generic PIOP + MLPCS compiler to obtain our (zero-knowledge) time- and space-efficient arguments. Finally, as all our protocols are public-coin, applying Fiat-Shamir yields time- and space-efficient (zk)SNARKs from symmetric-key primitives (i.e., collision-resistant hashing). Our Brakedown-based constructions have (O(log T)) rounds and (widetilde O(sqrt T))-size proofs and verification time, with two complementary prover profiles: (i) (widetilde O(S)) space (which is optimal) and (widetilde O(T^{3/2})) time, and (ii) (widetilde O(T)) time (nearly optimal) and (widetilde O(S+sqrt T)) space. Our BaseFold-based constructions achieve polylog(T) proof size and verification time with (O(log T)) rounds. We again obtain two complementary prover profiles: (i) an encoder parameterized construction with (widetilde O(T+T_{Enc})) time and (widetilde O(S + S_{Enc})) space, where (T_{Enc}, S_{Enc}) are the running time and space of a streaming log-space encoder for a suitable linear code, and (ii) an unconditional sub-quadratic instantiation (widetilde O(T^{3/2})) time and (widetilde O(S+sqrt T)) space.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2433) | 2026-10-09
