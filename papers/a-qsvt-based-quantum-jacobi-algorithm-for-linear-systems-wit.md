---
title: "A QSVT-Based Quantum Jacobi Algorithm for Linear Systems with Application to the Poisson Equation"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.24266"
summary: "arXiv:2609.24266v1 Announce Type: new Abstract: Many computational fluid dynamics (CFD) algorithms solve partial differential equations by discretization, resulting in large and sparse systems of line"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.24266v1 Announce Type: new Abstract: Many computational fluid dynamics (CFD) algorithms solve partial differential equations by discretization, resulting in large and sparse systems of linear equations. While iterative methods are widely used to solve these systems classically, most existing quantum linear system solvers target the solution through matrix inversion rather than approximating it using an iterative procedure. In this work, we develop a quantum implementation of the Jacobi method based on quantum singular value transformation (QSVT). By reformulating the Jacobi iteration as a polynomial transformation of a block-encoded operator, the algorithm requires only a constant ancilla overhead with respect to the number of iterations while maintaining a circuit depth that scales linearly with the iteration number. We demonstrate the algorithm for one- and two-dimensional Poisson problems, including the pressure Poisson equation arising in Chorin's projection method for the lid-driven cavity flow. The proposed algorithm provides a promising building block for future quantum implementations of multigrid methods and preconditioning techniques, bringing quantum algorithms closer to established CFD solution strategies.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.24266) | 2026-09-22
