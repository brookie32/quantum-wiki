---
title: "Towards Out-of-Distribution Uncertainty Quantification for Machine-Learned Interatomic Potentials via Pre-Training"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.41801"
summary: "arXiv:2610.41801v1 Announce Type: cross Abstract: Informative uncertainty quantification (UQ) is essential for the practical deployment of machine-learned interatomic potentials (MLIPs), as it provide"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41801v1 Announce Type: cross Abstract: Informative uncertainty quantification (UQ) is essential for the practical deployment of machine-learned interatomic potentials (MLIPs), as it provides insight into their reliability across chemical space. Although numerous post-hoc uncertainty estimation methods for MLIPs have recently been proposed, most have been trained in low-data regimes, restricting their applicability to narrow domains of interest. Inspired by the emergence of foundational MLIPs, we propose pre-training uncertainty estimators on large, diverse datasets to enable broader applicability. We pre-train several UQ models on large materials science datasets to quantify the uncertainty of different MLIPs, and evaluate their performance on both in-distribution and out-of-domain (OOD) adsorption-energy predictions. We find that pre-trained uncertainty estimators provide viable zero-shot uncertainty estimates across multiple datasets, while fine-tuning consistently yields positive correlations between predicted uncertainty and prediction error, even on the most challenging datasets. These results lay the groundwork for foundational UQ models for MLIPs, ultimately facilitating their deployment in practical settings by providing users with a priori information about model reliability and applicability.



## Related
- [[reference-free-certification-of-machine-learning-interatomic|Reference-free certification of machine-learning interatomic potentials]]
- [[data-efficient-construction-of-material-specific-machine-lea|Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynamics Trajectories]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.41801) | 2026-11-02
