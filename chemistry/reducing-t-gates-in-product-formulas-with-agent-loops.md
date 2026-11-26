---
title: "Reducing T gates in product formulas with agent loops"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33509"
summary: "arXiv:2611.33509v1 Announce Type: new Abstract: Quantum chemistry calculations on a fault-tolerant quantum computer usually require many ext{T} gates. This cost depends on the simulation method and ho"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33509v1 Announce Type: new Abstract: Quantum chemistry calculations on a fault-tolerant quantum computer usually require many ext{T} gates. This cost depends on the simulation method and how precisely its rotations are implemented. In this paper, we used Nemotron 3.5 Lightning, a large language model (LLM), in a coding-agent loop to optimize the structure and rotation-synthesis precision of product formulas (PFs) for quantum phase estimation (QPE). Each of five independent searches optimized a shared protocol across 115 HamLib molecular Hamiltonians spanning 4--16 qubits over 100 code mutations. The searches started from a calibrated, nested second-order PF with uniform synthesis precision. We minimized T_{95}, the estimated total ext{T}-gate cost including QPE queries and repeated attempts for 95% success probability, while requiring chemical accuracy for every training Hamiltonian. We name the best protocol found error-limited optimized Trotter evolution (ELOTE). It achieves chemical accuracy for its training data and achieved median and geometric-mean T_{95} reductions of 85.35% and 84.82%, respectively. ELOTE combines contributions to the same Pauli string, uses a first-order PF, and varies synthesis precision with coefficient magnitude, Pauli support, and diagonal character. We also tested ELOTE on 76 larger Hamiltonians with 18--22 qubits, which met chemical accuracy in every case. For ten reaction energies, we further optimized a shared elta-ELOTE protocol. It reduced geometric-mean T_{95} by 58.90% relative to ELOTE while preserving chemical accuracy for every signed reaction difference. These classically verified results show cost savings from shared protocols across molecules and reactions, and motivate similar searches in which energy measurements from quantum computers guide explorations in a coding-agent loop.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33509) | 2026-11-26
