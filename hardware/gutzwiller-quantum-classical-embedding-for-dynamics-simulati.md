---
title: "Gutzwiller Quantum-Classical Embedding for Dynamics Simulations of Correlated Electron Systems"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24592"
summary: "arXiv:2611.24592v1 Announce Type: new Abstract: Simulating the real-time dynamics of correlated electron systems requires a nonperturbative treatment of local correlations over long times, a challenge"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24592v1 Announce Type: new Abstract: Simulating the real-time dynamics of correlated electron systems requires a nonperturbative treatment of local correlations over long times, a challenge for classical methods. We present the time-dependent Gutzwiller quantum-classical embedding framework, t-GQCE, for generic multi-orbital lattice models with time-dependent Hamiltonians. Within the time-dependent ghost Gutzwiller approximation, the lattice dynamics is mapped onto a noninteracting quasiparticle lattice, propagated classically, coupled to finite interacting embedding models propagated on quantum processors. The two parts exchange only embedding Hamiltonian parameters and single-particle density matrices, and the framework is agnostic to the quantum dynamics solver. We demonstrate it with adaptive variational quantum dynamics simulations of interaction quenches in the Hubbard model on the Bethe lattice. Without ghost orbitals, the embedding problem reduces to a single qubit, simulated on IBM quantum hardware with two qubits, including an ancilla. With more ghost orbitals, t-GQCE suppresses the artificial undamped oscillations of the conventional Gutzwiller approximation and approaches nonequilibrium dynamical mean-field theory results for weak and strong quenches. Statevector simulations with 2, 4 and 6 ghost orbitals per spin, or 8, 12 and 16 qubits, give adaptive circuits that follow the embedding states with infidelities below 5imes10^{-4}. Under trapped-ion noise models, circuit compression, measurements in rotated orbital bases with post-selection, and noise mitigation reduce the measurement errors severalfold. At one third of the error rates of a hardware-benchmarked noise model, they reach an accuracy of 0.01 for the single-particle density matrix and the double occupancy with 10^5 shots per time step, and the Quantinuum H2-Emulator gives similar accuracy.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24592) | 2026-11-19
