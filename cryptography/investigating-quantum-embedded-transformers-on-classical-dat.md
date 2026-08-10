---
title: "Investigating Quantum-Embedded Transformers on Classical Datasets for Cross-Modality Classification"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06846"
summary: "arXiv:2608.06846v1 Announce Type: new Abstract: We test whether a parameterized quantum circuit (PQC) improves a hybrid quantum-classical model's performance on classical datasets, using an interface-"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06846v1 Announce Type: new Abstract: We test whether a parameterized quantum circuit (PQC) improves a hybrid quantum-classical model's performance on classical datasets, using an interface-matched classical map as the control while holding all other components fixed. Our architecture, Quantum-Embedded Attention (QEA), uses a learnable projector to compress backbone features into an n_q-dimensional angle vector, a shallow PQC to map those angles to one- and two-qubit Pauli expectations, and a classical attention decoder to produce class logits. We hypothesized the PQC would improve accuracy or seed-to-seed stability over a classical map with matched input/output dimensions. We test this with an interface-matched 2imes2 factorial on Breast Cancer Wisconsin at n_qin{4,8}, independently swapping the PQC for a classical map and the attention decoder for a linear head, across five paired seeds per cell. Three of four paired quantum-minus-classical 95% confidence intervals include zero; the fourth, a +1.63 percentage-point contrast for the attention decoder at n_q=4, reverses sign at n_q=8 and does not survive correction across the four contrasts. The experiment thus shows no consistent PQC contribution and cannot establish equivalence. A five-dataset cross-modality grid shows comparable accuracy on AG~News, Breast Cancer Wisconsin, and BirdCLEF but a large deficit on CIFAR-10; these cells are not interface-matched and are interpreted descriptively. We report all planned canonical runs, distinguish current Pauli-readout results from legacy probability-readout experiments, and analyze bottleneck, simulation, finite-shot, and noise limitations. The results do not establish a quantum advantage; they demonstrate why controlled component attribution is necessary before crediting a hybrid model's performance to its quantum layer.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06846) | 2026-08-10
