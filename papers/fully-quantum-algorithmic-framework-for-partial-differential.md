---
title: "Fully quantum algorithmic framework for partial differential equation-constrained optimization"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.14420"
summary: "arXiv:2511.14420v3 Announce Type: replace Abstract: Partial differential equation (PDE)-constrained optimization, where an optimization problem is subject to PDE constraints, arises in various applica"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2511.14420v3 Announce Type: replace Abstract: Partial differential equation (PDE)-constrained optimization, where an optimization problem is subject to PDE constraints, arises in various applications such as design, control, and inference. Solving such problems is computationally demanding because it requires repeatedly solving a PDE and using its solution within an optimization process. In this paper, we first propose a fully quantum algorithmic framework for solving PDE-constrained optimization problems. The proposed method combines a quantum PDE solver that prepares the solution vector as a quantum state, and a quantum optimizer that assumes oracle access to a quantized objective function. The central idea is the explicit construction of the oracle in a form of block-encoding for the objective function, which coherently uses the output of a quantum PDE solver. This enables us to avoid classical access to the full solution that requires quantum state tomography canceling out the potential quantum speedups. We also derive the overall computational complexity of the proposed method with respect to parameters for optimization and PDE simulation, where quantum speedup is inherited from the underlying quantum PDE solver. We numerically demonstrate the validity of the proposed method by applications, including a parameter calibration problem in the Black-Scholes equation and a material parameter design problem in the wave equation. This work presents the concept of composing quantum subroutines so that the weakness of one (i.e., prohibitive readout overhead) is neutralized by the strength of another (i.e., coherent oracle access), toward a bottleneck-free quantum algorithm.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.14420) | 2026-11-09
