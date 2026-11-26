---
title: "Amatlas: A 2D Array Architecture for Union-Find Decoding Without Global Coordination"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33665"
summary: "arXiv:2611.33665v1 Announce Type: new Abstract: Real-time decoding of the surface code is essential for fault-tolerant quantum computing, and scaling the decoder to large code distances in hardware re"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33665v1 Announce Type: new Abstract: Real-time decoding of the surface code is essential for fault-tolerant quantum computing, and scaling the decoder to large code distances in hardware remains a challenge. The locality of Union-Find (UF) decoding makes it a leading candidate for such a decoder in distributed hardware. Prior distributed UF decoders, however, map the three-dimensional decoding graph onto an array of processing elements (PEs) under a central controller that synchronizes all PEs at every stage, and a three-dimensional array of PEs scales poorly on planar hardware. This paper presents Amatlas, a two-dimensional PE array for UF decoding that operates without a central controller. Amatlas assigns one PE to each stabilizer on the two-dimensional qubit lattice and stores the states of all measurement rounds in the local memory of the PE, so every link connects adjacent PEs in the array. Every PE advances on every clock cycle without array-wide synchronization, and the clock is the only global signal of the array. Under circuit-level noise, the RTL implementation of Amatlas fits a VCU129 FPGA up to a code distance of 25, where the average decoding time is 462 ns per round at a physical error rate of 0.1%. Amatlas achieves a threshold of 0.72%, compared with 0.78% reported for UF decoding under the same noise model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33665) | 2026-11-26
