---
title: "Beyond the Four-Decade DIIS Default:Auxiliary-Curvature Acceleration of Self-Consistent-Field Calculations"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.07354"
summary: "arXiv:2608.07354v1 Announce Type: new Abstract: Direct inversion in the iterative subspace (DIIS), introduced in 1980, remains the practical default for accelerating Hartree-Fock and Kohn-Sham self-co"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.07354v1 Announce Type: new Abstract: Direct inversion in the iterative subspace (DIIS), introduced in 1980, remains the practical default for accelerating Hartree-Fock and Kohn-Sham self-consistent-field (SCF) calculations. Many later methods improve robustness or iteration count, but the near-zero overhead of DIIS makes a broad reduction in total wall time difficult. We introduce AURORA-SCF (auxiliary-curvature unified Riemannian orbital-response acceleration), which evaluates energy and gradient only with the requested target Hamiltonian while obtaining most orbital curvature from an independent valence-STO-3G model. A target-level, transported L-BFGS history corrects the model mismatch; a shifted matrix-free solve, trust region, and geodesic orbital update control the step. In 16 direct CPU RHF pairs spanning 137-1484 atomic orbitals, AURORA-SCF was faster in every case, reducing mean wall time by 26.2% and target J/K builds by 33.3%. In a separate set of 63 converged, energy-matched density-fitted GPU pairs spanning seven molecules, closed- and open-shell formalisms, and HF, PBE, B3LYP, and M06-2X, it was again faster in every included pair, with mean reductions of 26.5% in wall time and 31.9% in target J/K builds. Focused direct CPU and GPU sweeps show mean wall-time reductions of 30-34%. These results establish a specific advance beyond the four-decade DIIS default: transferred, secant-corrected curvature can reduce total SCF wall time, not merely iteration count, without changing the target stationary equations. The same optimization pattern also suggests a route to faster orbital optimization elsewhere in quantum chemistry and to multifidelity optimization across scientific computing.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.07354) | 2026-08-10
