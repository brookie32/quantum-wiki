---
title: "FNO-Based Inverse Co-Design of Semiconducting Quantum-Dot Devices"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06994"
summary: "arXiv:2611.06994v1 Announce Type: new Abstract: Gate-defined semiconductor quantum dots are promising building blocks for scalable spin-based quantum processors, however their operational properties d"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.06994v1 Announce Type: new Abstract: Gate-defined semiconductor quantum dots are promising building blocks for scalable spin-based quantum processors, however their operational properties depend on several fabrication and control parameters, such as lithographic gate layout and applied voltages. Existing device architectures have been refined through repeated fabrication and experimental testing, producing layouts that support reliable device operation. However, this process does not exhaustively explore the design space, limiting the ability to obtain qubits with targeted properties. We address these challenges by presenting a differentiable inverse co-design framework for electrostatically defined quantum dots that jointly optimises gate voltages and the gate electrode layout. A semiclassical Thomas--Fermi electrostatic simulator provides reference data for a Fourier neural operator (FNO) surrogate, which predicts the two-dimensional charge-density field. The desired spatial distribution of the confined charge defines the target quantum-dot geometry for inverse design. The FNO reproduces charge densities with a relative L^2 test error of just 0.6% and enables millisecond-scale differentiable evaluations. Relative to the CPU-based physics simulator, the FNO achieves a 17,000-fold speed-up on GPU for a single design, with further performance gains enabled by batched inference. When embedded in a gradient-based design loop with fabrication constraints, the FNO can produce both vertically and horizontally elongated double-dot confinement geometries from the same initial conditions. The ability to engineer these distinct confinement configurations demonstrates control over quantum-dot shape and position, providing a route towards designing devices with distinct qubit-relevant operating properties prior to fabrication.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06994) | 2026-11-06
