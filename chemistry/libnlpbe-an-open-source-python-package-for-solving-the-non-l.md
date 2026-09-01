---
title: "libNLPBE: An Open-Source Python Package for Solving the Non-Linear Poisson-Boltzmann Equation"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.28908"
summary: "arXiv:2608.28908v1 Announce Type: new Abstract: Solvent environments surrounding a solute can significantly alter its chemical properties. These changes become more prominent in electrolyte solutions,"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.28908v1 Announce Type: new Abstract: Solvent environments surrounding a solute can significantly alter its chemical properties. These changes become more prominent in electrolyte solutions, where mobile ions largely influence the solute through electrostatic interactions. A theoretical description of these ionic effects will benefit the design of chemistry performed in electrolyte solutions. As a result, the non-linear Poisson-Boltzmann equation (NLPBE) has emerged as an efficient implicit solvent model for electronic structure calculations to address such effects. However, the limited availability of NLPBE solvers for molecular electronic structure calculations greatly hinders theoretical investigation into the ionic effects. To improve accessibility of the NLPBE, we present libNLPBE, an open-source Python library, that solves the NLPBE for molecular systems in combination with density functional calculations, specifically to obtain electrostatic correction terms arising from the electrolyte solution environment for the Fock matrix. The library employs the density fitting (DF) approximation to efficiently calculate solute electrostatic potentials. Furthermore, we develop the modified Damped Inexact Newton Multigrid developed by Holst (mDINMH) method for solving the NLPBE. The mDINMH features a symmetric preconditioner for solving the Newton equation, which enables the use of robust multigrid methods designed for symmetric linear operators. In addition, an algebraic multigrid method has been incorporated into the mDINMH to support a broad range of grid points. We also present a GPU-accelerated version of libNLPBE to leverage parallelization efficiency of GPUs.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.28908) | 2026-09-01
