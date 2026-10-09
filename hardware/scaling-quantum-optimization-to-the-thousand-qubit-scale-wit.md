---
title: "Scaling Quantum Optimization to the Thousand-Qubit Scale with Distributed Quantum Sampling"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10772"
summary: "arXiv:2610.10772v1 Announce Type: new Abstract: The Minimum Birkhoff Decomposition (MBD) seeks a sparse weighted sum of matchings and is a challenging optimization problem with applications in network"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.10772v1 Announce Type: new Abstract: The Minimum Birkhoff Decomposition (MBD) seeks a sparse weighted sum of matchings and is a challenging optimization problem with applications in network scheduling and energy trading. We scale a quantum-assisted decomposition method by combining single-layer QAOA sampling with Extended Fully-Corrective Frank-Wolfe (E-FCFW) optimization, spectral graph partitioning, and greedy feasibility repair. We demonstrate the pipeline on the 1,354-node PEGASE bus test case (representing a 1,354-bus transmission grid with 1,710 transmission lines), whose 1,710 edges define a native 1,710-variable matching optimization problem requiring 1,710 qubits in the unpartitioned encoding. Partitioning enables distributed execution on IBM superconducting quantum processors. The best reported hardware result uses a 50-qubit partition bound, while reducing partitions to 20 qubits degrades convergence in the partition-size comparison. Larger partitions are more demanding for matrix product state (MPS) simulation, and bond-dimension tests show that truncating quantum correlations reduces candidate quality. The results therefore motivate retaining a substantive quantum sampling task within each partition as the overall problem scales. On the PEGASE-1354 benchmark, repaired QAOA samples achieve lower residual decomposition error than both simulated annealing and uniform random sampling baselines, while spatial circuit packing reduces hardware execution time by approximately a factor of three. These results demonstrate that combining spectral partitioning, spatial circuit packing, and classical feasibility repair provides an executable path for deploying gate-based quantum sampling on thousand-variable constrained optimization problems on current hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10772) | 2026-10-09
