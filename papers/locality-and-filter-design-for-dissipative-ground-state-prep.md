---
title: "Locality and filter design for dissipative ground-state preparation"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31266"
summary: "arXiv:2609.31266v1 Announce Type: new Abstract: Ground-state preparation is a fundamental challenge in quantum many-body physics, chemistry and materials science. Dissipative state-preparation techniq"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31266v1 Announce Type: new Abstract: Ground-state preparation is a fundamental challenge in quantum many-body physics, chemistry and materials science. Dissipative state-preparation techniques engineer a Lindbladian coupling to a bath that drives the system to its ground state, needing no initial overlap. Their cost is dominated by the Hamiltonian simulations inside the filtered jump operators, since each jump is a weighted sum of Heisenberg-evolved copies, or branches, of a coupling operator. We reduce this cost by following three simple observations to their logical end. First, on a fixed time grid, linear programming optimises the branch weights, trading the heating response against the circuit cost. Second, Lieb--Robinson bounds let each branch evolve on a patch whose radius grows with its duration. Third, if the dynamics converges quickly and truncation changes the jumps only slightly, the stationary state stays near the ground state even on patches smaller than the light cone. We validate our approach numerically. On a grid of 81 evolution times, the optimised filter reduces the worst-case heating response, or leakage, more than 116-fold at equal cost. Across fifteen molecules and six chains, the cost falls by 27 to 56% at matched design-grid leakage; at matched cost, the molecular leakage falls by a factor of 2.9 to 2imes10^{3}. Density-matrix simulations show high ground-state fidelity for both filters, and on Ising and Hubbard chains the cheaper filter keeps a ground-state population of at least 0.89 on patches of three or four sites. The same patches fail on a Heisenberg chain whose truncation error falls more slowly with patch size and whose Lindbladian gap is 12 times smaller than the Ising chain's, pointing to a role for the gap in how far patches can be truncated. At fixed radius the per-branch cost becomes independent of system size, reducing the cost of dissipative state preparation.



## Related
- [[dissipative-ground-state-preparation-of-a-quantum-spin-chain|Dissipative ground-state preparation of a quantum spin chain on a trapped-ion quantum computer]]
- [[lattice-lindbladian-simulation-by-patching-and-merging|Lattice Lindbladian simulation by patching and merging]]
- [[global-zero-excitation-state-preparation-through-subsystem-c|Global zero-excitation state preparation through subsystem cooling]]
- [[large-scale-quantum-simulations-of-dissipative-spin-12-heise|Large-scale quantum simulations of dissipative spin-1/2 Heisenberg chains]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31266) | 2026-09-28
