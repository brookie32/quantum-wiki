---
title: "Distributed Quantum-Centric Supercomputing with Multi-Layered Generative Learning for Intermolecular Interactions"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32968"
summary: "arXiv:2610.32968v1 Announce Type: new Abstract: Quantum-centric supercomputing (QCSC) approaches, such as sample-based quantum diagonalization (SQD), combine quantum processors with high-performance c"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32968v1 Announce Type: new Abstract: Quantum-centric supercomputing (QCSC) approaches, such as sample-based quantum diagonalization (SQD), combine quantum processors with high-performance computers (HPC), offering a promising route toward solving challenging electronic structure problems. However, implementation of QCSC approaches to large active space calculations is constrained by the associated number of qubits, deep quantum circuits, sampling cost, and large-scale Hamiltonian diagonalization. To overcome these limitations, we introduce a distributed QCSC framework that decomposes complex molecular problems into parallel sub-problems requiring fewer qubits, shallower circuits, and reduced shot budgets. A physically motivated, two-step aggregation scheme then reconstructs the global solution: first, a computational bit assignment strategy optimizes a cost function to appropriately map local bit indices to global ones, yielding a mapped tensor product state (MTPS); second, an inter-fragment correlation recovery module restores missing cross-fragment interactions. Herein, we employ a multi-layered generative machine learning architecture, starting with utilizing the recently proposed physics-informed generative SQD (PIGen-SQD) as a distributed QCSC solver, followed by a secondary generative module to model configuration distributions and identify dominant sectors of the global Hilbert space. For water and formamide dimers, our method achieves up to 95% reduction in the diagonalization dimension while enhancing energy accuracy by an order of magnitude over conventional SQD. Furthermore, application to the water hexamer ((H_2O)_6) cage successfully decomposes a 120-qubit problem into six 20-qubit monomeric subsystems, and stitches the monomers under a dimeric approximation, demonstrating excellent agreement with the reference classical methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32968) | 2026-10-26
