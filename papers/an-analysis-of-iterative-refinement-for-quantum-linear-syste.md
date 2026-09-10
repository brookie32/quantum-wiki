---
title: "An analysis of iterative refinement for quantum linear system solvers"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10250"
summary: "arXiv:2609.10250v1 Announce Type: new Abstract: We present and analyze an iterative refinement (IR) framework for improving the precision dependence of algorithms that combine a quantum linear system "
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.10250v1 Announce Type: new Abstract: We present and analyze an iterative refinement (IR) framework for improving the precision dependence of algorithms that combine a quantum linear system algorithm (QLSA) with quantum state tomography. Existing QLSAs achieve polylogarithmic dependence on the inverse error tolerance to prepare a quantum state encoding the solution, but extracting a classical description of such a state via tomography typically introduces a polynomial dependence on the target precision. To retain polylogarithmic dependence in the inverse error tolerance throughout the entire process, we develop an IR scheme that solves a sequence of related linear systems to progressively refine the solution while requiring only fixed-precision quantum subroutines, finally obtaining a classical description of a high-precision solution. We analyze the proposed framework under three input models: quantum-read/classical-write RAM (QRAM), linear combinations of unitaries (LCU), and sparse-access oracles. We evaluate the proposed scheme through numerical experiments on both quantum simulators and real quantum hardware. The results demonstrate that iterative refinement efficiently improves the precision of the solution and exhibits robustness to hardware noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10250) | 2026-09-10
