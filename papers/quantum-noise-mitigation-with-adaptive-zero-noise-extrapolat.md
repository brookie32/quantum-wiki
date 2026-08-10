---
title: "Quantum Noise Mitigation with Adaptive Zero-Noise Extrapolation: A Contextual Multi-Armed Bandits Approach"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06426"
summary: "arXiv:2608.06426v1 Announce Type: new Abstract: Variational quantum circuits (VQCs) are central to near-term quantum computing, yet their practical deployment is severely hindered by noise. While exis"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06426v1 Announce Type: new Abstract: Variational quantum circuits (VQCs) are central to near-term quantum computing, yet their practical deployment is severely hindered by noise. While existing error mitigation methods, such as zero-noise extrapolation (ZNE), typically assume static noise, real noisy intermediate-scale quantum (NISQ) systems exhibit dynamic, time-varying noise that remains largely unaddressed. To overcome this critical gap, our work introduces a novel adaptive noise mitigation framework for VQCs that integrates ZNE with contextual multi-armed bandits (CMAB), enabling dynamic, context-aware selection of circuit-folding levels based on ansatz parameters (e.g., depth, parameter count) and the evolving noise environment. Unlike fixed-fold or heuristic ZNE, our approach uses online adaptation to improve the accuracy of ZNE and reduce redundant quantum circuit executions. Our extensive simulations and experiments on real quantum hardware reveal the following important properties: (i) deeper VQCs accumulate noise, degrading accuracy and increasing the number of quantum circuit executions; (ii) ZNE restores estimator fidelity when the folding level is chosen appropriately; and (iii) CMAB-guided folding cuts quantum circuit execution round trips by up to 40%, bytes exchanged by up to 35%, and end-to-end cost by up to 30% under a 10~Mbps budget, with up to 6.9% higher estimator fidelity (CIFAR-10, depth 3, noise band eta=0.05), versus fixed-fold and grid-search ZNE. These results demonstrate substantial performance gains over existing noise mitigation methods, underscoring the effectiveness of our design in supporting robust noise mitigation for VQCs. The source code is also publicly released to support reproducibility.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06426) | 2026-08-10
