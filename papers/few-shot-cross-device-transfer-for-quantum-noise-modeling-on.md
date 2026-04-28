---
title: "Few-Shot Cross-Device Transfer for Quantum Noise Modeling on Real Hardware"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24397"
summary: "arXiv:2604.24397v1 Announce Type: new Abstract: In the noisy intermediate-scale quantum (NISQ) regime, quantum devices contain hardware-specific noise sources which restrict device-invariant error mit"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24397v1 Announce Type: new Abstract: In the noisy intermediate-scale quantum (NISQ) regime, quantum devices contain hardware-specific noise sources which restrict device-invariant error mitigation strategies. We explore transfer learning approaches to apply noise models learned on one quantum device to a different device with the help of a small amount of data. We create a real-hardware dataset from two IBM quantum devices, ibm_fez (source) and ibm_marrakesh (target), comprising 170 noisy and ideal circuit output distributions, with device calibration features added. We train a residual neural network on the source device to map noisy to ideal outcomes. The zero-shot transfer test shows a KL divergence of 1.6706 (up from 0.3014), establishing device specificity. With K = 20 fine-tuning samples, KL drops to 1.1924 (28.6% improvement over zero-shot), recovering 34.9% of the gap between zero-shot and in-domain KL. Ablation studies reveal that the major cause of mismatches across devices is CX gate error, followed by readout error. The results show quantum noise can be learned and fine-tuned with minimal samples, and provide a plausible approach to cross-device quantum error mitigation.



## Related
- [[quantum-circuit-cutting-complexity-and-optimization|Quantum Circuit Cutting: Complexity and Optimization]]
- [[diffqec-a-versatile-diffusion-model-for-quantum-error-correc|DiffQEC: A versatile diffusion model for quantum error correction]]
- [[quantum-decoherence-of-the-surface-code-a-generalized-caldei|Quantum Decoherence of the Surface Code: A Generalized Caldeira-Leggett Approach]]
- [[fixed-reservoir-vs-variational-quantum-architectures-for-cha|Fixed-Reservoir vs Variational Quantum Architectures for Chaotic Dynamics: Benchmarking QRC and QPINN on the Lorenz System]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24397) | 2026-04-28
