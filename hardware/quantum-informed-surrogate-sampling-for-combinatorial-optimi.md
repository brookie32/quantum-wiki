---
title: "Quantum-informed surrogate sampling for combinatorial optimization"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.22372"
summary: "arXiv:2607.22372v1 Announce Type: new Abstract: We introduce Quantum-Informed Surrogate Sampling (QISS), a post-processing framework that generates candidate solutions to combinatorial optimization pr"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.22372v1 Announce Type: new Abstract: We introduce Quantum-Informed Surrogate Sampling (QISS), a post-processing framework that generates candidate solutions to combinatorial optimization problems from low-weight correlations of shallow quantum circuits. The quantum device estimates local observables, which are directly accessible by repeated measurements and for which a wide range of error-mitigation tools are available, while candidate solutions are generated classically without explicit dependence on the combinatorial optimization problem itself. We evaluate QISS on Maximum Cut and Maximum Independent Set problems on N variables and show that only O(N) low-order correlators from shallow circuits suffice to produce competitive solutions that surpass vanilla QAOA. For MaxCut on 3-regular graphs, QISS from p=3 QAOA correlators outperforms vanilla QAOA at p=17 on average, with further improvements possible by warm-starting QAOA. We validate the procedure on the 54-qubit IQM Emerald quantum device and demonstrate its noise resilience. Our results support a regime for near-term optimization in which shallow circuits serve not as direct samplers but as generators of informative statistics for scalable classical sampling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.22372) | 2026-07-27
