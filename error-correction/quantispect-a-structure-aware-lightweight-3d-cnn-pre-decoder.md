---
title: "QuantiSpect: A Structure-Aware Lightweight 3D CNN Pre-Decoder for Scalable Surface Code Quantum Error Correction"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.18204"
summary: "arXiv:2607.18204v2 Announce Type: replace Abstract: Real-time decoding is a critical bottleneck for large-scale fault-tolerant quantum computing. AI-based neural pre-decoders locally correct most phys"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2607.18204v2 Announce Type: replace Abstract: Real-time decoding is a critical bottleneck for large-scale fault-tolerant quantum computing. AI-based neural pre-decoders locally correct most physical errors before passing residual syndromes to a global decoder, enabling sub-microsecond latencies. However, existing architectures carry significant overhead from dense 3D convolutions. We present QuantiSpect, a lightweight 3D convolutional neural network (CNN) pre-decoder for the rotated surface code, built on the decoding pipeline of Chamberland et al. The key idea is to replace the dense 3D convolutions with three parallel branches in each residual block: a depthwise spatial branch, a depthwise temporal branch, and a grouped spatio-temporal branch, followed by a squeeze-and-excitation channel gate. This reflects the structure of surface code errors, where spatial and temporal syndrome correlations are partially separable. On a unified 4xA100 GPU benchmark, QuantiSpect matches the receptive field of the Accurate baseline at R=13 while using ~2.71x fewer parameters (0.663M vs 1.80M) and ~2.84x fewer per-voxel convolutional MACs. It matches Accurate's circuit-level threshold and accuracy at moderate and large code distances, reduces the logical error rate by up to ~1.85x relative to uncorrelated PyMatching at d=13, p=0.5%, and speeds up the PyMatching decode by up to 3.11x at d=23. We also explored enlarging the receptive field by adding blocks. Even at R=21, the model uses only 1.18M parameters, fewer than both the R=13 Accurate baseline (1.80M) and the R=17 dense model (4.22M), despite its larger receptive field. This expanded variant significantly outperforms the Accurate model, raising the circuit-level threshold to ~0.80% and further reducing the logical error rate. Together, both variants show that a structure-aware factorized design is an effective, parameter-efficient alternative to a dense one for decoding the surface code.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.18204) | 2026-08-06
