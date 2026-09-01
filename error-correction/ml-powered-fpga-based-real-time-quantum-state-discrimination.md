---
title: "ML-Powered FPGA-based Real-Time Quantum State Discrimination Enabling Mid-circuit Measurements"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2406.18807"
summary: "arXiv:2406.18807v4 Announce Type: replace Abstract: Accurate and timely quantum state discrimination is critical for quantum computing, particularly in protocols requiring mid-circuit measurement (MCM"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2406.18807v4 Announce Type: replace Abstract: Accurate and timely quantum state discrimination is critical for quantum computing, particularly in protocols requiring mid-circuit measurement (MCM) and conditional feed-forward. While classical state readout in transistors is near-instantaneous, identifying the state of superconducting qubits remains latency-limited and error-prone. Existing approaches rely on post-processing measurement data transferred to host computers, introducing delays on the order of milliseconds -- vastly exceeding the coherence time of quantum states, which typically last only hundreds of microseconds. To bridge this latency gap, we present an in-situ machine learning (ML) inference engine implemented on a field-programmable gate array (FPGA), enabling real-time quantum state discrimination within 40 ns. Our system supports both two-level (qubit) and three-level (qutrit) systems and performs inference directly on digitized readout signals without host-side intervention. This low-latency operation facilitates mid-circuit measurements, where qubit states are measured and reused within a single quantum circuit, and enables real-time conditional operations essential for quantum error correction. Crucially, fast and accurate mid-circuit readout is a prerequisite for implementing practical fault-tolerant error correction, where errors must be detected and corrected within a single circuit cycle to preserve logical state coherence. We validate our system using superconducting transmon devices, demonstrating robust discrimination fidelity across multiple qubit and qutrit channels. Further, we implement a conditional qutrit logic protocol based on FPGA-resident state classification, highlighting the practical benefits of our approach for NISQ-era quantum algorithms and scalable fault-tolerant architectures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2406.18807) | 2026-09-01
