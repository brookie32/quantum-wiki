---
title: "GenerativeQC: A Generative, GPU-Accelerated Quantum Chemistry Program"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.24744"
summary: "arXiv:2611.24744v1 Announce Type: new Abstract: GenerativeQC is an open-source, GPU-accelerated quantum chemistry program that computes energies and analytic nuclear forces from Hartree-Fock (HF) and "
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24744v1 Announce Type: new Abstract: GenerativeQC is an open-source, GPU-accelerated quantum chemistry program that computes energies and analytic nuclear forces from Hartree-Fock (HF) and density functional theory (DFT) to closed-shell density-fitted CCSD(T) and an MP2-assisted CCSD(T)/complete-basis-set (CBS) composite. Its scientific compiler translates symbolic equations into C++ and CUDA code and uses automatic differentiation to generate the derivative and response programs that analytic forces require. A native runtime executes these programs together with hand-written iterative solvers and integral routines. Across HF and DFT benchmarks for eight methods on water clusters of up to 96 atoms, GenerativeQC is faster than GPU4PySCF in all 128 comparisons on an RTX 5090 GPU and in all but two comparisons on an H100 GPU. For correlated wave functions, compiler-generated derivative contractions and transpose Jacobian operators enable complete density-fitted CCSD(T) and CCSD(T)/CBS analytic forces on GPUs, completing a CCSD(T)/CBS energy-and-force calculation for heptane (23 atoms) in 4.5 min on a single H100 GPU (17 min on RTX 5090).

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.24744) | 2026-11-19
