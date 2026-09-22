---
title: "Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.23016"
summary: "arXiv:2609.23016v1 Announce Type: new Abstract: Deep learning models are powerful but opaque. As quantum machine learning matures, the field faces a defining choice: build quantum models that are equa"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23016v1 Announce Type: new Abstract: Deep learning models are powerful but opaque. As quantum machine learning matures, the field faces a defining choice: build quantum models that are equally opaque, or exploit the mathematical structure of quantum mechanics to make them inherently interpretable. We show that the latter is possible. By tracking quantum mutual information~(MI), entanglement entropy, and state fidelity through the layers of a Quantum Transformer Block (qtb{}), a fully-coherent variational circuit with quantum analogues of both attention and feedforward, we gain direct insight into how the model processes information: which tokens it attends to, when correlations form, and why predictions fail. On four tasks with known dependency structure we show that (i)~learned MI matrices align with ground-truth task structure (AUC,{=},0.69 on lookup), (ii)~disabling entangling gates collapses accuracy from 100% to 15% while MIo 0, proving entanglement is the mechanism, (iii)~accuracy and MI co-evolve during training (rho,{=},0.92 on lookup), and (iv)~per-sample MI predicts prediction correctness on the conditional task with ROC AUC,{=},0.84. All results are validated on IBM Quantum hardware (ibm_kingston, Heron~r2): the circuit's reasoning process, from product state through structured entanglement, is directly observable on a superconducting processor. These proof-of-concept results, obtained on small synthetic tasks, suggest that the physics of quantum computation can provide intrinsic interpretability signals with no direct classical counterpart, motivating study of whether this advantage persists at scale.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.23016) | 2026-09-22
