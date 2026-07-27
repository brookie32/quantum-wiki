---
title: "QRTlib: A Library for Fast Quantum Real Transforms"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.16625"
summary: "arXiv:2510.16625v2 Announce Type: replace Abstract: Real-valued transforms such as the discrete cosine, sine, and Hartley transforms play a central role in classical computing, complementing the Fouri"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2510.16625v2 Announce Type: replace Abstract: Real-valued transforms such as the discrete cosine, sine, and Hartley transforms play a central role in classical computing, complementing the Fourier transform in applications from signal and image processing to data compression. However, their quantum counterparts have not evolved in parallel, and no unified framework exists for implementing them efficiently on quantum hardware. This article addresses this gap by introducing QRTlib, a library for fast and practical implementations of quantum real transforms, including the quantum Hartley, cosine, and sine transforms of various types. We develop new algorithms and circuit optimizations that make these transforms efficient and suitable for near-term devices. In particular, we present a quantum Hartley transform based on the linear combination of unitaries (LCU) technique, achieving a fourfold reduction in circuit size compared to prior methods, and an improved quantum sine transform of Type I that removes large multi-controlled operations. We also introduce circuit-level optimizations, including two's-complement and or-tree constructions. QRTlib provides the first complete implementations of these quantum real transforms in Qiskit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.16625) | 2026-07-27
