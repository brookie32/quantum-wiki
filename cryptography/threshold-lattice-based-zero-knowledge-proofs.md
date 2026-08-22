---
title: "Threshold Lattice-Based Zero-Knowledge Proofs"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1750"
summary: "Lattice-based zero-knowledge proofs are now efficient enough for practical use, but in all known constructions a single prover holds the entire witness and is therefore a single point of failure. Thre"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Lattice-based zero-knowledge proofs are now efficient enough for practical use, but in all known constructions a single prover holds the entire witness and is therefore a single point of failure. Thresholdizing them is understood only for three-round Sigma-protocols, which certify shortness only extit{approximately}. The extit{exact} statements needed by applications such as anonymous credentials require more rounds and rely on rejection sampling, and neither property survives thresholdization. We construct the first lattice-based threshold zero-knowledge proof systems for exact relations. The witness is Shamir-shared among mathtt{n} parties, any mathtt{t} of them can jointly produce a proof, and the proof has the same form as a single-prover proof, only a factor sqrt{mathtt{t}} larger, with verification unchanged. We thresholdize the product proof of Attema, Lyubashevsky, and Seiler (CRYPTO 2020) and the exact proof of Esgin, Nguyen, and Seiler (ASIACRYPT 2020), making both rejection-free using Hint-MLWE and evaluating them over threshold homomorphic encryption. We define threshold commit-and-prove protocols with the corresponding zero-knowledge and simulation-extractability notions, and prove our constructions secure against passive adversaries that statically corrupt at most mathtt{t}-1 parties. Of independent interest, we show that the Fiat--Shamir transforms of both proof systems are simulation-extractable in the random oracle model, and that MLWE remains hard when secrets are drawn from the subring fixed by a ring automorphism.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1750) | 2026-08-20
