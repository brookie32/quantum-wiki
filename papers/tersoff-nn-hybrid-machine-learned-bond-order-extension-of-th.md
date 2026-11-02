---
title: "Tersoff-NN: Hybrid Machine-Learned Bond-Order Extension of the Tersoff Potential"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.15591"
summary: "arXiv:2610.15591v2 Announce Type: replace Abstract: Accurate, robust, and efficient interatomic potentials are highly desirable for large-scale molecular dynamics simulations. Although machine-learnin"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.15591v2 Announce Type: replace Abstract: Accurate, robust, and efficient interatomic potentials are highly desirable for large-scale molecular dynamics simulations. Although machine-learning interatomic potentials can reproduce first-principles potential-energy surfaces with high accuracy, they typically incur higher computational costs than conventional empirical potentials and may be less reliable outside their training domains. We developed Tersoff-NN, a hybrid machine-learning potential for Si, which retains the analytical radial interactions and cutoff structure of the Tersoff potential while representing its environment-dependent bond-order factor using compact neural networks (NNs). Benchmarks for 32,768-atom systems show that Tersoff-NN is 4-12 times faster than the Behler-Parrinello-type NN potentials tested in this study. Tersoff-NN improves the short-range structure of liquid Si relative to the conventional Tersoff potential, closely reproduces the ab initio radial and angular distributions, and reproduces the equilibrium structure of diamond Si and qualitative energetic trends among several crystalline phases. Furthermore, melt-quench simulations reveal a disordered solid with predominantly four-coordinated, tetrahedral-like local environments. Additionally, characteristic reconstruction motifs are retained on Si surfaces despite their exclusion from the training dataset. A direct comparison with an alternative atom-centered bond-order NN highlights the critical role of physical constraints in ensuring dynamic stability. Despite exhibiting comparable validation errors, the selected triplet-based architecture remains stable, while an alternative model exhibits unphysical bond-order growth and atomic collapse. These results confirm that learning only the bond-order term improves the description of diverse Si environments while retaining substantial computational efficiency and enhancing dynamical stability.



## Related
- [[generalizing-abell-tersoff-bond-order-potential-with-explici|Generalizing Abell-Tersoff bond-order potential with explicit high-order many-body correlations for robust extrapolation of potential energy surfaces]]
- [[mixture-of-experts-architectures-for-machine-learning-intera|Mixture of experts architectures for machine learning interatomic potentials]]
- [[data-efficient-construction-of-material-specific-machine-lea|Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynamics Trajectories]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.15591) | 2026-10-19
