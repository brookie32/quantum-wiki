---
title: "Physical Design Automation for Planar Superconducting Quantum Chips"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.08580"
summary: "arXiv:2610.08580v1 Announce Type: new Abstract: Superconducting circuits have emerged as one of the most promising and scalable platforms for quantum com- puting, with substantial industrial adoption "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.08580v1 Announce Type: new Abstract: Superconducting circuits have emerged as one of the most promising and scalable platforms for quantum com- puting, with substantial industrial adoption driving qubit counts steadily upward. Yet the layout of the corresponding chips is still primarily performed manually, consuming multiple days or weeks of expert effort, even for moderately sized designs. Existing automation approaches sidestep this bottleneck by simplifying the underlying problem and relaxing physical constraints. Therefore, they fall short of fabrication-ready results. To overcome this scalability wall without such compromises, we first introduce a formal abstraction that translates physical device characteristics into a rigorous geometric problem formulation. This abstraction bridges physical realization and design automation. Building upon this abstraction, we then propose a three-stage design automation flow comprising geometry-aware global partitioning, ILP-based port assignment, and a hierarchical routing pipeline. Evaluations conducted by our interdisciplinary team of design au- tomation researchers and superconducting hardware experts con- firm that the resulting flow produces complete, manufacturing- ready layouts that comply with the physical design rules at the push of a button. That is, it operates fully automatically within seconds to a few minutes, and solves complex instances up to 25x faster than the state of the art. All methods are released as the fully open-source tool mqt-scpd as part of the Munich Quantum Toolkit, providing the first readily usable, end- to-end design flow for planar superconducting quantum chips that explicitly addresses the underlying physical characteristics and requirements.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.08580) | 2026-10-07
