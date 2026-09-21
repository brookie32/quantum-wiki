---
title: "Pauli-string grouping for VQE measurement reduction on a sparse-connectivity quantum annealer"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20861"
summary: "arXiv:2609.20861v1 Announce Type: new Abstract: The Variational Quantum Eigensolver (VQE) requires a large number of measurements to evaluate molecular Hamiltonians. Expressing a molecular Hamiltonian"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.20861v1 Announce Type: new Abstract: The Variational Quantum Eigensolver (VQE) requires a large number of measurements to evaluate molecular Hamiltonians. Expressing a molecular Hamiltonian as a linear combination of Pauli strings creates a measurement bottleneck: non-commuting Pauli strings cannot be measured simultaneously. Consequently, mutually commuting Pauli strings must be grouped and measured together to minimise the number of quantum-state preparations. This task maps to the minimum clique cover problem on a commutativity graph, an NP-hard problem typically addressed using classical heuristics. Although an Ising-model formulation has recently been explored on fully connected CMOS Ising machines and demonstrated on physical quantum annealers only at small scale, the embedding cost that governs its behaviour on hardware with sparse connectivity, where each logical variable must be represented by a chain of physical qubits, has not been characterised. In this work, we formulate the Pauli-grouping problem as a standard QUBO colouring model and study its scalability on a D-Wave quantum annealer. Across a series of molecular systems and for both qubit-wise and full commutativity, we quantify the growth in the number of logical variables and the QUBO interaction density, characterise the physical-qubit and chain-length overhead required for embedding on the Zephyr topology, and compare the annealer's time-to-solution and solution quality with those of heuristic classical baselines. This analysis identifies the threshold of molecular complexity beyond which hardware connectivity prevents viable embedding, and shows that a second, practical limit is reached earlier. The threshold therefore measures how far current annealers are from the regime in which pre-optimising a VQE measurement scheme on hardware would be worth considering.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20861) | 2026-09-21
