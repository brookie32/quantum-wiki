---
title: "Good Stabilizer Codes from Shallow Clifford Circuits with Random Matchings"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18536"
summary: "arXiv:2608.18536v1 Announce Type: new Abstract: Encoding quantum information with low circuit overhead is a fundamental challenge in fault-tolerant quantum computation. Random circuits provide a natur"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18536v1 Announce Type: new Abstract: Encoding quantum information with low circuit overhead is a fundamental challenge in fault-tolerant quantum computation. Random circuits provide a natural mechanism for rapidly spreading logical information through simple gates applied in parallel. Brown and Fawzi showed that random Clifford circuits on two-qubit Clifford gates provide such encoders that achieve the quantum Gilbert-Varshamov rate-distance tradeoff with depth O(log^3 n). We show that the same asymptotic tradeoff is attained in optimal O(log n) depth under a gate distribution with a more restricted support. For every fixed elta>0 and sufficiently large n, if frac kn < 1 - H(frac{d}{n}) - frac{d}{n}log_2 3 - elta, we can construct random circuits of depth O(log n) which define, with high probability, an [n,k] stabilizer code of distance at least d+1, which matches the Omega(log n) light-cone lower bound for linear distance encoders. Our ensemble employs a random matching circuit architecture consisting of T independent permutation-invariant layers. In each layer, the qubits are paired up by a uniformly random perfect matching, and a random independent two-qubit Clifford gate is applied to each pair. The gate distribution need not be uniform over, or even have full support on, the two-qubit Clifford group; rather, we allow for very general distributions on Clifford gates satisfying three regularity conditions. In particular, the construction can be implemented using n/2 CNOT gates on randomly matched pairs in each layer, with parallel one-qubit Clifford twirls. These regularity conditions allow us to reduce the second-moment dynamics of our random circuits to a reversible Markov chain on binary support strings. We establish logarithmic hitting-time bounds for this Markov chain and comparisons of its stationary distribution to prove the coding properties of the circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18536) | 2026-08-20
