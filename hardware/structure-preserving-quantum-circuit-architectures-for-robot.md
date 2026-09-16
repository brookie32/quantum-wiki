---
title: "Structure-Preserving Quantum Circuit Architectures for Robot Kinematics"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16089"
summary: "arXiv:2609.16089v1 Announce Type: cross Abstract: Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16089v1 Announce Type: cross Abstract: Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite-depth hardware. This work introduces a quantum representation and circuit architecture for rigid-body transformations and specializes it to Denavit--Hartenberg kinematics of serial open-chain manipulators. Each translational contribution is factorized into a classical metric magnitude and a signed unit direction encoded by a single-qubit Bloch vector, while parameterized rotations reproduce the ordered propagation of frame directions. A selector register prepares probabilities proportional to the contribution magnitudes, and the reduced state of a designated readout qubit encodes their normalized weighted sum. The retained classical scale then reconstructs the metric end-effector position. Two additional readout qubits encode terminal-frame axes, providing a compact and geometrically interpretable pose interface. At the ideal expectation-value level, measured Pauli observables reproduce the corresponding classical kinematic quantities. Alternative circuit architectures realize the same representation with different tradeoffs in qubit count, circuit depth, controlled operations, and measurement requirements. Validation on a serial manipulator yields numerically negligible position and orientation reconstruction errors under ideal simulation. Finite-shot simulations, noisy executions, transpilation analysis, and a hardware demonstration further characterize statistical error, noise sensitivity, and implementation overhead without asserting computational advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16089) | 2026-09-16
