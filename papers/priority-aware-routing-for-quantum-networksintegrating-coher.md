---
title: "Priority-Aware Routing for Quantum Networks:Integrating Coherence-Time Constraints into Scheduling"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38380"
summary: "arXiv:2609.38380v1 Announce Type: cross Abstract: Quantum networks face a fundamental challenge absent in classical networks; finite memory coherence times mean that queuing delay directly degrades in"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38380v1 Announce Type: cross Abstract: Quantum networks face a fundamental challenge absent in classical networks; finite memory coherence times mean that queuing delay directly degrades information quality, causing decoherence that has no classical analog. Existing routing protocols optimize for hop count or channel fidelity while treating scheduling delays as a secondary concern, leaving fidelity vulnerable to congestion-induced decoherence. We present a coherence-aware routing protocol that integrates decoherence constraints into path selection via a priority-modulated aging model derived analytically from Weighted Fair Queueing theory, where high-priority traffic receives compressed effective queue delay. We build a custom discrete-event simulator verified against NetSquid (across 104 states), and evaluate across two structurally diverse topology classes under identical physical parameters, isolating topology structure as the sole independent variable. In all experiments, our protocol is benchmarked against loss-only Dijkstra routing and FIFO scheduling as baselines. On topologies, P2 traffic achieves 96.08% fidelity under a 9x load increase with only 0.04 percentage point degradation, versus a 13.51 percentage point collapse for the loss-only baseline; P2 tail latency holds stable at 0.055 ms while Dijkstra degrades 5.5x. On Barabasi-Albert scale-free topologies, our protocol delivers a +4.12 percentage point fidelity advantage with 97.8% higher aggregate throughput at operational loads over the baseline, with a clearly characterized hub-saturation boundary at 160k QPS. FIFO scheduling provides negligible priority differentiation on both topology classes, providing strong evidence that coherence-aware routing-not scheduling alone is responsible for the observed QoS gains.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38380) | 2026-10-01
