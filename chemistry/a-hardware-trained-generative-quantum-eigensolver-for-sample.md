---
title: "A Hardware-Trained Generative Quantum Eigensolver for Sample-Based Quantum Diagonalization of Organotin Hydroxides up to 70 Qubits"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13755"
summary: "arXiv:2611.13755v1 Announce Type: new Abstract: Quantum hardware can provide feedback for training circuit generators beyond the reach of exact classical simulation. We train generative quantum eigens"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13755v1 Announce Type: new Abstract: Quantum hardware can provide feedback for training circuit generators beyond the reach of exact classical simulation. We train generative quantum eigensolver (GQE) policies, transformers conditioned on molecular descriptors, to generate the state-preparation circuits for sample-based quantum diagonalization (SQD). Training runs first on a noiseless simulator and then with the IBM Heron processor ibm_kobe inside the loop, at 46 and 70 qubits (1.2 imes 10^8 shots for the four main training runs). A classical CCSD(T) reference energy of the training molecules enters only an admission gate and two auxiliary reward terms. During hardware training, a reward penalty prevents collapse to circuits that sample only the Hartree-Fock determinant. Policies trained on transition-metal complexes are applied without retraining to Sn(OH)_3-Me and its hydrates, minimal models of organotin photoresists for extreme-ultraviolet lithography, from 32 to 70 qubits. After one round of hardware sampling, followed by classical ranking and recovery of the cached counts with the molecular Hamiltonian and no further QPU calls, 27 of 28 runs at 46-70 qubits are within 15 mHa of the density-matrix renormalization group (DMRG) reference (median 4.5 mHa), and in all eight runs with an untrained control the trained policy is more accurate. At 56-70 qubits the selected circuits use 34-72 times fewer two-qubit gates than the local unitary cluster Jastrow (LUCJ) circuit transpiled for the same device. These results demonstrate that circuit generators can be trained with quantum hardware at 70 qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13755) | 2026-11-11
