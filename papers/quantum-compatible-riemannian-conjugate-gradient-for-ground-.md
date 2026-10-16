---
title: "Quantum-compatible Riemannian conjugate gradient for ground-state preparation"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21782"
summary: "arXiv:2610.21782v1 Announce Type: new Abstract: Riemannian optimization provides a natural geometric framework for designing quantum algorithms for ground-state preparation, most notably through quant"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21782v1 Announce Type: new Abstract: Riemannian optimization provides a natural geometric framework for designing quantum algorithms for ground-state preparation, most notably through quantum imaginary-time evolution. However, existing geometry-aware approaches primarily employ steepest-descent updates, leaving more advanced methods from classical Riemannian optimization largely unexplored. In this work, we introduce quantum conjugate gradient descent (QCGD), a quantum-compatible implementation of Riemannian conjugate gradient that combines the steepest descent direction with information retained from previous search directions. In our numerical experiments, the proposed approach achieves faster convergence per iteration than the baseline double-bracket quantum imaginary-time evolution (DB-QITE) algorithm, and we quantify the associated circuit cost with gate counts produced by Qrisp. This improvement, however, comes at the cost of increased circuit depth for each update step, revealing a trade-off between convergence rate and implementation complexity. Nevertheless, since the circuit depth for those algorithms grows exponentially with the number of iterations, the proposed method may offer practical advantages, particularly in the early fault-tolerant regime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21782) | 2026-10-16
