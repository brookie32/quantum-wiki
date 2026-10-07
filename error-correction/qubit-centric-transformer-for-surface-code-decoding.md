---
title: "Qubit-centric Transformer for Surface Code Decoding"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.11593"
summary: "arXiv:2510.11593v3 Announce Type: replace Abstract: For reliable large-scale quantum computation, quantum error correction (QEC) is essential to protect logical information distributed across multiple"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2510.11593v3 Announce Type: replace Abstract: For reliable large-scale quantum computation, quantum error correction (QEC) is essential to protect logical information distributed across multiple physical qubits. Taking advantage of recent advances in deep learning, neural network-based decoders have emerged as a promising approach to improve the reliability of QEC. We propose the qubit-centric transformer (QCT), a novel and universal QEC decoder based on a transformer architecture with a qubit-centric attention mechanism. Our decoder transforms input syndromes from the stabilizer domain into qubit-centric tokens via a specialized embedding strategy. These qubit-centric tokens are processed through attention layers to effectively identify the underlying logical error. Furthermore, we introduce a graph-based masking method that incorporates the topological structure of quantum codes, enforcing attention toward relevant qubit interactions. Across various code distances for surface codes, QCT achieves state-of-the-art decoding performance, significantly outperforming existing neural decoders and the belief propagation (BP) with ordered statistics decoding (OSD) baseline. Notably, QCT achieves a high threshold of 18.1% under depolarizing noise, which closely approaches the theoretical bound of 18.9% and surpasses both the BP+OSD and the minimum-weight perfect matching (MWPM) thresholds. This qubit-centric approach provides a scalable and robust framework for surface code decoding, advancing the path toward fault-tolerant quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.11593) | 2026-10-07
