---
title: "Depth-reduced quantum simulation of Lindbladian dynamics via adaptive variational quantum trajectory compression"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09051"
summary: "arXiv:2607.09051v2 Announce Type: replace Abstract: Quantum simulation of open quantum systems in the noisy intermediate-scale quantum (NISQ) era is hindered by the non-unitary nature of dissipative d"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2607.09051v2 Announce Type: replace Abstract: Quantum simulation of open quantum systems in the noisy intermediate-scale quantum (NISQ) era is hindered by the non-unitary nature of dissipative dynamics and the limited quantum resources available on near-term quantum processors, namely restricted qubit counts and noise-limited circuit depths. In this work, we propose an efficient quantum algorithm for simulating Lindbladian dynamics on NISQ devices. For open quantum systems with Pauli dissipations, we first derive a compact and stable mixed-unitary adjoint channel that approximates the target dissipative dynamics and enables ancilla-free implementation through trajectory sampling. To further reduce the circuit depth required for implementing the sampled trajectories, we introduce an adaptive variational quantum trajectory compression framework. In this framework, a depth-adaptive parameterized quantum circuit is trained to approximate repeated Hamiltonian simulation operators, which are then used to replace repeated unitary segments appearing in the sampled trajectories. Importantly, the training procedure can also be performed without auxiliary qubits. Numerical simulations of the dissipative quantum XY model and the interacting disordered XXZ chain demonstrate the accuracy and reduced execution gate counts of the proposed algorithm. Our results provide a practical route toward ancilla-free and depth-reduced simulation of open quantum systems on near-term quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09051) | 2026-11-09
