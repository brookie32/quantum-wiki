---
title: "Multitask learning with semiempirical orbital charges enables sample-efficient MLIPs"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2605.24073"
summary: "arXiv:2605.24073v2 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) require generating computationally expensive, large-scale training datasets to accurately simulate m"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2605.24073v2 Announce Type: replace Abstract: Machine learning interatomic potentials (MLIPs) require generating computationally expensive, large-scale training datasets to accurately simulate materials and molecules. Incorporating electronic structure information using multitask learning improves sample efficiency, however, training on full Hamiltonian matrices, which scale quadratically with the number of atoms, is intractable for large datasets. In this work, we show that multitask learning utilizing orbitally resolved semiempirical charges significantly improves sample efficiency and accuracy in MLIPs. To efficiently predict orbital charges, we implement a specialized equivariant model, reducing charge prediction error compared to an invariant baseline. By augmenting training with computationally inexpensive GFN1-xTB orbital charges, which scale linearly with the number of atoms, our model achieves a 58% reduction in energy mean absolute error relative to energy-only baselines, and requires five times less data to match their performance. Against the stronger baseline of joint energy-and-force training, orbital charges still reduce the energy error by 12%. Furthermore, our approach matches or outperforms models trained on expensive density functional theory (DFT) atomic charges, capturing orbitally resolved electronic complexity and forcing the network to learn a physically accurate latent space that spontaneously clusters metals by shared chemical properties. Because orbital charges are only required during training, this approach preserves inference efficiency, providing a scalable recipe for developing accurate, data-efficient foundation models for complex chemical systems.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2605.24073) | 2026-10-19
