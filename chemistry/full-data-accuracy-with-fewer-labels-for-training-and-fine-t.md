---
title: "Full-data accuracy with fewer labels for training and fine-tuning machine-learning force fields"
date: "2026-10-27"
updated: "2026-10-27"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.14486"
summary: "arXiv:2607.14486v2 Announce Type: replace Abstract: Machine-learning force fields (MLFFs) are reliable only near their training distribution, making efficient construction of diverse training sets a m"
last_verified: "2026-10-27"
review_by: "2027-01-25"
stale: false
---

arXiv:2607.14486v2 Announce Type: replace Abstract: Machine-learning force fields (MLFFs) are reliable only near their training distribution, making efficient construction of diverse training sets a major bottleneck for both train-from-scratch and foundation fine-tuning workflows. Active learning can reduce this cost, but standard model-committee uncertainty is impractical for foundation MLFFs because each committee member requires a separate fine-tuning run. We present an active-learning workflow based on last-layer-projection regression (LLPR), a forward-pass-cheap per-configuration uncertainty estimator. Across molecular, condensed-phase, and electrolyte systems, LLPR identifies compact, high-value training sets that recover full-data accuracy using only a small fraction of electronic-structure labels. In foundation-model fine-tuning, LLPR-selected configurations approach the practical fine-tuning ceiling with substantially fewer labels than random selection. In iterative electrolyte fine-tuning, LLPR detects unphysical local coordination before new labelling, calibrates uncertainty in force-error units, and supports retrospective convergence monitoring. The resulting models reproduce reference density and Li--O coordination structure, providing a scalable uncertainty-quantification strategy across MLFF training regimes.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.14486) | 2026-10-27
