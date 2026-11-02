---
title: "Finite-Element Electromagnetic Analysis and Evaluation of Antenna Performance Metrics Using a Quantum Linear System Solver"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.40693"
summary: "arXiv:2610.40693v1 Announce Type: new Abstract: Electromagnetic analysis based on the finite element method is widely used in antenna design. At higher frequencies, however, the required mesh refineme"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.40693v1 Announce Type: new Abstract: Electromagnetic analysis based on the finite element method is widely used in antenna design. At higher frequencies, however, the required mesh refinement makes solving large sparse linear systems the main contributor to computational cost. Quantum linear system solvers offer a potential means of accelerating this step, but their output is a superposition state: reconstructing all components of the classical solution vector would forfeit the quantum speedup. Prior studies have proposed methods for obtaining physical quantities such as scattering cross sections and scattering parameters from the solution state. To support antenna design using fault-tolerant quantum computers, we formulate the total radiated power, the radiated power within a prescribed solid angle, and the dielectric and conductive losses as observables for efficient evaluation from a quantum solution state. These observables avoid the measurement cost of reconstructing all components of the output quantum state. We develop an end-to-end hybrid quantum--classical workflow that combines finite-element electromagnetic analysis, matrix preconditioning, a quantum linear system solver, and the evaluation of antenna design metrics. To validate the workflow, we performed numerical experiments evaluating these observables for an axisymmetric coaxially fed monopole antenna. Under idealized conditions, the relative errors in the total radiated power and the dissipated power with respect to the classical finite-element solution were on the order of 10^{-3}, confirming the consistency of the workflow. The proposed method is expected to provide a basis for using quantum linear system solvers to evaluate antenna performance and, in the future, to design high-frequency wireless devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.40693) | 2026-11-02
