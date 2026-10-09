---
title: "Parallelizing the Variational Quantum Eigensolver: From JIT Compilation to Multi-GPU Scaling"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.09951"
summary: "arXiv:2601.09951v2 Announce Type: replace Abstract: The Variational Quantum Eigensolver (VQE) is a hybrid quantum-classical algorithm for ground-state energies of molecular systems. We compute the pot"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2601.09951v2 Announce Type: replace Abstract: The Variational Quantum Eigensolver (VQE) is a hybrid quantum-classical algorithm for ground-state energies of molecular systems. We compute the potential energy surface of the hydrogen molecule (H2) at 100 bond lengths with PennyLane on the ERAU Vega cluster (AMD EPYC 9654 CPUs, 4 NVIDIA H100 GPUs) and compare a serial baseline, an Optax and Catalyst JIT version, a lightning.gpu version, and an MPI version. Early stopping, a larger learning rate, and warm starts reduce the iteration count from 30,000 to 7,033 and the runtime from 593.95 s to 143.80 s, while the time per iteration stays between 0.0198 s and 0.0204 s. At 4 qubits, lightning.gpu lowers the time per iteration to 0.0145 s. MPI runs with 2 to 32 ranks finish in 8.45 s to 5.04 s; the serial and MPI jobs ran under different core allocations, so we do not report their ratio as a parallel speedup. In a 4 to 26 qubit study with different CPU and GPU software stacks, the CPU/GPU time ratio ranges from 3.5 to 81.5. One H100 runs up to 29 qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.09951) | 2026-10-09
