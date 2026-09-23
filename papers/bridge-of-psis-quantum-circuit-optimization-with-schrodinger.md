---
title: "Bridge of Psi's: Quantum Circuit Optimization with Schrodinger Bridges"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25947"
summary: "arXiv:2609.25947v1 Announce Type: new Abstract: Quantum circuit optimization replaces a circuit with an equivalent one of fewer gates and lower depth, reducing execution cost and error rate. We ask wh"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25947v1 Announce Type: new Abstract: Quantum circuit optimization replaces a circuit with an equivalent one of fewer gates and lower depth, reducing execution cost and error rate. We ask whether a generative model can learn this transformation directly from examples, rather than selecting from a fixed rewrite library or rigid algebraic routines. We present Bridge of Psi's (BOPS), a generative model based on Schrodinger bridges, using a custom denoiser architecture, that learns a transformation from a source circuit into an equivalent optimized circuit. We train it on data constructed to be hard for existing optimizers, by applying rewrite rules backwards so that each input has a known lower-cost target. On held-out 8 qubits imes 64 depth Clifford+T circuits, BOPS reduces gate count by 2.46imes and depth by 2.45imes in geometric mean, outperforming all nine baseline optimizers. This constitutes the first generative model bridging quantum circuits and frontier machine learning methods, opening up the quantum compilation stack to learned optimization along multiple axes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25947) | 2026-09-23
