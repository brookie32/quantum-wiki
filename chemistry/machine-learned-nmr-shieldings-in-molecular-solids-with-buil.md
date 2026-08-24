---
title: "Machine-Learned NMR Shieldings in Molecular Solids with Built-In Hybrid-Functional Molecular Corrections"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.21313"
summary: "arXiv:2608.21313v1 Announce Type: new Abstract: Fast and accurate chemical shielding estimators are essential for shielding-driven Nuclear Magnetic Resonance (NMR) crystallography. Machine-learning mo"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.21313v1 Announce Type: new Abstract: Fast and accurate chemical shielding estimators are essential for shielding-driven Nuclear Magnetic Resonance (NMR) crystallography. Machine-learning models for shielding predictions have matured significantly and today are primarily limited by the electronic structure reference data they are trained on. Here, we introduce ShiftML4, a shielding-tensor model trained directly on monomer-corrected calculations that approximate PBE0, rather than the PBE reference targeted by earlier ShiftML models. ShiftML4 is trained on a diverse set of structures containing 12 of the most common NMR nuclei in molecular organic solids. On experimental benchmark sets, the 13C isotropic RMSE against experiment is 1.67 ppm, compared with 2.34 ppm for GIPAW-PBE on the same geometries. ShiftML4 gives a similar 1H prediction RMSE to ShiftML3 (0.5 ppm) and improves the 15N RMSE from 7.24 to 6.08 ppm. The model also reduces errors in the shielding-tensor anisotropy, with an RMSE of 4.63 ppm on 13C CSA principal components against 5.85 ppm for GIPAW. The improvements in prediction accuracy are retained on better geometries. Basing shift predictions on structures relaxed with PET-MOLS, a recent machine-learned interatomic potential that reaches approximate hybrid-DFT geometries in seconds, lowers the ShiftML4 errors further to 0.48 ppm (1H), 1.49 ppm (13C) and 3.66 ppm (15N).

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.21313) | 2026-08-24
