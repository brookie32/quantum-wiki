---
title: "Do Quantum Transformers Help? A Systematic VQC Architecture Comparison on Tabular Benchmarks"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23931"
summary: "arXiv:2604.23931v1 Announce Type: new Abstract: Variational quantum circuits (VQCs) are a leading approach to quantum machine learning on near-term devices, yet it remains unclear which circuit archit"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23931v1 Announce Type: new Abstract: Variational quantum circuits (VQCs) are a leading approach to quantum machine learning on near-term devices, yet it remains unclear which circuit architecture yields the best accuracy-parameter trade-off on classical tabular data. We present a systematic empirical comparison of four VQC families -- multi-layer fully-connected (FC-VQC), residual (ResNet-VQC), hybrid quantum-classical transformer (QT), and fully quantum transformer (FQT) -- across five regression and classification benchmarks. Our key findings are: extbf{(i)}~FC-VQCs achieve 90-96% of the R^2 of attention-based VQCs while using 40-50% fewer parameters, and consistently outperform equal-capacity MLPs (mean R^2{=}0.829 vs. MLP_{720}'s 0.753 on Boston Housing, 3-seed average); extbf{(ii)}~FC-VQC's Type~4 inter-block connectivity provides partial cross-token mixing that approximates the role of attention -- explicit quantum self-attention yields only marginal gains on most datasets while significantly increasing parameter count; extbf{(iii)}~expressibility saturates at circuit depth~{approx},3, explaining why shallow VQCs already cover the Hilbert space effectively; extbf{(iv)}~LayerNorm on the fully quantum transformer improves classification accuracy, suggesting normalization is important when all operations are quantum; extbf{(v)}~in our noise study on Boston Housing, FQT degrades gracefully under depolarizing noise while QT collapses. All results are validated across three random seeds. These findings provide practical architectural guidance for deploying VQCs on near-term quantum hardware.



## Related
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[calibrating-the-role-of-entanglement-in-variational-quantum-|Calibrating the Role of Entanglement in Variational Quantum Algorithms from a Geometric Perspective]]
- [[a-spectral-gap-informed-parameter-schedule-for-qaoa|A Spectral Gap Informed Parameter Schedule for QAOA]]
- [[practical-lower-bounds-for-hybrid-quantum-interior-point-met|Practical lower bounds for hybrid quantum interior point methods in linear programming]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23931) | 2026-04-28
