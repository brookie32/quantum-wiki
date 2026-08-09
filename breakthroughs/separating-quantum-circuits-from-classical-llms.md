---
title: "Separating quantum circuits from classical LLMs"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03962"
summary: "arXiv:2608.03962v1 Announce Type: new Abstract: Modern large language models - transformers and diffusion language models - are built around two canonical algorithmic tasks: prediction and generation."
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03962v1 Announce Type: new Abstract: Modern large language models - transformers and diffusion language models - are built around two canonical algorithmic tasks: prediction and generation. We prove unconditional separations between low-depth quantum computation and the corresponding bounded-resource classical language-model architectures in both regimes. Concretely, we exhibit the following: 1. Distributional separation. We give a distribution that is sampleable by extsf{QNC}^0 circuits (i.e., a family of constant-depth quantum circuits consisting of bounded fan-in gates) that no constant-round diffusion language model (extsf{DLM}) with shallow scheduling and denoising can sample within constant distance, even when allowed sublinear chain-of-thought and output-token revision/remasking events, the very features modern extsf{DLM}s rely on. 2. Functional separation. We exhibit a function computable in land irc extsf{QNC}^0[loglog n] (i.e., a family of O(loglog n)-depth extsf{QNC}^0 circuits, where n is the input length, followed by a single classical mathsf{AND} gate) such that any constant-depth decoder-only transformer computing the function must be large: it would have to have width n^{Omega(1)}. Together, our work initiates the study of quantum advantage in the era of large language models.



## Related
- [[entanglement-geometry-separates-circuit-cutting-classical-ha|Entanglement geometry separates circuit cutting, classical hardness, and trainability]]
- [[hardness-and-complexity-transition-of-noisy-random-circuit-s|Hardness and Complexity Transition of Noisy Random Circuit Sampling]]
- [[the-impact-of-qubit-connectivity-on-quantum-advantage-in-noi|The Impact of Qubit Connectivity on Quantum Advantage in Noisy IQP Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03962) | 2026-08-05
