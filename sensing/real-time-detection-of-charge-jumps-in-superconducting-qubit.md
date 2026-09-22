---
title: "Real-Time Detection of Charge Jumps in Superconducting Qubits with a Convolutional Neural Network"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.14293"
summary: "arXiv:2607.14293v2 Announce Type: replace Abstract: Ionizing radiation from cosmic rays and gammas can induce discontinuous jumps in the environmental charge of superconducting qubits (charge jumps), "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2607.14293v2 Announce Type: replace Abstract: Ionizing radiation from cosmic rays and gammas can induce discontinuous jumps in the environmental charge of superconducting qubits (charge jumps), causing correlated errors that challenge fault-tolerant quantum computing while simultaneously providing a detection signature for quantum sensing applications. Current detection methods operate offline, introducing latency incompatible with in-the-loop qubit control. In this paper, an online detector of charge jumps for superconducting qubits, based on a dilated causal convolutional neural network (DCCNN) designed for in-the-loop deployment on the Quantum Instrumentation Control Kit (QICK) platform, is presented. The network is trained on synthetic Ramsey tomography scans generated from qubit templates measured at the Northwestern Experimental Underground Site (NEXUS) at Fermilab, and translated to FPGA firmware via hls4ml with ap_fixedlangle 16,6 rangle quantization, reaching a per-inference latency of 32.0 mus on the Zynq UltraScale+ RFSoC ZCU216. At this operating point the DCCNN matches the detection efficiency of the established offline hi^2 algorithm (0.843 pm 0.022 vs. 0.868 pm 0.007 on |Delta q| in [0.1, 0.5] e at matched false-positive rate), while requiring no per-qubit hyperparameter tuning. This shifts charge-jump detection from a post-hoc diagnostic to a control-loop primitive, enabling adaptive protocols that respond to radiation-induced events in situ, with applications to quantum-computing error mitigation and to the use of superconducting qubits as particle detectors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.14293) | 2026-09-22
