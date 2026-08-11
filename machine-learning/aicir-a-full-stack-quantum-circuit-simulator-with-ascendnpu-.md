---
title: "Aicir: A Full-Stack Quantum Circuit Simulator with AscendNPU Support"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09733"
summary: "arXiv:2608.09733v1 Announce Type: new Abstract: Quantum computing is a promising way to study problems that are difficult for classical methods, but current quantum hardware still faces limits in scal"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09733v1 Announce Type: new Abstract: Quantum computing is a promising way to study problems that are difficult for classical methods, but current quantum hardware still faces limits in scale, noise, and fidelity. Running quantum algorithms on physical machines can also be costly. Quantum circuit simulators therefore remain important because they let researchers design and test algorithms on classical computers before using quantum hardware. Most high-performance simulators provide GPU backends, while few offer native support for NPUs. This gap limits the computing platforms available for quantum-algorithm research. We developed Aicir to provide a full-stack quantum circuit simulator with a native Huawei Ascend NPU backend. Aicir connects circuit construction, several state representations, measurement, differentiation, variational algorithms, quantum machine learning, and quantum architecture search through one programming model. It also supports noise simulation, tensor-network and matrix-product-state engines, and distributed state simulation. On the NPU, paired real tensors, fixed-rank gate views, and hardware-specific formulas keep the tested simulation paths on the device. The same representation lets Aicir partition a state across 2^{p} NPUs while retaining reverse-mode differentiation. We validated native execution with CPU fallback disabled and checked distributed communication and gradients on 2, 4, and 8 NPUs. For the tested fused layered circuits, Aicir's CPU runtime is within 0.97--1.28imes that of Qiskit Aer and 0.76--1.10imes that of Cirq. These results place its CPU execution in the same range as established simulators for this workload, while the NPU tests establish correct native execution rather than CPU-to-NPU speedup.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09733) | 2026-08-11
