---
title: "SQUARE: Structured Quantum Representation Adapters as Compact Quadratic Feature Maps for Frozen Language Models"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37134"
summary: "arXiv:2609.37134v1 Announce Type: new Abstract: Frozen language models (LMs) are increasingly used as fixed feature extractors for downstream reranking, scoring, and preference modeling, raising a pra"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37134v1 Announce Type: new Abstract: Frozen language models (LMs) are increasingly used as fixed feature extractors for downstream reranking, scoring, and preference modeling, raising a practical question: how should a compact module represent interactions among features in a fixed low-dimensional bottleneck? Common linear and low-rank adapters remain linear at the adaptation module itself, whereas explicit second-order alternatives introduce pairwise interactions through direct parameterization or predefined factorizations. We propose SQUARE, a Structured QUAntum REpresentation adapter that amplitude-encodes the bottleneck vector, applies a parameterized quantum circuit, and measures the resulting state. We show that each basis-probability feature is exactly a normalized quadratic form in the bottleneck coordinates, while the additional Pauli-Z readouts are signed linear combinations of these probabilities. The measured map can therefore parameterize interactions over O(d^2) coordinate pairs through a small set of shared circuit parameters, where d is the bottleneck dimension. It provides a structured parameterization within, rather than beyond, the classical normalized-quadratic feature class. In a disjoint same-pipeline evaluation over eight GLUE-derived controlled interaction tasks and five shared seeds, SQUARE achieves an average test accuracy of 0.7565, compared with 0.7355 for an affine normalized-quadratic predictor, 0.7271 for the evaluated parameter-matched Givens mixing model, 0.6817 for an MLP, and 0.6155 for a frozen-circuit control. Under reduced supervision, it also shows consistent gains over the strongest evaluated classical comparator, with the same qualitative pattern across multiple frozen LM backbones. All circuit experiments use simulation, while the learned feature map can be evaluated exactly in batched PyTorch without quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37134) | 2026-09-30
