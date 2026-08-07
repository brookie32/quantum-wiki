---
title: "Quantum Error Management in Practice: A Cross-Stack Benchmark"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05202"
summary: "arXiv:2608.05202v1 Announce Type: new Abstract: Quantum processors have crossed the one-hundred-qubit mark, but noise continues to limit circuit performance, while full quantum error correction remain"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05202v1 Announce Type: new Abstract: Quantum processors have crossed the one-hundred-qubit mark, but noise continues to limit circuit performance, while full quantum error correction remains too costly for routine use. Error suppression and mitigation therefore play an important role in extracting value from current hardware, yet independent comparisons of commercial solutions on identical workloads and devices remain scarce. We benchmark IBM Qiskit Runtime, Q-CTRL Performance Management, and Qedma QESEM on IBM Pittsburgh, a 156-qubit IBM Quantum Heron r3 processor. For Sampler workloads, we run Bernstein-Vazirani, quantum phase estimation, GHZ-state preparation, and randomized mirror circuits with up to 100 measured qubits, comparing raw execution, IBM measurement twirling, and Q-CTRL. For Estimator workloads, we measure chain-averaged magnetization and correlation observables of an eight-layer transverse-field Ising circuit at 25, 50, and 75 qubits against an exact matrix-product-state reference, comparing IBM raw execution, IBM TREX plus twirling, Q-CTRL, and QESEM. Q-CTRL produced the best results on the three structured Sampler workloads while keeping reported QPU times within the same order as the IBM configurations. Across six Ising observable and system-size cases, aggregate mean absolute error was 0.0883 for IBM raw execution, 0.0807 for IBM TREX plus twirling, 0.0285 for Q-CTRL, and 0.0188 for QESEM. Relative to raw execution, Q-CTRL and QESEM reduced aggregate error by factors of 3.10 and 4.70, respectively, while QESEM used 7.5 to 11.1 times the reported QPU time of Q-CTRL. These results show that managed error suppression and mitigation can substantially improve current hardware performance, but with distinct accuracy and execution-time tradeoffs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05202) | 2026-08-07
