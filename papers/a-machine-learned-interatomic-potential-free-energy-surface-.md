---
title: "A Machine-Learned Interatomic Potential Free-Energy Surface for the First Step of MIL-101(Cr) Secondary Building Unit Formation"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-atom-ph]
url: "https://arxiv.org/abs/2609.38518"
summary: "arXiv:2609.38518v1 Announce Type: cross Abstract: Metal-organic framework (MOF) self-assembly mechanisms remain poorly characterized because ab initio molecular dynamics (AIMD) are accurate but too co"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38518v1 Announce Type: cross Abstract: Metal-organic framework (MOF) self-assembly mechanisms remain poorly characterized because ab initio molecular dynamics (AIMD) are accurate but too computationally expensive to converge the free-energy surfaces (FES) that govern secondary building unit (SBU) nucleation and growth. This work addresses that limitation for the first step of MIL-101(Cr) SBU formation. Using MACE-POLAR-M, a long-range-aware equivariant machine-learned interatomic potential fine-tuned on a compact DFT reference dataset built from exploratory metadynamics, this work obtains a converged 2D FES for this step at a level of theory ({omega}B97M-V/def2-TZVPP) at which AIMD would be prohibitively expensive. The pre-trained model samples relevant configurations but gets the thermodynamics wrong, predicting an endothermic reaction and a false global minimum. Fine-tuning corrects both, recovering the expected exothermic process and the correct product basin in agreement with proposed literature mechanisms. The resulting FES also refines the mechanism. It shows that water release from the chromium center proceeds stepwise, through two sequential energy barriers, rather than the single concerted step originally proposed. We find that model accuracy is specific to the reaction coordinate and does not extend to the dissociated fragment configurations excluded from fine-tuning, a direct consequence of the training-data choice that protects accuracy along the reaction path for the FES prediction task. Together, these results establish a validated, computationally tractable route to obtain free-energy surfaces for MOF formation chemistry, transferable to other reactions where AIMD remains prohibitive, and identify training-data composition as the key determinant of which reaction properties a fine-tuned checkpoint can reliably describe.

**Source:** [arXiv physics.atom-ph](https://arxiv.org/abs/2609.38518) | 2026-10-01
