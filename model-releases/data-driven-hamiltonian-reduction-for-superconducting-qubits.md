---
title: "Data-Driven Hamiltonian Reduction for Superconducting Qubits via Meta-Learning"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24912"
summary: "arXiv:2604.24912v1 Announce Type: new Abstract: We introduce HAML (Hamiltonian Adaptation via Meta-Learning), a framework for fast online adaptation of effective Hamiltonian models of superconducting "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.24912v1 Announce Type: new Abstract: We introduce HAML (Hamiltonian Adaptation via Meta-Learning), a framework for fast online adaptation of effective Hamiltonian models of superconducting quantum processors. HAML proceeds in two phases. A supervised training phase uses an ensemble of simulated devices to learn an offline map from control inputs and device parameters to effective Hamiltonian coefficients. An online adaptation phase then uses a small number of hardware-accessible measurements to identify the unknown parameters of a new device. By training directly against effective two-qubit coefficients extracted from full multi-mode simulations, HAML implicitly learns the reduction from full multi-mode Hamiltonians to effective qubit descriptions without invoking perturbation theory. We further show that a variance-maximizing greedy selection of measurement configurations boosts online adaptation efficiency. We demonstrate HAML on a transmon-coupler-transmon system, recovering effective two-qubit coefficients across a wide range of operating regimes, including parameter regions where Schrieffer-Wolff perturbation theory (SWPT) breaks down. This establishes a scalable, sample-efficient approach to Hamiltonian reduction and characterization for near-term quantum processors, with direct implications for calibration, control, and error mitigation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24912) | 2026-04-29
