---
title: "Highly Efficient 3-in-1 FPGA-Based Unit Combining an ADC, DAC, and Multichannel Pulse Generator for Pulsed EPR Spectroscopy"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "industry"
tags: [industry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.16151"
summary: "arXiv:2608.16151v1 Announce Type: new Abstract: A hardware and software system for pulsed electron paramagnetic resonance (EPR) spectroscopy is presented, built around a single PCI Express (PCIe) card"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16151v1 Announce Type: new Abstract: A hardware and software system for pulsed electron paramagnetic resonance (EPR) spectroscopy is presented, built around a single PCI Express (PCIe) card that combines a 16-bit digital-to-analog converter (DAC) with a 10 GS/s effective sample rate, a 2.5 GS/s 14-bit analog-to-digital converter (ADC), and an 11-channel pulse generator on board. Custom firmware reloads the pulse-generator and DAC buffers and streams the digitized data in parallel with a running experiment, so that no time is lost on data input or output. The unit is integrated into the open-source Atomize software and controlled at the level of pulse sequences through a high-level Python application programming interface (API). Benchmarking with a four-pulse double electron-electron resonance (DEER) sequence shows that the card reaches close to 100% time efficiency for accumulation times of a few milliseconds per pulse sequence, even for demanding arbitrary waveform generator (AWG) protocols. Although demonstrated for a single sequence, the efficiency proved insensitive to the number of pulses, the number of measurement points, or the phase-cycling depth, so that comparable performance is expected for any protocol whose shot repetition time exceeds the ~2 ms reprogramming time of the card. The on-the-fly reprogramming, which makes every successive sequence fully independent, also enables nonuniform sampling and acquisition. The system design, its firmware, the Python API, and its performance in pulsed EPR applications are described.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.16151) | 2026-08-18
