---
title: "Low-Depth and Noise-Resilient Quantum State Preparation for Partial Differential Equations via Virtual Rz"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17249"
summary: "arXiv:2608.17249v1 Announce Type: new Abstract: Preparing smooth real-amplitude quantum states is a key subroutine in quantum solvers for dissipative PDEs, such as LCHS, where discretized positive wei"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17249v1 Announce Type: new Abstract: Preparing smooth real-amplitude quantum states is a key subroutine in quantum solvers for dissipative PDEs, such as LCHS, where discretized positive weights must be encoded into amplitudes. Exact state-preparation decompositions can reach unit fidelity ideally, but their two-qubit depth grows quickly and causes severe fidelity loss on NISQ hardware. We propose a low-depth, hardware-aware variational ansatz tailored to smooth, weakly entangled, near-real target distributions typical of damped PDE dynamics. The circuit uses one layer of local Ry rotations to generate real amplitudes, a nearest-neighbor CZ entangling layer to introduce limited entanglement, and additional Rz rotations implemented virtually as frame updates. Virtual Rz operations add no physical pulses and do not increase circuit duration, providing extra degrees of freedom without enlarging the gate footprint; in simulation they are treated as ideal to isolate their benefit. From a tensor-network viewpoint, the alternating structure restricts the state to a low-bond-dimension MPS, matching the target smoothness (for 3 qubits, bond dimension <= 2). We optimize parameters with COBYLA to minimize infidelity and benchmark against exact state preparation (Qiskit) and a RealAmplitudes (CZ) baseline. Under depolarizing noise representative of NISQ and early fault-tolerant regimes, the proposed single-layer circuit achieves high ideal fidelity with O(n) depth and substantially higher noisy fidelity than deeper exact constructions. In coherent-noise sweeps, virtual Rz parameters absorb systematic phase errors and axis mismatch, maintaining near-unity fidelity over a wide error range. These results indicate that virtual-Rz-enabled, low-depth circuits provide a practical, noise-resilient state-preparation primitive for PDE solvers on NISQ and early FTQC hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17249) | 2026-08-19
