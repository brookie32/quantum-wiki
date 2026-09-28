---
title: "Oracle Distillation"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31596"
summary: "arXiv:2609.31596v1 Announce Type: new Abstract: Learning and sensing are among the most promising applications of quantum technology, often with provable quantum advantages. In any realistic experimen"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31596v1 Announce Type: new Abstract: Learning and sensing are among the most promising applications of quantum technology, often with provable quantum advantages. In any realistic experiment, however, noise threatens to erase these advantages as the problem size grows. We introduce oracle distillation, a procedure that distills many queries to a noisy oracle into a single high-fidelity oracle. Here the oracle, an unknown unitary from a known family, models the interface through which a quantum device learns about an unknown system. We construct an explicit protocol that distills any Boolean oracle, both under adversarial noise that corrupts a constant fraction of the input qubits and under i.i.d. depolarizing noise at a constant rate on every qubit. At the heart of the protocol is the weak query, in which the device deliberately queries the oracle only weakly, trading response strength for the ability to correct errors. Our protocol is near-optimal among all protocols that distill the oracle while keeping its errors correctable, revealing a fundamental tension between these two requirements. An important implication of the protocol is a threshold theorem: every Boolean oracle problem whose quantum advantage is polynomial in the domain size, including Grover search, k-forrelation, and Simon's problem, retains a quantum advantage whenever the per-qubit depolarizing rate is below a constant threshold. In particular, the quadratic quantum advantage of Grover search, long believed fragile under noise, survives nearly intact at low error rates even when almost every query involves errors on one or more qubits. We further extend the protocol to fractional and continuous-time Boolean oracles. Quantum error correction can thus protect not only prescribed operations but also unknown dynamics. Our results make a large family of quantum advantages in learning robust against noise and open a path toward robust computational sensing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31596) | 2026-09-28
