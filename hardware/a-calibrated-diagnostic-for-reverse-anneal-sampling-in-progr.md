---
title: "A calibrated diagnostic for reverse-anneal sampling in programmable quantum annealers"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.19381"
summary: "arXiv:2605.19381v2 Announce Type: replace Abstract: Reverse annealing is widely used as a heuristic sampler on programmable quantum annealers, but it is often unclear whether the readout has erased it"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2605.19381v2 Announce Type: replace Abstract: Reverse annealing is widely used as a heuristic sampler on programmable quantum annealers, but it is often unclear whether the readout has erased its initialization memory or whether the resulting samples represent any calibrated target distribution. We introduce a subsystem-level validation protocol that pairs a memory order parameter M with the total-variation distance D_{TV} between the measured subsystem readout and a fixed, independently calibrated conditional-Boltzmann reference, and apply it on two D-Wave QPU generations. The protocol delivers three things: a diagnostic that separates relaxed, memory-retaining and "wrong-basin" readouts; the isolation of relaxed-but-non-thermal trapping, in which a readout passes the initial-state-independence test while concentrating on the wrong basin; and an engineering control showing that SDK auto-scale, embedding choice and environment preparation shift apparent thresholds, so calibration metadata must be logged to interpret them. Relaxed ferromagnetic readouts are near-deterministic, so the small distances seen there are a consistency check rather than a thermometric measurement; the diagnostic earns its value in the opposite regime. Across 494 conditions on one processor, 113 pass the memory criterion and 110 of those agree with the reference at D_{TV}0.94; a 60-condition replication confirms that the diagnostic transfers to a second processor. We provide the protocol as a transferable, reproducible validation workflow for annealer-as-sampler applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.19381) | 2026-08-11
