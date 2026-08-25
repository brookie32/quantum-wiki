---
title: "A Unified Quantum Neural Network Framework for Hamiltonian Learning and Emulation of Unknown Quantum Systems"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.23025"
summary: "arXiv:2608.23025v1 Announce Type: new Abstract: Accurate identification of unknown quantum systems is essential for quantum computing, sensing, and control because the Hamiltonian governs quantum stat"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.23025v1 Announce Type: new Abstract: Accurate identification of unknown quantum systems is essential for quantum computing, sensing, and control because the Hamiltonian governs quantum state evolution. This work proposes a QNN based framework for black box Hamiltonian learning and quantum system emulation using full density matrix trajectory learning. Unlike approaches based only on final states or selected observables, the method exploits the complete temporal evolution of the density matrix under Lindblad dynamics. A synthetic dataset of physically admissible Hamiltonians and dissipation parameters is generated to emulate experimental measurements. The QNN learns a nonlinear mapping from control inputs to a 32-dimensional Hamiltonian coefficient vector, enabling reconstruction and differentiable emulation of the unknown system. Chirped excitation and randomized initial quantum states are incorporated to improve robustness and provide richer dynamical information. Performance is evaluated using trajectory density loss, quantum-state fidelity, and trace distance. Randomized initialization improves state-level reconstruction, increasing fidelity to 0.929 for the single qubit benchmark and 0.787 for the unknown system, while reducing trace distance to 0.124 and 0.316, respectively. In contrast, chirped excitation primarily improves optimization by accelerating convergence and reducing trajectory density loss. Finally, the learned Hamiltonian is mapped onto a physical two qubit bus resonator architecture in the dispersive regime, yielding key circuit parameters including transmon capacitances, Josephson inductances, qubit separation, and bus-resonator length. The framework therefore establishes a data-driven pathway from black box quantum system identification to physical quantum emulation, with potential applications in quantum digital twin modeling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.23025) | 2026-08-25
