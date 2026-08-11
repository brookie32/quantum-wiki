---
title: "Multi-agent discovery of practical quantum LDPC codes"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08996"
summary: "arXiv:2608.08996v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes can encode multiple logical qubits using sparse parity checks, yet searching for useful finite-length ins"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08996v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) codes can encode multiple logical qubits using sparse parity checks, yet searching for useful finite-length instances remains a challenging design problem because code performance must be optimized while satisfying practical constraints. Motivated by recent advances in artificial-intelligence agents for scientific discovery, we develop a multi-agent framework for discovering practical qLDPC codes. The framework combines specialist proposal and review, persistent scientific memory, long-horizon evolution of executable programs, and deterministic construction and evaluation within a closed-loop search. These programs instantiate coset-orbit balanced-product codes, providing a search space that includes bicycle and lifted-product constructions as well as non-normal subgroup actions. To incorporate practical constraints, we restrict the search to binary CSS codes with block length nleq400 and overall weight wleq10. Within this regime, the framework discovers codes with leading or competitive rate--distance performance in every weight class considered, with representative instances including [[288,16,18]] at w=7, [[288,18,18]] at w=9, and [[234,28,18]] at w=10. The search also uncovers structurally distinct, high-performing constructions, including a [[336,12,leq24]] candidate and a [[368,18,16]] code, both of which are genuine balanced-product constructions with non-normal subgroup actions. When evaluated under code-capacity depolarizing noise using a common BP-OSD decoding protocol, the discovered codes also exhibit low logical failure rates. Together, these results provide hardware-relevant finite-length candidates for further experimental evaluation and show how structured agentic search can contribute to scientific discovery.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08996) | 2026-08-11
