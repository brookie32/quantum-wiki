---
title: "RubriQ: Rubric-Guided Group Relative Policy Optimization for Constraint-Aware Quantum Circuit Synthesis"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.07554"
summary: "arXiv:2607.07554v2 Announce Type: replace Abstract: Quantum circuits are crucial for understanding quantum algorithms and must be correct and efficient on quantum processing units (QPUs). Reinforcemen"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2607.07554v2 Announce Type: replace Abstract: Quantum circuits are crucial for understanding quantum algorithms and must be correct and efficient on quantum processing units (QPUs). Reinforcement learning (RL) with verifiers can train large language models (LLMs) to synthesize circuits; however, the reward system is unclear. In this study, we present RubriQ, a quantum rubric, where a verifier ensures correctness and scores assess cost. We demonstrate that, leveraging group relative policy optimization, the verifier controls correctness, while scores rank correct circuits. Our evaluation includes unitary, statevector, stabilizer-tableau, and randomized verifiers consisting of quantum Fourier transform (QFT), phase-estimation (QPE), and Trotter unitaries, along with Clifford, entanglement, unitary, arithmetic, and adder quantum circuits, up to 192 qubits. Our results show that training increases correct outputs from 7% to 91%, whereas the binary reward closes less than 10%. Notably, among verified circuits, the rubric reduces average cost by 91%. We believe our framework provides valuable insights into practical quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.07554) | 2026-11-26
