---
title: "SMP: A General Hyperedge-Based Framework for Circuit-Level Quantum Error Correction"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02734"
summary: "arXiv:2610.02734v1 Announce Type: new Abstract: Hyperedge faults remain a major challenge in circuit-level quantum error correction. Accurately exploiting hyperedge correlations often requires substan"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02734v1 Announce Type: new Abstract: Hyperedge faults remain a major challenge in circuit-level quantum error correction. Accurately exploiting hyperedge correlations often requires substantial computational resources, which complicates real-time decoding. Matching-based decoders are fast and scalable, but their pairwise graph representation limits the use of higher-order fault information. Here, we introduce Syndrome Motif Projection (SMP), a general framework for incorporating hyperedge information into matching-based decoding. The key idea is that a hyperedge fault produces a characteristic local syndrome motif. Observing such a motif provides evidence for the corresponding fault. SMP extracts this information directly from the measured syndrome with linear-complexity preprocessing while preserving the matching backend. It can therefore serve as a lightweight front end to existing scalable and real-time matching decoders. We demonstrate SMP across surface code memories, color code memories, and logical gate circuits. On Google's Willow experimental surface code data, SMP improves both standard and correlated matching and outperforms the tested belief matching baseline. For color code memories, SMP combined with Chromobius reduces logical failure probabilities by up to 77.8%. For logical gate circuits, SMP reduces the failure probability of a six-CNOT circuit by 35.5% relative to logical observable matching while achieving performance comparable to iterative belief matching. These results demonstrate that SMP provides a lightweight and transferable approach to hyperedge decoding, with a clear path toward integration into scalable real-time decoding architectures for fault-tolerant quantum computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02734) | 2026-10-05
