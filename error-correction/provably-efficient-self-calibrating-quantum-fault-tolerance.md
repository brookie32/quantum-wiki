---
title: "Provably Efficient Self-Calibrating Quantum Fault Tolerance"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05686"
summary: "arXiv:2608.05686v1 Announce Type: new Abstract: Quantum error correction protects logical information only when every physical operation remains below the fault-tolerance threshold, a condition that m"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05686v1 Announce Type: new Abstract: Quantum error correction protects logical information only when every physical operation remains below the fault-tolerance threshold, a condition that must be maintained continuously rather than only at the initial calibration. In practice, however, analog control parameters inevitably drift because of environmental fluctuations. As future fault-tolerant quantum computations are expected to run for days or even months, interrupting computation for repeated recalibration becomes fundamentally impractical. A promising alternative is to integrate calibration directly into computation by repurposing syndrome measurements as a calibration signal (Sivak et al, Nature 2026), but whether such self-calibration can be achieved with provable efficiency remains an open question. Here we establish a theoretical framework for self-calibrating quantum fault tolerance. We prove that, for a broad class of control-induced errors, the detection rate defines a locally strongly convex surrogate objective for analog calibration with high probability. This geometric property enables efficient online optimization using only syndrome measurements collected during normal error correction. We prove convergence to an arepsilon detection rate within O(1/arepsilon^2) epochs for time-independent drifts and also establish guarantees for time-dependent drifts. We further show that the convergence rate is independent of the code distance for quantum low-density parity-check (LDPC) codes. Pulse-level simulations of neutral-atom arrays and large-scale circuit-level Clifford simulations confirm these theoretical predictions. Our results establish self-calibrating fault tolerance as a provably efficient paradigm in which the same syndrome measurements simultaneously protect logical information and stabilize the underlying hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05686) | 2026-08-07
