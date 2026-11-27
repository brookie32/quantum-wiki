---
title: "BIFOLD: Memory-Efficient Homomorphic CNN Inference over Bivariate Rings"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3054"
summary: "Fully homomorphic encryption (FHE) enables private convolutional neural network (CNN) inference, but large evaluation keys hinder practical deployment. We introduce an exponential bootstrapping method"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Fully homomorphic encryption (FHE) enables private convolutional neural network (CNN) inference, but large evaluation keys hinder practical deployment. We introduce an exponential bootstrapping method exploiting an exact trigonometric identity to achieve latency comparable to standard bootstrapping, alongside low-depth and efficient functional bootstrapping for densely packed inputs. GL's bivariate ring enables compact plaintexts and convolution fused into bootstrapping. At ring degree N=2^{15}, ResNet-20 inference on an RTX 5090 takes 127.8 ms, 2.19imes faster than RBOOT, the fastest state-of-the-art baseline implemented on the same GPU backend, with 6.1imes smaller evaluation keys. Seeding mask polynomials reduces keys to 0.84 GB at 140.1 ms latency, advancing practical privacy-preserving machine learning.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3054) | 2026-11-26
