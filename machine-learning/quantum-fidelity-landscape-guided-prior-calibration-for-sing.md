---
title: "Quantum Fidelity Landscape-Guided Prior Calibration for Single-Circuit QGAN Image Generation"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36702"
summary: "arXiv:2609.36702v1 Announce Type: new Abstract: Quantum Generative Adversarial Networks (QGANs) have emerged as representative generative models in the Noisy Intermediate-Scale Quantum (NISQ) era and "
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36702v1 Announce Type: new Abstract: Quantum Generative Adversarial Networks (QGANs) have emerged as representative generative models in the Noisy Intermediate-Scale Quantum (NISQ) era and have attracted increasing attention in quantum machine learning. However, most existing QGAN methods rely on patch-based decomposition strategies, which weaken the global consistency of generated images and increase quantum resource overhead. In this work, we investigate a simpler approach: pixel-level, end-to-end image generation using a single-quantum-circuit QGAN. By analyzing the structural matching relationship between the quantum prior and the target data distribution in Hilbert space, we provide a new theoretical perspective for understanding the training behavior of naive end-to-end QGANs. Specifically, we introduce the Quantum Fidelity Landscape (QFL), defined as the pairwise-fidelity structure induced by an ensemble of quantum states and preserved under shared unitary transformations of the quantum generation process. We show that, under a fixed Lipschitz readout, this invariant imposes a one-sided bound on decoded sample separation, motivating calibration of the prior-induced QFL before adversarial training. To validate this theoretical insight, we propose BasicQGAN, a QGAN framework incorporating quantum prior calibration. Before adversarial optimization, BasicQGAN aligns the prior-induced QFL with the data-induced QFL. Experimental results on small-scale grayscale image datasets show that BasicQGAN achieves stable and effective end-to-end pixel-level image generation while requiring fewer qubits and trainable parameters than representative patch-based quantum generators. Furthermore, experiments with different initial quantum-state ensembles show that QFL-calibrated ensembles achieve better generative performance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36702) | 2026-09-30
