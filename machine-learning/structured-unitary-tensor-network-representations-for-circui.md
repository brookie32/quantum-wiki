---
title: "Structured Unitary Tensor Network Representations for Circuit-Efficient Quantum Data Encoding"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.16266"
summary: "arXiv:2602.16266v2 Announce Type: replace Abstract: Encoding classical data into quantum states is a central bottleneck in quantum machine learning: many widely used encodings are circuit-inefficient,"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2602.16266v2 Announce Type: replace Abstract: Encoding classical data into quantum states is a central bottleneck in quantum machine learning: many widely used encodings are circuit-inefficient, requiring deep circuits and substantial quantum resources, which limits scalability on quantum hardware. In this work, we propose tensor network-based quantum data encoding (TNQE), a circuit-efficient framework built on structured unitary tensor network (TN) representations. TNQE first represents each classical input via a TN decomposition and then compiles the resulting tensor cores into an encoding circuit through two complementary core-to-circuit strategies. To make this compilation trainable while respecting the unitary nature of quantum operations, we introduce a unitary-aware constraint that parameterizes TN cores as learnable block unitaries, enabling them to be directly optimized and directly encoded as quantum operators. The proposed TNQE framework enables explicit control over circuit depth and qubit resources, allowing the construction of shallow, resource-efficient circuits. Across a range of benchmarks, TNQE achieves encoding circuits as shallow as 0.04imes the depth of amplitude encoding, while naturally scaling to high-resolution images (256 imes 256) and demonstrating practical feasibility on real quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.16266) | 2026-10-23
