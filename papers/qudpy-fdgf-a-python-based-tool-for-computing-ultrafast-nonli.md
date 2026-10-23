---
title: "QuDPy-FDGF: A Python-Based Tool for Computing Ultrafast Nonlinear Optical Responses Using Frequency Domain Green's Functions"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.30398"
summary: "arXiv:2610.30398v1 Announce Type: new Abstract: We present QuDPy-FDGF, an open-source Python framework that evaluates Liouville-space pathways as hybrid chains of time propagators and frequency-domain"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30398v1 Announce Type: new Abstract: We present QuDPy-FDGF, an open-source Python framework that evaluates Liouville-space pathways as hybrid chains of time propagators and frequency-domain Green's functions. Frequency-resolved intervals are computed directly through shifted linear systems, without time propagation followed by a Fourier transform, while other intervals may remain in the time domain. A model-agnostic block interface separates the physical model from pathway construction, numerical propagation, and detection. The released implementation provides an explicit dense Liouville-space backend for reference calculations and a sector-resolved sparse backend using matrix-free generator actions, Krylov time propagation, and generalized minimal residual (GMRES) resolvent solves. Its observable layer reuses propagated pathway responses to evaluate operator expectation values, action-detected readout interactions, instantaneous jump rates, and integrated mean jump counts. The framework is assessed on an analytically solvable open two-level system and on two examples of increasing complexity: the complete third-order rephasing response, with its eight sequences, of a thermally initialized anisotropic Heisenberg (XXZ) spin chain with unequal excitation sectors, and two coupled dissipative anharmonic modes whose spectra depend on the detected observable, with the fifth-order double-quantum response of their closed limit. The calculations reproduce the analytical two-level response, check the matrix-free sparse evaluation against the dense assembly of the generator, and recover the harmonic-limit cancellation of the fifth-order signal when the required three-excitation manifold is retained. QuDPy-FDGF therefore provides a unified framework for pathway- and observable-resolved nonlinear spectroscopy in finite or truncated Hilbert spaces with unitary or Markovian Gorini--Kossakowski--Sudarshan--Lindblad (GKSL) dynamics.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.30398) | 2026-10-23
