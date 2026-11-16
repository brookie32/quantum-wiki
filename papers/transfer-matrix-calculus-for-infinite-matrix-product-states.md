---
title: "Transfer-Matrix Calculus for Infinite Matrix Product States"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18427"
summary: "arXiv:2611.18427v1 Announce Type: cross Abstract: Long-range interactions, from the Coulomb repulsion between electrons to the power-law interactions of trapped ions and Rydberg atoms, are widespread "
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18427v1 Announce Type: cross Abstract: Long-range interactions, from the Coulomb repulsion between electrons to the power-law interactions of trapped ions and Rydberg atoms, are widespread in quantum many-body physics. For infinite systems, however, MPS algorithms, the standard classical reference in one dimension, conventionally rely on a computational compromise: replacing these interactions by fitted sums of exponentials. We develop transfer-matrix calculus (TMC), a unified framework for deriving infinite-MPS algorithms. In TMC, an interaction is written as a function of the transfer matrix, and one set of contraction rules then yields the effective Hamiltonians of DMRG and VUMPS, the tangent-space excitation action, and the energy variance, without an MPO. Long-range interactions thus enter with their prescribed distance dependence. For the half-filled lattice Coulomb chain with a 1/d interaction of strength V, theory predicts CDW order for all V>0, but at weak coupling this order is too weak for earlier numerics to resolve. Using TMC, we obtain infinite-MPS ground states at V=2 directly in the thermodynamic limit, with an energy variance per site of 2imes10^{-10}. Our data, extrapolated to zero energy variance, indicate a small nonzero CDW amplitude, m_0=0.002213(14), consistent with this prediction. The complete V=2 optimization workflow across the full series of bond dimensions takes less than a day on a single AMD MI250X GPU die. For an exactly solvable long-range hopping model, TMC reproduces the nonanalytic |k| cusp of the one-particle dispersion that any fixed finite sum of decaying exponentials rounds off. We also use TMC to optimize first-quantized MPS directly in the thermodynamic limit. For half-filled free fermions, our entanglement entropy data show scaling consistent with central charge c=1 over the studied bond dimensions, as for second-quantized MPS.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18427) | 2026-11-16
