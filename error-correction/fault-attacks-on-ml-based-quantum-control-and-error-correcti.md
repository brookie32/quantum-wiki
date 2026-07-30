---
title: "Fault Attacks on ML-based Quantum Control and Error Correction"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.20077"
summary: "arXiv:2512.20077v2 Announce Type: replace Abstract: Machine-learning (ML) models are increasingly used in quantum computing systems to discriminate multi-qubit readouts, mitigate correlated readout er"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2512.20077v2 Announce Type: replace Abstract: Machine-learning (ML) models are increasingly used in quantum computing systems to discriminate multi-qubit readouts, mitigate correlated readout errors, and decode quantum error-correcting codes, making them an integral component of today's quantum computer control and readout stacks. This paper is the first to analyze the susceptibility of such ML models to physical fault injection, which can cause quantum computers to return incorrect results or perform wrong error correction operation. This work studies two representative architectures: (i) a fully connected neural network for 5-qubit (32-class) readout error correction (HERQULES), and (ii) a convolutional neural network used as a Deep Q-learning (Deep Q) decoder for the distance-5 Surface Code. Using the ChipWhisperer Husky for voltage glitching together with automated search over the fault parameter space, this work localizes successful fault settings to specific layers of each target ML model. On the HERQULES model, fault susceptibility is strongly layer-dependent: early layers exhibit higher misprediction rates than later layers. On the Deep Q decoder, a single trigger-aligned voltage glitch in either the first convolutional layer or the final fully connected output layer reduces decoding accuracy from 100% to as low as 21.57%. We further characterize the resulting failures at the bitstring level using Hamming-distance and per-bit flip statistics, showing that single-shot glitches can induce structured corruption rather than purely random noise. These results motivate treating ML-based quantum readout and error-correction decoding as security-critical components, and highlight the need for lightweight fault-detection and redundancy mechanisms in quantum computing pipelines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.20077) | 2026-07-30
