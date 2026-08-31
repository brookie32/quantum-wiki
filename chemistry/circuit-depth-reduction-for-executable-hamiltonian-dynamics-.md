---
title: "Circuit Depth Reduction for Executable Hamiltonian Dynamics of Covalent Inhibitor Reactivity on Quantum Hardware"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2412.15804"
summary: "arXiv:2412.15804v4 Announce Type: replace Abstract: Quantum chemistry applications in the noisy intermediate-scale quantum era require end-to-end approaches that balance algorithmic fidelity with prac"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2412.15804v4 Announce Type: replace Abstract: Quantum chemistry applications in the noisy intermediate-scale quantum era require end-to-end approaches that balance algorithmic fidelity with practical executability on existing hardware. We present an end-to-end Hamiltonian dynamics case study for predicting the reactivity of pharmaceutically relevant covalent inhibitors containing sulfonyl fluoride warheads, using a quantum-centric data-driven research and development framework that combines Hamiltonian time evolution with classical machine learning. To make such simulations executable on current quantum processors, we introduce a systematic circuit reduction strategy based on Hamiltonian term truncation with observable error bounds, Clifford Decomposition and Transformation, and hardware-aware transpilation. Across representative molecular fragments, this approach achieves circuit depth reductions of up to 28.5x under all-to-all connectivity assumptions and up to 15.5x on IBM Heron-class architectures. For an eight-qubit Hamiltonian dynamics simulation, a transpiled instruction set architecture (ISA) circuit depth of 1330 is rendered executable through middleware-enabled circuit decomposition, enabling the execution of sub-circuits with depths up to 371 and containing up to 216 two-qubit gates on real hardware. We evaluate the impact of circuit reduction on downstream reactivity prediction accuracy and show that chemically meaningful predictions can be retained despite aggressive circuit simplifications, clarifying the trade-offs that govern practical quantum chemistry workflows on near-term quantum systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2412.15804) | 2026-08-31
