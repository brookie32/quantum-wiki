---
title: "Linear-Scaling Potential-Free Data-Driven Molecular Dynamics for Arbitrary-Sized Water Clusters (ext{H}_2ext{O})_n"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2412.04442"
summary: "arXiv:2412.04442v5 Announce Type: replace-cross Abstract: Conventional molecular dynamics (MD) simulation approaches, such as extit{ab initio} MD (AIMD) and empirical force field MD (EFFMD), face sign"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2412.04442v5 Announce Type: replace-cross Abstract: Conventional molecular dynamics (MD) simulation approaches, such as extit{ab initio} MD (AIMD) and empirical force field MD (EFFMD), face significant trade-offs between physical accuracy and computational efficiency. This work presents a linear-scaling potential-free data-driven molecular dynamics (PDMD) framework for predicting system energy and atomic forces of arbitrary-sized water clusters (ext{H}_2ext{O})_n. Specifically, PDMD employs a Gaussian-based atomic geometry descriptor to generate high-dimensional, atomistic footprints, then leverages ChemGNN, a graph neural network model that adaptively learns the atomic chemical environments without requiring extit{a priori} knowledge. Through an iterative self-consistent training approach, the converged PDMD achieves a mean absolute error of 1.39 meV/atom for energy, outperforming other state-of-the-art models such as DeepMD, MACE, NequIP, and SevenNet by at least 2.6x in accuracy with the same dataset. As a result, the linear-scaling PDMD can reproduce the AIMD properties of water clusters at orders-of-magnitude lower computational cost, as illustrated by simulations of systems consisting of thousands or more molecules. These results demonstrate that the proposed PDMD offers multiphase predictive power and enables ultra-fast, general-purpose MD simulations while retaining AIMD-level accuracy. This accuracy is achieved by efficiently capturing many-body potentials that are critical in numerous polyatomic systems but are often missing in EFFMD. Moreover, we have constructed an extit{ab initio} dataset with over 300,000 (ext{H}_2ext{O})_n structures, standardized in a unified PyTorch Geometric framework, to support scalable evaluation of artificial intelligence methods for molecular dynamics.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2412.04442) | 2026-07-24
