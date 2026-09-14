---
title: "LLM Compression by Block Removal with Constrained Binary Optimization"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.00161"
summary: "arXiv:2602.00161v3 Announce Type: replace-cross Abstract: In this paper, we formulate the compression of large language models (LLMs) by optimally deleting transformer blocks (``block removal'') as a "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2602.00161v3 Announce Type: replace-cross Abstract: In this paper, we formulate the compression of large language models (LLMs) by optimally deleting transformer blocks (``block removal'') as a constrained binary optimization (CBO) problem that can be mapped to a physical system (Ising glass), whose energies are a strong proxy for downstream model performance. This formulation enables an efficient ranking of a large number of candidate block-removal configurations yielding many high-quality, non-trivial solutions beyond those only removing consecutive regions. Our method performs strongly in the deep compression regime, such as for 50% compression of Llama-3.3-70B-Instruct, where we achieve an almost 23 percentage point increase on the MMLU benchmark compared to other state-of-the-art (SOTA) block-removal methods. For lighter compression, it performs on par with those methods across several benchmarks for Llama-3.1-8B-Instruct, Qwen3-14B (both before and after retraining), as well as Llama-3.3-70B-Instruct. The approach is computationally efficient and requires only forward and backward passes on a calibration dataset for a few active parameters. Additionally, we demonstrate that using good heuristic solvers for the CBO problem provides solutions that perform well on downstream tasks in negligible runtime when it is unfeasible to solve the problem exactly. The method can be readily applied to any architecture. We illustrate this generality on the recent NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 model, which exhibits a highly inhomogeneous and challenging block structure, and where we outperform SOTA for AIME25 and GPQA when removing either 2 attention layers or 3 mixture-of-experts layers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.00161) | 2026-09-14
