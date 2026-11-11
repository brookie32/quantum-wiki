---
title: "A Compiler for Fault Tolerant Quantum Computing"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13301"
summary: "arXiv:2611.13301v1 Announce Type: new Abstract: Fault-tolerant quantum computing (FTQC) needs compiler intermediate representations (IRs) that preserve error-correcting-code choices, syndrome informat"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13301v1 Announce Type: new Abstract: Fault-tolerant quantum computing (FTQC) needs compiler intermediate representations (IRs) that preserve error-correcting-code choices, syndrome information, and non-Clifford resource requirements through analysis, simulation, and hardware lowering. We report practical experience building FTQC, an open-source Multi-Level Intermediate Representation (MLIR) dialect that makes logical qubits, syndromes, magic states, and Pauli frames typed static single assignment (SSA) values. Its error-correction-aware type system, two-level lowering design, and IR-resident resource analysis provide one inspectable pipeline to Open Quantum Assembly Language~3 (OpenQASM~3), the Quantum Intermediate Representation (QIR), Stim, and IQM hardware. Case studies across three code families show that typed metadata makes code-specific decisions verifiable and retargetable: on the 20-qubit Pathfinder at Oak Ridge National Laboratory, decoding reduced logical readout error by 3.3 times. They also expose hidden architectural costs: for a three-qubit Quantum Fourier Transform (QFT-3), a magic-state factory requires five times the peak qubits of the encoded circuit. These experiences demonstrate a practical foundation for developing and evaluating fault-tolerant compiler transformations across software and hardware targets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13301) | 2026-11-11
