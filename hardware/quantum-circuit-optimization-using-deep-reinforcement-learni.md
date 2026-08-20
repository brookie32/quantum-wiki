---
title: "Quantum circuit optimization using deep reinforcement learning: Applications across multiple gate sets"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19103"
summary: "arXiv:2608.19103v1 Announce Type: new Abstract: The practical implementation of quantum algorithms on noisy intermediate-scale quantum devices encounters operational limitations due to decoherence and"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.19103v1 Announce Type: new Abstract: The practical implementation of quantum algorithms on noisy intermediate-scale quantum devices encounters operational limitations due to decoherence and other sources of noise inherent in real hardware. To mitigate these errors while preserving the original functionality of the algorithm, shorter quantum circuits are therefore preferred. This motivates the development of effective quantum circuit optimization algorithms. Learning-based approaches have emerged as a leading candidate, yet existing autonomous agents remain inefficient, spending most of their training capacity rediscovering elementary reductions that deterministic rule-based methods already handle reliably. To address this challenge, we propose a reinforcement learning framework that embeds a deterministic Commutation-and-Reduction (CR) algorithm directly into the training environment. After every agent action, the CR algorithm automatically resolves elementary commutations and cancellations, enabling the agent to focus its learning capacity on the non-trivial optimizations where reinforcement learning adds real value. Empirical evaluation across two gate sets, the universal Clifford+T basis and the CNOT+Pauli basis, shows that RL+CR produces shorter circuits than a standard RL agent at all tested scales. We demonstrate that RL trained on smaller quantum circuits can be applied to larger quantum circuits. On 20-qubit Clifford+T circuits, five times larger than the training circuits, RL+CR removes twice as many gates as standard RL. This work provides a robust approach that could accelerate the compilation and optimization processes for future fault-tolerant and utility-scale quantum systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19103) | 2026-08-20
