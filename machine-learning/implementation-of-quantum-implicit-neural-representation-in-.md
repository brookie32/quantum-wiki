---
title: "Implementation of Quantum Implicit Neural Representation in Deterministic and Probabilistic Autoencoders for Image Reconstruction/Generation Tasks"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.06755"
summary: "arXiv:2603.06755v3 Announce Type: replace-cross Abstract: We propose a quantum implicit neural representation (QINR)-based autoencoder (AE) and variational autoencoder (VAE) for image reconstruction a"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2603.06755v3 Announce Type: replace-cross Abstract: We propose a quantum implicit neural representation (QINR)-based autoencoder (AE) and variational autoencoder (VAE) for image reconstruction and generation tasks. Our purpose is to demonstrate that the QINR in VAEs and AEs can transform information from the latent space into highly rich, periodic, and high-frequency features. Additionally, we aim to show that the QINR-VAE can be more stable than various quantum generative adversarial network (QGAN) models in image generation because it can address the low diversity problem. Our quantum-classical hybrid models consist of a classical convolutional neural network (CNN) encoder and a quantum-based QINR decoder. We train the QINR-AE/VAE with binary cross-entropy with logits (BCEWithLogits) as the reconstruction loss. For the QINR-VAE, we additionally employ Kullback-Leibler divergence for latent regularization with beta/capacity scheduling to prevent posterior collapse. We introduce learnable angle-scaling in data reuploading to address optimization challenges. We test our models on the MNIST, E-MNIST, and Fashion MNIST datasets to reconstruct and generate images. Our results demonstrate that the QINR structure in VAE can produce a wider variety of images with a small amount of data than various generative models that have been studied. We observe that the generated/reconstructed images from the QINR-VAE/AE are clear with sharp boundaries and details. Overall, we find that the addition of QINR-based quantum layers into the AE/VAE frameworks shows improved performance of reconstruction/generation under the constrained experimental setting relative to the specific baselines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.06755) | 2026-09-22
