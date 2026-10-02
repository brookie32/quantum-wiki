---
title: "Time-space lower bounds for breaking quantum cryptography"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02101"
summary: "arXiv:2610.02101v1 Announce Type: new Abstract: We prove near-optimal time-space lower bounds for breaking quantum cryptography in the random oracle model. Specifically, we show that a T-query adversa"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.02101v1 Announce Type: new Abstract: We prove near-optimal time-space lower bounds for breaking quantum cryptography in the random oracle model. Specifically, we show that a T-query adversary with S qubits of non-uniform advice can recover a random key k from the n-qubit binary phase state |psi_krangle propto sum_{x} R(k,x) |xrangle with probability at most O(frac{T^2 + sqrt{ST}}{N}) for N=2^n. In contrast, the best known bound for post-quantum one-way functions is O(frac{T^2 + ST}{N}), with a trivial attack at S = N. This demonstrates a new advantage of quantum cryptography over classical cryptography: n qubits of communication suffice for security against preprocessing attacks with space up to N^2 rather than N. Our methodology is simple: express the optimal preprocessing attack as the operator norm of a random matrix, and bound this value in expectation over the random oracle via the trace-moment method. These trace moments have a natural interpretation using compressed oracles [Zhandry, Crypto 2019], which we then analyze. This can be viewed as a simplification and generalization of the approach of Liu [Eurocrypt 2023] for proving time-space tradeoffs for breaking post-quantum cryptography. We also prove the following results: (1) We tighten Liu's analysis of post-quantum PRGs in QROM, achieving a distinguishing advantage bound of O(frac{T^2}N + sqrt{frac{ST}N}). (2) For unitary synthesis, we extend the one-query lower bound of Lombardi-Ma-Wright [STOC 2024] to hold against adversaries that can make one arbitrary function query along with polynomially many (adaptive) queries to the random oracle, either before or after the function query. This also interprets the original LMW24 result in terms of compressed oracles. (3) Finally, we prove a tight O(frac{sqrt{S}}N) bound for the pseudorandomness of random binary phase states against space S distinguishers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02101) | 2026-10-02
