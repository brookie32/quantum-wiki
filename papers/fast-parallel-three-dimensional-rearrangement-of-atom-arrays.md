---
title: "Fast, parallel, three-dimensional rearrangement of atom arrays using superpositions of elementary holograms"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21609"
summary: "arXiv:2610.21609v1 Announce Type: cross Abstract: Assembling defect-free arrays of neutral atoms requires real-time rearrangement of stochastically loaded optical tweezers. Conventional rearrangement "
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21609v1 Announce Type: cross Abstract: Assembling defect-free arrays of neutral atoms requires real-time rearrangement of stochastically loaded optical tweezers. Conventional rearrangement methods shuttle atoms sequentially, whereas high-speed spatial light modulators (SLMs) can move all atoms in parallel, which scales more favorably as the array size grows. For fast parallel rearrangement, the sequence of holograms displayed on the SLM should be computed more rapidly than the SLM refresh rate, and there should be phase continuity between successive holograms to minimize transient intensity fluctuations. We calculate holograms analytically by adding together the complex fields needed to produce each individual trap, and we ramp the phase of each trap linearly as it moves to its target location. Trap positions enter as continuous variables, rather than tied to points on a grid, so the method provides high positioning accuracy. Using a single GPU, we compute each intermediate hologram in 0.284 ms, considerably faster than the SLM refresh time of 0.696 ms, so the rearrangement speed is hardware-limited. In each step, we use the free processing time to iteratively optimize the holograms for equal intensity across the traps, decreasing trap non-uniformity to 1.24% during rearrangement at no cost in total time. Starting from an array of 256 sites loaded stochastically with ^{87}Rb atoms, we assemble a 100-atom array in under 20 ms with a rearrangement survival probability of 99.31(12)% per atom. This rearrangement increases the temperature of the atoms by 9(3) muK, which is small compared to the trap depth of 480 muK. Our method can also move individual atoms axially, enabling transport in different planes. We demonstrate this capability with a rearrangement protocol where one set of atoms leapfrogs over another.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21609) | 2026-10-16
