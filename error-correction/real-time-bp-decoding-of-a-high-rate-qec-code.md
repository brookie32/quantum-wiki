---
title: "Real-time BP decoding of a high-rate QEC code"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41413"
summary: "arXiv:2610.41413v1 Announce Type: new Abstract: We present a real-time FPGA decoder for a high-rate [[512,174,8]] 3D product qLDPC code. We construct a circuit-level detector-error model for a compact"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41413v1 Announce Type: new Abstract: We present a real-time FPGA decoder for a high-rate [[512,174,8]] 3D product qLDPC code. We construct a circuit-level detector-error model for a compact syndrome-extraction schedule and propose a small parallel ensemble of row-wise serial min-sum decoders with cumulative memory. The decoder matches ext{BP+OSD-CS}_ext{10} accuracy with one core and Relay-BP accuracy with three cores. The FPGA implementation meets the latency budget of neutral-atom and trapped-ion systems. An ASIC implementation would improve the latency, enabling real time decoding even for superconducting systems. At a physical error rate of p=10^{-3}, three FPGA devices decode 174 logical qubits with a logical error rate of 5imes10^{-7} and effective distance 6. For p=10^{-4}, and assuming the number of BP iterations is capped to 30, the decoder's average latency is 5.1,extmu s and its worst-case latency is 97.9,extmu s.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41413) | 2026-11-02
