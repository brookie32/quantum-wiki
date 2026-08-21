---
title: "Benchmarking Quantum Machine Learning for Power-System Attack Detection: Evaluation Choices Decide the Outcome Before the Models Do"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.15617"
summary: "arXiv:2608.15617v1 Announce Type: cross Abstract: Machine-learning detectors for power-system cyberattacks are themselves attack surfaces, and quantum machine learning has been proposed for them. We b"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.15617v1 Announce Type: cross Abstract: Machine-learning detectors for power-system cyberattacks are themselves attack surfaces, and quantum machine learning has been proposed for them. We benchmark fidelity-kernel SVMs and variational classifiers against six tuned classical models on public power-system attack data (Mississippi State/ORNL), across white-box, transfer, decision-based black-box, and poisoning attacks. Our headline finding is methodological: the benchmark's answers are set by the evaluator's choices before the models. Eight choices -- six in the evaluation protocol, two in the tuning the benchmark itself runs -- each reversed or moved a conclusion at fixed models. The largest is the split: the row-level protocol scores 0.905 macro-F1 where holding whole source files out leaves 0.594, and in the capped matched-dimensionality regime the quantum arm sits within noise of chance with the classical arm 0.024 above it. A fidelity kernel looks most robust until attacked directly (retention 0.886 to 0.064); a mis-fitted surrogate manufactures a 10x asymmetry; an unseeded black-box attack moves 75% between restarts. A positive control explains the accuracy null: the labels, not the pipeline. We give the control that catches each choice and release the seeded benchmark.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.15617) | 2026-08-21
