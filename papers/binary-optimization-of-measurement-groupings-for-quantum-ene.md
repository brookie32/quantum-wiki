---
title: "Binary Optimization of Measurement Groupings for Quantum Energy Estimation"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10339"
summary: "arXiv:2610.10339v1 Announce Type: new Abstract: Repeated measurements can dominate the resources required for quantum energy estimation, making the choice of which Pauli observables to measure togethe"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10339v1 Announce Type: new Abstract: Repeated measurements can dominate the resources required for quantum energy estimation, making the choice of which Pauli observables to measure together a central optimization problem for variational quantum algorithms. We formulate fully commuting measurement grouping as a classical binary optimization problem based on clique selection and construct non-overlapping groups using mixed-integer linear programming (MILP). For a benchmark of molecular Hamiltonians, groupings optimized with approximate covariances reduce the non-overlapping measurement requirement arepsilon^2M by 51.8% on average relative to sorted insertion (SI). Using the MILP groups to initialize iterative coefficient splitting (ICS), denoted MILP-ICS, yields an average 24.3% reduction relative to ICS initialized from SI (SI-ICS). The optimized groups also transfer across nearby molecular geometries while preserving substantial measurement savings. We further introduce O-clique, which directly optimizes overlapping commuting supports through candidate-clique selection and coefficient profiles. Although O-clique provides only modest additional reductions beyond MILP-ICS, it reduces the measurement requirement by 27.3% on average relative to SI-ICS with 100 iterations, despite using only five final coefficient refinement iterations, indicating improved support quality. Finally, we extend the comparison to Fermi--Hubbard, Kitaev--Heisenberg--Gamma, and XYZ lattice Hamiltonians, where MILP-based groupings substantially outperform the corresponding SI-based strategies. Together, these results show that variance-informed optimization of measurement-group structure can substantially reduce sampling costs across molecular and lattice Hamiltonians, with optimized non-overlapping groups providing strong, transferable initializations and direct overlapping optimization offering further gains.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10339) | 2026-10-08
