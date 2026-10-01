---
title: "QuLoC: Photonic Quantum-Assisted Low-Rank LLM Compression"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40146"
summary: "arXiv:2609.40146v1 Announce Type: new Abstract: As LLMs grow in size, compression becomes increasingly important for efficient deployment. SVD-based low-rank compression reduces parameter counts but c"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40146v1 Announce Type: new Abstract: As LLMs grow in size, compression becomes increasingly important for efficient deployment. SVD-based low-rank compression reduces parameter counts but can degrade downstream performance. To improve performance after compression, we introduce QuLoC, a photonic quantum-assisted LLM compression algorithm that uses quantum circuit outputs to gate the retained low-rank components during training. Model performance is recovered through local functional reconstruction followed by end-to-end knowledge distillation. After training, the gating coefficients are absorbed into the low-rank factors, allowing the compressed model to run on classical hardware without executing quantum circuits during inference. Experiments on Qwen3.5-4B show that QuLoC achieves a 9.73% relative improvement in average accuracy over state-of-the-art baselines across multiple downstream tasks, demonstrating its effectiveness. We further evaluate QuLoC on LLaMA-7B at different parameter compression ratios. It consistently achieves higher average downstream accuracy than state-of-the-art baselines, supporting its applicability to a larger model across different compression settings. Notably, experiments using the photonic quantum hardware retain these benefits with a small accuracy loss relative to simulation, suggesting robustness to hardware noise. These results motivate further exploration of photonic quantum-assisted compression for larger models and more complex agentic tasks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40146) | 2026-10-01
