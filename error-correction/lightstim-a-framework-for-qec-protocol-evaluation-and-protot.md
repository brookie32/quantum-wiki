---
title: "LightStim: A Framework for QEC Protocol Evaluation and Prototyping with Automated DEM Construction"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.21472"
summary: "arXiv:2604.21472v3 Announce Type: replace Abstract: Fault-tolerant quantum computing increasingly demands rigorous, circuit-level evaluation of diverse quantum error correction (QEC) protocols and eff"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2604.21472v3 Announce Type: replace Abstract: Fault-tolerant quantum computing increasingly demands rigorous, circuit-level evaluation of diverse quantum error correction (QEC) protocols and efficient prototyping of new ones. Such evaluation requires both the physical circuit and its Detector Error Model (DEM) to estimate end-to-end logical error rates. However, DEM construction today is performed by manual annotation, a tedious and error-prone process that effectively limits evaluation to simple memory experiments. We present LightStim, a framework that automates DEM construction concurrently with circuit compilation by maintaining a Pauli tableau augmented with measurement records, with no protocol-specific input required. We benchmark LightStim across protocols from memory experiments to end-to-end distillation circuits; cross-validation against public implementations confirms exact detector and observable counts and consistent logical error rates. Additionally, we demonstrate a novel heterogeneous cross-code lattice surgery design between surface and punctured quantum Reed-Muller codes. These capabilities together make LightStim a unified infrastructure for systematic QEC protocol evaluation and exploration. LightStim is open-sourced at https://github.com/QuTone/LightStim.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.21472) | 2026-08-28
