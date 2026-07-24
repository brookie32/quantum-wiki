---
title: "Neural Guided Sampling for Quantum Circuit Optimization"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.12430"
summary: "arXiv:2510.12430v2 Announce Type: replace Abstract: Translating a general quantum circuit on a specific hardware topology with a reduced set of available gates, also known as transpilation, comes with"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2510.12430v2 Announce Type: replace Abstract: Translating a general quantum circuit on a specific hardware topology with a reduced set of available gates, also known as transpilation, comes with a substantial increase in the length of the equivalent circuit. Due to decoherence, the quality of the computational outcome can degrade seriously with increasing circuit length. Thus, there is major interest to reduce a transpiled quantum circuit to an equivalent circuit which is in its gate count as short as possible. This is, what we call quantum circuit reduction: Finding a quantum circuit with a reduced amount of gates without changing its unitary. One method to address efficient transpilation, e.g. as a post-transpilation process, is based on approaches known from stochastic optimization, e.g. by using random sampling and local resynthesis strategies. Here, a core challenge is that these methods can suffer from sampling efficiency, causing long and energy consuming optimization time. As a remedy, we propose in this work 2D neural guided sampling. Thus, given a 2D representation of a quantum circuit, a neural network predicts groups of gates in the quantum circuit, which are likely reducible. It leads to a sampling prior which can heavily reduce the compute time for quantum circuit reduction. In several experiments, we demonstrate that our method is superior to results obtained from different qiskit or BQSKit optimization levels.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.12430) | 2026-07-24
