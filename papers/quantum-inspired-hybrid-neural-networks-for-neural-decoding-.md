---
title: "Quantum-Inspired Hybrid Neural Networks for Neural Decoding: A Controlled Ablation Study of Learnable Quantum Sidecar Integration"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.22475"
summary: "arXiv:2608.22475v1 Announce Type: cross Abstract: We study parameterized quantum circuits (PQCs) integrated as residual sidecar modules within a ResNet-50 backbone for 31-class neural population decod"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.22475v1 Announce Type: cross Abstract: We study parameterized quantum circuits (PQCs) integrated as residual sidecar modules within a ResNet-50 backbone for 31-class neural population decoding---imagined handwriting classification from multi-neuron spike rasters. Under strictly controlled conditions (fixed data splits, seeds, and optimizer), we compare four model variants: baseline, quantum sidecar with frozen input projection, quantum sidecar with backbone-gradient-trained projection, and a measurement-guided variant that aligns angle encodings with circuit measurement outcomes. The backbone-gradient variant improves accuracy in 3/4 seeds (+0.19% mean, 95% CI [-1.10%, +1.48%]) and consistently reduces Linear CKA similarity to baseline features (Delta=-0.025, 4/4 seeds), indicating genuine structural reorganization of representations. A nine-variant ablation identifies simple shallow architectures as the most effective and reproducible configuration. Measurement-guided training consistently improves representation geometry without reducing accuracy. All results use noiseless statevector simulation on 4 qubits, a regime chosen to reflect the practical constraints of current near-term superconducting hardware; no quantum computational advantage over classical methods is claimed.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.22475) | 2026-08-25
