---
title: "Lottery BP: Unlocking Quantum Error Decoding at Scale"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.00038"
summary: "arXiv:2605.00038v3 Announce Type: replace-cross Abstract: During a QEC cycle, quantum error decoding stands on the critical path. To enable fault tolerance on millions of qubits in real time, scalable"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2605.00038v3 Announce Type: replace-cross Abstract: During a QEC cycle, quantum error decoding stands on the critical path. To enable fault tolerance on millions of qubits in real time, scalable decoding is necessary, which motivates this paper. Existing decoding algorithms (decoders), such as clustering, matching, belief propagation (BP), and neural networks, suffer from one or more of inaccuracy, costliness, and incompatibility, upon a broad set of quantum error correction codes, such as surface code and bivariate bicycle code. Therefore, there exists a gap between existing decoders and an ideal decoder that is accurate, fast, general, and scalable simultaneously. To move closer to the goal above, this paper contributes in three aspects, including decoder algorithm, decoder architecture, and decoding simulator. First, we propose Lottery BP, a lightweight decoder that introduces guided randomness to break the symmetric deadlock caused by quantum degeneracy during decoding. Lottery BP improves the decoding accuracy over BP by up to 6 orders. Second, we design a PolyQec architecture that implements Lottery BP as a local decoder and ordered statistics decoding (OSD) as a global decoder, exemplifying a hierarchical decoder architecture. PolyQec is configurable for surface code and X/Z check. Since Lottery BP boosts the local decoding accuracy, PolyQec invokes the costly global OSD decoder less frequently over BP+OSD to enhance the scalability, e.g., up to 4 orders of magnitude less for surface codes. Third, we develop Syndrilla, a modular PyTorch-based decoding simulator that enables fair, extensible decoder evaluation with unified accuracy and performance metrics. On GPUs, Syndrilla runs 1 order of magnitude faster than CUDAQX.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.00038) | 2026-08-04
