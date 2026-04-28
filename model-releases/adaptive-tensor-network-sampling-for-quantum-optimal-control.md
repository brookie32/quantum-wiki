---
title: "Adaptive Tensor Network Sampling for Quantum Optimal Control"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24467"
summary: "arXiv:2604.24467v1 Announce Type: new Abstract: Quantum optimal control (QOC) provides a systematic framework for achieving high-fidelity operations in quantum systems and plays a central role in task"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24467v1 Announce Type: new Abstract: Quantum optimal control (QOC) provides a systematic framework for achieving high-fidelity operations in quantum systems and plays a central role in tasks such as gate synthesis, state transfer, and pulse design. Existing QOC methods broadly fall into two categories: gradient-based and gradient-free algorithms. The associated optimization landscape is often high-dimensional, non-convex, and populated by numerous local minima, making efficient gradient-free search strategies essential. To address this, we introduce a gradient-free matrix product state/tensor train (MPS/TT) sampling heuristic for discrete quantum optimal control. In our approach, the MPS defines a score function over the space of discrete control parameters, which in turn induces a sampling distribution over candidate control sequences. This distribution is iteratively refined through selection of better performing sequences and local tensor updates to bias the search toward high-performing sequences. We evaluate the method on a range of benchmark problems, including single-qubit state transfer, Bell-pair preparation, qutrit gate implementation, and open-system population transfer. Across these tasks, the method exhibits stable convergence behavior and competitive empirical performance relative to established gradient-free baselines. These results suggest that tensor network sampling offers a viable heuristic framework for discrete quantum control.



## Related
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[a-spectral-gap-informed-parameter-schedule-for-qaoa|A Spectral Gap Informed Parameter Schedule for QAOA]]
- [[architecture-aware-unitary-synthesis|Architecture-aware Unitary Synthesis]]
- [[exhaustive-and-feasible-parametrisation-with-applications-to|Exhaustive and feasible parametrisation with applications to the travelling salesperson problem]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24467) | 2026-04-28
