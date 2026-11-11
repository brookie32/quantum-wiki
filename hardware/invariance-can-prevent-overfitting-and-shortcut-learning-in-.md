---
title: "Invariance can prevent overfitting and shortcut learning in Quantum Neural Networks"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14368"
summary: "arXiv:2611.14368v1 Announce Type: new Abstract: Many image classification tasks have labels that are unchanged by rotations and reflections. Equivariant quantum neural networks incorporate such symmet"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14368v1 Announce Type: new Abstract: Many image classification tasks have labels that are unchanged by rotations and reflections. Equivariant quantum neural networks incorporate such symmetries by design, but the specific benefit of symmetry is difficult to isolate. Equivariant quantum circuits are usually compared with architectures that also differ in gates, structure or size. Here, we investigate the role of invariance in a controlled setting, classifying images whose labels are invariant under the dihedral group D_4. We compare four eight-qubit models with identical encoding, circuit structure and number of trainable parameters, and equivalent dynamical Lie algebras, and benchmark invariant implementations against non-invariant ones in terms of generalization error, robustness to shortcut learning and resilience to a realistic noise model. On four binary tasks, including MNIST and two scientific data sets of galaxies and red blood cells, the invariant models trained on a few tens of images show better generalization than non-invariant ones. Invariance also makes the models immune to orientation shortcuts: when trained with a class-dependent corner watermark, the non-invariant models learn the watermark and often drop to chance level when it is moved. We show that the gain in accuracy of invariant models persists also under a realistic noise model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14368) | 2026-11-11
