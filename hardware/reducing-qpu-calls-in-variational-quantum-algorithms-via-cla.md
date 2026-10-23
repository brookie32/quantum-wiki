---
title: "Reducing QPU Calls in Variational Quantum Algorithms via Classical Offloading of Gradient Computation"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.16361"
summary: "arXiv:2503.16361v3 Announce Type: replace Abstract: Variational quantum algorithms (VQAs) are a promising approach for leveraging near-term quantum computers, but trainability and quantum-resource cos"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2503.16361v3 Announce Type: replace Abstract: Variational quantum algorithms (VQAs) are a promising approach for leveraging near-term quantum computers, but trainability and quantum-resource costs remain major challenges. Here we address these challenges with the extbf{H}ardware extbf{E}fficient and dynamical extbf{LI}e algebra supported extbf{A}nsatz (HELIA) and two training methods combining the classical-enhanced g method with the quantum-based Parameter-Shift Rule (PSR). This distributes gradient estimation and training across classical and quantum hardware. We evaluate ground-state estimation of 6- to 18-qubit Hamiltonians using the Variational Quantum Eigensolver (VQE) and quantum phase classification for Hamiltonians up to 12 qubits. For VQE, our methods improve accuracy and success rates, with a mean reduction in estimated logical quantum evaluations of up to 60% relative to Full-PSR training of the same ansatz. For classification, the largest improvement in mean peak test accuracy relative to Full-PSR is 2.8 percentage points. We also use these methods as a warm-start pretraining strategy for Hamiltonians with exponential-dimensional dynamical Lie algebras. Gradient diagnostics for the studied Hamiltonian configurations show slower gradient-variance decay than the selected deep hardware-efficient reference over the simulated system sizes, potentially paving the way for training large-qubit quantum models.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.16361) | 2026-10-23
