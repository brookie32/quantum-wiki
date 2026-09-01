---
title: "Accelerated Quantum-Assisted Selected Configuration Interaction via Fast-Annealing-Based Determinant Selection"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.30482"
summary: "arXiv:2608.30482v1 Announce Type: new Abstract: Full configuration interaction (FCI) provides exact electronic structure within a given atomic basis, but its computational cost grows exponentially wit"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30482v1 Announce Type: new Abstract: Full configuration interaction (FCI) provides exact electronic structure within a given atomic basis, but its computational cost grows exponentially with the number of spin orbitals. Selected configuration interaction (SCI) methods alleviate this limitation by retaining only the most important Slater determinants. However, the repeated identification of important determinants remains a major computational bottleneck. We present a quantum assisted selected configuration interaction (QASCI) method that combines SCI with graph based block diagonalization (GBBD) of FCI Hamiltonian. The GBBD method partitions FCI Hamiltonian into independent blocks, within which determinant selection problem is formulated as a quadratic unconstrained binary optimization (QUBO) problem. The QUBO problems for selecting determinants to construct SCI space are iteratively solved using a fast annealing approach. We benchmark method on H8-H18 hydrogen chains and Li2S in STO3G basis. For Hn chains, chemical accuracy is achieved while retaining only a small fraction of Slater determinants, and this fraction decreases with increasing n, despite the exponential growth of the FCI Hilbert space. For Li2S, QASCI results remain within chemical accuracy while retaining substantially fewer determinants than the full FCI space. We apply QASCI to N2 using the 631G basis, considering both active orbital and full orbital treatments. The full orbital QASCI calculation, using 50000 determinants, yields a lower ground state energy than an FCI calculation within an active space comprising 12 spin orbitals and 12 electrons. These results demonstrate that the combination of QASCI and the GBBD approach can substantially reduce computational cost of determinant selection while maintaining the accuracy of FCI based electronic structure calculations, thereby enabling accurate calculations in larger orbital spaces.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.30482) | 2026-09-01
