---
title: "Graph Neural Network Force Fields (GPTFF-mol) for Organic Molecules from Optimization Trajectories (OpenGEM26)"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.21369"
summary: "arXiv:2607.21369v1 Announce Type: new Abstract: Density functional theory (DFT) serves as a reliable tool for atomistic molecular simulations, while machine learning potentials have become powerful co"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21369v1 Announce Type: new Abstract: Density functional theory (DFT) serves as a reliable tool for atomistic molecular simulations, while machine learning potentials have become powerful complements to balance accuracy and efficiency. In this work, we release OpenGEM26 (Open Generated Ensemble of Molecules, 2026), a large-scale dataset comprising 200,000 unique molecules and 4.4 million conformations composed of H, C, N, O, S and Cl with up to ten heavy atoms. All calculations are carried out at the {omega}B97X-D/Def2-SVP and Def2-TZVP levels with dispersion corrections, and complete structural optimization trajectories and abundant non-equilibrium structures are recorded. Statistical analyses confirm that this dataset covers a broader conformational space than QM9 in terms of energy, bond lengths and bond angles. A graph neural network-based potential GPTFF-mol is trained using the new dataset, achieving an energy mean absolute error of 16 meV/molecule, which is equivalent to 0.82meV/atom, and superior force prediction performance compared with ANI-2x. Validated by butane rotation and keto-enol tautomerization tests, the model accurately describes molecular dynamical behaviors and reaction barriers at distorted geometries. This work provides a high-quality resource and robust ML potential for efficient simulations of sulfur- and chlorine-containing organic molecules.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.21369) | 2026-07-24
