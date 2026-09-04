---
title: "MakoXC: Rearchitecting DFT Exchange-Correlation with Matrix-Aligned and Knowledge-Organized Sparsity"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.01025"
summary: "arXiv:2609.01025v2 Announce Type: replace-cross Abstract: Density Functional Theory (DFT) is indispensable for materials science and drug discovery, yet the exchange--correlation (XC) evaluation remai"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.01025v2 Announce Type: replace-cross Abstract: Density Functional Theory (DFT) is indispensable for materials science and drug discovery, yet the exchange--correlation (XC) evaluation remains a major bottleneck due to its cubic scaling. Although linear-scaling methods exploit electronic nearsightedness to reduce asymptotic complexity, they produce irregular sparse workloads that hide implicit sparsity and prevent efficient use of modern AI accelerators. We present MakoXC, a modular matrix-aligned XC evaluation engine that rearchitects nearsightedness-induced sparsity into regular, accelerator-friendly computations. MakoXC co-designs three key techniques: (1) Matrix-Aligned Cells reorganize nearsightedness-induced interactions into dense, accelerator-aligned data clusters; (2) Sparsity-Guided Activation translates deeper implicit sparsity into numerically correct structured execution for practical linear scaling; and (3) Kernel-Fused Pipeline consolidates fragmented workloads into a unified, compute-intensive execution path that fully unleashes accelerator throughput. Extensive evaluations show that MakoXC achieves average speedups of 67.8imes speedup over standard XC evaluation and 4.7imes over state-of-the-art linear-scaling methods. When integrated into a production-grade commercial DFT package, MakoXC scales XC evaluation to ubiquitin (1,231 atoms, def2-SVP) on 64 GPUs, enabling the end-to-end DFT calculation to complete in under five minutes. By restructuring XC evaluation into a unified, structured computation, MakoXC demonstrates how scientific workloads can achieve genuine low complexity while maximizing parallel efficiency on AI accelerators.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.01025) | 2026-09-04
