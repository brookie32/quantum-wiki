---
title: "Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11911"
summary: "arXiv:2608.11911v1 Announce Type: new Abstract: A central promise of useful quantum advantage is the ability to compute ground states of Hamiltonian systems beyond the reach of classical simulation me"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11911v1 Announce Type: new Abstract: A central promise of useful quantum advantage is the ability to compute ground states of Hamiltonian systems beyond the reach of classical simulation methods. Here we demonstrate that this problem can be effectively amortized across an arbitrary and universal set of Hamiltonians by a foundation model with sim0.5B variational parameters, trained with contemporary techniques from large language models and deep reinforcement learning. To do this, we formulate ext{spin-}1/2 quantum ground-state learning as manifold variational optimisation over centrally odd scalar functions on SU(2)^N. This replaces explicit Hilbert-space vector amplitudes with manifold functions on which the Hamiltonian acts through Lie derivatives, evaluated by custom automatic differentiation primitives. We prove that the resulting variational principle on this manifold preserves the ext{spin-}1/2 sector's ground-state upper bound using the Peter-Weyl theorem, then pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths, bringing together a century of many-body literature. Using a novel SU(2) replica-exchange Langevin sampler and sharded natural-gradient optimisation, we train our model with our own extension of the Kronecker-Factored Approximate Curvature (KFAC) optimiser on system sizes up to 64 qubits. On a held-out generalisation dataset, we fine-tune our model on system sizes of up to 1024 qubits, and evaluate on systems up to 8100 qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11911) | 2026-08-13
