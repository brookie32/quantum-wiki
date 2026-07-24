---
title: "QSTAR: Quantum Selective Transfer with Adaptive Routing"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21411"
summary: "arXiv:2607.21411v1 Announce Type: new Abstract: Quantum transfer learning (QTL) is often evaluated by replacing a classical classifier with a fixed variational quantum head, but this hides a key quest"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21411v1 Announce Type: new Abstract: Quantum transfer learning (QTL) is often evaluated by replacing a classical classifier with a fixed variational quantum head, but this hides a key question: when is the quantum branch actually useful? We propose QSTAR: Quantum Selective Transfer with Adaptive Routing, a selective QTL framework that keeps high-confidence classical predictions and routes only low-confidence samples to a fallback branch. Using a frozen ResNet18 backbone on Fashion-MNIST, we compare manually designed QTL heads, KetGPT-designed quantum heads, and parameter-matched classical baselines under a common data split and optimization schedule. Standard QTL heads reach at most 57.0% accuracy, while the strongest KetGPT head in the main filtered sweep reaches 78.5% accuracy and 0.785 F1-score. Although the strongest fixed classical head remains higher at 81.6%, selective routing gives the quantum branch a clearer role. On low-confidence samples, KetGPT #180 improves accuracy over a parameter-matched MLP fallback by 6.82, 4.31, and 3.03 percentage points at thresholds of 0.70, 0.80, and 0.90. At the full-system level, Adaptive KetGPT-QTL reaches 80.9% accuracy and 0.807 F1-score, outperforming the adaptive classical baseline. A separate compact-circuit ablation identifies KetGPT #160 as a stronger fixed-head candidate, reaching 81.9% accuracy with only 10 quantum parameters and 9 gates. These results suggest that architecture-searched quantum heads are most useful as targeted fallback branches for uncertain inputs rather than uniform replacements for classical classifiers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21411) | 2026-07-24
