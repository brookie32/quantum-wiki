---
title: "Fast Trainable Multilinear Bases for Image Compression"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00053"
summary: "arXiv:2608.00053v1 Announce Type: cross Abstract: The Discrete Fourier Transform, the Discrete Cosine Transform, and their block-wise variants underpin most deployed image and video codecs. Their effe"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00053v1 Announce Type: cross Abstract: The Discrete Fourier Transform, the Discrete Cosine Transform, and their block-wise variants underpin most deployed image and video codecs. Their effectiveness rests on three properties: they run in near-linear time (linear up to a polylogarithmic factor), they are exactly invertible, and they carry few to no parameters. In this work, we generalize these bases to isometric multilinear bases, allowing a small number of extra parameters, polylogarithmic in the image size, while preserving all three properties. Given an image dataset, we develop a systematic framework that searches this family for the basis compressing the dataset most effectively: the basis is parameterized as an isometric tensor network, inspired by quantum many-body theory, and trained with Riemannian optimization on the manifold of unitary matrices. Across natural photographs and line drawings, the trained bases consistently improve on their fixed, non-parametric counterparts. On Quick Draw line-drawing compression, they store images in roughly 20% fewer bytes than JPEG's 8 imes 8 block cosine transform at the same reconstruction quality.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00053) | 2026-08-04
