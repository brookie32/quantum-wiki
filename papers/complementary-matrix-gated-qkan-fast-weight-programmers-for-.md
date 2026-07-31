---
title: "Complementary Matrix-Gated QKAN Fast-Weight Programmers for Quantum Dynamics Forecasting"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.27945"
summary: "arXiv:2607.27945v1 Announce Type: new Abstract: Sequence models must decide what to write into memory and what to retain. In quantum and quantum-inspired sequence learning, nonlinear recurrent updates"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.27945v1 Announce Type: new Abstract: Sequence models must decide what to write into memory and what to retain. In quantum and quantum-inspired sequence learning, nonlinear recurrent updates often require repeated circuit evaluations and sequential backpropagation through time, making long contexts costly. Gated fast-weight programmers (FWPs) based on quantum-inspired Kolmogorov-Arnold networks (QKANs) alleviate this bottleneck by storing context in time-varying fast parameters. However, their scalar gate applies one retention-write balance to every fast-state coordinate, forcing all parameters to share a memory timescale. We introduce Self-Modulating QKAN-based FWPs, which replace this broadcast gate with low-rank-generated element-wise modulation of the new-proposal branch, a bounded old-state branch, or both. We further propose Complementary Matrix Gating (CMG), which uses one sigmoid matrix gate to retain the old state and its complement to write the new proposal. CMG provides coordinate-wise memory control while preserving the bounded convex update and affine prefix-scan structure of scalar gating, at the modulation-head cost of a single-branch rule. We compare four self-modulating rules with scalar gating across four FWP architectures combining classical and QKAN-based slow and fast programmers. Across seven single-step forecasting benchmarks and five sequence lengths, CMG gives the most consistent improvements for architectures whose fast programmer incorporates a QKAN-based module. In direct multi-step forecasting of Jaynes-Cummings and transmon-resonator dynamics simulated with CUDA-Q Dynamics, CMG models maintain mean-squared errors on the order of 0.001 or lower across forecasting horizons of 4, 8, and 16 steps, while improving on their scalar-gated counterparts by at least 91.2%. These results establish coordinate-wise complementary modulation as a stable and effective update for QKAN-based FWPs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.27945) | 2026-07-31
