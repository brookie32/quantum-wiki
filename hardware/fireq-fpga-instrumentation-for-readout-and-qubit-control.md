---
title: "FIREQ: FPGA Instrumentation for Readout and Qubit control"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.29399"
summary: "arXiv:2608.29399v1 Announce Type: new Abstract: We present FIREQ (FPGA Instrumentation for Readout and Qubit control), an open-source RFSoC-based framework for the control and readout of superconducti"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.29399v1 Announce Type: new Abstract: We present FIREQ (FPGA Instrumentation for Readout and Qubit control), an open-source RFSoC-based framework for the control and readout of superconducting qubits. FIREQ combines a modular AXI-compliant firmware architecture with a PYNQ-based software stack designed to support extensible hardware integration, deterministic experiment timing, and low-overhead execution of repeated calibration and characterization workflows. The firmware implements direct RF synthesis and acquisition, trigger-based sequencing, programmable pulse generation, frequency-multiplexed readout, and memory-efficient acquisition and waveform buffering. The software adopts a client-server architecture with streamed data transfer and dependency-aware configuration updates to reduce host-device and reconfiguration overhead during parameter sweeps. On an AMD Zynq UltraScale+ RFSoC ZCU216, FIREQ generates RF pulses up to 9.3 GHz with a pulse-duration resolution of 107 ps and an event-timing resolution of 1.7 ns. FPGA resource utilization is compared with representative open-source RFSoC control frameworks, showing a low BRAM footprint while retaining full-rate I/Q generation and acquisition. The RF output is characterized in terms of phase noise, noise spectral density, and inter-channel timing skew. End-to-end operation is validated on a superconducting qubit through resonator spectroscopy, Rabi, Ramsey, and relaxation measurements, yielding T1 = 6.94 us and T2* = 13.50 us. FIREQ can therefore be used both as a qubit-control platform and as an experimental environment for evaluating alternative control and readout IP architectures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.29399) | 2026-09-01
