---
title: "Evaluating the Effect of the Order of Optimization Passes in Quantum Circuit Optimization"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29406"
summary: "arXiv:2609.29406v1 Announce Type: new Abstract: Quantum circuit optimization is critical for mitigating the noise inherent in current quantum hardware. Quantum compilers typically sequentially apply m"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29406v1 Announce Type: new Abstract: Quantum circuit optimization is critical for mitigating the noise inherent in current quantum hardware. Quantum compilers typically sequentially apply multiple optimizations (also called ``optimization passes'') to improve the circuit. The impact of the order in which these passes are executed has yet been largely unexplored. This paper investigates the significance of the order of optimization passes within quantum circuit compilation, specifically analyzing interactions between different optimization methods and quantifying their mutual influences. Using Qiskit's compiler, we systematically evaluate pairwise combinations of 16 selected optimization passes, measuring circuit depth and gate count across various benchmark circuits. Our findings indicate dependencies between certain optimization passes, demonstrating that the order of the passes affects the optimization quality. In some cases, the worse performing sequence can be corrected through repeated pass application. %such that they are as good as the best performing one by extending the sequence. Experiments on multi-pass sequences show that more than two optimization passes may have an impact on each other but that this always links to the previously found pairwise effects. We observe that it is important to initially choose the best order of optimization passes to get the best possible optimization for the given circuit. The experiments reveal some factors which are important to choose the best, or at least a good, order; among those, the resulting optimization sequence depends the most on the native gate set.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29406) | 2026-09-25
