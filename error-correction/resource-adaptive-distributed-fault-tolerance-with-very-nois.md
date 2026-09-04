---
title: "Resource-adaptive distributed fault tolerance with very noisy Bell pairs"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03048"
summary: "arXiv:2609.03048v1 Announce Type: new Abstract: Distributed architectures have been proposed as a pathway to large-scale quantum computers. Combined with the need for fault-tolerance, such architectur"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03048v1 Announce Type: new Abstract: Distributed architectures have been proposed as a pathway to large-scale quantum computers. Combined with the need for fault-tolerance, such architectures require distributed quantum error correction (DQEC) and distributed logical gates. An important challenge is how to realize DQEC primitives in the setting where interaction between modules is restricted to shared Bell pairs that are significantly noisier than on-chip operations. We extend the framework known as fault tolerance by construction to this setting, deriving different strategies for handling the additional noise. Through fault-improvement we recover conventional entanglement distillation, and also find more dynamical protocols that enable space-time trade-offs. We show that integrated decoding halves the required distillation code distance compared to entanglement distillation implemented using separate decoding, thus requiring significantly fewer Bell pairs. As a main focus of the work, we synthesize efficient circuits for an important primitive in distributed fault tolerance: distributed stabilizer measurements. These circuits can be adapted to resource constraints, e.g. on the Bell pair generation rate or the space available for on-chip auxiliary qubits. Noting that full local fault-tolerance is not always needed to preserve the correct scaling of logical error rates, we further optimize the circuits depending on the surrounding context. We consider in particular the surface code and the color code, both as distributed memories and in the case of lattice surgery across separate modules. Here, robustness to certain hook and readout errors reduces the number of required Bell pairs even further, compared to the context-free setting. We numerically benchmark the resulting implementations under circuit level noise with additional interconnect noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03048) | 2026-09-04
