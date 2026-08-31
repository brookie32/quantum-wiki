---
title: "Efficient Quantum Simulation of Variable-Coefficient Transport with Continuous Source Injection"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27712"
summary: "arXiv:2608.27712v1 Announce Type: new Abstract: Quantum time-marching algorithms for transport PDEs often represent variable coefficients and forcing through register-expanding dilations, block-encodi"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27712v1 Announce Type: new Abstract: Quantum time-marching algorithms for transport PDEs often represent variable coefficients and forcing through register-expanding dilations, block-encoding oracles, or repeated postselection. We present an alternative algorithm for a forced variable-coefficient advection-diffusion equation in flow-inspired skew-symmetric form that incorporates spatially varying velocity, viscous dissipation, and persistent source injection with a peak logical requirement of n_q+1 qubits. A centered skew-symmetric discretization makes the advection operator strictly skew-Hermitian for arbitrary velocity profiles, enabling an ancilla-free unitary realization using a Gray-code Trotter sequence of controlled-R_y rotations. Diffusion is applied in the Fourier basis through a uniformly controlled rotation on one postselected ancilla, which is measured, reset, and reused between the two diffusion half-steps, while the source is incorporated classically through second-order Strang splitting. Statevector simulations for N=16 and 32 recover second-order temporal convergence against high-accuracy classical solutions, while Richardson extrapolation gives fourth-order accuracy and reduces kernel calls by factors of four to fourteen. Independent tests through N=256 confirm second-order spatial consistency. We further show that the per-step ancilla failure probability is proportional to the instantaneous viscous dissipation rate, making postselection cost self-regulating over a fifty-fold viscosity range. Stable evolution is demonstrated for 5imes10^4 time steps without observable secular error growth, while Gray-code advection accounts for 71--95% of transpiled controlled-NOT gates. The fixed-width kernel provides a qubit-efficient building block for near-term hardware studies, although classical readout and state re-preparation remain the main obstacles to coherent multistep evolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27712) | 2026-08-31
