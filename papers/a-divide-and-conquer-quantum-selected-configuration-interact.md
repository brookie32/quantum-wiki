---
title: "A Divide-and-Conquer Quantum-Selected Configuration Interaction for Evaluating pi-pi Stacking Interaction Energies in the Benzene Dimer"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36708"
summary: "arXiv:2609.36708v1 Announce Type: new Abstract: Accurate evaluation of pi--pi stacking interactions requires a description of electron correlation on a small energy scale. Direct variational quantum c"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36708v1 Announce Type: new Abstract: Accurate evaluation of pi--pi stacking interactions requires a description of electron correlation on a small energy scale. Direct variational quantum calculations of the benzene dimer with CAS(28e,20o) require 40 qubits and deep circuits. Here, we propose Divide-and-Conquer Quantum-Selected Configuration Interaction (Deep QSCI), combining the divide-and-conquer idea of Deep VQE with QSCI, and apply it to the sandwich benzene dimer. We perform QSCI for one monomer and construct a reduced local basis by applying particle-number-conserving one-electron excitations to its ground state. Using this basis and the intermonomer interaction Hamiltonian, we build and diagonalize an effective Hamiltonian of the dimer. Since the monomers have the same structure, the QSCI result is reused for both monomers and across intermolecular distances, reducing the required quantum register from 40 to 20 qubits for the monomer CAS(14e,10o). With 6-31G**, the model gives an attractive minimum of -0.91 kcal/mol at 4.0 r{A}, compared with the counterpoise-corrected CCSD(T) value of -1.14 kcal/mol. With cc-pVDZ, a large cancellation appears between the product-state interaction energy and the energy lowering by diagonalization. This may reflect insufficient consistency of the active orbitals and reduced local bases between monomers. Orbital consistency, reduced-space convergence across basis sets, and charge transfer remain key issues for quantitative accuracy. Deep QSCI thus provides a resource-efficient approach to constructing model interaction curves without repeating monomer quantum calculations at each separation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36708) | 2026-09-30
