---
title: "StudDFT: A quantum chemistry program for educational and research purposes"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.37483"
summary: "arXiv:2610.37483v1 Announce Type: new Abstract: StudDFT is a quantum chemistry program for Hartree--Fock (HF), density functional theory (DFT), and second-order M{o}ller--Plesset (MP2) calculations of"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.37483v1 Announce Type: new Abstract: StudDFT is a quantum chemistry program for Hartree--Fock (HF), density functional theory (DFT), and second-order M{o}ller--Plesset (MP2) calculations of small and medium-sized molecules. It is intended primarily for teaching and student research, but its accuracy suffices for routine research calculations. Version 1.30.2 implements the RHF/UHF, RKS/UKS, and RMP2/UMP2/PUMP2 schemes in Gaussian basis sets, including effective core potentials (ECP); LDA, GGA (BLYP, BP86, BPW91, PBE), meta-GGA (r^2SCAN), global hybrid (B3LYP, PBE0) and range-separated hybrid (omegaB97, omegaB97X, omegaB97X-D) functionals; analytical gradients and Hessians; geometry optimization, transition-state and reaction-path (IRC) searches, potential energy surface scans, harmonic frequencies and IR intensities, thermochemistry, counterpoise corrections, D3(BJ) dispersion, polarizable continuum solvation, density fitting (RI-J/RI-JK), linear-response TDDFT, and fractional-occupation smearing. The program has been verified against ORCA and PySCF on 50 molecules (30 for optimizations): the mean absolute deviations of the single-point energies do not exceed 7 muHa for HF, MP2, and the LDA, GGA, and global hybrid functionals except PBE and PBE0, whose systematic shifts of several tens of muHa are traced mainly to the value of mu in the PBE exchange; those of the optimized interatomic distances and harmonic frequencies do not exceed 1.2imes10^{-4} {AA} and 1.2 cm^{-1}. Corrections made since the first public version (0.82), mainly affecting vibrational frequencies, are documented with their effect on the verification results. Unlike large multi-language packages, StudDFT is a monolithic Fortran code with OpenMP parallelization, which simplifies its use in courses. Binaries for Windows and Linux, the documentation, and all test inputs and outputs are freely available.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.37483) | 2026-10-28
