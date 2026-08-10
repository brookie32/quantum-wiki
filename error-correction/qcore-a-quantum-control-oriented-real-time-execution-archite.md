---
title: "QCORE: A Quantum-Control-Oriented Real-Time Execution Architecture with Extensible Closed-Loop Services and Shared AI Acceleration"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06875"
summary: "arXiv:2608.06875v1 Announce Type: new Abstract: Scalable quantum processors require control, readout, feedback, calibration, and error correction to coexist under bounded latency and shared-resource c"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06875v1 Announce Type: new Abstract: Scalable quantum processors require control, readout, feedback, calibration, and error correction to coexist under bounded latency and shared-resource constraints, whereas existing platforms typically optimize only a subset of these capabilities. This article presents QCORE (Quantum-Control-Oriented Real-Time Execution), a QPU-side digital control reference architecture positioned between the Host and a platform-specific analog/mixed-signal front end. QCORE separates task management, shared resources, hard-real-time execution, and long-timescale services into four hardware partitions. A fast-result sideband closes same-round feedback, a Measurement Packet provides a traceable measurement and service interface, and a common service-control skeleton, Tile-local QEC, and versioned safe-point commit organize calibration, error correction, and long-term state updates. Transaction-level, event-driven, and quantum-behavioral models are used for evaluation. At a background load of 0.8, the P_{99} latency of the shared Measurement Packet/Event feedback path is (1.984pm0.004)L_{max}. Closed-loop operation reduces the mean frequency error by 83.2%pm0.8% and lowers the state-assignment error at maximum readout drift from 10.39%pm0.54% to 5.37%pm0.29%. No unsafe acceptance or mixed-version observation is observed in 100,000 configuration transactions, and Tile-local QEC reduces modeled global-boundary demand and yields a 2.08imes capacity-normalized scaling estimate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06875) | 2026-08-10
