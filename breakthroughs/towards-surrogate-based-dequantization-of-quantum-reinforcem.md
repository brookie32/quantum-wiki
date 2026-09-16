---
title: "Towards Surrogate Based Dequantization of Quantum Reinforcement Learning"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16266"
summary: "arXiv:2609.16266v1 Announce Type: new Abstract: In recent years, the utility of parameterized quantum circuits as function approximators has been widely studied. In the context of reinforcement learni"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16266v1 Announce Type: new Abstract: In recent years, the utility of parameterized quantum circuits as function approximators has been widely studied. In the context of reinforcement learning, this approach has led to variational quantum algorithms such as quantum Q-learning. While these methods show promising empirical results, and can provide provable advantages for artificial problems, it remains unclear whether they can provide a provable quantum advantage over classical approaches for problems of practical relevance. A natural way to investigate this question is through the lens of dequantization: The construction of efficient classical algorithms capable of matching the performance of quantum variational methods. Building on recent kernel-based dequantization results for supervised learning, we take steps towards extending this surrogate-based dequantization program to reinforcement learning. Specifically, we study the simplified setting of reinforcement learning with a uniform generative model in which uniformly random state-action samples are available, which models the regime of sampling from a large experience replay buffer after sufficient exploration. Within this setting, we provide finite sample guarantees for classical kernelized Fitted Q-Iteration, with classical kernels designed to match the inductive bias of particular parameterized quantum circuits. Using these results, we then provide a set of sufficient conditions, on the data-encoding strategy of a parameterized quantum circuit, the corresponding classical kernel, and the problem structure, under which kernelized Fitted Q-Iteration provides a meaningful dequantization of quantum Q-learning, in this simplified setting. Apart from providing rigorous dequantization guarantees when these conditions are met, these results also motivate the use of kernelized fitted Q-iteration as a dequantization heuristic when these sufficient conditions cannot be verified.



## Related
- [[learning-to-coordinate-via-quantum-entanglement-in-multi-age|Learning to Coordinate via Quantum Entanglement in Multi-Agent Reinforcement Learning]]
- [[bounded-error-quantum-simulation-via-hamiltonian-and-lindbla|Bounded-Error Quantum Simulation via Hamiltonian and Lindbladian Learning]]
- [[evaluating-system-level-fidelity-with-peaked-random-circuits|Evaluating System-Level Fidelity with Peaked Random Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16266) | 2026-09-16
