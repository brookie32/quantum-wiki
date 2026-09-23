---
title: "Adaptive thresholding for scalable measurement-based qubit reset"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25208"
summary: "arXiv:2609.25208v1 Announce Type: new Abstract: Fast, high-fidelity qubit initialization is a key primitive for scalable quantum information processing, but conventional reset protocols either require"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25208v1 Announce Type: new Abstract: Fast, high-fidelity qubit initialization is a key primitive for scalable quantum information processing, but conventional reset protocols either require long relaxation times or discard information contained in continuous measurement records. We demonstrate an adaptive measurement-based reset protocol for superconducting qubits that uses Bayesian inference to update the qubit-state estimate after each readout and dynamically adjust the feedback threshold. Unlike fixed-threshold or repeat-until-success (RUS) protocols, the method utilizes the full analog measurement history, enabling the reset decision to become progressively more conservative as confidence in ground-state preparation increases. Implemented with real-time FPGA-based feedback on a dispersively readout transmon qubit, the protocol achieves a ground-state initialization fidelity of 99.44pm0.04% after a small number of reset rounds. We further compare adaptive reset with RUS strategies in multi-qubit experiments and show that adaptive thresholding provides deterministic reset duration while maintaining a five-qubit simultaneous-reset fidelity of 98.78 pm 0.19%. These results establish Bayesian adaptive thresholding as a practical and scalable route to fast qubit reset in superconducting quantum processors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25208) | 2026-09-23
