---
title: "Simulating the Open System Dynamics of Multiple Exchange-Only Qubits using Subspace Monte Carlo"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.15577"
summary: "arXiv:2603.15577v2 Announce Type: replace Abstract: We propose a Monte Carlo based method for simulating the open system dynamics of multiple exchange-only (EO) qubits. In the EO encoding, the total s"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2603.15577v2 Announce Type: replace Abstract: We propose a Monte Carlo based method for simulating the open system dynamics of multiple exchange-only (EO) qubits. In the EO encoding, the total spin projection quantum number along the z-axis of the three constituent spins remains unchanged under exchange operations, in contrast to the open system (or multi-qubit miscalibration) setting where coherent and incoherent mixing of states with different quantum numbers occurs. In our approach, we choose to measure the total spin component along the z-axis of each EO qubit after every logical quantum operation, which decoheres coherent mixtures of states with different spin projection quantum numbers. Independent simulations thus give different trajectories of the system in the associated subspaces, so we refer to this method as the Subspace Monte Carlo method. With each EO qubit having a definite spin projection quantum number, the density matrix of n qubits can be represented by a vector of dimension 3^{2n}, instead of 8^{2n}, with an additional vector of dimension n to label the quantum number of each qubit. We show that this approximation of the dynamics remains faithful to the true dynamics when the simulated circuits twirl the noise, converting coherent errors to stochastic errors, which can be achieved using randomized compiling. We use this simulation approach to study how correlations in measurement outcomes of circuits with reset-if-leaked gadgets, such as a multi-round Bell state stabilization circuit that uses 6 EO qubits, are affected by the choice of CNOT implementations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.15577) | 2026-08-18
