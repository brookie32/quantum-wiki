---
title: "Fault-Tolerant Resource Comparison of Qudit and Qubit Encodings for Diagonal Quadratic Operators"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.26792"
summary: "arXiv:2604.26792v3 Announce Type: replace Abstract: Finite local Hilbert-space truncations arise naturally in quantum simulations of lattice field theories and motivate qudit encodings, but their faul"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2604.26792v3 Announce Type: replace Abstract: Finite local Hilbert-space truncations arise naturally in quantum simulations of lattice field theories and motivate qudit encodings, but their fault-tolerant advantage over qubit encodings remains unclear. We compare the non-Clifford cost of implementing quadratic diagonal evolutions, exemplified by U=e^{-itphi_x^2} in a uniform field-amplitude discretization of a real scalar field, using either one logical d-level qudit or n_b=lceil log_2 drceil logical qubits. We analyze two standard settings: product-formula simulation and LCU/block encoding, taking the resource metric to be the number of non-Clifford gates after synthesis into a discrete logical gate set. Because tight synthesis bounds for general single-qudit rotations are not known, we express the qudit constructions in terms of embedded two-level SU(2) rotations and derive explicit finite-d break-even conditions for their synthesis cost; these serve as compiler targets for when qudit encodings can outperform the qubit baseline. Within the constructive models studied here, product-formula implementations would require an exponentially stronger per-primitive synthesis advantage for qudits to win asymptotically, while in the LCU setting the qubit encoding is asymptotically cheaper in d. Nevertheless, the finite-d threshold analysis identifies low dimensional regions in which qudits can yield meaningful constant-factor savings, particularly for LCU-based implementations. As a secondary analysis of the LCU construction, we use an idealized negligible-overhead qubit-qudit code-switching model to give an absolute T-count comparison, and reinterpret the savings as an allowable per-switch overhead budget.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.26792) | 2026-07-30
