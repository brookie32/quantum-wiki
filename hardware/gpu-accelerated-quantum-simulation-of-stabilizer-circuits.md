---
title: "GPU-Accelerated Quantum Simulation of Stabilizer Circuits"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.14641"
summary: "arXiv:2603.14641v2 Announce Type: replace Abstract: We introduce new parallel algorithms for efficiently simulating stabilizer (Clifford) circuits on GPUs, with a focus on data-parallel tableau evolut"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2603.14641v2 Announce Type: replace Abstract: We introduce new parallel algorithms for efficiently simulating stabilizer (Clifford) circuits on GPUs, with a focus on data-parallel tableau evolution and scalable handling of projective measurements. Our approach reformulates key bottlenecks in stabilizer simulation -- such as Gaussian elimination and measurement updates -- into GPU-tailored primitives that eliminate sequential dependencies and maximize memory coalescing. We implement these techniques in QuaSARQ, a GPU-accelerated stabilizer simulator designed for large qubit counts and many-shot sampling. Across a broad benchmark suite reaching 180,000 qubits and depth 1,000 (roughly 130M gates), QuaSARQ shows substantial runtime improvements, with up to 105imes speedup, and over 80% energy reduction on demanding instances. Moreover, QuaSARQ consistently outperforms Stim, a state-of-the-art CPU-optimized stabilizer simulator, as well as Qiskit-Aer (CPU/GPU), Qibo, Cirq, and PennyLane. Finally, QuaSARQ exhibits a significant advantage in many-shot sampling on large workloads. These results demonstrate that our parallel algorithms can significantly advance the scalability of stabilizer-circuit simulation, particularly for workloads involving extensive measurements and sampling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.14641) | 2026-09-24
