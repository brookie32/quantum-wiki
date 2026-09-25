---
title: "Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting"
date: "2026-09-22"
updated: "2026-09-25"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2161"
summary: "This paper studies the cryptanalytic extraction of convolutional neural networks (CNNs). Existing cryptanalytic extraction attacks on CNNs assume that the network architecture is known, and try to rec"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

This paper studies the cryptanalytic extraction of convolutional neural networks (CNNs). Existing cryptanalytic extraction attacks on CNNs assume that the network architecture is known, and try to recover model parameters. In this paper, we prove for the first time that the architecture assumption can be removed for CNNs with both max and average pooling. Our core finding is that the spatial geometry of the weight vectors recovered by existing parameter-recovery attacks naturally leaks the architecture. We formalize this geometry and establish its correspondence with the architectural knowledge of a convolutional layer: (1) The sparsity consistency with the convolution receptive field reveals the layer type, the kernel size, and the stride; (2) The numerical consistency with the kernel parameters reveals the padding mode and the output-channel number; (3) The structural consistency with the pooling operation reveals the pooling type, the window size, and the stride. Although the recovered vectors are obtained using different methods in the raw-output and hard-label settings, their spatial geometry remains the same. Therefore, our architecture recovery is feedback-agnostic: combined with a parameter-recovery attack, it yields a complete cryptanalytic extraction framework that recovers both the architecture and the parameters in the black-box setting. Extensive experiments, including both layer-wise and end-to-end ones, on a wide range of CNNs demonstrate that simultaneously recovering the network architecture and the model parameters is practical.



## Related
- [[polynomial-time-cryptanalytic-extraction-of-deep-neural-netw|Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Limited Architecture Knowledge Setting]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2161) | 2026-09-22
