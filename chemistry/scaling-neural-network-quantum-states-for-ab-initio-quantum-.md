---
title: "Scaling Neural Network Quantum States for Ab Initio Quantum Chemistry"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.02929"
summary: "arXiv:2609.02929v1 Announce Type: new Abstract: Neural-network quantum states (NNQSs) can represent many-electron wave functions without explicitly enumerating the determinant space, but their accurac"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.02929v1 Announce Type: new Abstract: Neural-network quantum states (NNQSs) can represent many-electron wave functions without explicitly enumerating the determinant space, but their accuracy depends jointly on model size and variational-optimization effort. Here we characterize this dependence for a physics-conditioned autoregressive NNQS trained separately on two six-molecule source benchmarks. Across eight model sizes and five optimization milestones, we find that model size and optimization steps jointly shape the energy error. The capacity advantage of larger models becomes more apparent with sufficient optimization, while the returns from additional optimization vary with model size. We capture this coupling using an interaction scaling law and quantify the cumulative compute of each evaluated configuration. The resulting error-compute Pareto frontiers provide a practical decision rule for jointly selecting model size and optimization steps under a given compute budget within the evaluated range. Furthermore, we find that this beneficial scaling trend persists during fine-tuning on held-out N_2. Pretrained models show decreasing error with increasing model size, with a steeper reduction following pretraining on the Hard benchmark. Together, these results place autoregressive neural quantum states within the broader landscape of empirical neural scaling and open a quantitative route toward the systematic scaling of neural quantum solvers for ab initio quantum chemistry.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.02929) | 2026-09-04
