---
title: "Benchmarking quantum trial wavefunctions for phaseless auxiliary-field quantum Monte Carlo"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.02056"
summary: "arXiv:2605.02056v3 Announce Type: replace Abstract: The phaseless auxiliary-field quantum Monte Carlo (ph-AFQMC) method is a stochastic imaginary-time projection method for computing ground-state prop"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2605.02056v3 Announce Type: replace Abstract: The phaseless auxiliary-field quantum Monte Carlo (ph-AFQMC) method is a stochastic imaginary-time projection method for computing ground-state properties of strongly correlated quantum systems, whose accuracy depends critically on the trial wavefunction. We present a benchmarking study of trial wavefunctions prepared using parameterized quantum circuits, spanning unitary coupled cluster (UCC), Hamiltonian-informed, Jastrow-inspired, and adaptively constructed ansatzes, and evaluate their accuracy, expressibility, and resource requirements within the quantum-computing-enhanced AFQMC (QC-AFQMC) framework. Trial states are prepared with GPU-accelerated statevector simulations using CUDA-Q and tested on stretched linear hydrogen chains and nine closed-shell molecules at equilibrium with varying static correlation. We find that at similar parameter counts, ph-AFQMC largely removes differences between families for weakly and moderately correlated systems: every trial yields a ph-AFQMC energy within chemical accuracy despite trial energy errors spanning nearly three orders of magnitude, whereas ansatz choice becomes consequential as static correlation grows. Our results indicate that trial variational energy is not always a reliable indicator of ph-AFQMC quality, and that adding variational parameters can lower the trial energy while degrading the ph-AFQMC energy. Across our benchmark systems, trial fidelity ranks trials more reliably than variational energy, and for spin-contaminated trials, the singlet-projected fidelity is more reliable than unprojected fidelity. The UCCSD ansatz initialized from unrestricted CCSD amplitudes provides a robust and inexpensive-to-optimize baseline across benchmark systems, with circuit depth as its principal limitation, while adaptive and compact layered ansatzes remain competitive in accuracy under strong correlation with substantially shallower circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.02056) | 2026-10-28
