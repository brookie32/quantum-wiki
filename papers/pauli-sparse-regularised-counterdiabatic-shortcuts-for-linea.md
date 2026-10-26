---
title: "Pauli-Sparse regularised Counterdiabatic Shortcuts for Linear-Ramp QAOA"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.28536"
summary: "arXiv:2606.28536v2 Announce Type: replace Abstract: Combinatorial optimization is a leading target for quantum algorithms, but finite-depth QAOA can suffer from strong diabatic errors when the interpo"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2606.28536v2 Announce Type: replace Abstract: Combinatorial optimization is a leading target for quantum algorithms, but finite-depth QAOA can suffer from strong diabatic errors when the interpolation Hamiltonian has small, or exponentially small, spectral gaps. We propose a Pauli-sparse counterdiabatic extension of linear-ramp QAOA based on the regularised adiabatic gauge potential [ igl(mathcal L_H^2+eta Iigr)A_lambda^{(eta)} = -imathcal L_H(partial_lambda H), qquad mathcal L_H(X)=[H,X]. ] Instead of computing a dense AGP, we solve this equation approximately by an inexact conjugate-gradient method in Pauli coordinates, truncating the Pauli expansion during the iteration to obtain a gate-budget-aware set of implementable rotations. The selected support is then improved by a Galerkin refit and certified by an a posteriori residual bound. The regularization parameter (eta) acts as an energy-resolution scale: it suppresses transitions below (sqrt{eta}) while retaining larger-gap transitions. Thus, the method can avoid resolving exponentially small splittings inside a low-energy solution manifold while reducing leakage away from it. Numerical experiments on Ferromagnetic Chain (FC) and perturbed FC--MaxCut/MarketSplit instances show that the resulting LR-CD-QAOA ansatz improves approximation ratios over the uncorrected linear ramp, especially in regimes where LR-QAOA remains far from the optimum. Overall, the proposed regularized LR-CD-QAOA framework substantially broadens the practical applicability of QAOA to QUBO optimization by improving its robustness across heterogeneous problem landscapes, including instances with near-degenerate low-energy structures and small spectral gaps.



## Related
- [[counterdiabatic-quantum-optimization-for-efficient-state-pre|Counterdiabatic quantum optimization for efficient state preparation in the Schwinger model]]
- [[a-first-principles-thermodynamic-uncertainty-relation-for-sh|A First-Principles Thermodynamic Uncertainty Relation for Shortcuts to Adiabaticity]]
- [[spectral-gap-informed-ramp-qaoa|Spectral Gap Informed Ramp QAOA]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.28536) | 2026-10-26
