---
title: "Variational Relevance-Informed Sparsification of Term Measurements for Variational Quantum Algorithms"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22118"
summary: "arXiv:2611.22118v1 Announce Type: new Abstract: Repeated measurements are a major bottleneck in variational quantum algorithms (VQAs). We uncover and characterize parameter-specific sparsity in the ma"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22118v1 Announce Type: new Abstract: Repeated measurements are a major bottleneck in variational quantum algorithms (VQAs). We uncover and characterize parameter-specific sparsity in the matrix of qubit-wise commuting (QWC) group contributions to parameter-shift gradients: most absolute contribution mass concentrates in a subset of groups whose relevance varies across parameters and optimization states. Building on this structure, we introduce a learned controller that predicts group relevance from Hamiltonian, circuit, light-cone, and current-state features, then selects measurements through a tunable coverage threshold. Exact contributions provide offline supervision without being required at deployment. Across 15 molecular VQE settings, our method saves 49.6% of nominal gradient-measurement shots with a mean absolute energy gap of 5.67 mHa to Full-QWC. We then ask whether large language models (LLMs) can solve the same selection problem without fine-tuning. The results reveal both promise and a clear limitation: LLMs can identify useful measurement groups, yet without guidance, local models do not consistently prioritize the physical information that matters most. Our learned controller uses these cues more effectively. This contrast points toward a broader direction for AI-assisted science: combining the flexibility of general-purpose models with explicit physical representations, task-specific objectives, and domain-grounded validation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22118) | 2026-11-18
