---
title: "What Does a Semilocal Machine-Learning Correction Actually Learn? Size-Dependent Errors across Four Parent Functionals"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.37571"
summary: "arXiv:2609.37571v1 Announce Type: new Abstract: Machine-learning (ML) corrections to density functional approximations (DFAs) offer a route to improving electronic-structure predictions while retainin"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37571v1 Announce Type: new Abstract: Machine-learning (ML) corrections to density functional approximations (DFAs) offer a route to improving electronic-structure predictions while retaining the efficiency of semilocal functionals. An important question is whether such corrections learn transferable improvements or instead compensate for errors specific to the parent functional. Here, we address this question by applying the semilocal ML correction of Wang extit{et al.} [J.~Chem.~Phys.~extbf{158}, 154107 (2023)] to PBE, B3LYP, SCAN, and r^2SCAN, while keeping the network architecture, loss function, training set, and optimization protocol unchanged. We find that the learned correction develops a systematic size-dependent contribution to atomization energies for all four parents, with |r|geq0.9999 along the n-alkane series, where r is the Pearson coefficient of the linear fit. Its magnitude and sign depend systematically on the parent: the correction partially compensates the size-dependent errors of PBE and B3LYP, but introduces substantial size-dependent contributions for SCAN and r^2SCAN, whose parent errors show little size dependence. In contrast, ionization potentials, electron affinities, and isomerization energies are largely unaffected. Spatial decomposition further reveals distinct origins of this extensive contribution, with bonding regions dominating for B3LYP, SCAN, and r^2SCAN and core regions dominating for PBE. These results show that the global-energy ML correction is strongly dependent on the error structure of its parent DFA, highlighting size-dependent error accumulation as a critical consideration in the assessment and development of ML-enhanced density functionals.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.37571) | 2026-09-30
