---
title: "Quantum Homomorphic Encryption: Towards Practical QOTP-Encrypted Computation on Gate-Based Hardware"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.19256"
summary: "arXiv:2604.19256v2 Announce Type: replace Abstract: As quantum computing moves toward remote and cloud-based access, protecting quantum data during outsourced execution becomes important. Quantum one-"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2604.19256v2 Announce Type: replace Abstract: As quantum computing moves toward remote and cloud-based access, protecting quantum data during outsourced execution becomes important. Quantum one-time pad (QOTP) encryption provides information-theoretic hiding of quantum state, but evaluating gates on Pauli-encrypted data is nontrivial: Clifford operations allow classical Pauli-frame updates, whereas non-Clifford operations require key-dependent corrections. We introduce QOTPH, a client-side key-tracked compilation framework for encrypted quantum computation. The client retains the QOTP keys and transforms each operation into a corrected gate or decomposition. The resulting circuit is executed non-adaptively by the quantum server, which neither receives the keys nor performs key updates. We develop a unified Pauli frame compilation layer spanning Clifford operations, one- and two-qubit Pauli-generated rotations, explicit key-dependent parametrized controlled rotations, and recursively composed gates, and establish a global correctness result for circuits composed of the formally verified primitive rules. We also characterize the evaluator's view under a hidden logical circuit model, in which the QOTP frame, the uncompiled logical circuit, and the logical-to-physical instruction mapping remain client-side; the security of this model against various algorithms is also analyzed. The implementation is evaluated in Qiskit using noiseless simulation and IBM Quantum hardware, including in-circuit and local-decryption workflows. This work bridges the gap between algebraic QOTP key tracking and practical encrypted quantum computation by providing a unified, hardware-validated compilation framework for current gate-based quantum processors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.19256) | 2026-09-16
