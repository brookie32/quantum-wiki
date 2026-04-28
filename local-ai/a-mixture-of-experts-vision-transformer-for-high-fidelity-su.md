---
title: "A Mixture of Experts Vision Transformer for High-Fidelity Surface Code Decoding"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "local-ai"
tags: [local-ai, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.12483"
summary: "arXiv:2601.12483v2 Announce Type: replace Abstract: Quantum error correction is a key ingredient for large scale quantum computation, protecting logical information from physical noise by encoding it "
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2601.12483v2 Announce Type: replace Abstract: Quantum error correction is a key ingredient for large scale quantum computation, protecting logical information from physical noise by encoding it into many physical qubits. Topological stabilizer codes are particularly appealing due to their geometric locality and practical relevance. In these codes, stabilizer measurements yield a syndrome that must be decoded into a recovery operation, making decoding a central bottleneck for scalable real time operation. Existing decoders are commonly classified into two categories. Classical algorithmic decoders provide strong and well established baselines, but may incur substantial computational overhead at large code distances or under stringent latency constraints. Machine learning based decoders offer fast GPU inference and flexible function approximation, yet many approaches do not explicitly exploit the lattice geometry and local structure of topological codes, which can limit performance. In this work, we propose QuantumSMoE, a quantum vision transformer based decoder that incorporates code structure through plus shaped embeddings and adaptive masking to capture local interactions and lattice connectivity, and improves scalability via a mixture of experts layer with a novel auxiliary loss. Experiments on the toric code demonstrate that QuantumSMoE outperforms state-of-the-art machine learning decoders as well as widely used classical baselines.



## Related
- [[quantum-decoherence-of-the-surface-code-a-generalized-caldei|Quantum Decoherence of the Surface Code: A Generalized Caldeira-Leggett Approach]]
- [[taming-rydberg-decay-with-measurement-based-quantum-computat|Taming Rydberg Decay with Measurement-based Quantum Computation]]
- [[diffqec-a-versatile-diffusion-model-for-quantum-error-correc|DiffQEC: A versatile diffusion model for quantum error correction]]
- [[locating-rydberg-decay-error-in-swap-leakage-reduction-circu|Locating Rydberg Decay Error in SWAP-Leakage Reduction Circuit Protocol]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.12483) | 2026-04-28
