---
title: "Adaptive Sensing beyond Non-Adaptive Information Limits: End-to-End Co-Design of Geometry, Policy, and Inference"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25193"
summary: "arXiv:2604.25193v1 Announce Type: cross Abstract: Inverse design has made vast physical parameter spaces a substrate for emergent behavior. In sensing, the stakes of this principle are sharpest at the"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25193v1 Announce Type: cross Abstract: Inverse design has made vast physical parameter spaces a substrate for emergent behavior. In sensing, the stakes of this principle are sharpest at the analog-to-digital boundary, where any information the hardware fails to capture is information no downstream algorithm can recover; hardware optimization alone is therefore not enough, and the geometry must be co-designed with a rule for what to measure next. We formulate this co-design as joint dynamic programming (joint-DP): a single optimization over the continuous hardware geometry and a Bellman-optimal adaptive measurement policy. The outer hardware gradient is computed by differentiable dynamic programming with a sharp Bellman maximum, which the envelope theorem makes exact and bias-free, and a relaxation hierarchy carries the common framework from small discrete POMDPs to 10^5-pixel photonic topologies. Across three case studies, joint-DP beats the natural baseline of its community by a large factor: on a radar beam-search POMDP, classical information-bound-guided geometry selection loses 2.8imes in attainable adaptive value; on a superconducting-qubit flux sensor, joint-DP reduces deployed mean-squared error by 11.3imes over the joint Bayesian Cramer--Rao baseline, with both geometries numerically co-optimized under their respective objectives; and on a 90{,}000-pixel photonic metasensor, joint-DP via the Bayesian Fisher-information-matrix surrogate reduces deployed mean-squared error by 123imes relative to a randomized baseline. For any sensor whose hardware is designed once but whose policy runs for the device's lifetime, joint optimization of hardware and policy is the minimum principled procedure.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25193) | 2026-04-29
