---
title: "Quantum Large Language Models via Tensor Network Disentanglers"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2410.17397"
summary: "arXiv:2410.17397v2 Announce Type: replace Abstract: We introduce a framework for seamlessly integrating quantum computing into pretrained large language models (LLMs). The key idea is to construct a h"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2410.17397v2 Announce Type: replace Abstract: We introduce a framework for seamlessly integrating quantum computing into pretrained large language models (LLMs). The key idea is to construct a hybrid quantum-classical representation that exactly reproduces the original model, providing a principled starting point from which quantum resources can only improve performance. Our approach replaces the weight matrices in self-attention and multilayer perceptron layers with two variational quantum circuits coupled to a matrix product operator (MPO). Tensor network disentanglers transfer much of each layer's information into the quantum circuits, enabling the remaining tensor network to be compressed to a bond-dimension-one MPO with over three orders of magnitude fewer classical parameters (in our experiments, from 110,592 to approximately 36 for the replaced layer) and less than a 0.3% increase in perplexity. Training an added unitary adapter on top of this representation then surpasses the original model, reducing perplexity by up to 1.6%. Finally, we validate the hybrid architecture on a real quantum processor, demonstrating a practical route towards quantum-enhanced language models.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2410.17397) | 2026-08-18
