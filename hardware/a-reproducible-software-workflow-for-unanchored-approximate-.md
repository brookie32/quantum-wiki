---
title: "A Reproducible Software Workflow for Unanchored Approximate MUB Optimization: A Case Study in Dimension Six"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.10615"
summary: "arXiv:2607.10615v1 Announce Type: cross Abstract: We present a reproducible, parameter-driven software workflow for optimizing approximate mutually unbiased basis (AMUB) configurations in arbitrary di"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2607.10615v1 Announce Type: cross Abstract: We present a reproducible, parameter-driven software workflow for optimizing approximate mutually unbiased basis (AMUB) configurations in arbitrary dimensions d using a Lie-algebra unitary parameterization. The workflow is designed for portable execution across CPU, Apple MPS, CUDA-capable GPU, and HPC backends, using a Taylor-series matrix exponential layer as an accelerator compatibility pathway. As a dimension-six case study, we optimize unanchored configurations across 100 random seeds for basis counts n = 3, 4, 5, 6 in complex128 and complex64 arithmetic. The workflow recovers exact three-basis configurations, identifies a recurrent four-basis partial-exact hub-and-triangle structure, and finds no near-exact pairs for n = 5 or n = 6 in the reported campaigns under the primary tolerance. As a hardware-execution check, we embed the representative d = 6, n = 4 transition unitaries into three-qubit 8x8 unitaries and execute the resulting circuits on the 156-qubit Heron processor ibm-marrakesh using subspace post-selection. The measured QPU pairwise losses are dominated by a hardware and compilation noise floor of approximately 0.02-0.08, associated with compiled circuits averaging 37 native CZ gates, which obscures the distinction between classically near-exact and defective pairs. The results provide a reproducible computational framework for exploring AMUB landscapes, together with an initial assessment of the challenges involved in executing optimized dimension-six unitaries on current quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.10615) | 2026-08-06
