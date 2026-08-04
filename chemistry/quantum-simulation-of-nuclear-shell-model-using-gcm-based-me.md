---
title: "Quantum Simulation of Nuclear Shell Model Using GCM-Based Methods on NISQ Devices"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.01769"
summary: "arXiv:2608.01769v1 Announce Type: cross Abstract: Based on the Generator Coordinate Method (GCM), we use a Quantum GCM (QuGCM) within a hybrid quantum-classical framework to simulate low-lying eigenst"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.01769v1 Announce Type: cross Abstract: Based on the Generator Coordinate Method (GCM), we use a Quantum GCM (QuGCM) within a hybrid quantum-classical framework to simulate low-lying eigenstates of nuclear systems on quantum devices. The generator basis states are constructed from Hartree-Fock (HF) reference states, excited via symmetry-adapted unitary coupled-cluster (UCC) operators. These states are prepared as non-orthogonal quantum circuits and measured pairwise to compute the required overlap and Hamiltonian kernels. The resulting data is processed using a classical generalized-eigenvalue solver, following the GCM formalism, to extract the system's energy spectrum. To enhance efficiency and reduce circuit depth, we apply the Adaptive Generator Coordinate Inspired method (ADAPT-GCIM), which iteratively selects generator excitations based on energy gradients, thereby avoiding the need to explore the full Hilbert space. Our implementation is applied to nuclear systems, specifically the deuteron with the Reid68 potential and shell-model Hamiltonians of ^6Li and ^{38}Ar. For each system, both the QuGCM and ADAPT-GCIM methods produce energy spectra in agreement with classical diagonalization results, demonstrating robustness even under noise and limited-depth constraints. Additionally, we compare fermionic encoding strategies, specifically Jordan-Wigner (JW) transformations of one-hot (OH) encoding and Gray code (GC) mappings, and show that GC encoding reduces circuit complexity and improves fidelity during multi-reference state preparation. Our findings indicate that QuGCM and ADAPT-GCIM provide a practical and scalable path toward simulating correlated quantum systems, with lesser vulnerability to noise and better compatibility with the limitations of current quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.01769) | 2026-08-04
