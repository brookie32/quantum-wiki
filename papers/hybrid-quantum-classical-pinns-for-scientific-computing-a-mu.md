---
title: "Hybrid Quantum-Classical PINNs for Scientific Computing: A Multi-GPU Open-Source Framework"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.15645"
summary: "arXiv:2604.15645v2 Announce Type: replace-cross Abstract: We present QPINNACLE, an open-source computational framework for physics-informed neural networks (PINNs) that integrates modern training stra"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2604.15645v2 Announce Type: replace-cross Abstract: We present QPINNACLE, an open-source computational framework for physics-informed neural networks (PINNs) that integrates modern training strategies, multi-GPU acceleration, and hybrid quantum-classical architectures within a unified modular workflow. The framework enables systematic evaluation of PINN performance across benchmark problems including 1D hyperbolic conservation laws, incompressible flows, and electromagnetic wave propagation. It supports a range of architectural and training enhancements, including Fourier feature embeddings, random weight factorization, strict boundary condition enforcement, adaptive loss balancing, curriculum training, and second-order optimization strategies, with extensibility to additional methods. We provide a comprehensive benchmark study quantifying the impact of these methods on convergence, accuracy, and computational cost, and analyze distributed data parallel scaling in terms of runtime and memory efficiency. In addition, we extend the framework to hybrid quantum-classical PINNs and derive a formal estimate for circuit-evaluation complexity under parameter-shift differentiation. Results highlight the sensitivity of PINNs to architectural and training choices, confirm their high computational cost relative to classical solvers, and identify regimes where hybrid quantum models offer improved parameter efficiency. QPINNACLE provides a foundation for benchmarking physics-informed learning methods and guiding future developments through quantitative assessment of their trade-offs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.15645) | 2026-08-11
