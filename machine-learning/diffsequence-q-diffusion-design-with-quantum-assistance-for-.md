---
title: "DiffSequence-Q: Diffusion Design with Quantum Assistance for Biologically Active Proteins"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08434"
summary: "arXiv:2611.08434v1 Announce Type: new Abstract: Designing protein sequences that satisfy both secondary structure requirements and solubility targets remains challenging. We present DiffSequence-Q, a "
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.08434v1 Announce Type: new Abstract: Designing protein sequences that satisfy both secondary structure requirements and solubility targets remains challenging. We present DiffSequence-Q, a hybrid multinomial diffusion model conditioned on secondary structure at each residue and a continuous solubility target. To introduce quantum auxiliary supervision during training, we employ a quantum neural network (QNN) or quantum Kolmogorov-Arnold network (QKAN) as an auxiliary solubility prediction head over shared Transformer representations. The auxiliary prediction loss is jointly optimized with the diffusion objective, allowing quantum auxiliary supervision to influence the learned denoising model. Once trained, protein sequences are generated entirely through classical reverse diffusion. On the CATH benchmark, DiffSequence-Q achieved the highest secondary structure recovery among the four evaluated models for complete sequence generation. Evaluation with a separately trained solubility prediction model showed that the best QNN and QKAN configurations achieved mean predicted solubility scores 14.0% and 22.7% higher than the multilayer perceptron (MLP) baseline, respectively. Experimental characterization further demonstrated biological activity across three distinct protein families. Selected defensins exhibited pronounced inhibitory activity against Aspergillus niger, while xylanases and short-chain dehydrogenases exhibited substantial enzymatic activity. Together, these results support DiffSequence-Q as a framework for integrating structural requirements and solubility targets in protein generation, with experimentally demonstrated biological activity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08434) | 2026-11-06
