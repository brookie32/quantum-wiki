---
title: "PyCDFT: A Python-scriptable library for analytical evaluation of orbital conceptual density (matrix) functional theory"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.01727"
summary: "arXiv:2610.01727v1 Announce Type: new Abstract: Conceptual density functional theory (CDFT) defines chemical reactivity descriptors as derivatives of the electronic energy with respect to the number o"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01727v1 Announce Type: new Abstract: Conceptual density functional theory (CDFT) defines chemical reactivity descriptors as derivatives of the electronic energy with respect to the number of electrons and the external potential, or combinations thereof; in practice, however, researchers almost always replace these derivatives with finite-difference and frontier-orbital approximations, and no common software exists for their analytical evaluation. We present PyCDFT, to our knowledge, the first standardized, open-source, and scriptable code that analytically computes the descriptors of conceptual density (matrix) functional theory for ground and excited states up to second order, including the orbital hardness, the Fukui function and Fukui matrix, and the linear response function, from a single converged mean-field wavefunction imported from virtually any electronic-structure package. The descriptors are obtained from matrix-free, preconditioned Krylov-subspace solutions of the coupled-perturbed self-consistent-field equations for both spin-unpolarized and spin-polarized references, with the work distributed over MPI ranks and all data flowing through a single HDF5 checkpoint file that supports restart, post-processing, and the export of real-space descriptors as cube files for visualization. The design delegates integrals, grids, and exchange-correlation kernels to PySCF and Libxc, keeping the library compact, user-friendly, and interoperable. Worked examples on the ground state of H_2O and a broken-symmetry DeltaSCF excited state of NH_3 show that a complete second-order CDFT analysis requires only a few lines of user code.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.01727) | 2026-10-02
