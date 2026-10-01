---
title: "Oscillator-Qubit Primitives for a Molecular Quantum Dynamics Simulator"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40078"
summary: "arXiv:2609.40078v1 Announce Type: new Abstract: Molecular quantum dynamics simulations that treat both electrons and nuclei quantum mechanically are crucial for predicting chemical reactions. With cla"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40078v1 Announce Type: new Abstract: Molecular quantum dynamics simulations that treat both electrons and nuclei quantum mechanically are crucial for predicting chemical reactions. With classical computation, a full wave-function representation of both types of particles requires resources that grow exponentially with their number. Oscillator-qubit processors, including trapped-ion and circuit QED devices, represent electronic states with qubits and nuclear vibrations with oscillators. Their native operations produce linear vibronic interactions, from which programmable anharmonic interactions can be built. Product-formula approaches build the corresponding phase gates by repeating small noncommuting phase steps, and quantum signal processing (QSP) approaches approximate each gate directly with a Fourier series. Simulations apply many such gates in sequence, so accumulated cost and error limit how long the dynamics can be followed. We propose near-optimal quantum primitives for molecular quantum dynamics simulation, covering the representations of both types of particles and their interactions. We synthesize nonlinear and multimode bosonic phase gates using generalized Jacobi-Anger (GJA) expansions within QSP, with a cost that grows near-optimally in both interaction strength and precision. Our interaction model and gate synthesis each have their own accuracy setting. Chosen together, these settings make our multimode benchmark circuits about one-third shorter than those of the previous direct QSP approach. We then simulate energy exchange between the stretching and bending vibrations of a simplified carbon dioxide model. With circuit-QED noise, a short simulation narrowly misses our accuracy criteria at qubit and oscillator lifetimes near 2 ms and 5 ms. These lifetimes mark a concrete checkpoint on the way to simulating anharmonic multimode molecular quantum dynamics on near-term oscillator-qubit processors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40078) | 2026-10-01
