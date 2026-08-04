---
title: "Better accuracy with fewer qubits: Single-particle basis set optimization for quantum chemistry on quantum computers"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02119"
summary: "arXiv:2608.02119v1 Announce Type: new Abstract: In spite of recent advances, quantum computers are expected to be sufficiently noisy in the coming few years to the extent of limiting quantum chemical "
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.02119v1 Announce Type: new Abstract: In spite of recent advances, quantum computers are expected to be sufficiently noisy in the coming few years to the extent of limiting quantum chemical calculations to relatively small number of orbitals. However, even with reasonable quality single particle basis sets, small active spaces with limited orbitals can result in a significant fraction of correlation energy being lost, motivating the design of moderate quality qubit-efficient basis sets for quantum algorithms. We begin by reoptimizing the existing minimal basis sets using a genetic algorithm-inspired approach in conjunction with aggressive refinement strategies, and generate modified minimal basis sets (MSTO-kG basis; k = 2-11) for atoms from H through F. The ground state energies of H through F using our MSTO bases at FCI level of theory yield ground state energies that are comparable or sometimes even lower than those obtained using 6-31G basis sets. In the case of Li, the MSTO bases surpass the performance of cc-pVQZ bases. Thus, we obtain better atomic energies with same number of qubits relative to STO bases, and better/comparable energies with fewer qubits relative to higher quality bases. In the case of molecules, H2 performs poorly; a finding that is consistent with an earlier work in literature. For other molecules, Li2, C2, LiH, BeH and BeH2, the FCI results (except C2 for which we employ CISD) from our bases are comparable to/outperform those from 6-31G basis. Finally, we compare the resources required between different bases and find that MSTO bases yield better energies than the competing basis sets while incurring fewer qubits and two-qubit gates with VQE, QPE, and HHL. The logical T-gate counts are also found to be considerably lower for QPE and HHL respectively. Overall, our work paves way for more accurate yet less qubit-hungry quantum chemical calculations using near-term quantum computers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02119) | 2026-08-04
