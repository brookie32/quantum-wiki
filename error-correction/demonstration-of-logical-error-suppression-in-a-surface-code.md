---
title: "Demonstration of Logical Error Suppression in a Surface Code Memory on a Cloud-Accessible IBM Superconducting Processor"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23840"
summary: "arXiv:2610.23840v1 Announce Type: new Abstract: Quantum error correction can suppress logical errors exponentially with code distance when physical noise is below threshold. Realizing this on hardware"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23840v1 Announce Type: new Abstract: Quantum error correction can suppress logical errors exponentially with code distance when physical noise is below threshold. Realizing this on hardware requires tight coordination among quantum gates, mid-circuit measurements, and qubit coherence. Device variation, noise asymmetry, and correlations across space and time complicate the translation of these capabilities into logical error suppression. Here, we study rotated surface-code memory on an IBM Nighthawk r2 processor. Performance varies across tested processor placements, which we attribute to differences in qubit quality. We optimize the code by combining short readout, fused measurement and reset, and an XX echo on data qubits during ancilla readout. Compared with standard readout without reset or echo, the optimized syndrome extraction circuit reduces the median per-round logical error rate by factors of 3.8 in the X basis and 1.4 in the Z basis. In memory experiments of up to 150 rounds, the distance advantage weakens, alongside long-lived correlations that may reflect a persistent error component. Under our optimization recipe, increasing the protected distance from 3 to 6 while holding the other distance fixed reduces the per-round logical error rate from 0.53% to 0.24% in Z memory and from 0.52% to 0.22% in X memory. The corresponding error-suppression factors under maximum-likelihood decoding are 1.68 and 1.85. These results connect circuit compilation and optimization to surface-code memory performance and limitations, and motivate QPU and QEC circuit codesign for fault-tolerant quantum computing primitives on current cloud hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23840) | 2026-10-19
