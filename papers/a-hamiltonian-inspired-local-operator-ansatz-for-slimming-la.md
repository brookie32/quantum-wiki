---
title: "A Hamiltonian-Inspired Local-Operator Ansatz for Slimming Large Language Models"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.25344"
summary: "arXiv:2605.25344v2 Announce Type: replace-cross Abstract: Dense linear maps carry much of the parameter and computational burden of modern neural networks, yet their dense form leaves the organization"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2605.25344v2 Announce Type: replace-cross Abstract: Dense linear maps carry much of the parameter and computational burden of modern neural networks, yet their dense form leaves the organization of learned couplings implicit. Quantum many-body physics organizes exponentially large operators by writing a global Hamiltonian as a sum of local terms, (hat H=sum_khat h_k). Whether the same structural principle can carry learned neural maps is unknown. We introduce Tensor Mixture (MixT), which represents a dense map as a natively executable sum of overlapping local tensor operators without imposing an explicit matrix-rank constraint. The local-term count (N_T) sets the effective nonlocality and operator complexity, while the number of replaced Transformer blocks (N_B) extends this structural coordinate across network depth. Tests on Qwen3-8B and LLaMA2-7B reveal a broad recoverable regime followed by an abrupt, model-specific boundary that is remarkably stable against changes in (N_T). Accuracy and output-distribution statistics reorganize together across the boundary; in LLaMA2-7B, the same depth separates two scaling regimes of inter-layer geometry drift. The directly executed structure also reduces parameters, arithmetic, storage, and memory. These results establish the local-sum structure as a viable organizing principle for learned linear maps at billion-parameter scale and expose a sharp boundary in their tolerance to structural simplification.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.25344) | 2026-08-04
