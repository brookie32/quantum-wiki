---
title: "PyQLAS: A Quantum-Classical Hybrid Solver Library for Linear Systems"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41317"
summary: "arXiv:2610.41317v1 Announce Type: new Abstract: Quantum algorithms solve a linear system at a cost that grows only polylogarithmically in its dimension, but on present-day hardware that advantage is r"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41317v1 Announce Type: new Abstract: Quantum algorithms solve a linear system at a cost that grows only polylogarithmically in its dimension, but on present-day hardware that advantage is realised only if the quantum and the classical parts of a solve are apportioned deliberately. We present PyQLAS, a quantum--classical hybrid library for linear systems that exposes this apportionment as a design parameter rather than a fixed assumption. PyQLAS builds three nested solvers around a single variational core---a variational solver, an outer residual iteration, and a Krylov-subspace projection---so that the quantum subroutine can be held at a fixed circuit width while the classical host absorbs the growth of the problem. Around them, the library supplies preconditioning at two independent levels, dimension alignment, checkpointing, and device-budget control, and a solve written against the interface runs unchanged on an exact state-vector simulator, on a local sampler, and on a real superconducting processor. The library is validated on the IEEE 118-bus power flow, a standard test system in which the linear solver is embedded in a classical Newton iteration. There, the iteration converges to the specified tolerance and reproduces the classical reference solution to within 2.3imes10^{-8} p.u. in voltage magnitude and 3.4imes10^{-6} degrees in voltage angle.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41317) | 2026-11-02
