---
title: "Variational Quantum Transformer Architecture for Synthetic Language Generation"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.18565"
summary: "arXiv:2609.18565v1 Announce Type: new Abstract: We propose a compact NISQ-compatible quantum transformer architecture for synthetic QNLP sequence modelling. The model preserves the autoregressive next"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18565v1 Announce Type: new Abstract: We propose a compact NISQ-compatible quantum transformer architecture for synthetic QNLP sequence modelling. The model preserves the autoregressive next-token interface of a classical transformer, but replaces attention and feed-forward sublayers with variational quantum encoder blocks, connector circuits, decoder blocks and a direct two-qubit measurement readout. Token contexts are angle-encoded into small quantum registers, processed by parallel variational heads and encoder integration circuits and conditioned through decoder ancillae to produce a distribution over a four-token vocabulary. We evaluate several architecture variants on deterministic and lexicographic grammar-generation tasks against a compact classical transformer baseline. The quantum models are trainable end-to-end and learn nontrivial grammar structure, including perfect deterministic generation in individual runs and high lexicographic validity in the strongest variant. The classical baseline remains more accurate and stable and the quantum models are sensitive to initialization. The contribution is therefore not a claim of quantum advantage, but a concrete architecture and evaluation of transformer-inspired QNLP sequence modelling under near-term quantum constraints.



## Related
- [[separating-quantum-circuits-from-classical-llms|Separating quantum circuits from classical LLMs]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.18565) | 2026-09-17
