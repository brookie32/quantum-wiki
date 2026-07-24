---
title: "Machine-Learned Compact Subspace Generation for Quantum Selected Configuration Interaction within Density Matrix Embedding Framework"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20585"
summary: "arXiv:2607.20585v1 Announce Type: new Abstract: Sample-based Quantum Diagonalization (SQD), an extension of Quantum Selected Configuration Interaction (QSCI), has emerged as a promising hybrid quantum"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20585v1 Announce Type: new Abstract: Sample-based Quantum Diagonalization (SQD), an extension of Quantum Selected Configuration Interaction (QSCI), has emerged as a promising hybrid quantum-classical paradigm for computing molecular ground state energies. By leveraging quantum sampling instead of variational optimization, QSCI avoids barren plateaus and enables direct reconstruction of correlated electronic wavefunctions. However, existing configuration recovery techniques primarily enforce symmetry constraints without guaranteeing optimal selection of the most physically relevant configurations, often leading to unnecessarily large subspaces and increased classical diagonalization costs. In this work, we introduce a machine-learned compact subspace generation protocol based on Restricted Boltzmann Machines (RBMs), termed QSCI-RBM, and integrate it within the Density Matrix Embedding Theory (DMET) framework. The RBM is trained on quantum-sampled configurations to learn the underlying probability distribution of dominant determinants, enabling the targeted generation of high-probability configurations. We apply this framework to the simulation of a protein-ligand complex involving the inhibitor Carmofur bound to the SARS-CoV-2 main protease (M^{ext{pro}}). Our results demonstrate that DMET-QSCI-RBM achieves energies within the chemical accuracy threshold by accessing only approximately 4% of the configuration subspace. In contrast, standard DMET-SQD simulations failed to reach chemical accuracy while accessing up to 20% of the subspace, even as the chemical potential itself nearly converged. These findings highlight that RBM-assisted configuration generation produces significantly more compact subspaces while preserving physical accuracy, thereby reducing classical computational overhead and enabling the scalable quantum embedding simulation of complex biological systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20585) | 2026-07-24
