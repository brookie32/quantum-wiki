---
title: "Enhancing Pauli Correlation Encoding for quantum optimization via systematic expressivity analysis"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.09718"
summary: "arXiv:2609.09718v1 Announce Type: new Abstract: Quantum approaches for combinatorial optimization problems have attracted considerable attention in recent years. Among these approaches, Pauli Correlat"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09718v1 Announce Type: new Abstract: Quantum approaches for combinatorial optimization problems have attracted considerable attention in recent years. Among these approaches, Pauli Correlation Encoding (PCE) has emerged as a promising framework for quantum devices with limited qubit resources because it embeds optimization variables in expectation values of Pauli strings. However, the mechanisms underlying its performance and the reasons for its saturation remain unclear. In this work, we investigate these questions through a systematic analysis of expressivity and trainability. First, we compare PCE with classical surrogate models based on tensor networks whose structures progressively approach the topology of the PCE circuit. The results show that PCE attains comparable solution quality with substantially fewer trainable parameters, indicating strong parameter efficiency. Second, to determine whether the performance saturation of conventional PCE is caused by insufficient expressivity or by optimization difficulty, we perform a diagnostic expressivity test in which the circuit is trained toward reference configurations for Max-Cut. The results show that even shallow PCE circuits can represent strong solutions, indicating that the main bottleneck is not the representational power of the ansatz, but the trainability under the relaxed objective function. Motivated by this finding, we propose a multistage continuation framework that gradually transforms a smooth relaxed objective into a sharper objective that more closely approximates the target discrete problem. Numerical experiments on G-set instances with 800 vertices show that the proposed method consistently outperforms conventional PCE and is competitive with representative graph neural network (GNN) methods. These results clarify the main factors behind PCE performance and provide a practical strategy for improving PCE on quantum devices with limited qubit resources.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.09718) | 2026-09-10
