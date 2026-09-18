---
title: "A Protocol-Guided LLM Agent for Quantum Program Synthesis and Execution"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20258"
summary: "arXiv:2609.20258v1 Announce Type: new Abstract: This study evaluates a protocol-guided large language model (LLM) agent workflow for quantum program synthesis and execution. A versioned YAML protocol "
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.20258v1 Announce Type: new Abstract: This study evaluates a protocol-guided large language model (LLM) agent workflow for quantum program synthesis and execution. A versioned YAML protocol specifies interface and quantum-semantic requirements while leaving circuit design to the model. The workflow combines Qiskit circuit generation, evaluator-guided repair, and quantum processing unit (QPU) deployment. A matched ablation evaluates four LLM endpoints using the variational quantum eigensolver (VQE) for H_2, the quantum approximate optimization algorithm (QAOA) for MaxCut, and Fashion-MNIST quantum-kernel classification. Across 240 trials, protocol guidance increased evaluator completion from 80.0% to 99.2%, reduced mean repairs from 2.56 to 0.75, and reduced mean agent time from 55.70 to 30.58~s. Provider-reported token use decreased for three of four endpoints. Completed VQE trials meeting chemical accuracy increased from 16/40 to 29/40, while valid QAOA approximation ratios remained comparable. Semantic review identified rank-one fidelity kernels, reinforcing the distinction between evaluator completion and semantic validity. A 210-run IBM QPU study evaluated the combined generation-and-selection pipelines and confirmed deployment feasibility. The results support protocol guidance as a software-reliability layer that must be complemented by quantum-semantic validation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20258) | 2026-09-18
