---
title: "Computing hydration free energies and crystalline solubility of drug-like molecules with MACE"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.33408"
summary: "arXiv:2611.33408v1 Announce Type: new Abstract: Accurate prediction of thermodynamic solubility is critical in drug discovery, where it influences oral bioavailability and drives decisions in formulat"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33408v1 Announce Type: new Abstract: Accurate prediction of thermodynamic solubility is critical in drug discovery, where it influences oral bioavailability and drives decisions in formulation chemistry. First-principles calculations of intrinsic solubility offer the potential to achieve superior generalization to existing direct, data-driven predictors, which often suffer significant performance degradation outside of their training distribution. Whilst free energy perturbation calculations provide a rigorous framework to estimate these quantities, their accuracy is typically limited by the quality of the empirical force field used. In this work, we present a computational workflow driven by the MACE family of machine learning interatomic potentials to compute the solubility of neutral drug-like molecules. We introduce lambda-MACE, a potential optimised for condensed-phase free energy calculations, which enables hydration free energy calculations at experimental accuracy on an evaluation set of 70 compounds from the FreeSolv database selected for their relevance to medicinal chemistry. We further combine these hydration free energy calculations with sublimation free energy calculations to predict crystalline solubility given a known experimental crystal structure, on an additional set of 10 compounds. We achieve state-of-the-art performance for each leg of the calculation, with experimental accuracy for the hydration leg, and accuracy competitive with industry-standard DFT for the sublimation leg. However, the overall errors after combining both legs lead to accuracy of 1.53 log units. This is significantly above the experimental accuracy (0.17-0.6 log units). Closing this gap will require substantially tighter accuracy in each leg, on the order of half of chemical accuracy (0.5 kcal/mol), with crystalline thermodynamics the hardest remaining challenge.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.33408) | 2026-11-26
