---
title: "Qu-Trefoil: Large-Scale Quantum Circuit Simulator Working on FPGA With SATA Storages"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14285"
summary: "arXiv:2608.14285v1 Announce Type: new Abstract: Quantum circuits are fundamental components of quantum computing, and state-vector-based quantum circuit simulation is a widely used technique for track"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14285v1 Announce Type: new Abstract: Quantum circuits are fundamental components of quantum computing, and state-vector-based quantum circuit simulation is a widely used technique for tracking qubit behavior throughout circuit evolution. However, simulating a circuit with n qubits requires 2^{n+4} bytes of memory, making simulations of more than 40 qubits feasible only on supercomputers. To address this limitation, we propose the Qu-Trefoil, a system designed for large-scale quantum circuit simulations on an FPGA-based platform called Trefoil. Trefoil is a multi-FPGA system connected to eight storage subsystems, each equipped with 32 SATA disks. Qu-Trefoil integrates a suite of HLS-based universal quantum gates, including Clifford gates (Hadamard (H), Pauli-Z (Z), Phase (S), Controlled-NOT (CNOT)), the T gate, and unitary matrix computation, along with HDL-designed modules for system-wide integration. Our extensive evaluation demonstrates the system's robustness and flexibility, covering quantum gate performance, chunk size, disk extensibility, and efficiency across different SATA generations. We successfully simulated quantum circuits with over 43 qubits, which required more than 128 TB of memory, in approximately 3.72 to 13.06 hours on a single storage subsystem equipped with one FPGA. This achievement represents a significant milestone in the advancement of quantum computing simulations. Furthermore, thanks to its unique architecture, Qu-Trefoil is more accessible, flexible, and cost-efficient than other existing simulators for large-scale quantum circuit simulations, making it a viable option for researchers with limited access to supercomputers.



## Related
- [[entanglement-geometry-separates-circuit-cutting-classical-ha|Entanglement geometry separates circuit cutting, classical hardness, and trainability]]
- [[matrix-product-state-approach-to-lossy-boson-sampling-and-no|Matrix product state approach to lossy boson sampling and noisy IQP sampling]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14285) | 2026-08-17
