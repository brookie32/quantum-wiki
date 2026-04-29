---
title: "MCMit: Mid-Circuit Measurement Error Mitigation"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25863"
summary: "arXiv:2604.25863v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) and Quantum Error Correction (QEC) rely on dynamic circuits that include Mid-Circuit Measurements (MCMs) and classic"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25863v1 Announce Type: new Abstract: Distributed Quantum Computing (DQC) and Quantum Error Correction (QEC) rely on dynamic circuits that include Mid-Circuit Measurements (MCMs) and classical feedback. These operations present a major bottleneck: MCMs suffer from high error rates that lead to real-time branching errors, while MCM and classical feedback latencies amplify decoherence errors. Current hardware controllers, qubit-state discriminators, and software error mitigation techniques fail to address these challenges holistically. We propose MCMit, a hardware-software co-design to mitigate branching and latency-induced errors. MCMit introduces a scalable, constant-latency multi-control branch instruction for faster classical feedback and two qubit-state discriminators, a transformer, and a CNN, with high accuracy even under short measurement durations. On the software side, static MCM elimination and stochastic branching complement the hardware by mitigating residual branching errors that persist despite hardware improvements. We implement MCMit on Qubic and evaluate it using experimentally extracted QPU readout traces. Our branch instruction reduces feedback latency by up to 70%, improving circuit depths by up to 7imes over Qubic. Our CNN discriminator achieves 37-73% higher accuracy for short measurement durations than the baselines, leading to up to 80% lower logical error rates in QEC. Last, our software mitigation improves fidelity by 18--30% over baseline methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25863) | 2026-04-29
