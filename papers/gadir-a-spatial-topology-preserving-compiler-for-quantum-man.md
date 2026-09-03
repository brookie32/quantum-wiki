---
title: "GadIR: A Spatial-Topology Preserving Compiler for Quantum Many-Body Systems Simulation"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.01771"
summary: "arXiv:2609.01771v1 Announce Type: new Abstract: Simulating quantum many-body systems has been one of the most important applications of quantum computation. For simulation, the Hamiltonian of a physic"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.01771v1 Announce Type: new Abstract: Simulating quantum many-body systems has been one of the most important applications of quantum computation. For simulation, the Hamiltonian of a physical system is compiled into quantum programs with native instructions for quantum hardware. In previous works, the Hamiltonian is represented as Pauli strings, then compiled and optimized based on the quantum circuit model. Such representation paradigm neglects the spatial topology of original physical models, which is vital information to reducing the overhead of compiling many-body systems Hamiltonians. To address such neglect, we introduce a spatial-topology preserving compiler for quantum many-body simulation. Using Pauli gadgets as the representations of the Hamiltonian, we introduce our intermediate representation -- GadIR, to preserve the spatial-topology information of original physical models. Our compiler frontend performs the group reduction algorithm based on Pauli gadget model, which is a hardware-independent optimization. Our compiler backend performs trotterization and scheduling on Pauli gadgets, then synthesizes the Pauli gadgets into hardware-native quantum programs. We evaluate our compiler on all the canonical quantum many-body system models, while achieving a significant reduction on compilation overhead regarding four major quantum architectures. Overall, our spatial-topology preserving IR exploits the compilation optimization space for quantum many-body systems Hamiltonian.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.01771) | 2026-09-03
