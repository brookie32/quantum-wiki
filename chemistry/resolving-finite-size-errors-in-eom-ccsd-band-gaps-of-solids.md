---
title: "Resolving Finite-Size Errors in EOM-CCSD Band Gaps of Solids with Interacting-Bath Dynamical Embedding Theory"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2606.12621"
summary: "arXiv:2606.12621v3 Announce Type: replace-cross Abstract: Periodic equation-of-motion coupled-cluster theory with single and double excitations (EOM-CCSD) has shown promise for quantitative calculatio"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2606.12621v3 Announce Type: replace-cross Abstract: Periodic equation-of-motion coupled-cluster theory with single and double excitations (EOM-CCSD) has shown promise for quantitative calculations of band structures in solids. However, its steep computational scaling has limited calculations to relatively coarse k-point meshes, leading to sizable finite-size errors and discrepant estimates of thermodynamic-limit band gaps in recent benchmarks. In this work, we revisit EOM-CCSD band gaps for ten semiconductors and insulators using interacting-bath dynamical embedding theory (ibDET), a systematically improvable Green's function embedding framework that enables dense Brillouin-zone sampling at modest computational cost. By pushing the k-point sampling up to 10imes10imes10, well beyond the system sizes accessible in canonical periodic EOM-CCSD calculations, we significantly reduce finite-size errors and obtain stable thermodynamic-limit extrapolations. We further compare G_0W_0@PBE, G_0W_0@HF, and EOM-CCSD on an equal footing using the same numerical settings in PySCF. We find that EOM-CCSD yields a mean absolute error of 0.32 eV relative to experimental band gaps for a test set of ten semiconductors and insulators, lower than that of G_0W_0@PBE. For ZnO, EOM-CCSD also accurately describes the Zn 3d-band binding energy, despite overestimating the band gap. These results demonstrate that ibDET offers a practical route to high-accuracy many-body electronic structure calculations in periodic systems.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2606.12621) | 2026-08-18
