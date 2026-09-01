---
title: "Benchmarking Zero-Setup Quantum Circuit Simulators"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09882"
summary: "arXiv:2607.09882v2 Announce Type: replace Abstract: Practitioners increasingly rely on hosted simulation environments, but their performance characteristics remain poorly documented. We present a syst"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2607.09882v2 Announce Type: replace Abstract: Practitioners increasingly rely on hosted simulation environments, but their performance characteristics remain poorly documented. We present a systematic benchmarking study of GPU-accelerated approximate quantum simulation across two widely used methods: matrix product states (MPS) and Pauli path simulation (PPS), comparing BlueQubit (a hosted tool that handles hardware provisioning, simulator configuration, and job orchestration) against AWS Braket, Quantum Rings, PPS-Qiskit, and PauliPropagation.jl. For MPS, we find that GPU runtime yields sub-quadratic scaling with bond dimension, with a growing advantage over CPU at increasing scale. For Pauli path simulation on IBM's 127-qubit kicked Ising benchmark, GPUs deliver up to 1{,}400imes speedup at fine truncation thresholds (elta = 2.5 imes 10^{-5}, 27.6M Pauli terms), and are the only backends that reach accuracy regimes below elta = 10^{-5}, which remained inaccessible to the commodity CPU-based implementations and self-contained SDKs evaluated here. We also provide a reproducible characterization of these simulators across regimes, including tradeoffs that isolated evaluations do not show. To support transparency and reuse, we provide a public GitHub repository containing all benchmarking code and configurations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09882) | 2026-09-01
