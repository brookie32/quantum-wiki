---
title: "MERA: A Mid-Circuit-Measurement Error-Aware Compilation Framework for Quantum Circuits"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.10921"
summary: "arXiv:2511.10921v2 Announce Type: replace Abstract: Mid-circuit measurement (MCM) enables qubit reuse and dynamic control in quantum processors, underpinning resource-efficient algorithms and quantum "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2511.10921v2 Announce Type: replace Abstract: Mid-circuit measurement (MCM) enables qubit reuse and dynamic control in quantum processors, underpinning resource-efficient algorithms and quantum error correction. However, MCM introduces non-negligible errors, including measurement-induced crosstalk, idling-qubit decoherence, and reset infidelity. Additionally, MCM error rates vary across qubits within the same processor, with some exhibiting substantially higher errors. Existing compilers, including Qiskit-compiler and QR-Map, ignore MCM error variations, leading to fidelity loss in circuits with frequent MCM operations. In this paper, we present MERA, an MCM-error-aware quantum compilation framework that integrates MCM error modeling into the layout, routing, and scheduling stages. We first use the lightweight profiling method to capture a per-qubit MCM error distribution that remains stable for over 24 hours. The distribution guides MERA in applying MCM-error-aware layout and routing, while MERA further incorporates context-aware dynamic decoupling to improve fidelity. In evaluation, MERA delivers 24.94% -- 80.48% average fidelity gains over the Qiskit-compiler (optimization level 3) across different groups in selected benchmarks without additional SWAP overhead. It also boosts the fidelity of QR-Map-generated circuits by 29.26% on average (up to 122.58%), demonstrating its effectiveness for circuits with frequent MCM operations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.10921) | 2026-10-26
