---
title: "TATVA: A Reinforcement Learning Framework for Quantum Circuit Synthesis"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00945"
summary: "arXiv:2610.00945v1 Announce Type: new Abstract: One of the most important initial steps in quantum computing is high-fidelity quantum state preparation, because errors in it can affect the final compu"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00945v1 Announce Type: new Abstract: One of the most important initial steps in quantum computing is high-fidelity quantum state preparation, because errors in it can affect the final computational result. Therefore, one of the major challenges is to design a quantum circuit that can achieve the desired target state accurately with a smaller number of gates. Traditionally, circuits are designed using predefined rules and mathematical decompositions, but this makes it difficult to design circuits for different and complex target states. This paper presents TATVA, a reinforcement learning (RL) system for synthesizing quantum circuits. TATVA views circuit synthesis as a sequential decision problem in which the agents select one gate at a time and calculate the fidelity after each applied gate, with the gate producing the highest fidelity selected for the circuit. The system introduces a parallel architecture that uses two RL agents, Deep Q-Network (DQN) and Proximal Policy Optimization (PPO), along with Qiskit's statevector simulator. The system can synthesize up to 5 qubits while achieving a fidelity of 0.999999 and producing compact circuits. After achieving the desired fidelity, it performs a post-hoc optimization step that reduces the circuit depth while preserving the achieved fidelity. The circuit is finalized using fidelity, success rate, gate count, and circuit depth. Target states that are not used during training are used to test whether the system has learned effectively and can generalize beyond the training states. This approach aims to enable automatic quantum circuit synthesis with high fidelity using reinforcement learning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00945) | 2026-10-02
