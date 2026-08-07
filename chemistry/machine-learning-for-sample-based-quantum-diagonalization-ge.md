---
title: "Machine learning for sample-based quantum diagonalization: generative configuration recovery and the classical-simulability frontier"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05314"
summary: "arXiv:2608.05314v1 Announce Type: new Abstract: Sample-based quantum diagonalization (SQD), equivalently quantum-selected configuration interaction (QSCI), has in two years become a pragmatic centre o"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05314v1 Announce Type: new Abstract: Sample-based quantum diagonalization (SQD), equivalently quantum-selected configuration interaction (QSCI), has in two years become a pragmatic centre of gravity of pre-fault-tolerant quantum chemistry: a quantum processor samples electronic configurations, and the many-electron Hamiltonian is diagonalized classically in the resulting determinant subspace. Its accuracy is set entirely by which configurations enter that subspace, a selection problem for machine learning made acute by a coupon-collector bottleneck. We critically review the ecosystem of generative and learned selectors, organizing it by the object each method generates and the importance signal it exploits, and expose one conspicuous gap: a reward-proportional generative-flow-network proposer built for tail discovery. We then confront the field's central question -- whether the quantum sampler beats classical selected configuration interaction -- and report a carefully scoped negative: across published same-active-space comparisons, strong classical selected CI matches or beats the quantum-sampled subspace, and the flagship single-layer circuits now admit polynomial-time classical energy estimation. We distil a benchmarking standard and turn the negative into a regime map, then test it with FCI-exact experiments that confirm one prediction and refute another: the cheap prior's rank correlation with the exact weights declines with multireference character (a usable coordinate), but a controlled single-molecule noise sweep shows the one generative advantage we find, robustness to valid-shot starvation, to be generic rather than the multireference-specific effect a confounded contrast first suggested. Finally, we flag learning from quantum experiments, whose classical sample-complexity lower bound is an unconditional theorem, as the one adjacent frontier where a quantum advantage is provable but not yet bridged to chemistry.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05314) | 2026-08-07
