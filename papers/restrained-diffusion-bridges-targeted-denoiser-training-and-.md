---
title: "Restrained Diffusion Bridges: Targeted Denoiser Training and Refinement"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.02170"
summary: "arXiv:2611.02170v2 Announce Type: replace-cross Abstract: Diffusion models are often inaccurate in critical, data-sparse regions of the target distribution. Sampling from restrained distributions, bia"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.02170v2 Announce Type: replace-cross Abstract: Diffusion models are often inaccurate in critical, data-sparse regions of the target distribution. Sampling from restrained distributions, biased distributions used in classical enhanced sampling to concentrate data near chosen configurations, can control where training data are collected but biases the learned distribution. We establish that this bias cancels exactly when forward noising from restrained data is conditioned on the restrained configuration at an appropriately chosen intermediate time. This allows a pretrained model fine-tuned on restrained data to achieve high accuracy in any chosen region of the target distribution, regardless of its probability, using standard denoising or flow matching objectives without importance weights. When no target data are available, Gibbs sampling enables inference from a model trained exclusively on restrained data.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.02170) | 2026-11-05
