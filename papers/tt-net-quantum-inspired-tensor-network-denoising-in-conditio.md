---
title: "TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19789"
summary: "arXiv:2608.19789v1 Announce Type: cross Abstract: Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scient"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19789v1 Announce Type: cross Abstract: Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientific mainstream in quantum physics. Among various types of tensor networks, Tensor Trains (commonly know as Matrix Product States in the quantum computing community) have already found applications in machine learning. These methods often rely on a powerful linear algebra tool called the Singular Value Decomposition (SVD). Several conditional GAN architectures for image denoising incorporate SVD as a single-cut decomposition step applied to generator feature maps. In this work we introduce TT-Net, which replaces the per-channel SVD denoising block with a two-cut tensor-train decomposition capable of accessing cross-channel information directly, a capability absent from contemporary alternatives. In a controlled comparison differing only in this decomposition mechanism, TT-Net outperforms SVD-Net on PSNR and SSIM across all three noise types tested (Gaussian, motion blur, and salt-and-pepper), supporting the hypothesis that cross-channel access improves denoising quality. Training-dynamics analysis further shows that TT-Net's adversarial loss term consistently saturates to a stagnant state across all three noise types, more so than SVD-Net's, while reconstruction quality continues to improve regardless, raising an open question about the adversarial component's contribution that this work identifies but does not resolve. Furthermore, for Gaussian noise our method outperforms both the EigenGAN and the state of the art Pix2pix method which does not assume any linear algebra decompositions and does not retain any linear algebra information. Our manuscript shows how quantum inspired tools can be used as practical real world feature filters for deep learning applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19789) | 2026-08-21
