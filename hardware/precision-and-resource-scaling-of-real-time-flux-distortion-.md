---
title: "Precision and resource scaling of real-time flux distortion compensation for superconducting quantum control"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.27456"
summary: "arXiv:2609.27456v1 Announce Type: new Abstract: Real-time waveform generation supports dynamic quantum circuits without pre-storing complete waveforms for every execution path. However, long-lived dis"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.27456v1 Announce Type: new Abstract: Real-time waveform generation supports dynamic quantum circuits without pre-storing complete waveforms for every execution path. However, long-lived distortions in flux-control lines degrade gate fidelity, requiring compensation to account for the actual pulse history. A frequency-domain inversion and time-domain fitting method is proposed for resource-efficient real-time flux distortion compensation. The method fits the reconstructed compensation impulse response with a compact hybrid infinite impulse response (IIR) and finite impulse response (FIR) filter. Look-ahead parallelization enables this filter to process synthesized waveforms at 1.2GSa/s on a field-programmable gate array (FPGA). Two-qubit cross-entropy benchmarking shows that real-time IIR filtering achieves a median controlled-Z Pauli fidelity close to the software-reference value of 99.57%. Numerical analysis and FPGA synthesis indicate approximately logarithmic growth in hardware resource use with compensation timescale. Extending compensation from microsecond to hundred-microsecond timescales increases look-up table (LUT) and digital signal processing (DSP) resource use by only about 14% and 4%, respectively, while maintaining a relative arithmetic error below 10^{-4}. This work provides a scalable hardware foundation for high-fidelity flux control in dynamic superconducting quantum circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.27456) | 2026-09-24
