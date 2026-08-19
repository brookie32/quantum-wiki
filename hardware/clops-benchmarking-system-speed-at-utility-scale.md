---
title: "CLOPS: Benchmarking System Speed at Utility Scale"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18044"
summary: "arXiv:2608.18044v1 Announce Type: new Abstract: As quantum processors scale to hundreds of qubits, execution speed is a critical performance dimension alongside scale and quality. While substantial pr"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.18044v1 Announce Type: new Abstract: As quantum processors scale to hundreds of qubits, execution speed is a critical performance dimension alongside scale and quality. While substantial progress has been made in benchmarking circuit fidelity, existing speed metrics often fail to reflect the sustained, end-to-end throughput experienced by users running utility-scale workloads. This shortfall is especially pronounced for layered, parameterized circuits executed repeatedly within classical-quantum workflows, such as variational algorithms and error-mitigated simulations. In this work, we formalize CLOPS_h (Circuit Layer Operations Per Second) as a holistic speed benchmark defined over layered, hardware-aware circuits. CLOPS_h measures the sustained rate at which the system executes physical layers, parallel slices of qubit-disjoint two-qubit gates separated by synchronization barriers. Because each such layer is one time slice of an N-qubit circuit, this rate maps directly to the execution rate of layered N-qubit circuits, connecting CLOPS_h to published device capability claims, and to the device-level throughput ceiling we formalize as Max Circuits Per Second (MCPS). CLOPS_h is obtained under layer-fidelity operating conditions, binding the speed measurement to an independently verified quality envelope, and it shares its layer decomposition with scalable layer-fidelity (LF) quality benchmarks, enabling coherent interpretation of speed and quality without conflating the two.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18044) | 2026-08-19
