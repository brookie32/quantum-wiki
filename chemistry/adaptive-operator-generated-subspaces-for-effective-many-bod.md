---
title: "Adaptive operator-generated subspaces for effective many-body Hamiltonians"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00560"
summary: "arXiv:2608.00560v1 Announce Type: new Abstract: Electronic-structure and embedding workflows terminate in effective many-body Hamiltonians, whereas quantum eigensolver studies often start from hand-bu"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00560v1 Announce Type: new Abstract: Electronic-structure and embedding workflows terminate in effective many-body Hamiltonians, whereas quantum eigensolver studies often start from hand-built qubit models. We present the Adaptive Clifford-Algebra Subspace Eigensolver (A-CASE), a single-reference, operator-generated Rayleigh--Ritz method. Overlap, Hamiltonian, observable, and response matrices are reconstructed from one shared Pauli-expectation bank, while adaptive growth scores overlap-aware local pencils and rejects symmetry leakage or near-linear dependence. A strict FCIDUMP adapter supplies the active-space boundary. For linear H_4 in STO-3G with CAS(4e,4o), the mapped sector agrees with independent determinant FCI to 3.1imes10^{-15} Ha. At a nine-vector budget A-CASE has a 3.019 mHa error; replacing the determinant reference by a two-operator ADAPT-VQE state reduces it to 0.342 mHa, without implying a matched total-cost advantage. Under a matched contract, the fixed-reference route uses one state preparation versus ADAPT-VQE's ninety but measures roughly an order of magnitude more Pauli words. Exact fixed-angle ADAPT-GCIM gives 13.364 mHa at the nearest size match and 10.674 mHa at the iteration match, with its transition-pair burden reported separately. Across a broader benchmark ladder, fixed Krylov bases are generally more accurate and often narrower but substantially less well conditioned. A grouped bootstrap propagates finite-shot variability through thresholding, diagonalization, root matching, spectral weights, susceptibility, and broadening; its bands are explicitly heuristic and conditional, not finite-sample confidence certificates. The work establishes an executable path from an interchange Hamiltonian to energies, correlations, and response, without claiming materials accuracy, favorable scaling, or quantum advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00560) | 2026-08-04
