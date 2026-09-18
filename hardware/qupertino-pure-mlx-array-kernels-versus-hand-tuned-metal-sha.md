---
title: "Qupertino: Pure MLX Array Kernels versus Hand-Tuned Metal Shaders for Quantum Circuit Simulation on Apple Silicon"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.19147"
summary: "arXiv:2609.19147v1 Announce Type: new Abstract: We present Qupertino, an open-source quantum circuit simulator for Apple Silicon, and use it to ask how far a simulator written purely in MLX array oper"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19147v1 Announce Type: new Abstract: We present Qupertino, an open-source quantum circuit simulator for Apple Silicon, and use it to ask how far a simulator written purely in MLX array operations can go and what remains for hand-tuned Metal shaders. The framework ships two measured tiers. The pure tier dispatches structured gates to specialized MLX kernels: diagonal gates run as broadcast phase multiplies, controlled gates as masked half-state updates, and SWAP as an axis permutation; a paired dense-path ablation attributes a 25-33x speedup to this dispatch alone. The opt-in shader tier adds hand-written Metal kernels for every structured layer family in our benchmarks, including phase-LUT diagonals, GF(2) affine permutation gathers, fused tensor-product single-qubit layers, radix-4 QFT and Walsh-Hadamard butterflies, and basis-conjugated XX/YY Trotter layers; runtime fusion detectors route work to them while preserving circuit semantics exactly, confirmed by parity tests. In a four-way interleaved campaign on M1 Max (two warmups, ten measured repeats per cell), the shader tier is fastest by mean runtime in all 18 comparison cells against same-machine Qiskit Aer CPU and PennyLane lightning.qubit. At 25 qubits, gate-stream QFT runs in 0.0591 +/- 0.0029 s (paired 47.2x over Aer, 95.3x over PennyLane) and TFIM Trotter evolution in 0.495 +/- 0.035 s (36.2x and 67.2x). Across a 29-workload suite, the shader tier's paired speedup over pure MLX reaches 25x, with 25 of 29 workloads accelerating above parity. The framework also supports variational ansatz workloads, QAOA, QCBM, Trotter-Suzuki Hamiltonian simulation, and OpenQASM 2.0 import (unitary subset); a preliminary MPS backend reaches 150 qubits on limited-entanglement workloads. Correctness rests on 253 Python tests, independent complex128 checks, and a Trotter-error curve against exact diagonalization. State-vector memory remains exponential in qubit count.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.19147) | 2026-09-18
