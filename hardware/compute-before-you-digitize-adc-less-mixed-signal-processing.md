---
title: "Compute Before You Digitize: ADC-less Mixed-Signal Processing for Scalable Cryogenic Qubit Readout"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23448"
summary: "arXiv:2611.23448v1 Announce Type: new Abstract: We introduce DIRAC, an ADC-less in-cryostat qubit readout architecture that uses analog computing to redraw the analog-digital boundary. Directly operat"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23448v1 Announce Type: new Abstract: We introduce DIRAC, an ADC-less in-cryostat qubit readout architecture that uses analog computing to redraw the analog-digital boundary. Directly operating on the front-end's analog output, passive complex mixers perform the equivalent of digital demodulation, ping-pong active-RC integrators average their outputs into down-sampled per-qubit traces, and a time-domain stage digitizes them, eliminating Nyquist-rate ADCs. A TX-RX co-design derives the mixers' local oscillators from the readout transmitter's baseband rather than per-tone PLLs. A per-line calibration flow trains the matched filter jointly with the neural network, improving fidelity and enabling low-bit-width, low-voltage digital processing. Designed in 22 nm FD-SOI and evaluated at 4 K on 1.12M experimental shots, DIRAC matches the fidelity of a floating-point (FP32) digital pipeline for readout windows down to 750 ns, at 31.6imes and 238imes lower energy than the fixed-point (FxP) and FP32 pipelines. It cuts the total 4 K power per physical qubit by 50.4% and 68.6% relative to FxP and room-temperature flex cables, respectively. At a fixed logical-qubit count and 4 K budget, this yields, against FxP, a code distance larger by 2 to 6 and a 1.6-7.3imes (Willow) and 4.9-204imes (SI1000, p = 10^{-3}) lower logical error rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23448) | 2026-11-19
