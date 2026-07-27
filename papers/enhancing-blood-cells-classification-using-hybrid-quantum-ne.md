---
title: "Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.23324"
summary: "arXiv:2605.23324v3 Announce Type: replace-cross Abstract: Accurate classification of microscopic blood cells is still a critical task in medical image analysis, where subtle variations and limited dat"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2605.23324v3 Announce Type: replace-cross Abstract: Accurate classification of microscopic blood cells is still a critical task in medical image analysis, where subtle variations and limited data can challenge conventional deep learning models. As such, we investigate in this work the potential of Hybrid Quantum-Classical Neural Networks (HQNNs) to enhance feature representation and improve classification performance in this domain. We propose a modular architecture combining a pre-trained ResNet-50 backbone with a low-dimensional latent bottleneck and a variational quantum circuit, enabling a direct comparison between quantum-enhanced and purely classical transformation mechanisms. To isolate the contribution of the quantum component, we evaluate three architectures: a HQNN model, a Classical Matched Model with an additional nonlinear transformation layer of comparable capacity, and a baseline model without an intermediate transformation stage. Experiments conducted on two publicly available blood cell datasets, namely the Blood Cell Images dataset and the PBC dataset, demonstrate that HQNNs consistently achieve superior or more balanced performance across evaluation metrics. In the Blood Cell Images Dataset, the proposed approach improves macro F1-score by up to 3.7% compared to classical baselines, while improving the F1-score from 98.54% to 98.69% in the more challenging 8-class scenario with near-saturated performance. Additional evaluation on IBM quantum hardware shows that the model remains robust under noise, with only a modest performance degradation relative to simulated results. These results indicate that quantum feature transformations can enhance discriminative representations, particularly in challenging classification scenarios, and highlight the practical potential of HQNN models for medical imaging tasks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.23324) | 2026-07-27
