---
title: "QuScope: An Open-Source Python Framework for Quantum-Circuit Simulation of Transmission Electron Microscopy"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02782"
summary: "arXiv:2608.02782v1 Announce Type: new Abstract: Image formation in transmission electron microscopy (TEM) is governed by the coherent evolution of the electron wavefunction through the specimen and th"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.02782v1 Announce Type: new Abstract: Image formation in transmission electron microscopy (TEM) is governed by the coherent evolution of the electron wavefunction through the specimen and the objective lens. This physics maps naturally onto the gate model of quantum computation. We present QuScope, an open-source Python framework that expresses the complete TEM image-formation pipeline as quantum circuits. The Nimes N electron wavefunction is amplitude-encoded in 2log_2 N qubits, and every optical element, including phase-grating transmission, Fresnel propagation between specimen slices, and the aberrated objective lens, is implemented as a diagonal unitary conjugated by quantum Fourier transforms. On this foundation, QuScope v0.2.0 implements validated imaging pipelines, covering conventional TEM under the phase-object approximation, full multislice CTEM and STEM for thick specimens. All quantum results reported here come from exact, noise-free statevector simulation of the circuits on classical hardware, and every result is validated against a classical twin implementation. Quantum and classical multislice exit waves agree to unit fidelity, and all physical constants are verified against standard references. We provide transpiled quantum-resource estimates for each algorithm, an analysis of the diagonal-synthesis bottleneck that governs near-term hardware execution, and a fully tested, documented, and pip-installable package. QuScope v0.2.0 is available at https://github.com/QuScope/QuScope.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02782) | 2026-08-05
