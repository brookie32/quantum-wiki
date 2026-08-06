---
title: "Impact of molecular orbital localization on quantum computational resources for Hamiltonian simulation: A benchmark study of hydrogen chain systems"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.04481"
summary: "arXiv:2608.04481v1 Announce Type: new Abstract: We investigate how molecular orbitals used as the basis of wave function expansion and how operator coefficient-based and locality-based Hamiltonian tru"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2608.04481v1 Announce Type: new Abstract: We investigate how molecular orbitals used as the basis of wave function expansion and how operator coefficient-based and locality-based Hamiltonian truncation affects the computational cost of Trotter decomposition-based Hamiltonian simulation in one-dimensional hydrogen chain systems. The analysis is performed using both Hartree--Fock canonical molecular orbitals (CMOs) and Pipek--Mezey-based localized molecular orbitals (LMOs). For short hydrogen chains, we evaluate the ground-state energy and fidelity and find that, in the CMO-based wave function expansion, introducing a threshold on Hamiltonian coefficients is effective in reducing the gate cost while maintaining computational accuracy. In contrast, in the LMO-based wave function expansion, operator locality-based Hamiltonian truncation is found to be more effective. By fitting the relationship between the truncation threshold and the ground-state energies and fidelities with empirical formulas, we estimate the threshold values required to achieve high fidelity (F ge 0.99) in the ground-state wave function. Using the estimated thresholds, we then perform quantum gate resource estimation for longer hydrogen chains up to H_{100}. The results suggest an exponential advantage of the LMO-based wave function expansion with Hamiltonian truncation: the number of quantum gates required for Hamiltonian simulation grows polynomially when the CMO-based wave function expansion with operator coefficient-based Hamiltonian truncation is adopted, whereas it grows polylogarithmically when the LMO-based wave function expansion is combined with operator locality-based Hamiltonian truncation. These results provide useful guidelines for choosing orbital representations and Hamiltonian truncation strategies in large-scale quantum chemical simulations.



## Related
- [[zassenhaus-expansion-in-solving-the-schrodinger-equation|Zassenhaus Expansion in Solving the Schrodinger Equation]]
- [[optimized-tensor-network-renormalization-for-quantum-dynamic|Optimized Tensor-Network Renormalization for Quantum Dynamics: Resolving the Spectral Function of K_2Co(SeO_3)_2]]
- [[faster-algorithmic-quantum-and-classical-simulations-by-corr|Faster Algorithmic Quantum and Classical Simulations by Corrected Product Formulas]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.04481) | 2026-08-06
